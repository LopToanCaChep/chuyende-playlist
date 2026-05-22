# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Tổng số dòng: {len(lines)}")

# Tìm thẻ chứa id="theoryModal"
start_line = -1
for idx, line in enumerate(lines):
    if 'id="theoryModal"' in line:
        start_line = idx + 1
        print(f"Thẻ theoryModal bắt đầu tại dòng: {start_line}")
        print(f"Nội dung dòng: {line.strip()}")
        break

# Xem 15 dòng kể từ dòng start_line
if start_line != -1:
    print("\n--- 15 DÒNG TIẾP THEO ---")
    for i in range(start_line - 1, start_line + 15):
        print(f"Dòng {i+1}: {lines[i].rstrip()}")

# Tìm xem thẻ đóng ở đâu (thường ở ngay trước phần script)
# Script thường bắt đầu bằng <script> hoặc let, const
for idx in range(len(lines) - 1, -1, -1):
    if "let lastFocusBeforeModal" in lines[idx] or "// Render slide 0" in lines[idx] or "const theory = " in lines[idx]:
        print(f"\nPhần code JS bắt đầu xung quanh dòng: {idx + 1}")
        # In ra 10 dòng trước đó
        for i in range(idx - 15, idx):
            print(f"Dòng {i+1}: {lines[i].rstrip()}")
        break
