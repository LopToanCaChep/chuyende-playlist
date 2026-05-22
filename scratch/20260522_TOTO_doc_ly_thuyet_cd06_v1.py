# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_06.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

theory_start_marker = '<div class="theory-text" id="theory-content"'
ts = content.find(theory_start_marker)
if ts < 0:
    print("❌ Không tìm thấy marker lý thuyết")
    sys.exit(1)

# Lấy 3000 ký tự đầu của phần lý thuyết để xem cấu trúc
print("--- KHỞI ĐẦU PHẦN LÝ THUYẾT (3000 ký tự) ---")
print(content[ts:ts+3000])

print("\n--- PHẦN CUỐI PHẦN LÝ THUYẾT (1500 ký tự trước script) ---")
te = content.find('<script>', ts)
te_end = content.rfind('</div>', ts, te)
print(content[te_end-1500:te_end+6])
