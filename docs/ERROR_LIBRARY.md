# THƯ VIỆN LỖI (ERROR LIBRARY) — CHUYÊN ĐỀ HUB
Môi trường: Thư mục gốc `List_Chuyende_Web`
Mục đích: Lưu trữ các "bẫy" OCR, các lỗi Parser Markdown và các cách khắc phục đã được chuẩn hóa để tái sử dụng cho Pipeline Build tự động (`build_html.py`).

*Thư viện này kế thừa một phần từ dự án `Test_Web` và được bổ sung các lỗi đặc thù của giao diện Lý thuyết Chuyên đề.*

---

## 1. LỖI RENDER MATHJAX/KATEX VÀ HTML DOM

### 1.1. Lỗi thẻ HTML trong Toán học (`<` và `>`)
- **Biểu hiện:** Khi công thức có chứa các dấu `<` đứng liền trước chữ/số (VD: `1 < x < 2`), Parser HTML sẽ nhận diện nhầm `<x` thành một thẻ HTML mở. Hậu quả là công thức lỗi và làm vỡ DOM.
- **Giải pháp:** Mã hóa toàn cục `<` thành `&lt;` và `>` thành `&gt;` ở ngay đầu bước Parser (`text.replace('<', '&lt;')`). (Đã có sẵn trong `build_html.py`).

### 1.2. Lỗi công thức bị bóp nhỏ (`\lim` và `\frac`) [Đặc thù Chuyên Đề]
- **Biểu hiện:** Giá trị giới hạn (VD: `x -> 2`) nằm ngang bên phải `lim` thay vì nằm ngay phía dưới nó. Các phân số `\frac` bị bóp dẹt lại do KaTeX cố gắng tiết kiệm chiều cao dòng (inline math mode).
- **Giải pháp:** Viết Regex tự động thêm `\displaystyle` vào bên trong tất cả các block `$ ... $` nếu chúng chứa `\lim`, `\frac`, `\int`, `\sum`.
- **Triển khai:** Regex `re.sub(r'(?<!\$)\$([^$]+)\$(?!\$)', apply_display_style, text)` đã được nhúng vào `build_html.py`.

### 1.3. Lỗi bảng HTML bị in nguyên mã Markdown `**` [Đặc thù Chuyên Đề]
- **Biểu hiện:** Các dòng chữ trong bảng Lý thuyết hiển thị dạng `**Dạng 1**` thay vì in đậm. Nguyên nhân là do Parser chia cột bảng trước, rồi bỏ qua bước thay thế `**` thành `<strong>`.
- **Giải pháp:** Di chuyển Regex `re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)` lên đầu vòng lặp xử lý, ngay trước khi xử lý bảng.

### 1.4. Lỗi KaTeX không render được khối `$$ \begin{aligned} ... $$` đa dòng
- **Biểu hiện:** Các đoạn giải chứa công thức nhiều dòng bị vỡ, không được KaTeX xử lý mà hiển thị nguyên text kèm theo thẻ `<br>` (Ví dụ: `$$<br>\begin{aligned}<br>...`).
- **Nguyên nhân:** Hàm thay thế `text.replace('\n', '<br>')` đã bóp nghẹt cấu trúc xuống dòng nguyên thủy của KaTeX.
- **Giải pháp:** Sử dụng `re.split(r'(\$\$.*?\$\$)', text, flags=re.DOTALL)` để bóc tách và "bảo tồn" `\n` bên trong các khối block nhiều dòng, chỉ thay thế `<br>` ở đoạn văn bản thường.

---

## 2. LỖI BÓC TÁCH ĐÁP ÁN (PARSING) VÀ RÁC OCR

### 2.1. Lỗi mất ngoặc do Mathpix OCR [Đặc thù Chuyên Đề]
- **Biểu hiện:** Mathpix nhận diện nhầm các cụm ngoặc liền nhau thành khoảng trắng `\quad` hoặc nuốt mất ngoặc. VD: `(x+1)(x+2)` biến thành `x \quad x+1 \quad x+2`. Hoặc $y'(0)$ biến thành $y' 0$.
- **Giải pháp:** Tạo Dictionary cho các Regex phổ biến trong `ocr_cleaner.py` để chủ động bắt và sửa các cụm `\quad` bất thường trong công thức toán học nếu có thể. (Cần kiểm tra kỹ để tránh sửa nhầm).

### 2.2. Lỗi dư chữ "Hình 85", "Hình 45" [Kế thừa Test_Web]
- **Biểu hiện:** OCR đọc được chữ chú thích "Hình X" nằm bên dưới file ảnh gốc và đẩy vào văn bản ở dạng text lẻ tẻ làm rác nội dung đáp án.
- **Giải pháp:** Quét và loại bỏ triệt để các dòng mồ côi chứa chữ `Hình` và con số (`re.sub(r'(?mi)^H[iì]nh\s*\d+\s*$', '', md_text)`).

