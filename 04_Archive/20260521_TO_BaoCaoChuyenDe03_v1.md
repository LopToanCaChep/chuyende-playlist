# BÁO CÁO QC SỐ HÓA CHUYÊN ĐỀ 03
*Ngày thực hiện: 21/05/2026*
*Người thực hiện: Tô (Antigravity)*

---

### 1. THÔNG TIN CHUYÊN ĐỀ
* **ID Chuyên đề:** `chuyende_03`
* **Tên Chuyên đề:** Chuyên đề 3 - Bài toán tối ưu hệ phương trình 2 ẩn
* **Lớp:** 10
* **Môn học:** Đại số - Giải tích
* **Số câu trắc nghiệm:** 10 câu (đã chia mức độ)
* **Mật khẩu truy cập:** `cd03`

---

### 2. TIẾN TRÌNH THỰC HIỆN & KẾT QUẢ
* **Bước 1: OCR tài liệu gốc:**
  * Đã chạy thành công script `convert_pdf_to_md.py` bằng Mathpix API để chuyển đổi file [cd_03.pdf](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/01_Inputs/chuyende_03/cd_03.pdf) thành file Markdown thô [cd_03.md](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/01_Inputs/chuyende_03/cd_03.md).
* **Bước 2: Chuẩn hóa Markdown:**
  * Đã thêm thẻ định danh lý thuyết `## PHẦN A. KIẾN THỨC CẦN NHỚ` lên đầu file.
  * Tách biệt phần bài tập trắc nghiệm bắt đầu từ Câu 1 dưới tiêu đề `## PHẦN C. BÀI TẬP TRẮC NGHIỆM`.
  * Phân chia mức độ câu hỏi rõ ràng theo yêu cầu của Tí:
    * **Dành cho học sinh trung bình:** Câu 1 - Câu 4 (Tìm cực trị đơn giản trên miền nghiệm cho sẵn).
    * **Dành cho học sinh khá giỏi:** Câu 5 - Câu 10 (Bài toán tối ưu thực tế cần tự lập hệ và hàm mục tiêu).
  * Đã sửa lỗi chính tả OCR (ví dụ: `biết thức` -> `biểu thức`, `biểu diễn miền ngiệm` -> `biểu diễn miền nghiệm`...).
  * Sửa lỗi logic tính toán ở **Câu 10** (phần so sánh giá trị tại các đỉnh ghi nhầm kết luận $x=0,6; y=0,7$ đã được sửa lại thành $x=0,3; y=1,1$ để đúng với đáp án A).
  * Giữ nguyên các link ảnh gốc do Mathpix quét vì chuyên đề này không có thư mục `pic/` đi kèm.
  * File Markdown sau chuẩn hóa được lưu tại: [03_Bai_toan_toi_uu_he_phuong_trinh_2_an.md](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/02_Processing/03_Bai_toan_toi_uu_he_phuong_trinh_2_an.md).
* **Bước 3: Biên dịch HTML:**
  * Chạy biên dịch thành công file HTML tương tác: [chuyende_03.html](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/03_Outputs/chuyende_03.html).
* **Bước 4: Cập nhật cơ sở dữ liệu:**
  * Đã cập nhật số câu từ `0` thành `10` cho `chuyende_03` trong file [quan_ly_chuyen_de.csv](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/quan_ly_chuyen_de.csv).
* **Bước 5: Đồng bộ & Đẩy lên GitHub Pages:**
  * Đổi tên nhánh local từ `master` sang `main` để đồng bộ hoàn toàn với remote branch.
  * Thêm cấu hình bỏ qua thư mục `.github/` trong [.gitignore](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/.gitignore) để tránh lỗi phân quyền Personal Access Token khi push các tệp CI/CD workflows.
  * Chạy script `sync_chuyende.ps1` để tự động băm mật khẩu bảo mật cho chuyên đề mới, cập nhật danh sách hiển thị trên [index.html](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/index.html) và thực hiện push thành công lên GitHub repository.
  * *Cập nhật ngày 21/05/2026:* Sửa lỗi hiển thị LaTeX `\begin{array//l}` tại Lời giải Câu 7 thành `\begin{array}{l}`, build lại file HTML và đồng bộ lên GitHub thành công.

---

### 3. ĐÁNH GIÁ CHẤT LƯỢNG (QC CHECKLIST)
- [x] Hiển thị công thức Toán: Đúng chuẩn KaTeX/LaTeX, không bị lỗi hiển thị.
- [x] Phân tách Lý thuyết / Bài tập: Đúng chuẩn, Slide cover hiển thị đẹp.
- [x] Phân loại mức độ: Đúng tab Cơ bản (Cắt từ Câu 1) và Nâng cao (Cắt từ Câu 5).
- [x] Liên kết ảnh: Load ảnh sơ đồ miền nghiệm ổn định qua link Mathpix.
- [x] Đáp án đúng: Trích xuất và đối chiếu chính xác (Khớp 10/10 câu hỏi).
- [x] Đồng bộ hóa: Deploy thành công lên GitHub Pages, không lỗi runtime.
