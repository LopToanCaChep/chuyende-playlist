# -*- coding: utf-8 -*-
import sys, re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_06.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Cập nhật CSS lý thuyết
css_template = """/* ── Theory Heading System (3 cấp) ── */
    .theory-h2 {
        font-family: 'Unbounded'; font-weight: 800; font-size: 20px;
        color: var(--dark-blue, #003b99); margin: 40px 0 8px;
        letter-spacing: 0.3px; line-height: 1.4;
    }

    .theory-h2::before { display: none; }

    .theory-h3 {
        font-family: 'Manrope'; font-weight: 700; font-size: 17px;
        color: #334155; margin: 28px 0 12px;
        line-height: 1.5;
    }

    /* ── Theory Blocks (4 loại card pastel) ── */
    .theory-block {
        padding: 20px 22px; border-radius: 16px; margin: 18px 0;
    }
    .theory-block-title {
        font-family: 'Manrope'; font-weight: 800; font-size: 14px;
        margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.6px;
    }
    .theory-block .theory-text, .theory-block .theory-item {
        margin-bottom: 8px;
    }

    /* Lý thuyết tổng — Xanh lá cây pastel */
    .theory-block.summary {
        background: #f0fdf4; /* emerald-50 pastel */
        border: 1px solid #dcfce7;
    }
    .theory-block.summary .theory-block-title { color: #16a34a; }
    .theory-block.summary .theory-bullet { background: #22c55e; }
    .theory-block.summary .theory-text { color: #14532d; }

    /* Phương pháp giải — Xanh dương pastel */
    .theory-block.method {
        background: #eff6ff;
        border: 1px solid #dbeafe;
    }
    .theory-block.method .theory-block-title { color: #2563eb; }
    .theory-block.method .theory-bullet { background: #3b82f6; }

    /* Lưu ý — Đỏ/hồng pastel */
    .theory-block.warning {
        background: #fef2f2;
        border: 1px solid #fee2e2;
    }
    .theory-block.warning .theory-block-title { color: #dc2626; }
    .theory-block.warning .theory-bullet { background: #ef4444; }
    .theory-block.warning .theory-text { color: #7f1d1d; }

    /* Mẹo — Vàng/amber pastel */
    .theory-block.tip {
        background: #fffbeb;
        border: 1px solid #fef3c7;
    }
    .theory-block.tip .theory-block-title { color: #d97706; }
    .theory-block.tip .theory-bullet { background: #f59e0b; }
    .theory-block.tip .theory-text { color: #92400e; }

    /* ── Divider giữa các Dạng ── */
    .theory-divider {
        border: none; border-top: 1px solid #e2e8f0;
        margin: 36px 0;
    }

    /* ── Theory Items & Bullets ── */
    .theory-item {
        display: flex; gap: 12px; margin-bottom: 12px; align-items: flex-start;
    }
    .theory-bullet {
        width: 6px; height: 6px; background: #94a3b8;
        border-radius: 50%; margin-top: 10px; flex-shrink: 0;
    }

    /* ── Legacy classes (giữ tương thích) ── */
    .theory-box {
        padding: 20px; border-radius: 16px; margin: 24px 0;
        background: #f8fafc;
    }
    .theory-box-title {
        font-family: 'Manrope'; font-weight: 800; font-size: 12px;
        margin-bottom: 12px; color: var(--primary-blue, #2563eb);
    }
    .theory-note {
        padding: 20px 24px; border-radius: 16px; margin: 24px 0;
        background: #fffbeb;
    }
    .theory-note-title {
        font-family: 'Manrope'; font-weight: 800; font-size: 14px;
        color: #d97706; margin-bottom: 12px;
        text-transform: uppercase; letter-spacing: 0.5px;
    }
    .theory-note .theory-text, .theory-note .theory-item { color: #92400e; margin-bottom: 10px; }
    .theory-note .theory-bullet { background: #d97706; }

    /* ── Theory Table ── */
    .theory-table {
        width: 100%; border-collapse: separate; border-spacing: 0;
        margin: 24px 0; border-radius: 12px; overflow: hidden;
        border: 1px solid var(--border, #e2e8f0);
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .theory-table th {
        background: #f8fafc; color: var(--text-main, #1e293b); font-weight: 800;
        padding: 16px; text-align: left; border-bottom: 2px solid var(--border, #e2e8f0);
    }
    .theory-table td {
        padding: 16px; border-bottom: 1px solid var(--border, #e2e8f0); background: #fff;
    }
    .theory-table tr:last-child td { border-bottom: none; }

    .theory-text { font-size: 16px; line-height: 1.8; color: #334155; }


    /* Screen reader only */
    .sr-only {
        position: absolute !important;
        width: 1px; height: 1px; padding: 0; margin: -1px;
        overflow: hidden; clip: rect(0,0,0,0);
        white-space: nowrap; border: 0;
    }

    /* Score chip — góc phải trên */
    .score-chip {
        position: fixed; top: 23px; right: 20px;
        background: rgba(255,255,255,0.98); color: var(--dark-blue);
        border: none;
        border-radius: 12px; padding: 6px 14px;
        font-family: 'Manrope', sans-serif; font-weight: 800;
        text-align: center; z-index: 200;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        min-width: 70px;
    }
    @media (max-width: 768px) {
        .score-chip { top: 60px; right: 12px; padding: 4px 10px; min-width: 56px; }
        .score-chip span:last-child { font-size: 16px !important; }
        .question-card::before {
            right: 24px;
            left: auto;
            top: 10px;
            display: block;
            font-size: 9px;
            padding: 2px 8px;
        }
    }"""