### 2.3. Lỗi dư thừa khoảng trắng và chữ "Lời giải" [Kế thừa Test_Web]
- **Biểu hiện:** Markdown sinh ra cụm `## Lời giải.` (có dấu chấm) hoặc 2 dòng chữ "Lời giải" mồ côi (do OCR tách văn bản khi gặp ảnh chèn giữa).
- **Giải pháp:** Dọn dẹp: `re.sub(r'(?im)^\s*(?:##\s*)?Lời giải\.?\s*$', '', text)`.

### 2.4. Lỗi Parser không nhận diện được Đáp án đúng (Câu 65-87)
- **Biểu hiện:** Console văng lỗi `[CẢNH BÁO] Không tìm thấy đáp án đúng cho Câu 65`. Nguyên nhân là cấu trúc câu hỏi bị vỡ, hoặc không có dòng `## Chọn X` rõ ràng.
- **Giải pháp:** Thêm Regex thông minh hơn để bắt được đáp án kể cả khi OCR nhận diện thiếu chữ `## ` (Ví dụ: `(?i)(?:##\s*)?Chọn ([A-Da-d])`).

### 2.5. Lỗi Parser không bắt được đáp án bọc trong thẻ `\underline` và `\mathrm`
- **Biểu hiện:** Khác với chuẩn `\mathbf{A}`, đôi khi Mathpix OCR xuất đáp án dưới dạng `$ \underline{\mathbf{A}} $` hoặc `$ \underline{\mathrm{A}} $`. Regex phiên bản cũ bỏ sót trường hợp này dẫn đến CẢNH BÁO không tìm thấy đáp án.
- **Giải pháp:** Cập nhật Parser v2.1 với Regex `(?:\bmathbf\b|\bmathrm\b|\bunderline\b)` để lùng sục triệt để mọi tag định dạng bọc quanh chữ cái đáp án.

---

## LƯU Ý CHO ROBOT AUTO-CLEAN
Tất cả các Regex dọn rác sẽ được tập hợp trong Module `tools/ocr_cleaner.py`. Module này sẽ chạy như một bộ tiền xử lý (pre-processor) để "giặt" sạch Markdown thô trước khi đưa vào Build HTML.

---

## 3. LỖI UI/UX VÀ TỐI ƯU HÓA HIỂN THỊ (Cập nhật 08/05)

### 3.1. Lỗi văng trang (Reload) trên Safari iOS do tràn bộ nhớ (OOM)
- **Biểu hiện:** Học sinh làm được 2-3 câu thì trang web trên Safari (iPhone/iPad) tự động tải lại kèm thông báo "A problem repeatedly occurred".
- **Nguyên nhân:** 
  1. Thẻ điểm số (`.score-chip`) có `position: fixed` kết hợp với hiệu ứng kính mờ `backdrop-filter: blur()`. Khi DOM thay đổi liên tục (chọn đáp án), GPU của Safari bị quá tải.
  2. Hiệu ứng hiện Lời giải (`.solution`) dùng `transform: translateY` ép Safari tạo thêm composition layer đồ sộ chứa hàng tá thẻ KaTeX, gây cạn kiệt VRAM.
- **Giải pháp:** Đổi màu thẻ điểm thành solid/rgba không có blur. Đổi hiệu ứng hiển thị Lời giải thành `opacity` (`animation: fadeIn`).

### 3.2. Lỗi đứt đoạn số thứ tự khi xóa câu lỗi
- **Biểu hiện:** Số thứ tự trên Web bị nhảy (ví dụ: Câu 6 rồi nhảy sang Câu 8) do file Markdown bị xóa tay các câu lỗi OCR.
- **Giải pháp:** Dùng script Python để quét regex `Câu \d+.` và đánh số lại (renumber) tự động từ 1 đến hết.

### 3.3. Lỗi lệch (Misalignment) các nút Floating trên Mobile
- **Biểu hiện:** Ở giao diện Mobile (không có thanh `.nav`), nút nổi "Lý thuyết" (góc phải) bị lệch lên cao quá lố so với nút "MENU" (góc trái).
- **Nguyên nhân:** Nút "Lý thuyết" bị fix `bottom: 85px` để né thanh `.nav` (cao 70px) ở bản Desktop, trong khi "MENU" dùng `bottom: 25px`.
- **Giải pháp:** Đồng bộ cả hai nút về chung một giá trị `bottom: 25px`.

### 3.4. Lỗi căn giữa dọc nhãn "Câu X" (.q-number)
- **Biểu hiện:** Nhãn "Câu X" hiển thị bị lệch nhẹ 2px xuống phía dưới so với mép viền trên của thẻ câu hỏi.
- **Giải pháp:** Ép `left: 24px` để đưa nhãn về góc trái chuẩn form, và quan trọng nhất là áp dụng `top: 0; transform: translateY(-50%);` để ép tâm ngang của nhãn cắt đôi chính xác đường viền trên.

### 3.5. Lỗi dư dấu chấm cuối câu trả lời (Parsing ABCD)
- **Biểu hiện:** Phần nội dung đáp án bị dư dấu chấm câu ở cuối (VD: `y=4x-6.`). 
- **Khắc phục:** Cập nhật Parser (`build_html.py`) dùng `re.sub(r'\.\s*$', '', opt_val)` lột bỏ đúng dấu chấm câu cuối văn bản, giữ nguyên cấu trúc nhãn `A.`, `B.`.
