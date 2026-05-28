import os
import sys

# 1. Tự động cài đặt pymupdf và pillow nếu chưa có
try:
    import fitz # PyMuPDF
    print("PyMuPDF đã được cài đặt.")
except ImportError:
    print("Đang cài PyMuPDF...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz

try:
    from PIL import Image, ImageChops
    print("Pillow đã được cài đặt.")
except ImportError:
    print("Đang cài Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageChops

# 2. Hàm tự động cắt lề trắng (Trim white borders)
def trim_white_borders(image_path, tolerance=240):
    img = Image.open(image_path).convert("RGB")
    
    # Tạo ảnh nền trắng tinh cùng kích thước
    bg = Image.new(img.mode, img.size, (255, 255, 255))
    
    # Tính sự khác biệt giữa ảnh gốc và nền trắng
    diff = ImageChops.difference(img, bg)
    
    # Tăng cường độ tương phản của phần khác biệt để lọc các pixel gần trắng
    diff = ImageChops.add(diff, diff, 2.0, -100)
    
    # Lấy bounding box của vùng chứa nội dung (non-white)
    bbox = diff.getbbox()
    
    if bbox:
        # Thêm một chút padding (khoảng 20 pixel) để ảnh không bị sát viền nội dung quá
        left, top, right, bottom = bbox
        left = max(0, left - 20)
        top = max(0, top - 20)
        right = min(img.size[0], right + 20)
        bottom = min(img.size[1], bottom + 20)
        
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(image_path, "PNG")
        print(f"  ✂️ Đã cắt lề trắng thành công cho: {os.path.basename(image_path)}")
    else:
        print(f"  ⚠️ Không phát hiện nội dung khác màu trắng để cắt: {os.path.basename(image_path)}")

# 3. Định nghĩa đường dẫn
pdf_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\01_Inputs\chuyende_06\pic\lythuyetcd6.pdf"
output_dir = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\01_Inputs\chuyende_06\pic"

if not os.path.exists(pdf_path):
    print(f"❌ Không tìm thấy file PDF tại: {pdf_path}")
    sys.exit(1)

# 4. Tách các trang PDF thành ảnh PNG nét cao
doc = fitz.open(pdf_path)
print(f"📄 Tiến hành xử lý file PDF ({len(doc)} trang)...")

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    zoom = 4.16 # ~300 DPI
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    
    output_filename = f"LT_Page_{page_num + 1}.png"
    output_filepath = os.path.join(output_dir, output_filename)
    
    # Lưu ảnh thô tạm thời
    pix.save(output_filepath)
    
    # Tiến hành cắt lề trắng
    trim_white_borders(output_filepath)

print("\n🎉 HOÀN THÀNH! Toàn bộ 5 trang lý thuyết đã được tách và tự động cắt sạch lề trắng dư thừa.")
