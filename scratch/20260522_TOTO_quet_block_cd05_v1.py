# -*- coding: utf-8 -*-
import sys, re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Tìm các block và in toàn bộ
blocks = re.findall(r'<div class="theory-block[^"]*">.*?<!-- /theory-block -->', content, re.DOTALL)
if not blocks:
    blocks = re.findall(r'<div class="theory-block[^"]*">.*?</div>', content, re.DOTALL)

print(f"Tìm thấy {len(blocks)} blocks:")
for i, block in enumerate(blocks):
    print(f"\n--- Block {i+1} ---")
    print(block)
