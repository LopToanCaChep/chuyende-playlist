# Báo cáo sửa lỗi Chuyên đề 05 — Hàm số lượng giác

Chào Tí, Tô đã hoàn thành việc kiểm tra và khắc phục 4 lỗi hiển thị trên file [chuyende_05.html](file:///c:/Users/huyds/OneDrive/2.%20PARA/1%20-%20Projects/CaChep_Ecosystem/02_Distribution/List_Chuyende_Web/03_Outputs/chuyende_05.html). Dưới đây là chi tiết các thay đổi mà Tô đã thực hiện:

## 1. Câu 54 — Sửa lỗi phân số dính chùm
- **Vấn đề**: Các phân số ở phần hướng dẫn giải trong inline math như $\frac{\pi}{4}$, $\frac{\pi}{2}$ hiển thị rất nhỏ và dính sát vào nhau. Đồng thời, biểu thức cuối bị thiếu dấu ngoặc khoảng.
- **Giải pháp**: 
  - Thay thế toàn bộ các phân số dạng `\frac` thành `\dfrac` trong phần lời giải để hiển thị kích thước lớn chuẩn trực quan.
  - Khôi phục dấu ngoặc khoảng cho biểu thức cuối: `4 x \in [\pi ; 2 \pi]`.
- **Kết quả**: Công thức hiển thị to, rõ ràng và chuẩn xác.

## 2. Câu 55 — Xử lý tràn/mất công thức
- **Vấn đề**: Đoạn công thức chứa 4 hàm số liên tiếp được viết dưới dạng block math `$$y=\sin(...), y=\cos(...), y=\tan(...) \text{ và } y=\cot(...)$$` quá dài, dẫn đến tràn màn hình và bị cắt cụt một phần lớn trên giao diện điện thoại di động (chỉ hiển thị được đến `y = \cot(2x+`).
- **Giải pháp**: Tô đã chia nhỏ block math khổng lồ này thành 4 cụm inline math riêng biệt ngắn hơn, ngăn cách bằng dấu phẩy và chữ "và" thông thường.
  - *Mã nguồn mới*: `$y=\sin \left(2 x+\dfrac{\pi}{6}\right)$, $y=\cos \left(2 x+\dfrac{\pi}{6}\right)$, $y=\tan \left(2 x+\dfrac{\pi}{6}\right)$ và $y=\cot \left(2 x+\dfrac{\pi}{6}\right)$`
- **Kết quả**: Trình duyệt sẽ tự động xuống dòng (wrap) cực kỳ mượt mà ở các khoảng ngăn cách khi màn hình không đủ rộng, không bao giờ bị tràn hay mất công thức nữa.

## 3. Câu 58 — Khôi phục dấu ngoặc ở đáp án B
- **Vấn đề**: Đáp án B hiển thị thô là `Hàm số đã cho đồng biến trên 0; \pi` bị mất dấu ngoặc của khoảng.
- **Giải pháp**: 
  - Đã thêm dấu ngoặc tròn thành: `Hàm số đã cho đồng biến trên $(0 ; \pi)$`.
  - Đồng thời chuẩn hóa khoảng đáp án D bằng cách đưa dấu ngoặc đơn vào trong khối LaTeX để hiển thị nhất quán với các đáp án khác: `Hàm số đã cho đồng biến trên $\displaystyle \left(0 ; \frac{\pi}{4}\right)$ và nghịch biến trên $\displaystyle \left(\frac{\pi}{4} ; \pi\right)$`.

## 4. Câu 59 — Thay thế bảng biến thiên bằng ảnh gốc
- **Vấn đề**: Bảng biến thiên tự vẽ bằng bảng HTML (`<table>`) hiển thị không đẹp mắt, thiếu trực quan. Tí muốn lấy lại ảnh gốc ban đầu.
- **Giải pháp**: 
  - Tô đã quét lại file Markdown thô gốc (`cd05.md` trong cache) và tìm ra link ảnh bảng biến thiên do Mathpix tự crop ban đầu.
  - Tô đã tải ảnh này về, lưu tại thư mục local và chạy script `upload_images.py` để đẩy lên Cloudinary của Tí:
    - **Link ảnh Cloudinary mới**: `https://res.cloudinary.com/dud32vrhg/image/upload/v1779407122/chuyende_05/xyc3nicax1y4imievxwn.png`
  - Sửa đổi trong file HTML: Loại bỏ hoàn toàn thẻ `<table>` phức tạp và thay thế bằng thẻ `<img>` sử dụng link Cloudinary mới đặt trong thẻ bao `.img-wrap` để hiển thị căn giữa chuẩn thẩm mỹ.

## 5. Câu 23 — Sửa lỗi mất đáp án D
- **Vấn đề**: Giao diện chỉ hiển thị 3 đáp án A, B, C. Đáp án D bị trống.
- **Nguyên nhân**: Trong file Markdown gốc `05_Ham_so_luong_giac.md`, cả hai đáp án cuối đều ghi nhãn trùng nhau là `C.`. Khi parser chạy tạo file HTML, nó đã lấy dòng C thứ hai ghi đè lên dòng C thứ nhất (đáp án đúng), dẫn đến mất đáp án D và hiển thị sai nội dung đáp án C thực tế.
- **Giải pháp**:
  - Tô đã phân tích và sửa lại nhãn: Đưa đáp án đúng của bài toán về nhãn `C` (`[\frac{\pi}{2}+k2\pi; \frac{3\pi}{2}+k2\pi]`), và đưa đáp án gây nhiễu về nhãn `D` (`[-\frac{\pi}{2}+k2\pi; \frac{\pi}{2}+k2\pi]`).
  - Nâng cấp các phân số lên dạng `\dfrac` để công thức hiển thị to đẹp, không bị dính chùm.

---
Tô đã cập nhật trực tiếp vào file. Tí hãy reload trang web để kiểm tra lại thành quả nhé!
