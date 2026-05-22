# BÁO CÁO QC SỐ HÓA CHUYÊN ĐỀ 04 - PHIÊN BẢN V2 (CẬP NHẬT)
*Ngày thực hiện: 21/05/2026*
*Người thực hiện: Tô (Antigravity)*

---

### 1. NỘI DUNG CHỈNH SỬA & KHẮC PHỤC LỖI ĐỢT 1
1. **Lỗi giao diện (Hover đáp án A/B bị mất viền trên):** Đã thêm `padding: 4px 2px;` vào `.options-grid` trong file template.
2. **Câu 2 (Đáp án B bị dính vào đáp án A):** Sửa chữ `в.` thành `B.` và tách dòng.
3. **Câu 7 & 8 (Cập nhật bảng biến thiên dạng hình ảnh):** Thay thế bảng text lỗi bằng ảnh `bbt_cau_7.png` và `bbt_cau_8.png`.
4. **Câu 10 (Dư khoảng trống trong lời giải & Sai công thức):** Sửa công thức và đổi đáp án đúng sang D.
5. **Câu 20 (Đề bài bị hiển thị rời rạc):** Ghép lại đề bài liền mạch.
6. **Câu 23 (Dư số 1 sau hệ số c trong đề bài):** Sửa thành $y = ax^2 + bx + c$.

---

### 2. NỘI DUNG CHỈNH SỬA & KHẮC PHỤC LỖI ĐỢT 2 (YÊU CẦU MỚI)
Dưới đây là chi tiết các lỗi QC và nội dung toán học được cập nhật bổ sung theo yêu cầu chi tiết từ Tí:

1. **Câu 8 (Sửa kiến thức cơ bản & Đáp án đúng):**
   * **Lỗi:** Lời giải ghi "Parabol có bề lõm quay lên trên nên hệ số $a<0$" (sai kiến thức cơ bản vì $a<0$ thì bề lõm phải quay xuống dưới). Ngoài ra lời giải ghi "Chọn B" nhưng kết luận lại ghi "Chọn đáp án D" và thẻ HTML cài sai `data-correct="D"`.
   * **Khắc phục:** Đổi thành "Parabol có nhánh cuối đi xuống nên $a<0$". Cập nhật file Markdown để parser tự động gán `data-correct="B"`, hiển thị vòng tròn B và kết luận chọn đáp án B.

2. **Câu 32 (Giải đúng nhưng chọn sai đáp án):**
   * **Lỗi:** Lời giải ra kết quả $0 < m < 28$ (tương ứng đáp án D), nhưng HTML cài `data-correct="B"` và hiển thị chọn B. Dư dấu gạch ngang ở cuối câu giải (`28 -`).
   * **Khắc phục:** Đổi trong file Markdown thành `## Chọn D` để sinh `data-correct="D"` và vòng tròn D. Xóa dấu `-` thừa ở cuối câu.

3. **Câu 35 (Vỡ cấu trúc HTML làm mất đáp án C):**
   * **Lỗi:** OCR quét lỗi làm đáp án C bị mất thẻ `<div class="option">` và gộp dính vào đáp án B dưới dạng chữ rác `.c. (-\infty;-1)`.
   * **Khắc phục:** Chỉnh sửa lại cấu trúc đáp án C đúng chuẩn trong file Markdown để parser chia lưới `.options-grid` chính xác với 4 đáp án A, B, C, D rõ ràng.

4. **Câu 14 (Bổ dung nội dung hướng dẫn giải):**
   * **Lỗi:** Phần Hướng dẫn giải `<div class="sol-body"></div>` bị trống.
   * **Khắc phục:** Bổ sung lời giải: *"Trục đối xứng của đồ thị hàm số bậc hai $y = ax^2+bx+c$ ($a \neq 0$) là đường thẳng có phương trình $\displaystyle x = -\frac{b}{2a}$."*

