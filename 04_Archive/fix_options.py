# -*- coding: utf-8 -*-
import re
import os

md_path = r"02_Processing\Xác suất cổ điển.md"
with open(md_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    m = re.match(r"^([A-D]\.)\s+(.*)", line)
    if m:
        prefix = m.group(1)
        content = m.group(2).strip()
        
        # Remove trailing dot
        if content.endswith("."):
            content = content[:-1].strip()
            
        # Replace \frac with \dfrac
        content = content.replace(r"\frac", r"\dfrac")
        
        # Wrap standalone numbers (including decimals/negatives) in $
        if re.match(r"^-?\d+(?:,\d+)?$", content):
            content = f"${content}$"
            
        new_lines.append(f"{prefix} {content}\n")
    else:
        line = line.replace(r"\frac", r"\dfrac")
        new_lines.append(line)

with open(md_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("MD updated.")

