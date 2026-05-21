
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

css_addition = """
.exam-row.coming-soon { opacity: 0.6; cursor: default; pointer-events: none; }
.exam-row.coming-soon:hover { border-color: var(--cc-line); background: var(--cc-paper); transform: none; box-shadow: none; }
.exam-row.coming-soon:hover .exam-title { color: var(--cc-ink); }
.exam-row.coming-soon:hover .exam-meta { color: var(--cc-ink-soft); }
.exam-row.coming-soon:hover .exam-icon { background: #f1f5f9; color: var(--cc-blue-deep); border-color: var(--cc-line); }
.exam-row.coming-soon .exam-arrow { display: none; }
"""
content = content.replace("/* ========== PASSWORD MODAL ========== */", css_addition + "\n/* ========== PASSWORD MODAL ========== */")

js_replacement = """
    let gradeTag = '';
    if (cd.grade === '12') gradeTag = '<span class="exam-tag t12">Lớp 12</span>';
    else if (cd.grade === '11') gradeTag = '<span class="exam-tag t11">Lớp 11</span>';
    else if (cd.grade === '10') gradeTag = '<span class="exam-tag t10">Lớp 10</span>';
    
    const isComingSoon = cd.status === 'Coming_Soon';
    const statusTag = isComingSoon ? '<span class="exam-tag" style="background:#f1f5f9;color:#64748B">Sắp ra mắt</span>' : '';
    const extraClass = isComingSoon ? ' coming-soon' : '';
    
    const tag = (!cd.hasPassword && cd.file && !isComingSoon) ? 'a' : 'div';
    const hrefAttr = (!cd.hasPassword && cd.file && !isComingSoon)
      ? `href="${cd.file}" target="_blank" rel="noopener"`
      : '';

    return `
      <${tag} class="exam-row${extraClass}" data-id="${cd.id}" ${hrefAttr} role="button" tabindex="0">
        <div class="exam-icon">${cd.icon}</div>
        <div class="exam-info">
          <div class="exam-title">${cd.title}</div>
          <div class="exam-meta">
            ${isComingSoon ? '' : `<span>${cd.questions} câu hỏi</span>`}
            ${gradeTag}
            ${statusTag}
          </div>
        </div>
        <div class="exam-arrow">→</div>
      </${tag}>`;
"""
pattern = r"let gradeTag = ';.*?</\$\{tag\}>`;"
content = re.sub(pattern, lambda _: js_replacement.strip(), content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html")

