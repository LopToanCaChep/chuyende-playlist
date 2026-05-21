"""
Upload Images to Cloudinary — Toán Cá Chép
============================================
Cách dùng:
    python tools/upload_images.py chuyende_02
    python tools/upload_images.py chuyende_02 --file hinh_1.png

Script sẽ:
1. Scan folder 01_Inputs/pic/<tên_chuyên_đề>/
2. Upload từng hình lên Cloudinary (folder = tên chuyên đề)
3. In ra danh sách URL sẵn dùng trong HTML
"""

import hashlib, time, os, sys, requests, glob
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# ═══ CONFIG ═══
CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
API_KEY    = os.getenv("CLOUDINARY_API_KEY")
API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
if not all([CLOUD_NAME, API_KEY, API_SECRET]):
    print("❌ Thiếu Cloudinary credentials! Tạo file .env (xem .env.example).")
    sys.exit(1)

BASE_INPUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "01_Inputs")
EXTENSIONS = ("*.png", "*.jpg", "*.jpeg", "*.webp", "*.gif", "*.svg")

def upload_one(filepath, folder):
    """Upload 1 file lên Cloudinary, trả về secure_url."""
    timestamp = str(int(time.time()))
    params = f"folder={folder}&timestamp={timestamp}"
    signature = hashlib.sha1((params + API_SECRET).encode()).hexdigest()

    with open(filepath, "rb") as f:
        resp = requests.post(
            f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/image/upload",
            data={
                "api_key": API_KEY,
                "timestamp": timestamp,
                "signature": signature,
                "folder": folder,
            },
            files={"file": f}
        )
    
    data = resp.json()
    if "secure_url" in data:
        return data["secure_url"]
    else:
        print(f"  ❌ LỖI: {data.get('error', {}).get('message', 'Unknown')}")
        return None

def main():
    if len(sys.argv) < 2:
        print("❌ Thiếu tên chuyên đề!")
        print("Cách dùng: python tools/upload_images.py chuyende_02")
        sys.exit(1)

    chuyende = sys.argv[1]  # vd: chuyende_02
    single_file = None
    if "--file" in sys.argv:
        idx = sys.argv.index("--file")
        single_file = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None

    folder_path = os.path.join(BASE_INPUT, chuyende, "pic")
    
    if not os.path.isdir(folder_path):
        print(f"❌ Không tìm thấy thư mục: {folder_path}")
        print(f"→ Bỏ hình vào: 01_Inputs/{chuyende}/pic/")
        sys.exit(1)

    # Collect files
    if single_file:
        files = [os.path.join(folder_path, single_file)]
        if not os.path.isfile(files[0]):
            print(f"❌ Không tìm thấy file: {files[0]}")
            sys.exit(1)
    else:
        files = []
        for ext in EXTENSIONS:
            files.extend(glob.glob(os.path.join(folder_path, ext)))
        files.sort()

    if not files:
        print(f"❌ Không có hình nào trong: {folder_path}")
        sys.exit(1)

    print(f"📁 Thư mục: {folder_path}")
    print(f"📤 Upload {len(files)} hình lên Cloudinary (folder: {chuyende})...")
    print("─" * 60)

    results = []
    for f in files:
        name = os.path.basename(f)
        print(f"  ⏳ {name}...", end=" ")
        url = upload_one(f, chuyende)
        if url:
            print(f"✅")
            results.append((name, url))
        else:
            print()

    # Print summary
    print("─" * 60)
    print(f"\n✅ Upload thành công {len(results)}/{len(files)} hình\n")
    
    if results:
        print("📋 DANH SÁCH URL (copy dán vào HTML):")
        print("─" * 60)
        for name, url in results:
            print(f"<!-- {name} -->")
            print(f'<img src="{url}" alt="{name}">')
            print()

if __name__ == "__main__":
    main()
