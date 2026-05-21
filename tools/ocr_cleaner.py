import re

def clean_ocr(text):
    """
    Bộ tiền xử lý (Pre-processor) dọn rác OCR trước khi Build HTML.
    Kế thừa từ ERROR_LIBRARY của Toán Cá Chép.
    """
    if not text: return ""
    
    # 1. Dọn rác "Hình X" (OCR đọc dính chú thích ảnh)
    text = re.sub(r'(?mi)^H[iì]nh\s*\d+\s*$', '', text)
    
    # 2. Sửa lỗi thiếu chữ "## " trước đáp án (VD: "Chọn A" thay vì "## Chọn A")
    # Thay thế "Chọn [A-D]" thành "## Chọn [A-D]" nếu đầu dòng không có ##
    text = re.sub(r'(?mi)^(?!\s*##\s*)(?:Đáp án:\s*|Lời giải:\s*)?Chọn\s*([A-Da-d])\s*\.?\s*$', r'## Chọn \1', text)
    
    # 3. Dọn dẹp khoảng trắng dư thừa và chữ Lời giải mồ côi
    text = re.sub(r'(?im)^\s*(?:##\s*)?Lời giải\.?\s*$', '## Lời giải', text)

    # 4. (Tương lai) Có thể bổ sung Regex sửa ngoặc ở đây nếu Mathpix sai hệ thống.
    # VD: text = text.replace(r'\quad', '') # (Nguy hiểm, cần cẩn thận)
    
    return text
