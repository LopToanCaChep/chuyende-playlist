import os
import re
import sys
import argparse
from ocr_cleaner import clean_ocr


def apply_display_style(match):
    eq = match.group(1)
    if re.search(r'\\frac|\\lim|\\sum|\\int', eq):
        if not eq.strip().startswith(r'\displaystyle'):
            return r'$\displaystyle ' + eq.strip() + r'$'
    return match.group(0)

def fix_math_display(text):
    if not text: return ""
    return re.sub(r'(?<!\$)\$([^$]+)\$(?!\$)', apply_display_style, text)

def markdown_to_theory_html(text):
    if not text: return ""
    text = fix_math_display(text)
    
    # Bảo toàn <br> trước khi mã hóa HTML
    text = text.replace('<br>', '__BR__')
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    text = text.replace('__BR__', '<br>')
    
    lines = text.split('\n')
    html = []
    in_table = False
    in_note = False
    
    for line in lines:
        line = line.strip()
        if not line:
            if not in_table:
                html.append('<br>')
            continue
            
        # ƯU TIÊN XỬ LÝ IN ĐẬM ĐẦU TIÊN CHO MỌI DÒNG (kể cả trong bảng)
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            
        # Tiêu đề Heading 2
        if line.startswith('## '):
            if in_table:
                html.append('</table></div>')
                in_table = False
            if in_note:
                html.append('</div>')
                in_note = False
            title = line[3:].strip()
            html.append(f'<div class="theory-h2">{title}</div>')
            continue
            
        # Tiêu đề Heading 3
        if line.startswith('### '):
            if in_table:
                html.append('</table></div>')
                in_table = False
            if in_note:
                html.append('</div>')
                in_note = False
            title = line[4:].strip()
            html.append(f'<div class="theory-box-title">{title}</div>')
            continue

        # Lưu ý
        if line.lower().startswith('lưu ý'):
            if in_table:
                html.append('</table></div>')
                in_table = False
            if not in_note:
                html.append('<div class="theory-note">')
                html.append('<div class="theory-note-title">Lưu ý</div>')
                in_note = True
            
            content = re.sub(r'^Lưu ý:?\s*', '', line, flags=re.IGNORECASE)
            if content:
                html.append(f'<p class="theory-text">{content}</p>')
            continue

        # Table
        if line.startswith('|'):
            if not in_table:
                html.append('<div style="overflow-x: auto; width: 100%;"><table class="theory-table">')
                in_table = True
            
            # check separator row
            if re.match(r'^\|[\s:-]+\|', line):
                continue
            
            # split cells
            cells_raw = re.split(r'(?<!\\)\|', line)
            cells = [c.strip() for c in cells_raw[1:-1]]
            
            # if this is the first row after <table>, it is a header
            if len(html) > 0 and html[-1] == '<div style="overflow-x: auto; width: 100%;"><table class="theory-table">':
                row = "<tr>" + "".join(f"<th>{c}</th>" for c in cells) + "</tr>"
                html.append(row)
            else:
                row = "<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
                html.append(row)
            continue
        elif in_table:
            html.append('</table></div>')
            in_table = False

        # Bullet List
        if line.startswith('- ') or line.startswith('* '):
            content_list = line[2:]
            html.append(f'<div class="theory-item"><span class="theory-bullet"></span><div>{content_list}</div></div>')
            continue

        # Ảnh
        line_img = re.sub(r'!\[\]\((.*?)\)', r'<div class="img-wrap"><img src="\1" alt="Math Image" style="max-width: 100%; height: auto;"></div>', line)
        if line_img != line:
            html.append(line_img)
            continue
            
        # Plain text
        html.append(f'<p class="theory-text">{line}</p>')
        
    if in_table:
        html.append('</table></div>')
    if in_note:
        html.append('</div>')
        
    return "\n".join(html)


