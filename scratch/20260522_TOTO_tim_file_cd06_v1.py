# -*- coding: utf-8 -*-
import os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

root = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web"
matches = []
for r, dirs, files in os.walk(root):
    for f in files:
        if "chuyende_06" in f or "cd06" in f or "CD06" in f:
            matches.append(os.path.join(r, f))

print("Các file liên quan đến chuyende_06:")
for m in matches:
    print(f"  - {m}")