5. **Sửa các ký tự rác do quét OCR ở nhiều câu:**
   * **Câu 3:** Sửa "tung độ bằng ${ }^{c}$" thành "tung độ bằng $c$".
   * **Câu 6:** Sửa Đáp án B từ `${ }^{9}$` thành `9`.
   * **Câu 13:** Sửa Đáp án A từ `${ }^{I(0 ; 1)}$` thành `$I(0 ; 1)$`. Thêm dấu `\Rightarrow` trước `y=3\left(\frac{1}{3}\right)^{2}...` trong lời giải.
   * **Câu 17:** Sửa ký hiệu kết luận không phù hợp `∴` thành dấu `\Rightarrow`.
   * **Câu 18:** Sửa font $a$ lỗi trong biểu thức $y=\mathrm{ax}^{2}...$ thành $y=ax^2...$ dạng in nghiêng đồng bộ.
   * **Câu 21:** Sửa chính tả "đinh" thành "đỉnh". Bỏ lặp từ "ta có (P) có đỉnh" thành "ta có (P) đỉnh".
   * **Câu 22:** Sửa số mũ lỗi $S:^{2+(-3)=-1}$ thành $S: 2 + (-3) = -1$.
   * **Câu 23:** Sửa sai chính tả "cắt trụ hoành" thành "trục hoành". Xóa dấu chấm thừa ở đầu câu lời giải.
   * **Câu 24:** Sửa dấu hỏi chấm nhảy vào block toán $A(1 ;-4)_{\text {? }}$ thành $A(1 ;-4)$?. Xóa chữ "## Lời giải" bị dư thừa trong phần lời giải.
   * **Câu 29:** Sửa định dạng mũ thừa ( ${ }^{x_{A}<x_{B}}$ ) thành ( $x_A < x_B$ ).
   * **Câu 30:** Sửa lỗi gõ nhầm đề bài parabol $y=x^2+2x+1$ thành $y=x^2+2x-1$ đúng như đề cho.
   * **Câu 38:** Thêm dấu phẩy trong dòng kết luận: "So sánh điều kiện, kết luận...".
   * **Câu 39 & 40 (Sửa lỗi dính chùm hệ phương trình & ngoặc nhọn):**
     * **Câu 39:** Đổi `\end{array}\left\{\begin{array}{l}` thành `\end{array}\right. \Leftrightarrow\left\{\begin{array}{l}`.
     * **Câu 40:** Đổi `}{ }_{\Leftrightarrow\left\{\begin{array}{l}` thành `\right. \Leftrightarrow\left\{\begin{array}{l}`.

---

### 3. KẾT QUẢ ĐỒNG BỘ HÓA GITHUB
* **File HTML biên dịch mới:** [chuyende_04.html](file:///c:/Users/huyds/OneDrive/2. PARA/1 - Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/03_Outputs/chuyende_04.html).
* **Đồng bộ hóa hệ thống:** Chạy script `sync_chuyende.ps1` thành công, tự động mã hóa bảo mật, cập nhật [index.html](file:///c:/Users/huyds/OneDrive/2. PARA/1 - Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/index.html) và push lên GitHub.
* **Commit mới nhất:** Đã đẩy commit sync bổ sung toàn bộ thay đổi lên branch `main`.

---

### 4. ĐÁNH GIÁ CHẤT LƯỢNG SAU CẬP NHẬT (QC CHECKLIST)
- [x] Lỗi kiến thức Câu 8 và đáp án đúng được sửa đổi hoàn tất (đáp án B, data-correct="B").
- [x] Câu 32 cập nhật đúng đáp án D, xóa ký tự thừa.
- [x] Câu 35 hiển thị đầy đủ 4 đáp án A, B, C, D trên giao diện.
- [x] Câu 14 đã có hướng dẫn giải đầy đủ.
- [x] Toàn bộ lỗi ký tự rác OCR từ Câu 3 đến Câu 40 được dọn dẹp sạch sẽ, LaTeX hiển thị chuẩn mực 100%.
- [x] Deploy lên GitHub Pages thành công không có lỗi build.
