# -*- coding: utf-8 -*-

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. All cards render as div (clickable for password)
c = c.replace(
    "const tag = (!cd.hasPassword && cd.file) ? 'a' : 'div';",
    "const tag = 'div';"
)
c = c.replace(
    """const hrefAttr = (!cd.hasPassword && cd.file)
      ? `href="${cd.file}" target="_blank" rel="noopener"`
      : '';""",
    "const hrefAttr = '';"
)

# 2. Click handler: remove A-tag skip and hasPassword check
c = c.replace(
    "  if (row.tagName === 'A') return;\n",
    ""
)
c = c.replace(
    "  if (!cd || !cd.hasPassword) return;",
    "  if (!cd) return;"
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Done - all cards clickable with password")
