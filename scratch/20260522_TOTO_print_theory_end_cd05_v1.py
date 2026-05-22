# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- PHẦN CUỐI CỦA LÝ THUYẾT (Dòng 2570 đến 2605) ---")
for i in range(2569, min(len(lines), 2605)):
    print(f"Dòng {i+1}: {lines[i].rstrip()}")
