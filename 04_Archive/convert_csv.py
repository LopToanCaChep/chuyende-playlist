
import csv

# Read Phan_chia_chuyen_de.csv
input_file = "Phan_chia_chuyen_de.csv"
output_file = "quan_ly_chuyen_de.csv"

topics = []
with open(input_file, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        topics.append(row)

# Format for quan_ly_chuyen_de.csv
# ID_ChuyenDe,Ten_ChuyenDe,Mon_Hoc,Lop,So_Cau,Mat_Khau,Trang_Thai

out_rows = []
for topic in topics:
    stt = int(topic["Số thự tự"])
    id_cd = f"chuyende_{stt:02d}"
    ten = f"Chuyên đề {stt} - {topic['Tên chuyên đề']}"
    lop = topic["Lớp"]
    phan_loai = topic["Phân loại"]
    
    # Special case for "Xác suất cổ điển" which is now ID 02
    if stt == 2:
        so_cau = 76
        mat_khau = "123"
        trang_thai = "Hien"
    else:
        so_cau = 0
        mat_khau = ""
        trang_thai = "Coming_Soon"
        
    out_rows.append({
        "ID_ChuyenDe": id_cd,
        "Ten_ChuyenDe": ten,
        "Mon_Hoc": phan_loai,
        "Lop": lop,
        "So_Cau": so_cau,
        "Mat_Khau": mat_khau,
        "Trang_Thai": trang_thai
    })

with open(output_file, mode="w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ID_ChuyenDe","Ten_ChuyenDe","Mon_Hoc","Lop","So_Cau","Mat_Khau","Trang_Thai"])
    writer.writeheader()
    writer.writerows(out_rows)

print("Created quan_ly_chuyen_de.csv with 43 rows.")

