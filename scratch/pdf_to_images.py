import os
import sys

# 1. Tự động cài đặt pymupdf nếu chưa có
try:
    import fitz # PyMuPDF
    print("PyMuPDF đã được cài đặt sẵn.")
except ImportError:
    print("Chưa cài PyMuPDF. Đang tiến hành cài đặt...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz
    print("Cài đặt PyMuPDF thành công!")

# 2. Định nghĩa đường dẫn
pdf_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\01_Inputs\chuyende_06\pic\lythuyetcd6.pdf"
output_dir = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\01_Inputs\chuyende_06\pic"

if not os.path.exists(pdf_path):
    print(f"❌ Không tìm thấy file PDF tại: {pdf_path}")
    sys.exit(1)

# 3. Tách các trang PDF thành ảnh PNG nét cao (300 DPI)
doc = fitz.open(pdf_path)
print(f"📄 Tệp PDF có {len(doc)} trang.")

created_files = []
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    
    # Thiết lập độ phân giải 300 DPI bằng cách tăng scale (mặc định là 72 DPI, 300 / 72 ≈ 4.16)
    zoom = 4.16
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    
    # Đặt tên ảnh đầu ra
    output_filename = f"LT_Page_{page_num + 1}.png"
    output_filepath = os.path.join(output_dir, output_filename)
    
    pix.save(output_filepath)
    print(f"  ✅ Đã xuất: {output_filename}")
    created_files.append(output_filename)

print("\n🎉 Hoàn thành tách trang PDF thành ảnh chất lượng cao!")
print(f"Tổng cộng đã tạo ra {len(created_files)} ảnh trong thư mục {output_dir}")
