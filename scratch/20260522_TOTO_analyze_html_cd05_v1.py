# -*- coding: utf-8 -*-
import sys
import re

# Cấu hình stdout ghi Unicode tiếng Việt
sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Tổng số dòng: {len(lines)}")

# Tìm các dòng chứa từ khóa liên quan đến modal hoặc ly thuyết
print("\n--- Tìm vị trí liên quan đến lý thuyết/modal ---")
for idx, line in enumerate(lines):
    if "theory" in line.lower() or "modal" in line.lower():
        if idx < 1000: # bỏ qua style ở đầu file
            continue
        print(f"Dòng {idx + 1}: {line.strip()[:150]}")

# Tìm dòng chứa Câu 50
print("\n--- Tìm Câu 50 ---")
for idx, line in enumerate(lines):
    # Tìm câu hỏi
    if "q50" in line.lower() or "câu 50" in line.lower() or "cau 50" in line.lower() or "data-id=\"50\"" in line.lower():
        print(f"Dòng {idx + 1}: {line.strip()[:150]}")
