# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_06.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Kiểm tra sự cân bằng của thẻ div trong toàn bộ file
open_divs = content.count("<div")
close_divs = content.count("</div>")
print(f"Toàn bộ file: <div = {open_divs}, </div> = {close_divs}, Chênh lệch = {open_divs - close_divs}")

# Kiểm tra vùng từ theoryModal trở đi
ts = content.find('id="theoryModal"')
if ts >= 0:
    section = content[ts:]
    sec_open = section.count("<div")
    sec_close = section.count("</div>")
    print(f"Từ theoryModal trở đi: <div = {sec_open}, </div> = {sec_close}, Chênh lệch = {sec_open - sec_close}")
else:
    print("❌ Không tìm thấy theoryModal")
