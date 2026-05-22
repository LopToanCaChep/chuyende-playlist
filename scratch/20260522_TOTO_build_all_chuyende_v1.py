import os
import sys
import csv

# Cau hinh stdout sang UTF-8 de in tieng Viet tren Windows khong bi loi
if sys.version_info >= (3, 7):
    sys.stdout.reconfigure(encoding='utf-8')

# Them thu muc tools vao path de import build_html
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools')))
from build_html import build_html

MAPPING = {
    "chuyende_01": "01_Dai_so_to_hop.md",
    "chuyende_02": "Xac suat co dien.md",
    "chuyende_03": "03_Bai_toan_toi_uu_he_phuong_trinh_2_an.md",
    "chuyende_04": "04_Ham_so_bac_2_va_dau_tam_thuc_bac_2.md",
    "chuyende_05": "05_Ham_so_luong_giac.md",
    "chuyende_06": "06_Phuong_trinh_luong_giac.md",
    "chuyende_12": "12_Đao_Hàm.md"
}

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(base_dir, "quan_ly_chuyen_de.csv")
    processing_dir = os.path.join(base_dir, "02_Processing")
    outputs_dir = os.path.join(base_dir, "03_Outputs")
    template_path = os.path.join(base_dir, "template", "chuyende_template.html")

    print("=== BẮT ĐẦU BUILD TOÀN BỘ CHUYÊN ĐỀ ===")
    
    if not os.path.exists(csv_path):
        print(f"Lỗi: Không tìm thấy file {csv_path}")
        return

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        # Clean headers triet de
        headers = [h.replace('"', '').replace('\ufeff', '').strip() for h in header]
        print(f"Headers đã clean: {headers}")
        
        for row_data in reader:
            if not row_data:
                continue
            row = dict(zip(headers, [val.replace('"', '').strip() for val in row_data]))
            cd_id = row.get("ID_ChuyenDe")
            title = row.get("Ten_ChuyenDe")
            status = row.get("Trang_Thai")
            
            if cd_id in MAPPING:
                md_filename = MAPPING[cd_id]
                md_path = os.path.join(processing_dir, md_filename)
                out_path = os.path.join(outputs_dir, f"{cd_id}.html")
                
                # Check thay the ten file
                if md_filename == "Xac suat co dien.md":
                    md_path_real = os.path.join(processing_dir, "Xác suất cổ điển.md")
                else:
                    md_path_real = md_path
                
                if os.path.exists(md_path_real):
                    print(f"Build: {cd_id} ({title}) từ {os.path.basename(md_path_real)}...")
                    build_html(md_path_real, template_path, out_path, title)
                else:
                    print(f"Cảnh báo: File markdown {md_path_real} không tồn tại.")
            else:
                if status == "Hien" and row.get("So_Cau") != "0":
                    print(f"Cảnh báo: ID {cd_id} ({title}) không có trong mapping.")

    print("=== HOÀN THÀNH BUILD TOÀN BỘ ===")

if __name__ == "__main__":
    main()
