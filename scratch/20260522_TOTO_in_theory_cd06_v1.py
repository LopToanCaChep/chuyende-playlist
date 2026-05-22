# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_06.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Tìm đoạn chứa id="theoryModal"
start_idx = content.find('id="theoryModal"')
if start_idx < 0:
    start_idx = content.find("id='theoryModal'")

if start_idx < 0:
    print("❌ Không tìm thấy theoryModal")
    sys.exit(1)

# Lấy 15000 ký tự từ start_idx
theory_section = content[start_idx:start_idx+15000]

# Ghi ra một file tạm để đọc nếu quá dài
with open("theory_section_cd06.html", "w", encoding="utf-8") as out:
    out.write(theory_section)

print("Đã xuất 15000 ký tự của theoryModal ra file theory_section_cd06.html")
# In ra 3000 ký tự đầu tiên
print(theory_section[:3000])
