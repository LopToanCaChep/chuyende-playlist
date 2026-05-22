# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. Tìm vị trí thẻ modal lý thuyết (thường chứa "theory-header" hoặc "theoryModal")
start_idx = -1
end_idx = -1
for idx, line in enumerate(lines):
    if "theoryModal" in line and "<div" in line:
        start_idx = idx
        break

# Tìm thêm từ khóa theory-header nếu không tìm thấy theoryModal
if start_idx == -1:
    for idx, line in enumerate(lines):
        if "theory-header" in line:
            start_idx = max(0, idx - 5)
            break

# Giả định dòng kết thúc lý thuyết nằm gần dòng 2598 (trước đoạn khai báo script)
if start_idx != -1:
    print(f"Bắt đầu lý thuyết tại dòng: {start_idx + 1}")
    # In ra 30 dòng từ start_idx
    print("\n--- 30 DÒNG ĐẦU CỦA LÝ THUYẾT ---")
    for i in range(start_idx, min(len(lines), start_idx + 30)):
        print(f"Dòng {i+1}: {lines[i].rstrip()}")

    # Tìm dòng kết thúc lý thuyết (nơi chứa script hoặc kết thúc div)
    # Chúng ta tìm từ dòng 2580 đến 2610
    print("\n--- CÁC DÒNG KẾT THÚC LÝ THUYẾT ---")
    for i in range(2570, min(len(lines), 2605)):
        print(f"Dòng {i+1}: {lines[i].rstrip()}")

# 2. Trích xuất xung quanh câu 50
print("\n--- CHI TIẾT CÂU 50 (dòng 1570 đến 1620) ---")
for i in range(1560, min(len(lines), 1620)):
    print(f"Dòng {i+1}: {lines[i].rstrip()}")