def markdown_to_html_basic(text):
    if not text: return ""
    text = fix_math_display(text)
    text = text.replace('<br>', '\n')
    text = text.replace('<', '&lt;').replace('>', '&gt;')

    # Tách các khối $$...$$ để bảo toàn \n bên trong
    parts = re.split(r'(\$\$.*?\$\$)', text, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith('$$'):
            parts[i] = parts[i].replace('\n', '<br>')
            parts[i] = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', parts[i])
            parts[i] = re.sub(r'!\[\]\((.*?)\)', r'<div class="img-wrap"><img src="\1" alt="Math Image"></div>', parts[i])
    
    return "".join(parts)

def parse_markdown(md_content, title="Chuyên đề"):
    md_content = clean_ocr(md_content)
    theory_pattern = re.compile(r'##\s*PH.*?N\s*A', re.IGNORECASE)
    mcq_pattern = re.compile(r'##\s*PH.*?N\s*C', re.IGNORECASE)
    
    level_patterns = [
        {"id": "tb", "name": "Dành cho học sinh trung bình", "regex": re.compile(r'##\s*DÀNH\s*CHO\s*HỌC\s*SINH\s*TRUNG\s*B.*NH', re.IGNORECASE)},
        {"id": "kg", "name": "Dành cho học sinh khá giỏi", "regex": re.compile(r'##\s*DÀNH\s*CHO\s*HỌC\s*SINH\s*KHÁ\s*GIỎI', re.IGNORECASE)}
    ]
    
    theory_match = theory_pattern.search(md_content)
    mcq_match = mcq_pattern.search(md_content)
    
    theory_html = ""
    mcq_text = md_content
    
    if theory_match and mcq_match:
        theory_start = theory_match.start()
        theory_content_start = md_content.find('\n', theory_start)
        if theory_content_start == -1: theory_content_start = theory_match.end()
        mcq_start = mcq_match.start()
        theory_text = md_content[theory_content_start:mcq_start].strip()
        theory_html = markdown_to_theory_html(theory_text)
        mcq_content_start = md_content.find('\n', mcq_start)
        if mcq_content_start == -1: mcq_content_start = mcq_match.end()
        mcq_text = md_content[mcq_content_start:].strip()
    elif mcq_match:
        mcq_start = mcq_match.start()
        mcq_content_start = md_content.find('\n', mcq_start)
        mcq_text = md_content[mcq_content_start:].strip()

    level_positions = []
    for lp in level_patterns:
        for m in lp["regex"].finditer(mcq_text):
            level_positions.append({"pos": m.start(), "end": m.end(), "id": lp["id"], "name": lp["name"]})
    level_positions.sort(key=lambda x: x["pos"])
    
    fragments = []
    if not level_positions:
        fragments.append({"level_id": "none", "level_name": "", "text": mcq_text})
    else:
        if level_positions[0]["pos"] > 0:
            fragments.append({"level_id": "none", "level_name": "", "text": mcq_text[:level_positions[0]["pos"]]})
        for i in range(len(level_positions)):
            start = level_positions[i]["end"]
            end = level_positions[i+1]["pos"] if i+1 < len(level_positions) else len(mcq_text)
            fragments.append({
                "level_id": level_positions[i]["id"],
                "level_name": level_positions[i]["name"],
                "text": mcq_text[start:end]
            })

    questions_html = ""
    questions_html += f'''<div class="slide" data-i="0" id="slide-0">
            <div class="question-card cover-card">
                <div class="cover-top">
                    <div style="font-family:'Unbounded'; font-weight:900; font-size:24px; letter-spacing:-1px; color:#fff;">TOÁN CÁ CHÉP</div>
                    <div class="cover-eyebrow">Hệ thống Chuyên đề</div>
                </div>

                <div class="cover-middle">
                    <h1 class="cover-title">
                        {title}
                        <span class="cover-subject">Đại số - Giải tích</span>
                    </h1>
                    <p class="cover-subtitle">
                        Nắm vững lý thuyết, thành thạo bài tập phân mức Cơ bản và Nâng cao.
                    </p>
                    <div class="cover-badges">
                        <span class="cover-badge" style="cursor:pointer;" onclick="document.getElementById('levelPopup').classList.add('show')">CƠ BẢN & NÂNG CAO ▼</span>
                    </div>
                </div>

                <div class="cover-footer">
                    <div style="font-size: 13px; opacity: 0.8; font-family:'Manrope';">Lớp Toán Cá Chép · 2026</div>
                    <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1778198273/chuyende_assets/f6ahieihwhupukjagl8x.png" alt="Mascot Cá Chép" style="height: 80px; object-fit: contain;">
                </div>
                
                <div class="cover-mascot" style="font-size: 200px; color: rgba(255,255,255,0.05); line-height: 1;">🐟</div>
            </div>
        </div>
'''
    
    slide_idx = 1
    question_pattern = re.compile(r'Câu\s+(\d+)[\.\s:]+(.*?)(?=(Câu\s+\d+[\.\s:]+|##\s*DÀNH\s*CHO|$))', re.DOTALL | re.IGNORECASE)
    
    for frag in fragments:
        if frag["level_name"]:
            questions_html += f'<h2 class="level-header">{frag["level_name"]}</h2>'
            
        questions = question_pattern.finditer(frag["text"])
        for q in questions:
            q_num = q.group(1)
            raw_q_text = q.group(2).strip()
            
            sol_split = re.split(r'(?m)^(?:\s*##\s*)?(?:Lời giải|Giải|Đáp án:)', raw_q_text, maxsplit=1, flags=re.IGNORECASE)
            q_body = sol_split[0].strip()
            sol_body = sol_split[1].strip() if len(sol_split) > 1 else ""
            
            # Nếu không có Lời giải nhưng có ## Chọn X nằm trong q_body → tách ra
            chon_in_body = re.search(r'(?m)^\s*##\s*Chọn\s+[A-Da-d]', q_body)
            if chon_in_body and not sol_body:
                sol_body = q_body[chon_in_body.start():].strip()
                q_body = q_body[:chon_in_body.start()].strip()
            
            # Trích xuất đáp án đúng (SIÊU MẠNH MẼ - PHIÊN BẢN 2.0)
            correct_ans = ""
            
            # Cải tiến 1: Tìm cụm từ rõ ràng nhất trước
            ans_match = re.search(r'(?im)(?:Chọn|Đáp án|Chọn đáp án|=>|Vậy chọn|Do đó chọn)\s*[:\s]*[\$\\\{\}\*\_a-zA-Z]*(?:\bmathbf\b|\bmathrm\b|\bunderline\b)?[\{\\\s]*([A-Da-d])[\}]?[\$\\\{\}\*\_]*', raw_q_text)
            
            if not ans_match:
                # Cải tiến 2: Tìm chữ cái A,B,C,D đứng độc lập ở cuối câu với các dấu chấm, phẩy
                ans_match = re.search(r'(?im)(?:Chọn|Đáp án|Vậy)\s*[:\s]*([A-Da-d])(?:[\.\s]|$)', raw_q_text)
                
            if not ans_match:
                # Cải tiến 3: Bắt các trường hợp như "**A**", "**B.**" ở dòng cuối cùng
                ans_match = re.search(r'(?im)[\*\s]*([A-Da-d])[\.\*\s]*$', sol_body)
            
            if ans_match:
                correct_ans = ans_match.group(1).upper()
            else:
                print(f"[CẢNH BÁO] Không tìm thấy đáp án đúng cho Câu {q_num}. Vui lòng kiểm tra lại file Markdown gốc!")

            sol_text = re.sub(r'(?im)^\s*##\s*(?:Chọn|Đáp án|=>|Vậy chọn).*?$', '', sol_body).strip()
            sol_text = re.sub(r'(?im)^\s*(?:Chọn|Đáp án|=>|Vậy chọn).*?$', '', sol_text).strip()
            
            opts_match = re.split(r'\n(?=[A-Da-d][\.\s\)])', q_body)
            q_text = opts_match[0].strip()
            
            options = {}
            has_opts = False
            for opt in opts_match[1:]:
                has_opts = True
                opt_letter = opt[0].upper()
                opt_text = re.sub(r'^[A-Da-d][\.\s\)]+', '', opt).strip()
                options[opt_letter] = opt_text
                
            questions_html += f'''
            <div class="slide" data-i="{slide_idx}" id="slide-{slide_idx}">
            <div class="question-card" data-correct="{correct_ans}" data-level="{frag["level_id"]}">
                <div class="q-number">Câu {q_num}</div>
                <div class="q-content">{markdown_to_html_basic(q_text)}</div>
            '''
            if has_opts:
                questions_html += '<div class="options-grid">'
                for k in ['A', 'B', 'C', 'D']:
                    opt_val = options.get(k, '')
                    if opt_val:
                        # Remove trailing dot from the option text
                        clean_opt_val = re.sub(r'\.\s*$', '', opt_val)
                        questions_html += f'<div class="option" data-ans="{k}"><div class="opt-label">{k}.</div><div class="opt-text">{markdown_to_html_basic(clean_opt_val)}</div></div>'
                questions_html += '</div>'
            questions_html += f'''
                <div class="solution">
                    <div class="solution-title">Hướng dẫn giải</div>
                    <div class="sol-body">{markdown_to_html_basic(sol_text)}</div>
                    <div class="sol-final">→ Chọn đáp án <span class="ans-circle">{correct_ans}</span></div>
                </div>
            </div>
            </div>
            '''
            slide_idx += 1
    return theory_html, questions_html

def build_html(md_path, template_path, output_path, title):
    if not os.path.exists(md_path): return
    with open(md_path, 'r', encoding='utf-8') as f: md_content = f.read()
    theory_html, questions_html = parse_markdown(md_content, title)
    if not os.path.exists(template_path): return
    with open(template_path, 'r', encoding='utf-8') as f: template = f.read()
    html = template.replace('{{TITLE}}', title).replace('{{THEORY}}', theory_html).replace('{{CONTENT}}', questions_html)
    with open(output_path, 'w', encoding='utf-8') as f: f.write(html)
    print(f"[*] Da build thanh cong: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--md", required=True); parser.add_argument("--out", required=True); parser.add_argument("--title", default="Chuyên đề")
    args = parser.parse_args()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(script_dir, '..', 'template', 'chuyende_template.html')
    build_html(args.md, template_file, args.out, args.title)
