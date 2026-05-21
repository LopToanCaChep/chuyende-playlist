import os
import re
import requests
from pathlib import Path

# Thư mục làm việc
chuyende_dir = Path("c:/Users/huyds/OneDrive/2. PARA/1 - Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/01_Inputs/chuyende_05")
md_file_path = chuyende_dir / "cd05.md"
pic_dir = chuyende_dir / "pic"
pic_dir.mkdir(parents=True, exist_ok=True)

# Đọc file markdown
with open(md_file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Tìm tất cả link ảnh của Mathpix
# Định dạng: ![](https://cdn.mathpix.com/cropped/...)
pattern = r'!\[\]\((https://cdn\.mathpix\.com/cropped/[^)]+)\)'
matches = re.findall(pattern, content)

print(f"Tìm thấy {len(matches)} ảnh Mathpix trong file Markdown.")

# Phân loại và tải ảnh
downloaded_count = 0
mapping = {}

# Regex để đọc tham số hình ảnh
# Ví dụ: ?height=123&width=274&top_left_y=2464&top_left_x=975
params_pattern = re.compile(r'top_left_y=(\d+)')

img_idx = 1
for url in matches:
    # Kiểm tra xem đây có phải là footer quảng cáo không
    # Vị trí y thường > 2400 ở chân trang của trang giấy A4 (thường là 2462, 2464)
    y_match = params_pattern.search(url)
    if y_match:
        y_val = int(y_match.group(1))
        # Nếu y > 2400 và có kích thước nhỏ của footer (thường height ~ 125, width ~ 274)
        if y_val > 2400 and ("height=12" in url or "width=27" in url):
            print(f"-> Bỏ qua ảnh quảng cáo chân trang: {url[:80]}...")
            # Xóa ảnh quảng cáo chân trang này khỏi nội dung Markdown
            content = content.replace(f"![]({url})", "")
            continue
            
    # Nếu là ảnh hợp lệ, kiểm tra xem đã tải chưa
    if url in mapping:
        # Nếu url trùng nhau thì dùng lại ảnh cũ
        content = content.replace(f"![]({url})", f"![](pic/{mapping[url]})")
        continue

    # Tên file ảnh cục bộ mới
    ext = ".jpg"
    if ".png" in url:
        ext = ".png"
    elif ".gif" in url:
        ext = ".gif"
    
    local_name = f"pic_{img_idx:02d}{ext}"
    local_path = pic_dir / local_name
    
    print(f"Dang tai ảnh {img_idx}: {url[:80]}...")
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            with open(local_path, "wb") as img_f:
                img_f.write(resp.content)
            mapping[url] = local_name
            content = content.replace(f"![]({url})", f"![](pic/{local_name})")
            img_idx += 1
            downloaded_count += 1
        else:
            print(f"  ❌ Lỗi tải ảnh (Status {resp.status_code})")
    except Exception as e:
        print(f"  ❌ Lỗi kết nối: {e}")

# Ghi lại file markdown đã được cập nhật đường dẫn local và loại bỏ quảng cáo
updated_md_path = chuyende_dir / "cd05_local.md"
with open(updated_md_path, "w", encoding="utf-8") as f:
    f.write(content)

print("─" * 60)
print(f"Hoàn tất! Đã tải {downloaded_count} ảnh về {pic_dir}")
print(f"File markdown mới đã lưu tại: {updated_md_path}")