# Thay thế phần CSS lý thuyết cũ
css_start = content.find("/* ── Theory Heading System")
css_end = content.find("/* Final score modal")
if css_start >= 0 and css_end >= 0:
    content = content[:css_start] + css_template + "\n\n        " + content[css_end:]
    print("✅ Đã cập nhật CSS lý thuyết")
else:
    print("❌ Không tìm thấy vùng CSS lý thuyết để thay thế")

# 2. Cập nhật HTML lý thuyết (theoryModal)
new_html_theory = """            <div class="theory-text" id="theory-content"
                style="font-size:16px; line-height:1.8; color:#334155; padding: 10px 0;">
                
                <!-- Lý thuyết tổng: Công thức lượng giác -->
                <div class="theory-block summary">
                    <div class="theory-block-title">Công thức lượng giác</div>
                    <div class="img-wrap"><img
                            src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779413099/chuyende_06/a5vhtl9dqpaomljitslr.png"
                            alt="Công thức lượng giác cơ bản" style="max-width: 100%; height: auto; border-radius: 12px;">
                    </div>
                    <div class="img-wrap"><img
                            src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779413102/chuyende_06/cantd9daftmvfx0khynv.png"
                            alt="Công thức cộng và hệ thức liên hệ giữa các cung đặc biệt"
                            style="max-width: 100%; height: auto; border-radius: 12px;"></div>
                </div>

                <hr class="theory-divider">
                <div class="theory-h2">Dạng 1 - Phương trình lượng giác cơ bản</div>
                
                <!-- 1. Phương trình sin x = m -->
                <div class="theory-block summary">
                    <div class="theory-block-title">1. Phương trình $\\sin x = m$</div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Nếu $\\left[\\begin{array}{l}m&gt;1 \\\\ m&lt;-1\\end{array}\\right.$ thì phương trình $\\sin x = m$ vô nghiệm.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Nếu $-1 \\leq m \\leq 1$ thì phương trình $\\sin x = m$ có nghiệm.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $\\displaystyle m \\in\\left\\{0 ; \\pm \\frac{1}{2} ; \\pm \\frac{\\sqrt{2}}{2} ; \\pm \\frac{\\sqrt{3}}{2} ; \\pm 1\\right\\}$ thì áp dụng công thức: $\\sin x=\\sin \\alpha \\Leftrightarrow\\left[\\begin{array}{l}x=\\alpha+k 2 \\pi \\\\ x=\\pi-\\alpha+k 2 \\pi\\end{array}\\right., k \\in \\mathbb{Z}$.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $m$ không thỏa điều trên thì đặt $\\displaystyle m=\\sin \\alpha, \\alpha \\in\\left[-\\frac{\\pi}{2} ; \\frac{\\pi}{2}\\right]$. Khi đó phương trình trở thành $\\sin x=\\sin \\alpha$ và tiếp tục giải như vế trên.</div>
                    </div>
                </div>

                <!-- 2. Phương trình cos x = m -->
                <div class="theory-block summary">
                    <div class="theory-block-title">2. Phương trình $\\cos x = m$</div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Nếu $\\left[\\begin{array}{l}m&gt;1 \\\\ m&lt;-1\\end{array}\\right.$ thì phương trình $\\cos x = m$ vô nghiệm.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Nếu $-1 \\leq m \\leq 1$ thì phương trình $\\cos x = m$ có nghiệm.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $\\displaystyle m \\in\\left\\{0 ; \\pm \\frac{1}{2} ; \\pm \\frac{\\sqrt{2}}{2} ; \\pm \\frac{\\sqrt{3}}{2} ; \\pm 1\\right\\}$ thì áp dụng công thức: $\\cos x=\\cos \\alpha \\Leftrightarrow\\left[\\begin{array}{l}x=\\alpha+k 2 \\pi \\\\ x=-\\alpha+k 2 \\pi\\end{array}\\right., k \\in \\mathbb{Z}$.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $m$ không thỏa điều trên thì đặt: $m=\\cos \\alpha, \\alpha \\in[0 ; \\pi]$. Khi đó phương trình trở thành $\\cos x=\\cos \\alpha$ và tiếp tục giải như vế trên.</div>
                    </div>
                </div>

                <!-- 3. Phương trình tan x = m -->
                <div class="theory-block summary">
                    <div class="theory-block-title">3. Phương trình $\\tan x = m$</div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với mọi $m$, phương trình $\\tan x=m$ luôn có nghiệm thỏa điều kiện $\\displaystyle x \\neq \\frac{\\pi}{2}+k \\pi$.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Xét phương trình $\\tan x=m$ :</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $\\displaystyle m \\in\\left\\{0 ; \\pm \\frac{1}{\\sqrt{3}} ; \\pm 1 ; \\pm \\sqrt{3}\\right\\}$ thì áp dụng công thức: $\\tan x=\\tan \\alpha \\Leftrightarrow x=\\alpha+k \\pi, k \\in \\mathbb{Z}$.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $m$ không thỏa các điều trên thì đặt $\\displaystyle m=\\tan \\alpha, \\alpha \\in\\left(-\\frac{\\pi}{2} ; \\frac{\\pi}{2}\\right)$. Khi đó phương trình trở thành $\\tan x=\\tan \\alpha$ và tiếp tục giải như vế trên.</div>
                    </div>
                </div>

                <!-- 4. Phương trình cot x = m -->
                <div class="theory-block summary">
                    <div class="theory-block-title">4. Phương trình $\\cot x = m$</div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với mọi $m$, phương trình $\\cot x=m$ luôn có nghiệm thỏa điều kiện $x \\neq k \\pi$.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Xét phương trình $\\cot x=m$ :</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $\\displaystyle m \\in\\left\\{0 ; \\pm \\frac{1}{\\sqrt{3}} ; \\pm 1 ; \\pm \\sqrt{3}\\right\\}$ thì áp dụng công thức: $\\cot x=\\cot \\alpha \\Leftrightarrow x=\\alpha+k \\pi, k \\in \\mathbb{Z}$.</div>
                    </div>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>Với $m$ không thỏa các điều trên thì đặt $m=\\cot \\alpha, \\alpha \\in(0 ; \\pi)$. Khi đó phương trình trở thành $\\cot x=\\cot \\alpha$ và tiếp tục giải như vế trên.</div>
                    </div>
                </div>

                <hr class="theory-divider">
                <div class="theory-h2">Dạng 2 - Tìm nghiệm thuộc khoảng, đoạn cho trước</div>
                
                <div class="theory-block method">
                    <div class="theory-block-title">Phương pháp giải</div>
                    <p class="theory-text">Bước 1. Giải phương trình lượng giác đã cho và tìm các họ nghiệm (nếu có)</p>
                    <p class="theory-text">Bước 2. Với mỗi họ nghiệm tìm được ở Bước 1, ta cho thuộc khoảng (đoạn) theo giả thiết và cô lập $k$.</p>
                    <p class="theory-text">Bước 3. Ứng với mỗi giá trị $k$ nguyên vừa tìm được, thế vào họ nghiệm ban đầu để tìm nghiệm tương ứng.</p>
                    <p class="theory-text">Bước 4. So sánh với điều kiện xác định (nếu có) để loại nghiệm không thỏa.</p>
                </div>

                <div class="theory-h3">Ví dụ 2.1 - Tìm nghiệm thuộc khoảng $\\displaystyle \\left(-\\frac{\\pi}{4} ; 2 \\pi\\right)$</div>
                <div class="theory-block method">
                    <div class="theory-block-title">Lời giải</div>
                    <p class="theory-text">$\\displaystyle \\cdot \\sin \\left(\\frac{\\pi}{6}+2 x\\right)=-1 \\Leftrightarrow \\frac{\\pi}{6}+2 x=-\\frac{\\pi}{2}+k 2 \\pi \\Leftrightarrow x=-\\frac{\\pi}{3}+k \\pi$.</p>
                    <div class="theory-item"><span class="theory-bullet"></span>
                        <div>YCBT $\\displaystyle \\Leftrightarrow-\\frac{\\pi}{4}&lt;-\\frac{\\pi}{3}+k \\pi&lt;2 \\pi \\Leftrightarrow \\frac{7}{12}&lt;k&lt;\\frac{7}{3} \\Leftrightarrow 0,58&lt;k&lt;2,33$. Vì $k \\in \\mathbb{Z}$ nên $\\displaystyle \\left[\\begin{array}{l}k=1 \\Rightarrow x=\\frac{2 \\pi}{3} \\\\ k=2 \\Rightarrow x=\\frac{5 \\pi}{3}\\end{array}\\right.$.</div>
                    </div>
                </div>

                <div class="theory-block warning">
                    <div class="theory-block-title">Lưu ý</div>
                    <p class="theory-text">1. Số giá trị $k$ ứng với số nghiệm thuộc khoảng cho trước.</p>
                    <p class="theory-text">2. Nếu đề bài yêu cầu số vị trí biểu diễn các nghiệm trên đường tròn lượng giác:</p>
                    <p class="theory-text"><strong>Cách 1:</strong> Ta giải họ nghiệm thuộc nửa khoảng $[0 ; 2 \\pi)$.</p>
                    <p class="theory-text"><strong>Cách 2:</strong> Lấy $\\displaystyle \\frac{2 \\pi}{m}$ hoặc $\\displaystyle \\frac{360^{\circ}}{m}$ (tùy vào đơn vị góc) với $m$ là hệ số gắn với biến chạy $k$ trong họ nghiệm.</p>
                    <p class="theory-text">Nếu ra số nguyên thì lấy luôn, còn chưa nguyên thì nhân với một nguyên lượng để ra số nguyên gần nhất.</p>
                    <p class="theory-text">3. Nếu đề bài tìm nghiệm dương nhỏ nhất thì ta giải "họ nghiệm $&gt;0$" và lấy $k_{\\min}$ từ đó suy ra nghiệm.</p>
                    <p class="theory-text">Nếu đề bài tìm nghiệm âm lớn nhất thì ta giải "họ nghiệm $&lt;0$" và lấy $k_{\\max}$ từ đó suy ra nghiệm.</p>
                </div>

                <div class="theory-block tip">
                    <div class="theory-block-title">Ví dụ minh họa điểm biểu diễn</div>
                    <p class="theory-text"><strong>Ví dụ 2.2:</strong> Số điểm biểu diễn trên đường tròn lượng giác của họ nghiệm $\\displaystyle x=\\frac{\\pi}{3}+k \\pi$ là $\\displaystyle \\frac{2 \\pi}{\\pi}=2$ điểm.</p>
                    <p class="theory-text"><strong>Ví dụ 2.3:</strong> Số điểm biểu diễn trên đường tròn lượng giác của họ nghiệm $x=60^{\circ}+k \\cdot 80^{\circ}$:</p>
                    <p class="theory-text">Ta tính $\\displaystyle \\frac{360^{\circ}}{80^{\circ}}=\\frac{9}{2}$ (chưa là số nguyên), do đó ta nhân thêm mẫu số của phân số tối giản (ở đây là 2) để được: $\\displaystyle \\frac{9}{2} \\cdot 2 = 9$ điểm.</p>
                </div>

                <hr class="theory-divider">
                <div class="theory-h2">Dạng 3 - Tìm điều kiện tham số để phương trình có nghiệm</div>
                
                <div class="theory-block method">
                    <div class="theory-block-title">Phương pháp giải</div>
                    <p class="theory-text">Bước 1. Cô lập $m$, đưa phương trình về dạng $f(x)=m$.</p>
                    <p class="theory-text">Bước 2. Tìm miền giá trị $[a ; b]$ của hàm số $y=f(x)$.</p>
                    <p class="theory-text">Bước 3. Kết luận, để phương trình $f(x)=m$ có nghiệm thì $m \\in[a ; b]$.</p>
                </div>

                <div class="theory-block warning">
                    <div class="theory-block-title">Lưu ý</div>
                    <p class="theory-text">1. Để tìm $[a;b]$ thì xem lại dạng toán tìm GTLN, GTNN của hàm số.</p>
                    <p class="theory-text">2. Nếu đổi biến, nhớ tìm miền giá trị của biến mới.</p>
                    <p class="theory-text">3. Nhớ cách xét dấu tam thức bậc 2.</p>
                </div>

                <div class="theory-h3">Ví dụ 4 - Tìm $m$ để phương trình lượng giác sau có nghiệm: $2 \\sin 3 x=m-1$</div>
                <div class="theory-block method">
                    <div class="theory-block-title">Lời giải</div>
                    <p class="theory-text">$\\displaystyle \\cdot 2 \\sin 3 x=m-1 \\Leftrightarrow \\sin 3 x=\\frac{m-1}{2}$</p>
                    <p class="theory-text">Vì $-1 \\leq \\sin 3 x \\leq 1$ nên để phương trình có nghiệm thì $\\displaystyle -1 \\leq \\frac{m-1}{2} \\leq 1 \\Leftrightarrow -2 \\leq m-1 \\leq 2 \\Leftrightarrow -1 \\leq m \\leq 3$.</p>
                </div>

                <hr class="theory-divider">
                <div class="theory-h2">Dạng 4 - Biến đổi về phương trình lượng giác cơ bản</div>
                
                <div class="theory-block method">
                    <div class="theory-block-title">Phương pháp giải</div>
                    <p class="theory-text">Vận dụng các công thức đã được học để đưa về các phương trình cùng loại:</p>
                    <p class="theory-text">1. Đổi từ $\\sin x$ sang $\\displaystyle \\cos x: \\sin x=\\cos \\left(\\frac{\\pi}{2}-x\\right)=\\cos \\left(x-\\frac{\\pi}{2}\\right)$.</p>
                    <p class="theory-text">2. Đổi từ $\\cos x$ sang $\\displaystyle \\sin x: \\cos x=\\sin \\left(\\frac{\\pi}{2}-x\\right)=\\sin \\left(x+\\frac{\\pi}{2}\\right)$.</p>
                    <p class="theory-text">3. Đổi từ $\\tan x$ sang $\\displaystyle \\cot x: \\tan x=\\cot \\left(\\frac{\\pi}{2}-x\\right)$.</p>
                    <p class="theory-text">4. Đổi từ $\\cot x$ sang $\\displaystyle \\tan x: \\cot x=\\tan \\left(\\frac{\\pi}{2}-x\\right)$.</p>
                    <p class="theory-text">5. Sử dụng công thức hạ bậc.</p>
                    <p class="theory-text">6. Tích thành tổng.</p>
                    <p class="theory-text">7. Tổng thành tích.</p>
                </div>
            </div>"""

