
import re
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

css_addition = """
.exam-tag.subject { background: #f8fafc; color: #475569; border: 1px solid #e2e8f0; }
.exam-row.coming-soon { opacity: 0.6; cursor: default; pointer-events: none; }
.exam-row.coming-soon:hover { border-color: var(--cc-line); background: var(--cc-paper); transform: none; box-shadow: none; }
.exam-row.coming-soon:hover .exam-title { color: var(--cc-ink); }
.exam-row.coming-soon:hover .exam-meta { color: var(--cc-ink-soft); }
.exam-row.coming-soon:hover .exam-icon { background: #f1f5f9; color: var(--cc-blue-deep); border-color: var(--cc-line); }
.exam-row.coming-soon .exam-arrow { display: none; }
"""
content = content.replace("</style>", css_addition + "\n</style>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated CSS in index.html")

