# -*- coding: utf-8 -*-
import re

html_path = r"03_Outputs\chuyende_01.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace \frac with \dfrac globally
content = content.replace(r"\frac", r"\dfrac")

# 2. Process options to remove trailing dot and wrap standalone numbers
# Option pattern looks like: <div class="option" data-ans="A" ...><div class="opt-label">A.</div> CONTENT</div>
def fix_option(match):
    prefix = match.group(1) # <div class="option"...>
    label = match.group(2)  # <div class="opt-label">A.</div>
    opt_content = match.group(3).strip() # CONTENT
    
    # Remove trailing dot if it ends with one
    if opt_content.endswith("."):
        opt_content = opt_content[:-1].strip()
        
    # Wrap standalone numbers (including decimals/negatives) in $
    if re.match(r"^-?\d+(?:,\d+)?$", opt_content):
        opt_content = f"${opt_content}$"
        
    return f"{prefix}{label} {opt_content}</div>"

# Use regex to find and replace option contents
# Note: we need to match carefully because it's HTML.
# A typical option looks like:
# <div class="option" data-ans="A" role="button" tabindex="0" aria-label="Phuong án A"><div class="opt-label">A.</div> 0.</div>
pattern = r'(<div class="option"[^>]*>)\s*(<div class="opt-label">[A-D]\.</div>)\s*(.*?)\s*</div>'
content = re.sub(pattern, fix_option, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("HTML updated.")