# Định vị phần lý thuyết trong content
ts_html = content.find('<div class="theory-text" id="theory-content"')
# Tìm thẻ đóng của theory-content trước script
te_script = content.find('<script>', ts_html)
# Tìm thẻ đóng </div> cuối cùng trước <script>
te_div = content.rfind('</div>', ts_html, te_script)
# Để chắc chắn, ta xem các div kết thúc.
# Đoạn kết thúc của theoryModal:
#             </div>
#         </div>
#     </div>
# </div>
# Chúng ta muốn thay thế từ '<div class="theory-text" id="theory-content"'
# đến hết thẻ đóng của 'theory-content'.
# Theo cấu trúc nguyên bản:
# <div class="theory-text" id="theory-content"...>
# ...
# </div> (kết thúc theory-text)
# Cần tìm thẻ đóng div kết thúc cho theory-content.
# Ta sẽ dùng thuật toán đếm thẻ mở/đóng div từ ts_html để xác định đúng thẻ đóng div của theory-text.

def find_closing_div(html, start_pos):
    pos = start_pos
    # Bỏ qua '<div' đầu tiên
    open_divs = 1
    pos = html.find('<div', pos + 1)
    
    # Duyệt qua các tag <div và </div
    current_pos = start_pos + 1
    while open_divs > 0:
        next_open = html.find('<div', current_pos)
        next_close = html.find('</div>', current_pos)
        
        if next_close == -1:
            break
            
        if next_open != -1 and next_open < next_close:
            open_divs += 1
            current_pos = next_open + 4
        else:
            open_divs -= 1
            current_pos = next_close + 6
            
    return current_pos - 6

closing_pos = find_closing_div(content, ts_html)
print(f"ts_html: {ts_html}, closing_pos: {closing_pos}")

# Cắt và chèn
content_new = content[:ts_html] + new_html_theory + content[closing_pos + 6:]

# Lưu file
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content_new)

print("✅ Đã cập nhật HTML lý thuyết và sửa lỗi thẻ div thành công!")
