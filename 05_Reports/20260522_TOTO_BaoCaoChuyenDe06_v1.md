# BÁO CÁO QC SỐ HÓA CHUYÊN ĐỀ 06
- **ID Chuyên đề:** `chuyende_06`
- **Tên Chuyên đề:** Chuyên đề 6 - Phương trình lượng giác
- **Lớp:** 11
- **Môn học:** Đại số - Giải tích
- **Người thực hiện:** Tô (Antigravity)

---

## LỊCH SỬ CẬP NHẬT

### Đợt 1 (Cập nhật ngày 22/05/2026)
Dưới đây là chi tiết các lỗi hiển thị, công thức và giao diện đã được điều chỉnh theo yêu cầu của Tí:

1. **Sửa lỗi công thức chưa render ở Câu 48:**
   - *Lỗi:* Công thức của hai phương trình tương đương được viết bằng cặp `$$` đa dòng bị xen kẽ xuống dòng nên KaTeX auto-render bỏ qua, hiển thị thô dạng raw code LaTeX.
   - *Khắc phục:* Cập nhật hàm `pre_process_multiline_math` trong file `build_html.py` để tự động dọn dẹp các ký tự xuống dòng `\n` và khoảng trắng dư thừa bên trong cặp `$$ ... $$` trước khi biên dịch sang HTML. Hiện tại công thức đã nằm gọn trên một dòng duy nhất và render chính xác 100%.

2. **Cập nhật giãn dòng & padding toán inline (Đặc biệt lưu ý Câu 54):**
   - *Yêu cầu:* Tí phản hồi các câu có công thức inline lớn (như phân số đứng dùng `\displaystyle` ở Câu 54 và các tùy chọn đáp án) có khoảng cách quá sát nhau, làm chữ và công thức đè nhau.
   - *Khắc phục:* 
     - Tăng giãn dòng `line-height` của `.q-content`, `.sol-body`, và `.opt-text` từ `1.85` lên `2.15` trong file template.
     - Tăng padding dọc của `.katex` từ `3px 0` lên `6px 0` để tạo vùng đệm an toàn xung quanh các ký tự toán học inline.

3. **Điều chỉnh khoảng cách Hướng dẫn giải (.solution):**
   - *Yêu cầu:* Tí nghĩ hướng dẫn giải hơi sát với các tùy chọn đáp án ở trên.
   - *Khắc phục:* Tăng `margin-top` của class `.solution` từ `28px` lên `40px` để đẩy xa hộp giải thích ra khỏi phần đáp án, giúp giao diện thông thoáng, dễ nhìn. Đồng thời tăng nhẹ kích thước chữ lên `15.5px` và `line-height` lời giải lên `1.85`.

---

## ĐÁNH GIÁ CHẤT LƯỢNG (QC CHECKLIST CUỐI CÙNG)
- [x] Công thức Câu 48 hiển thị chuẩn mực và render KaTeX thành công.
- [x] Câu 54 và toàn bộ chuyên đề được áp dụng line-height `2.15` siêu thoáng.
- [x] Hộp Hướng dẫn giải có khoảng cách `margin-top: 40px` rộng rãi, không bị sát đáp án.
- [x] Đồng bộ hóa và deploy thành công lên GitHub Pages qua script `sync_chuyende.ps1`.
