import re

with open("03_Outputs/chuyende_02.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace title
content = re.sub(r'<title>.*?</title>', '<title>{{TITLE}}</title>', content)

# Replace theory content
# The theory content is inside <div id="theory-content"...> ... </div>
# We need to find the exact boundaries.
theory_pattern = re.compile(r'(<div id="theory-content".*?>)(.*?)(</div>\s*</div>\s*</div>)', re.DOTALL)
content = theory_pattern.sub(r'\1\n            {{THEORY}}\n        \3', content)

# Replace content slides
# The slides are inside <div id="content-container"> ... </div>
# But we need to make sure we don't capture the closing div of container.
content_pattern = re.compile(r'(<div id="content-container">)(.*?)(</div>\s*</div>\s*<!-- Nav Bar)', re.DOTALL)
content = content_pattern.sub(r'\1\n        {{CONTENT}}\n    \3', content)

with open("template/chuyende_template.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Template extracted and saved to template/chuyende_template.html")
