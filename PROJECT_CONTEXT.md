# PROJECT CONTEXT — PLAYLIST CHUYÊN ĐỀ TƯƠNG TÁC (TOÁN CÁ CHÉP)
Môi trường: Thư mục gốc `List_Chuyende_Web` | Cập nhật: 08/05/2026
Trạng thái: 🟢 Production — Đang hoạt động trên GitHub Pages (Premium)

---

## 1. MỤC TIÊU & DEFINITION OF DONE

**Dự án này là gì?**
`List_Chuyende_Web` là hệ thống **phân phối chuyên đề học tập** tập trung. Học sinh truy cập 1 URL → thấy danh sách chuyên đề → chọn chuyên đề → học và luyện tập ngay với chế độ Mode Chill.

**Mối quan hệ với hệ thống thiết kế:**
- **Design Core** (`Kienthuc/design`) = Nơi quy định thẩm mỹ (Variant D - Print).
- **Chuyên đề Hub** = Nơi trưng bày các tệp chuyên đề đã được xuất bản.

**Dự án đã ĐẠT CHUẨN (08/05/2026):**
- [x] Giao diện Modern Flat: bo góc 20px, đổ bóng nhẹ, không viền cứng.
- [x] Progress Panel thay thế Level Popup: grid điều hướng 76 câu + filter Cơ bản/Nâng cao.
- [x] Font Manrope tối giản cho nội dung, Unbounded cho bìa/tiêu đề.
- [x] Nền mobile xanh dương nhạt chấm bi (#E8F4FF + #3C9EEF dots).
- [x] Màu đề bài xanh thương hiệu (#003B99), text-align justify.
- [x] Nhãn câu + nhãn mức độ đồng bộ màu (Cơ bản: #3C9EEF, Nâng cao: #F7C800).
- [x] Xóa hoàn toàn chức năng "Làm lại câu".
- [x] Robot `sync_chuyende.ps1` tự động quét kho, cập nhật `index.html` và đẩy lên GitHub.

---

## 2. KIẾN TRÚC KỸ THUẬT

### 2.1. Cấu trúc file

```text
List_Chuyende_Web/
├── 01_Inputs/                ← Nguyên liệu thô (43 thư mục con)
│   ├── chuyende_01/
│   │   ├── *.pdf             ← PDF gốc
│   │   └── pic/              ← Hình vẽ cho chuyên đề này
│   ├── chuyende_02/
│   │   ├── *.pdf
│   │   └── pic/
│   └── ... (đến chuyende_43)
├── 02_Processing/            ← File .md sau khi OCR
├── 03_Outputs/               ← File .html thành phẩm (Nguồn để Sync)
├── 04_Archive/               ← Scripts cũ, demo, báo cáo (Lưu trữ)
├── Pic/                      ← Tài nguyên Hub (Logo, Mascot)
├── chuyende/                 ← Thư mục phân phối (Robot tự động quản lý)
├── template/                 ← Template HTML gốc cho chuyên đề
├── tools/                    ← Scripts (build_html.py, upload_images.py)
├── index.html                ← Playlist Hub Premium
├── quan_ly_chuyen_de.csv     ← Database metadata & mật khẩu (43 chuyên đề)
├── sync_chuyende.ps1         ← Robot build & push
├── Push_Web.bat              ← Nút bấm 1-click
├── PROJECT_CONTEXT.md    
└── README.md             
```

### 2.2. Luồng hoạt động (Workflow: PDF → MD → HTML → WEB)

1. **Bước 1: Nhập liệu**: Bỏ file PDF vào `01_Inputs/`.
2. **Bước 2: OCR**: Sử dụng Mathpix chuyển PDF sang Markdown -> Lưu vào `02_Processing/`.
3. **Bước 3: Chuyển đổi**: Chạy script chuyển từ MD sang HTML (Unified format) -> Lưu vào `03_Outputs/`.
4. **Bước 4: Sync lên Web**:
   - Bấm đúp `Push_Web.bat`.
   - Robot quét `03_Outputs/`, băm mật khẩu, copy sang `chuyende/`, cập nhật `index.html` và đẩy lên GitHub.

---

## 3. QUY TẮC KỸ THUẬT

### 3.1. Thiết kế (Modern Flat)
- **Phong cách**: Modern Flat — bo góc 20px, soft shadow, không viền cứng.
- **Màu chủ đạo**: `#003B99` (xanh đậm thương hiệu) + `#F7C800` (vàng điểm nhấn).
- **Màu phụ**: `#3C9EEF` (cyan-blue cho Cơ bản), `#E8F4FF` (nền mobile).
- **Font bìa/tiêu đề**: `Unbounded` (font-weight 700-900).
- **Font nội dung**: `Manrope` (font-weight 400-900) — tối giản, không dùng Bangers.
- **Nền mobile**: Xanh dương nhạt chấm bi `radial-gradient(#3C9EEF 1.5px, transparent 1.5px)`.
- **Nền desktop**: Xanh đậm `#0f172a` với pattern dots.

### 3.2. Nhãn câu & mức độ
- **Cơ bản (tb)**: Nhãn câu + badge nền `#3C9EEF`, chữ trắng.
- **Nâng cao (kg)**: Nhãn câu + badge nền `#F7C800`, chữ `#003B99`.
- **Đề bài**: Màu `#003B99`, font-weight 700, text-align justify.

### 3.3. Quy tắc KaTeX
- Phân số đứng riêng → dùng `\dfrac` (to).
- Phân số trên mũ, chỉ số dưới log, hoán vị/tổ hợp/chỉnh hợp → dùng `\frac` hoặc `\tfrac` (nhỏ).

### 3.4. Kỹ thuật chung
- **Responsive**: Mobile-first, giao diện Hub hiển thị tốt trên 375px+.
- **Encoding**: UTF-8 with BOM cho mọi tệp text.
- **Bảo mật**: SHA-256 cho mật khẩu. File có mật khẩu tự đổi tên thành hash.
- **Chức năng "Làm lại"**: ĐÃ XÓA HOÀN TOÀN — học sinh trả lời là chốt.

---

## 4. QUY TRÌNH VẬN HÀNH CHO TÍ

1. **Đưa chuyên đề mới lên**: Ném file vào `03_Outputs/`, sau đó bấm đúp `Push_Web.bat`.
2. **Sửa thông tin**: Mở `quan_ly_chuyen_de.csv`, sửa Tên, Lớp hoặc Số câu, sau đó bấm `Push_Web.bat`.
3. **Lọc theo lớp**: Sử dụng link `index.html?grade=10` để chỉ hiện chuyên đề lớp 10.

---

## 5. HOSTING

| Hạng mục | Giá trị |
|---|---|
| **Nền tảng** | GitHub Pages |
| **Repo** | `LopToanCaChep/chuyende-playlist` |
| **URL** | `https://loptoancachep.github.io/chuyende-playlist/` |
| **Nhúng** | Embed trong website qua iframe |
| **Deploy** | Tự động qua `sync_chuyende.ps1` (git push → live) |

---

## 6. LỊCH SỬ CẬP NHẬT

### 08/05/2026 (Patch 2) — UI/UX Polish & Safari Optimization
- **Hiệu suất**: Khắc phục lỗi văng trang (OOM) trên Safari iOS bằng cách gỡ bỏ `backdrop-filter: blur` và đổi hiệu ứng `slideUp` thành `fadeIn`.
- **Căn chỉnh UI**: Đồng bộ nút Floating (Menu và Lý thuyết) về chung `bottom: 25px`. Căn giữa dọc nhãn "Câu X" (`translateY(-50%)`) và dóng sang mép trái thẻ câu hỏi.
- **Parser**: Nâng cấp `build_html.py` để lột bỏ dấu chấm thừa cuối đáp án, giữ nguyên cấu trúc nhãn `<div class="opt-label">`.
- **Bảo trì**: Bổ sung toàn bộ 5 lỗi kỹ thuật vào `ERROR_LIBRARY.md`.

### 08/05/2026 — Modern Flat + Progress Panel
- **UI/UX**: Chuyển sang phong cách Modern Flat (bo góc, shadow mềm, pastel).
- **Progress Panel**: Thay thế Level Popup → Grid 76 câu + filter tabs + điểm realtime.
- **Font**: Gỡ Bangers, chuyển toàn bộ nội dung sang Manrope tối giản. Giữ Unbounded cho bìa.
- **Mobile**: Nền xanh dương nhạt chấm bi (#E8F4FF) thay nền trắng.
- **Nhãn màu**: Cơ bản (#3C9EEF) / Nâng cao (#F7C800) đồng bộ badge + q-number.
- **Xóa**: Chức năng "Làm lại câu" bị loại bỏ hoàn toàn.
- **Dọn dẹp**: Di chuyển 13 file .py + 4 demo vào `04_Archive/`.

### 07/05/2026 — Foundation
- **UI/UX**: Nâng cấp `index.html` theo mẫu Premium, đồng bộ màu sắc thương hiệu.
- **Security**: Triển khai hệ thống mật khẩu SHA-256.
- **Robot**: Nâng cấp `sync_chuyende.ps1` hỗ trợ băm mật khẩu, tự động tính số câu.
- **Content**: Hoàn thiện Chuyên đề 02 (Xác suất cổ điển) - Lớp 10.
- **Organization**: Tái cấu trúc theo chuẩn 4 Zone Standard.

---

## 7. NEXT STEPS (Kế hoạch)

1. **Template Generator**: Khi có 5-10 chuyên đề thật → xây pipeline `Template + Data YAML → 42 HTML standalone`.
2. **Nội dung**: Ưu tiên hoàn thiện nội dung 42 chuyên đề trước khi optimize kiến trúc.
3. **QA**: Kiểm tra cross-browser (Safari iOS, Chrome Android) cho từng chuyên đề mới.

---

## 8. TÔ ĐỌC FILE NÀY → LÀM GÌ

Nếu có request liên quan đến dự án `List_Chuyende_Web`, Tô tự kiểm tra:
1. ✅ **Chuẩn 4 Zone**: File đúng vị trí (HTML nguồn ở `03_Outputs`, scripts cũ ở `04_Archive`).
2. ✅ **Modern Flat**: Không dùng Bangers, không viền cứng, bo góc mềm.
3. ✅ **Bảo mật**: Chuyên đề có mật khẩu phải dùng cơ chế băm file của Robot.
4. ✅ **Mobile-First**: Nền chấm bi #E8F4FF, giao diện mượt trên 375px.
5. ✅ **KaTeX**: `\dfrac` chỉ khi đứng riêng, `\frac`/`\tfrac` khi trên mũ/chỉ số.
6. ✅ **UTF-8 with BOM**: Bắt buộc cho mọi tệp text.
7. ✅ **Không "Làm lại"**: Học sinh trả lời là chốt, không reset.
