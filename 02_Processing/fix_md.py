import re
import os

md_path = '02_Processing/01_Dai_so_to_hop.md'
with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix wrong answers
ans_fixes = {
    '9': 'A', '10': 'B', '16': 'B', '25': 'D', '33': 'B', '34': 'B',
    '36': 'B', '38': 'D', '39': 'D', '41': 'D', '44': 'D', '49': 'A', '51': 'D'
}

def replace_ans(match):
    q_num = match.group(1)
    q_body = match.group(2)
    
    if q_num in ans_fixes:
        new_ans = ans_fixes[q_num]
        q_body = re.sub(r'(##\s*(?:Chọn|Đáp án)\s*.*?[A-D].*)', lambda m: re.sub(r'[A-D]', new_ans, m.group(1)), q_body)
    
    # 2. Cau 58
    if q_num == '58':
        q_body = re.sub(r'C\.\s*\d+\s*\.', r'C. 1050 .', q_body)
        q_body = re.sub(r'ban nam', 'ba nam', q_body)
        # Sửa lời giải TH1 của câu 58
        q_body = re.sub(
            r'Số cách chia là: C_7\^1 \\cdot C_3\^1 \\cdot C_6\^3 \\cdot C_2\^1=840 \(cách\)\.',
            r'Tức là $\\frac{C_7^1 \\cdot C_3^1 \\cdot C_6^3 \\cdot C_2^1}{2!} = \\mathbf{420}$ (cách).',
            q_body
        )
        q_body = re.sub(
            r'Suy ra có: 840\+630=1470 \(cách\)\.',
            r'TH2 tính đúng là $630$. Vậy tổng đúng của bài này chỉ là $420 + 630 = \\mathbf{1050 \\text{ cách}}$.',
            q_body
        )

    # 3. Cau 49
    if q_num == '49':
        q_body = re.sub(r'Vậy có 30\+150\+200\+75=455\.', 
            'Số cách chọn 5 bông hoa tùy ý từ 11 bông (gồm vàng và trắng) là $C_{11}^5 = 462$.\n'
            'Số cách chọn 5 bông chỉ toàn màu vàng là $C_6^5 = 6$.\n'
            'Số cách chọn 5 bông chỉ toàn màu trắng là $C_5^5 = 1$.\n'
            'Vậy số cách chọn bó hoa có đủ 2 màu là: $462 - 6 - 1 = 455$ (cách).', q_body)

    # 4. Add missing sol body
    missing_sol = {
        '1': r'Công việc được hoàn thành bởi một trong hai hành động độc lập. Theo quy tắc cộng, ta có $a + b$ cách để hoàn thành.',
        '2': r'Công việc phải trải qua 2 hành động liên tiếp. Theo quy tắc nhân, ta có $a \cdot b$ cách để hoàn thành.',
        '3': r'Vì bạn An chỉ mượn 1 quyển sách nên có thể mượn sách Toán hoặc Vật lí. Theo quy tắc cộng, An có $100 + 120 = 220$ cách chọn.',
        '4': r'Theo công thức tính số chỉnh hợp chập $k$ của $n$ phần tử, ta có: $A_{n}^{k} = \frac{n!}{(n-k)!} = n(n-1) \ldots(n-k+1)$.',
        '5': r'Tổ hợp chập $k$ của $n$ phần tử là một tập con gồm $k$ phần tử được lấy ra từ $n$ phần tử của tập hợp $A$ (không phân biệt thứ tự).',
        '6': r'Khẳng định sai là B. Công thức đúng của tổ hợp là $C_{n}^{k}=\frac{n!}{(n-k)!k!}$. Công thức ở đáp án B thực chất là của chỉnh hợp.',
        '21': r'Theo định nghĩa, số chỉnh hợp chập $k$ của $n$ phần tử được tính bằng công thức: $A_{n}^{k}=\frac{n!}{(n-k)!}$.',
        '27': r'Chọn 2 nam từ 16 nam có $C_{16}^2$ cách. Chọn 3 nữ từ 18 nữ có $C_{18}^3$ cách. Theo quy tắc nhân, ta có $C_{16}^2 \cdot C_{18}^3$ cách.'
    }
    if q_num in missing_sol:
        safe_sol = missing_sol[q_num].replace('\\', '\\\\')
        q_body = re.sub(r'(##\s*Lời giải\s*\n)(##\s*(?:Chọn|Đáp án))', r'\1' + safe_sol + r'\n\n\2', q_body)

    # 5. Typo
    if q_num == '4':
        q_body = q_body.replace(r'$A_{n}=n(n-1) \ldots(n-k+1)$', r'$A_{n}^{k} = n(n-1) \ldots(n-k+1)$')
    if q_num == '46':
        q_body = q_body.replace('1,2 , 3', '1, 2, 3')
    if q_num == '54':
        q_body = q_body.replace(r'\{1 ; 2 ; 3 ; 4 ; 5\}', r'$\{1 ; 2 ; 3 ; 4 ; 5\}$')
        q_body = q_body.replace(r'P 5=5 !', r'$P_{5} = 5!$')

    return f"Câu {q_num}. {q_body}"

# Use regex to find and replace each question block
new_text = re.sub(r'Câu\s+(\d+)[\.\s:]+(.*?)(?=(Câu\s+\d+[\.\s:]+|##\s*DÀNH\s*CHO|$))', replace_ans, text, flags=re.DOTALL | re.IGNORECASE)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Done")
