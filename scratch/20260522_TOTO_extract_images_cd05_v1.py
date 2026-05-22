# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Trích xuất phần lý thuyết từ theory-content đến hết thẻ div của nó
theory_content_match = re.search(r'<div class="theory-text" id="theory-content".*?>(.*?)</div>\s*</div>\s*</div>', html_content, re.DOTALL)

if theory_content_match:
    theory_html = theory_content_match.group(1)
    print("Đã tìm thấy phần HTML lý thuyết!")
    
    # Tìm các thẻ img
    imgs = re.findall(r'<img\s+[^>]*src="([^"]+)"[^>]*>', theory_html)
    print(f"Tổng số ảnh tìm thấy: {len(imgs)}")
    for idx, img in enumerate(imgs):
        print(f"Ảnh {idx + 1}: {img}")
        
    # Ghi phần HTML lý thuyết cũ ra file để xem tham khảo
    with open("theory_extracted_old_cd05.html", "w", encoding="utf-8") as out:
        out.write(theory_html)
    print("Đã xuất HTML lý thuyết cũ ra file 'theory_extracted_old_cd05.html' để tham khảo.")
else:
    print("Không tìm thấy phần lý thuyết bằng regex thông thường. Có thể do lỗi đóng div.")
    # Thử tìm theo dòng từ 2303 đến 2588
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    theory_lines = lines[2302:2588]
    theory_html = "".join(theory_lines)
    
    imgs = re.findall(r'src="([^"]+)"', theory_html)
    print(f"Tổng số ảnh tìm thấy (theo dòng): {len(imgs)}")
    for idx, img in enumerate(imgs):
        print(f"Ảnh {idx + 1}: {img}")
        
    with open("theory_extracted_old_cd05.html", "w", encoding="utf-8") as out:
        out.write(theory_html)
    print("Đã xuất HTML lý thuyết cũ theo dòng ra file 'theory_extracted_old_cd05.html' để tham khảo.")
