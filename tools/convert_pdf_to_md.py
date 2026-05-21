import os
import sys
import time
import hashlib
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# --- CACHE (SHA-256 PDF → .cache/mathpix/) ---
_CACHE_DIR = Path(__file__).resolve().parents[1] / ".cache" / "mathpix"


def _pdf_sha256(pdf_path: str) -> str:
    with open(pdf_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _load_cache(pdf_hash: str) -> str | None:
    p = _CACHE_DIR / f"{pdf_hash}_raw.md"
    return p.read_text(encoding='utf-8') if p.exists() else None


def _save_cache(pdf_hash: str, md_text: str):
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (_CACHE_DIR / f"{pdf_hash}_raw.md").write_text(md_text, encoding='utf-8')

# =======================================================
# MATHPIX API: PDF to Markdown Converter
# =======================================================

APP_ID = os.getenv("MATHPIX_APP_ID")
APP_KEY = os.getenv("MATHPIX_APP_KEY")
if not APP_ID or not APP_KEY:
    print("❌ Thiếu MATHPIX_APP_ID / MATHPIX_APP_KEY trong .env")
    sys.exit(1)

def pdf_to_markdown(pdf_path, output_md_path):
    print(f"[*] Dang xu ly file PDF: {pdf_path}")
    
    headers = {
        "app_id": APP_ID,
        "app_key": APP_KEY
    }
    
    # 1. Upload PDF
    options = {
        "conversion_formats": {"md": True},
        "math_inline_delimiters": ["$", "$"],
        "math_display_delimiters": ["$$", "$$"]
    }
    
    with open(pdf_path, "rb") as f:
        print("[*] Dang upload len Mathpix...")
        response = requests.post(
            "https://api.mathpix.com/v3/pdf",
            headers=headers,
            data={"options_json": json.dumps(options)},
            files={"file": f}
        )
    
    if response.status_code != 200:
        print(f"[!] Loi API: {response.text}")
        return False
        
    pdf_id = response.json().get("pdf_id")
    print(f"[*] Upload thanh cong! PDF_ID: {pdf_id}")
    
    # 2. Wait for completion
    while True:
        status_url = f"https://api.mathpix.com/v3/pdf/{pdf_id}"
        status_resp = requests.get(status_url, headers=headers)
        status_data = status_resp.json()
        status = status_data.get("status")
        
        if status == "completed":
            print("\n[*] Xu ly xong!")
            break
        elif status == "error":
            print(f"\n[!] Loi trong qua trinh xu ly: {status_data}")
            return False
            
        print(".", end="", flush=True)
        time.sleep(3)
        
    # 3. Download Markdown
    print("[*] Dang tai ve Markdown...")
    md_url = f"https://api.mathpix.com/v3/pdf/{pdf_id}.md"
    md_resp = requests.get(md_url, headers=headers)
    
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(md_resp.text)
        
    print(f"[*] Hoan tat! Luu tai: {output_md_path}")
    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert PDF → Markdown (Mathpix, có cache)")
    parser.add_argument("pdf_path", help="Đường dẫn file PDF")
    parser.add_argument("--force", action="store_true", help="Bỏ qua cache, gọi API mới")
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print("[!] Khong tim thay file PDF!")
        sys.exit(1)

    pdf_path = args.pdf_path
    out_file = str(Path(pdf_path).with_suffix('.md'))

    # --- Cache check ---
    pdf_hash = _pdf_sha256(pdf_path)
    print(f"[*] PDF SHA-256: {pdf_hash[:16]}...")

    cached = None if args.force else _load_cache(pdf_hash)
    if cached:
        print("[⚡] Cache HIT — dùng kết quả đã cache, bỏ qua API call.")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(cached)
        print(f"[*] Hoan tat! Luu tai: {out_file}")
    else:
        if args.force:
            print("[*] --force: gọi API Mathpix mới...")
        else:
            print("[*] Cache MISS — gọi API Mathpix...")
        ok = pdf_to_markdown(pdf_path, out_file)
        if ok:
            # Cache raw result (nội dung đã lưu vào out_file)
            with open(out_file, "r", encoding="utf-8") as f:
                _save_cache(pdf_hash, f.read())
            print(f"[💾] Đã lưu cache: {pdf_hash[:16]}..._raw.md")
        sys.exit(0 if ok else 1)
