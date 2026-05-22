# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- KIỂM TRA CÂU 50 SAU KHI SỬA ---")
start_print = False
for idx, line in enumerate(lines):
    if "Câu 50" in line and "q-number" in line:
        start_print = True
    if start_print:
        # In ra 12 dòng từ dòng này
        for i in range(idx - 1, idx + 15):
            print(f"Dòng {i+1}: {lines[i].rstrip()}")
        break
