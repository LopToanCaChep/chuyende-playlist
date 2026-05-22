# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- TÌM CÁC DẠNG BÀI TRONG FILE HTML ---")
for idx, line in enumerate(lines):
    if "dạng " in line.lower() or "dang " in line.lower():
        # Chỉ in các dòng không thuộc lý thuyết (dưới dòng 800) và không chứa ".theory"
        if idx > 800 and "theory" not in line.lower():
            print(f"Dòng {idx + 1}: {line.strip()[:120]}")
