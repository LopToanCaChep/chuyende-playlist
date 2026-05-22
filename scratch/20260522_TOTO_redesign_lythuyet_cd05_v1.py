# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"
new_theory_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\scratch\20260522_TOTO_new_theory_cd05_v1.html"

# Đọc file HTML gốc
with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Đọc nội dung lý thuyết mới
with open(new_theory_path, 'r', encoding='utf-8') as f:
    new_theory_content = f.read()

# 1. Tìm vị trí thay thế lý thuyết
start_idx = -1
for idx, line in enumerate(lines):
    if '<div class="theory-text" id="theory-content"' in line:
        start_idx = idx
        break

end_idx = -1
for idx, line in enumerate(lines):
    if '<script>' in line and idx > start_idx:
        end_idx = idx
        break

if start_idx == -1 or end_idx == -1:
    print("❌ Lỗi: Không xác định được vị trí phần lý thuyết trong file HTML.")
    sys.exit(1)

print(f"Xác định phần lý thuyết từ dòng {start_idx + 1} đến trước dòng {end_idx + 1}")

# Dựng lại phần lý thuyết:
# Thay thế phần lý thuyết cũ bằng nội dung mới + đóng modal
# Nội dung mới đã có sẵn <div class="theory-text" id="theory-content"> và đóng </div> tương ứng ở cuối.
# Ta chỉ cần thêm thẻ đóng cho .modal-content và #theoryModal.
modal_close_tags = "\n    </div>\n</div>\n\n"

# Cắt ghép nội dung mới
lines_before = lines[:start_idx]
lines_after = lines[end_idx:]

new_html_content = "".join(lines_before) + new_theory_content + modal_close_tags + "".join(lines_after)

# 2. Sửa lỗi câu 50 bị lọt Dạng 4
# Đoạn text cần tìm và xóa: "<br>### Dạng 4. Sự đồng biến - nghịch biến của hàm số"
target_err = "<br>### Dạng 4. Sự đồng biến - nghịch biến của hàm số"
if target_err in new_html_content:
    new_html_content = new_html_content.replace(target_err, "")
    print("✅ Đã tìm thấy và loại bỏ tiêu đề Dạng 4 lọt trong lời giải Câu 50.")
else:
    # Thử tìm không có dấu khoảng trắng ở đầu hoặc dạng markdown thô
    target_err_raw = "### Dạng 4. Sự đồng biến - nghịch biến của hàm số"
    if target_err_raw in new_html_content:
        new_html_content = new_html_content.replace(target_err_raw, "")
        print("✅ Đã tìm thấy và loại bỏ tiêu đề Dạng 4 thô trong lời giải Câu 50.")
    else:
        print("⚠ Không tìm thấy chuỗi lỗi trực tiếp. Sẽ dùng Regex để quét và sửa trong câu 50.")
        # Dùng regex tìm trong khu vực câu 50
        pattern = r"(Chọn A\. Các hàm số.*?không tuần hoàn\.)<br>### Dạng 4\. Sự đồng biến - nghịch biến của hàm số(</div>)"
        if re.search(pattern, new_html_content):
            new_html_content = re.sub(pattern, r"\1\2", new_html_content)
            print("✅ Đã sửa lỗi bằng Regex thành công.")
        else:
            print("❌ Không sửa được lỗi câu 50 bằng Regex. Cần kiểm tra lại nội dung câu 50.")

# Ghi đè lại file HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html_content)

print("✅ Đã ghi đè thành công lý thuyết mới vào file HTML.")
