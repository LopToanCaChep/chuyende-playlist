import os
import sys
import glob

# 1. Tự động cài đặt các thư viện cần thiết
try:
    import fitz # PyMuPDF
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz

try:
    from PIL import Image, ImageChops
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageChops

# 2. Hàm tự động cắt lề trắng (Trim white borders)
def trim_white_borders(image_path, padding=20):
    img = Image.open(image_path).convert("RGB")
    bg = Image.new(img.mode, img.size, (255, 255, 255))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    
    if bbox:
        left, top, right, bottom = bbox
        left = max(0, left - padding)
        top = max(0, top - padding)
        right = min(img.size[0], right + padding)
        bottom = min(img.size[1], bottom + padding)
        
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(image_path, "PNG")
        print(f"  ✂️ Đã cắt lề trắng thành công cho: {os.path.basename(image_path)}")
    else:
        print(f"  ⚠️ Không phát hiện nội dung khác màu trắng để cắt: {os.path.basename(image_path)}")

def main():
    if len(sys.argv) < 2:
        print("❌ Thiếu tên chuyên đề!")
        print("Cách dùng: python scratch/pdf_to_images_cropped.py chuyende_05")
        sys.exit(1)
        
    chuyende = sys.argv[1] # ví dụ: chuyende_05
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pic_dir = os.path.join(base_dir, "01_Inputs", chuyende, "pic")
    
    if not os.path.exists(pic_dir):
        print(f"❌ Không tìm thấy thư mục pic tại: {pic_dir}")
        sys.exit(1)
        
    # Tìm kiếm file PDF lý thuyết
    pdf_files = glob.glob(os.path.join(pic_dir, "*.pdf"))
    if not pdf_files:
        print(f"❌ Không tìm thấy file PDF lý thuyết nào trong thư mục: {pic_dir}")
        sys.exit(1)
        
    # Ưu tiên file có chứa chữ "lythuyet" hoặc lấy file đầu tiên tìm thấy
    pdf_path = None
    for f in pdf_files:
        if "lythuyet" in os.path.basename(f).lower():
            pdf_path = f
            break
    if not pdf_path:
        pdf_path = pdf_files[0]
        
    print(f"📁 Thư mục làm việc: {pic_dir}")
    print(f"📄 Tìm thấy file PDF lý thuyết: {os.path.basename(pdf_path)}")
    
    # 3. Tách các trang PDF thành ảnh PNG nét cao
    doc = fitz.open(pdf_path)
    print(f"⏳ Đang xử lý tệp PDF gồm {len(doc)} trang...")
    
    created_files = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        zoom = 4.16 # ~300 DPI
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        output_filename = f"LT_Page_{page_num + 1}.png"
        output_filepath = os.path.join(pic_dir, output_filename)
        
        pix.save(output_filepath)
        trim_white_borders(output_filepath)
        created_files.append(output_filename)
        
    print(f"\n🎉 HOÀN THÀNH! Đã xuất {len(created_files)} ảnh lý thuyết sạch lề trắng cho {chuyende}!")

if __name__ == "__main__":
    main()
