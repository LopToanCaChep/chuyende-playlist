# BÁO CÁO QC SỐ HÓA CHUYÊN ĐỀ 04 - PHIÊN BẢN V2
*Ngày thực hiện: 21/05/2026*
*Người thực hiện: Tô (Antigravity)*

---

### 1. NỘI DUNG CHỈNH SỬA & KHẮC PHỤC LỖI (V2)

Dưới đây là chi tiết các lỗi hiển thị và nội dung toán học đã được khắc phục hoàn toàn trên tệp Markdown [04_Ham_so_bac_2_va_dau_tam_thuc_bac_2.md](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/02_Processing/04_Ham_so_bac_2_va_dau_tam_thuc_bac_2.md) và file template [chuyende_template.html](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/template/chuyende_template.html):

1. **Lỗi giao diện (Hover đáp án A/B bị mất viền trên):**
   * **Nguyên nhân:** Khi di chuyển chuột vào các nút đáp án (A, B, C, D), hiệu ứng di chuyển dọc `transform: translateY(-1px)` và bóng đổ `box-shadow` được kích hoạt. Do container `.options-grid` không có đủ không gian đệm trên/dưới nên viền trên của đáp án hàng đầu tiên bị cắt mất.
   * **Khắc phục:** Thêm `padding: 4px 2px;` vào định nghĩa lớp `.options-grid` trong file template. Lớp đệm này tạo thêm không gian render, đảm bảo khi hover các nút đáp án di chuyển lên vẫn giữ nguyên viền trên sắc nét.

2. **Câu 2 (Đáp án B bị dính vào đáp án A):**
   * **Nguyên nhân:** Lỗi OCR nhận diện ký tự đáp án B thành chữ `в.` (chữ cái Cyrillic viết thường) thay vì chữ cái Latin in hoa `B.` và viết liền dòng.
   * **Khắc phục:** Sửa chữ `в.` thành `B.` và tách dòng độc lập trong file Markdown gốc. Sau khi biên dịch lại, đáp án B đã hiển thị thành một ô lựa chọn riêng biệt đúng chuẩn.

3. **Câu 7 & 8 (Cập nhật bảng biến thiên dạng hình ảnh):**
   * **Câu 7:** Đã cập nhật bằng hình ảnh bảng biến thiên phẳng, màu sắc trực quan do Tí gửi trực tiếp trong chat (giúp học sinh dễ nhìn và chuyên nghiệp hơn).
   * **Câu 8:** Đã trích xuất trực tiếp ảnh bảng biến thiên từ file PDF gốc [cd04.pdf](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/01_Inputs/chuyende_04/cd04.pdf).
   * **Đường dẫn ảnh lưu trữ:**
     * [Pic/bbt_cau_7.png](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/Pic/bbt_cau_7.png) (Ảnh Tí gửi)
     * [Pic/bbt_cau_8.png](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/Pic/bbt_cau_8.png) (Ảnh trích từ PDF)
   * Thay thế các khối biểu diễn bảng text lỗi bằng mã ảnh markdown `![](../Pic/bbt_cau_7.png)` và `![](../Pic/bbt_cau_8.png)`. Cả 2 hình ảnh này đã được đồng bộ hóa thành công lên GitHub Pages.

4. **Câu 10 (Dư khoảng trống trong lời giải & Sai công thức):**
   * **Khắc phục:**
     * Dọn dẹp dấu chấm thừa và dòng trống thừa ở đầu khối Lời giải.
     * Sửa đáp án đúng từ `Chọn A` thành `Chọn D` cho phù hợp với kết quả tính toán.
     * Sửa biểu thức toán học từ $2\left(x+\frac{1}{4}\right)-\frac{25}{8}$ (thiếu bình phương) thành công thức chính xác: $2\left(x+\frac{1}{4}\right)^2-\frac{25}{8}$ trong LaTeX.

5. **Câu 20 (Đề bài bị hiển thị rời rạc):**
   * **Khắc phục:** Chỉnh sửa lại đề bài Câu 20 trong tệp Markdown thành một câu hoàn chỉnh liền mạch: `Cho Parabol $(P): y=x^{2}+m x+n$ ( $m, n$ tham số). Xác định $m, n$ để $(P)$ nhận điểm $I(2 ;-1)$ làm đỉnh.`

6. **Câu 23 (Dư số 1 sau hệ số c trong đề bài):**
   * **Khắc phục:** Sửa công thức hàm số từ $y = ax^2 + bx + c1$ thành công thức đúng $y = ax^2 + bx + c$.

---

### 2. KẾT QUẢ ĐỒNG BỘ HÓA GITHUB

* **File HTML biên dịch mới:** [chuyende_04.html](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/03_Outputs/chuyende_04.html).
* **Đồng bộ hóa hệ thống:** Chạy thành công script `sync_chuyende.ps1` để biên dịch, mã hóa chuyên đề bảo mật, tự động cập nhật [index.html](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/index.html) và thực hiện commit đẩy toàn bộ lên kho lưu trữ GitHub của lớp học.
* **Commit hash:** `c1de808c36c80e16c41910427e03b10cc711ffa1` (với thông điệp `"Auto-sync Chuyen De 2026-05-21 15:28"`).

---

### 3. ĐÁNH GIÁ CHẤT LƯỢNG SAU CẬP NHẬT (QC CHECKLIST)
- [x] Không còn lỗi giao diện khi di chuột hover lên các đáp án (viền trên hiển thị đầy đủ sắc nét).
- [x] Đáp án Câu 2 được tách rời độc lập, đầy đủ 4 đáp án A, B, C, D.
- [x] Bảng biến thiên Câu 7 và Câu 8 dạng ảnh load nét và nhanh, không bị vỡ bố cục.
- [x] Lời giải Câu 10 sạch sẽ, công thức toán học có số mũ bình phương chính xác, đáp án hiển thị Chọn D.
- [x] Câu 20 đề bài mạch lạc, liền chữ.
- [x] Câu 23 công thức đúng chuẩn không dư thừa ký tự.
- [x] Đồng bộ hóa Git hoạt động hoàn hảo, đã deploy lên GitHub Pages thành công.
