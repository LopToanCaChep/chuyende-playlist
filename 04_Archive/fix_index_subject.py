
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to add the CSS for .exam-tag.subject
css_addition = """
.exam-tag.subject { background: #f8fafc; color: #475569; border: 1px solid #e2e8f0; }
"""
# Insert before /* ========== FOOTER ========== */
content = content.replace("/* ========== FOOTER ========== */", css_addition + "\n/* ========== FOOTER ========== */")

js_replacement = """
    let gradeTag = '';
    if (cd.grade === '12') gradeTag = '<span class="exam-tag t12">Lớp 12</span>';
    else if (cd.grade === '11') gradeTag = '<span class="exam-tag t11">Lớp 11</span>';
    else if (cd.grade === '10') gradeTag = '<span class="exam-tag t10">Lớp 10</span>';
    
    let subjectTag = '';
    if (cd.subject === 'Thống kê - Xác suất') subjectTag = '<span class="exam-tag subject">XS-TK</span>';
    else if (cd.subject === 'Đại số - Giải tích') subjectTag = '<span class="exam-tag subject">ĐS-GT</span>';
    else if (cd.subject === 'Hình học') subjectTag = '<span class="exam-tag subject">Hình</span>';
    
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
            ${subjectTag}
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
print("Updated index.html with subject tags")

