# Báo cáo: Xử lý và Đồng bộ Đề thi Cấp Tốc 09 (LD09) lên Live

- **Người thực hiện**: Tô (AI Assistant)
- **Thời gian hoàn thành**: 2026-05-22 12:00:00 (GMT+7)
- **Dự án**: CaChep_Ecosystem / List_Captoc_Web

---

## 1. Nội dung công việc đã thực hiện

1. **Chỉnh sửa file Unified HTML (`09_Unified.html`)**:
   - Thay thế giao diện modal nhập Họ tên / Lớp / SĐT thành **Modal nhập mã học sinh Cấp Tốc** (validate regex `^CT\d{2,}$`).
   - Cấu hình các tham số Cấp Tốc đặc thù cho đề trên lớp `LD09`:
     - `EXAM_ID = 'LD09'`
     - `EXAM_LOAI = 'tren_lop'`
     - `EXAM_BUOI = 5`
     - `SHOW_SOLUTION = false` (Không cho phép học sinh xem lời giải chi tiết sau khi nộp bài).
   - Đổi `SCRIPT_URL` từ URL Apps Script của Chuyên Đề sang URL của **Cấp Tốc**:
     `https://script.google.com/macros/s/AKfycbllKcqwe2zMfBuxRxri8AmL2PC5XrCybhohrkMTRohX7aR29hE64_2sLyXx8dWZcS-/exec`

2. **Sao chép và Lưu trữ**:
   - Copy file `09_Unified.html` sau khi đã chỉnh sửa từ `01_Factory/Test_Web/Captoc/20260522_CT_09/03_Outputs/` vào thư mục lưu trữ gốc của hệ thống Distribution `02_Distribution/List_Captoc_Web/01_Kho_De_Goc/` dưới tên **`CT_09.html`** (khớp với cấu hình trong CSV).

3. **Cập nhật Cấu hình Đề thi**:
   - Chỉnh sửa trạng thái của đề `LD09` trong file `quan_ly_de_thi.csv` từ `An` sang `Hien` để kích hoạt đồng bộ.

4. **Chạy Robot Đồng bộ (`sync_playlist.ps1`)**:
   - Thực thi script để tự động dọn dẹp thư mục `de/`, tính toán mã băm SHA-256 từ mật khẩu `ld09` để đổi tên file thành công, cập nhật Hub chính `index.html` và các trang danh sách `A1_dethi.html`, `A2_denha.html`.
   - Kết quả: **Validate CSV thành công (Sạch)** và đã tự động **Git push** đẩy dữ liệu mới lên GitHub Pages tại kho lưu trữ `captoc-2026.git`.

---

## 2. Kết quả kiểm tra
- Trạng thái nộp bài và validate: Thành công 100%.
- Đề thi đã xuất hiện trên trang Hub và có thể làm trực tuyến với mật khẩu truy cập `ld09`.
