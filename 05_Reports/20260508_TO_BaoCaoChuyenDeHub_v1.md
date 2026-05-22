# 📋 Báo cáo công việc — Chuyên Đề Hub
**Ngày:** 08/05/2026 (00:00 – 01:27)  
**Dự án:** List_Chuyende_Web — Toán Cá Chép  
**Số lần deploy:** 17 lần push lên GitHub Pages  

---

## 1. Sửa lỗi nội dung bài thi (Xác suất cổ điển)

| Hạng mục | Chi tiết |
|----------|---------|
| Dấu chấm thừa | Quét sạch toàn bộ dấu `..` dư thừa ở đáp án và lời giải (76 câu) |
| Phân số nhỏ | Nâng cấp `\frac` → `\dfrac` để phân số hiển thị to, rõ ràng |
| Số trần trụi | Bọc các số đơn lẻ (0, 1, ...) vào `$...$` KaTeX cho đồng nhất font |
| Xóa dấu chấm cuối | Loại bỏ toàn bộ dấu `.` ở cuối mỗi đáp án A/B/C/D |
| Lỗi font UTF-8 | Sửa lỗi mất tiếng Việt do thiếu BOM khi ghi file |

---

## 2. Quy hoạch 43 chuyên đề

- Nhập toàn bộ **43 chuyên đề** từ file `Phan_chia_chuyen_de.csv` vào hệ thống
- Đổi mã bài "Xác suất cổ điển" từ `chuyende_01` → **`chuyende_02`** theo đúng thứ tự quy hoạch mới
- Cập nhật `quan_ly_chuyen_de.csv` với đầy đủ thông tin: ID, tên, môn, lớp, mật khẩu

---

## 3. Nâng cấp giao diện Index (Hub)

### 3.1 Thẻ phân loại màu sắc
| Thẻ | Màu nền | Màu chữ |
|-----|---------|---------|
| Lớp 10 | Xanh lá `#dcfce7` | `#16a34a` |
| Lớp 11 | Xanh dương `#e0f2fe` | `#0284c7` |
| Lớp 12 | Vàng `#fef08a` | `#ca8a04` |
| ĐS-GT | Tím `#f3e8ff` | `#7e22ce` |
| Hình | Đỏ `#fee2e2` | `#dc2626` |
| XS-TK | Xám `#f1f5f9` | `#475569` |

### 3.2 Thanh lọc (Filter Tabs)
- Thêm **3 nút lọc phân loại** mới: ĐS-GT, Hình, XS-TK
- Thêm **thanh phân cách** (`|`) giữa nhóm Lớp và nhóm Phân loại
- Mỗi nút khi active sẽ sáng lên **đúng màu đặc trưng** của nó
- Logic `renderList()` đã hỗ trợ lọc theo cả **khối lớp** lẫn **phân loại môn**

### 3.3 Slogan mới
- Đổi subtitle hero từ "Học sâu, hiểu kỹ, mười điểm ngay" → **"Chép chăm, Chép đúng, Chép thành cao thủ"**

### 3.4 Mũi tên hình ảnh
- Thay ký tự text `→` bằng **ảnh PNG mũi tên tròn** (`arrow_1.png` / `arrow.png`)
- Mặc định: Mũi tên vàng trên nền xanh 🔵
- Hover: Đổi sang mũi tên xanh trên nền vàng 🟡
- Fix lỗi viền trắng do CSS cũ `background:#fff`

### 3.5 Ô số thứ tự (Icon)
- Hover: Nền đổi sang **vàng `#F7C800`**, chữ đổi sang **xanh `#003c9e`**

---

## 4. Bảo mật & Tương tác

| Hạng mục | Chi tiết |
|----------|---------|
| Bật mật khẩu toàn bộ | 43/43 chuyên đề đều yêu cầu nhập mật khẩu |
| Mật khẩu riêng biệt | Mỗi bài dùng pass riêng: `cd01`, `cd02`, ..., `cd43` |
| Click anywhere | Nhấn bất kỳ đâu trên thẻ đều mở modal nhập mật khẩu |
| An toàn | Bài chưa có nội dung → nhập pass sẽ báo "Sai mật khẩu" |

---

## 5. Cập nhật Robot (`sync_chuyende.ps1`)

- Sửa logic để **không bỏ qua** các bài chưa có file HTML — vẫn hiển thị thẻ trên giao diện
- Hỗ trợ trạng thái `Coming_Soon` và `Hien` đồng thời
- Log rõ ràng: `CHUA CO FILE: ... - Van hien thi the`

---

## 6. Trạng thái hiện tại

| Mục | Trạng thái |
|-----|-----------|
| GitHub Pages | ✅ Live tại `https://loptoancachep.github.io/chuyende-playlist/` |
| Tổng chuyên đề | 43 (hiển thị đủ) |
| Có nội dung thực | 1/43 (Chuyên đề 2 - Xác suất cổ điển, pass: `cd02`) |
| Mật khẩu cũ `123` | ❌ Đã thay đổi → `cd02` |
| Nhúng Ghost (iframe) | ⚠️ Cần cập nhật hướng dẫn pass cho học sinh |

---

## 7. Việc cần làm tiếp

- [ ] Cập nhật hướng dẫn mật khẩu mới (`cd02`) trên trang Ghost cho học sinh
- [ ] Tiếp tục phát triển nội dung 42 chuyên đề còn lại (thêm file `.md` vào `02_Processing/`)
- [ ] Dọn dẹp các file script tạm (`fix_*.py`, `convert_csv.py`) khỏi repo
- [ ] Cân nhắc thêm tính năng lưu điểm vào LocalStorage cho mỗi chuyên đề
