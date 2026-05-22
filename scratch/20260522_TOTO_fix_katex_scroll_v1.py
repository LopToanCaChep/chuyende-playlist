import os
import re

def fix_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Pattern 1: Tìm block .katex {...} có chứa overflow-x: auto; và sửa thành overflow: visible !important;
    # Sử dụng Regex để match chính xác block .katex và các thuộc tính của nó
    pattern = r'(\.katex\s*\{[^}]*?)(overflow-x:\s*auto;?\s*|overflow-y:\s*hidden;?\s*)+'
    
    # Thay thế cả overflow-x và overflow-y bằng overflow: visible !important;
    # Đầu tiên xem thử có match không
    if re.search(r'\.katex\s*\{[^}]*?overflow-x:\s*auto', content):
        # Ta sẽ dùng regex thay thế chính xác nội dung bên trong block .katex
        def replace_katex_props(match):
            block = match.group(0)
            # Thay thế các thuộc tính overflow
            block = re.sub(r'overflow-x:\s*auto;?', 'overflow: visible !important;', block)
            block = re.sub(r'overflow-y:\s*hidden;?', '', block)
            return block
            
        new_content = re.sub(r'\.katex\s*\{[^}]+?\}', replace_katex_props, content)
        
        # Ghi đè lại file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully fixed KaTeX scroll in: {file_path}")
        return True
    else:
        print(f"No KaTeX scroll issue found in: {file_path}")
        return False

def main():
    base_dir = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web"
    
    # 1. Sửa file template
    template_path = os.path.join(base_dir, "template", "chuyende_template.html")
    fix_file(template_path)
    
    # 2. Sửa các file HTML trong 03_Outputs
    outputs_dir = os.path.join(base_dir, "03_Outputs")
    if os.path.exists(outputs_dir):
        for file_name in os.listdir(outputs_dir):
            if file_name.endswith(".html"):
                file_path = os.path.join(outputs_dir, file_name)
                fix_file(file_path)

if __name__ == "__main__":
    main()
