# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_06.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Đếm các thẻ div mở/đóng trong từng đoạn
ts_modal = content.find('id="theoryModal"')
ts_content = content.find('id="theory-content"')
te_script = content.find('<script>', ts_modal)

print("1. Đoạn từ theoryModal đến theory-content:")
sec1 = content[ts_modal:ts_content]
print(f"  <div: {sec1.count('<div')}, </div>: {sec1.count('</div>')}")
print(sec1)

print("\n2. Đoạn từ theory-content đến script:")
sec2 = content[ts_content:te_script]
print(f"  <div: {sec2.count('<div')}, </div>: {sec2.count('</div>')}")
# In 200 ký tự cuối của sec2 để xem các thẻ đóng div
print("200 ký tự cuối:")
print(sec2[-200:])
