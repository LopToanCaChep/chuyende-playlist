# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

template_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\template\chuyende_template.html"

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Tìm body và in 2000 ký tự đầu của body
body_idx = content.find("<body>")
print("--- KHỞI ĐẦU BODY TEMPLATE ---")
print(content[body_idx:body_idx+2000])

# Tìm đoạn lý thuyết (theoryModal) và in ra
theory_idx = content.find('id="theoryModal"')
print("\n--- KHỞI ĐẦU THEORYMODAL TEMPLATE ---")
print(content[theory_idx:theory_idx+2000])
