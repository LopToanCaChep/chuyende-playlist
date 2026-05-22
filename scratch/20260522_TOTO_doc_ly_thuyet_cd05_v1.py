# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

theory_start_marker = '<div class="theory-text" id="theory-content"'
ts = content.find(theory_start_marker)
if ts < 0:
    print("❌ Không tìm thấy marker lý thuyết trong CD05")
    sys.exit(1)

print("--- KHỞI ĐẦU LÝ THUYẾT CHUYÊN ĐỀ 05 ---")
print(content[ts:ts+4000])
