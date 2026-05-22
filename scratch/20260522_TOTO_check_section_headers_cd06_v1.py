# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_06.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- KIỂM TRA TIÊU ĐỀ DẠNG BÀI TRONG CHUYÊN ĐỀ 6 ---")
for idx, line in enumerate(lines):
    if "dạng " in line.lower() or "dang " in line.lower():
        if idx > 500 and "theory" not in line.lower():
            print(f"Dòng {idx + 1}: {line.strip()[:120]}")
            
# Tìm xem có thẻ h2 hoặc h3 nào ngoài slide không
print("\n--- KIỂM TRA CÁC THẺ HEADING NGOÀI SLIDE TRONG CHUYÊN ĐỀ 6 ---")
for idx, line in enumerate(lines):
    if idx > 500 and ("<h1" in line or "<h2" in line or "<h3" in line) and "theory" not in line.lower():
        print(f"Dòng {idx + 1}: {line.strip()[:120]}")
