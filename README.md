# Chuyên Đề Hub — Toán Cá Chép 🐟

> **Mục tiêu:** Hệ thống phân phối các bài giảng chuyên đề tương tác. Học sinh học tập trong không gian hiện đại, tập trung và đầy cảm hứng.

---

## 🚀 Cấu Trúc Dự Án

```
List_Chuyende_Web/
├── 01_Kho_Chuyen_De/       ← File chuyên đề gốc (Source of Truth)
├── Pic/                    ← Logo & Mascot thương hiệu
├── chuyende/               ← Thư mục phân phối (Auto-gen)
├── index.html              ← Cổng vào chính (Playlist Hub)
├── quan_ly_chuyen_de.csv   ← Cấu hình thông tin chuyên đề
├── sync_chuyende.ps1       ← Robot quét kho & build web
├── Push_Web.bat            ← Nút bấm 1-click cho Tí
├── PROJECT_CONTEXT.md      ← Ngữ cảnh kỹ thuật cho AI
└── README.md               ← File này
```

---

## 🛠 Hướng Dẫn Vận Hành

### 1. Thêm chuyên đề mới
1. Xuất file HTML từ hệ thống thiết kế.
2. Ném file vào thư mục `01_Kho_Chuyen_De`.
3. Bấm đúp **`Push_Web.bat`**. Robot sẽ tự đặt ID, cập nhật danh sách và đẩy lên Web.

### 2. Sửa thông tin (Tên, Lớp, Số câu)
1. Mở tệp `quan_ly_chuyen_de.csv`.
2. Sửa các cột tương ứng (Lưu ý: Giữ đúng định dạng CSV).
3. **Lưu lại (Ctrl + S)** và bấm đúp **`Push_Web.bat`**.

---

## 📅 Nhật Ký Cập Nhật (07/05/2026)

### 💎 Nâng cấp giao diện & Trải nghiệm
- **Đồng bộ thương hiệu**: Chuyển toàn bộ hệ thống sang tông màu **Xanh Dương Cá Chép** (#003B99) và **Vàng** (#F7C800).
- **Trang Hub cao cấp**: Bố cục Grid 2 cột trên máy tính, hiệu ứng Hover mượt mà, hỗ trợ lọc theo lớp qua URL.
- **Tối ưu Chuyên đề 01**:
  - Thiết kế lại trang bìa theo chuẩn A5 Print (D_Print).
  - Sửa lỗi tiêu đề đè dòng và clipping số câu.
  - Thêm Popup lựa chọn mức độ (Cơ bản/Nâng cao) cho học sinh.
  - Tăng cỡ chữ phân số KaTeX giúp dễ đọc hơn.

### 🤖 Tự động hóa & GitHub
- Thiết lập Robot `sync_chuyende.ps1` để tự động hóa quy trình từ kho lưu trữ đến môi trường Production.
- Hoàn thiện bộ tài liệu kỹ thuật (`README.md`, `PROJECT_CONTEXT.md`) để hỗ trợ AI cộng tác tốt hơn.

---

## ⚠️ Lưu Ý Quan Trọng
- **Encoding**: Luôn sử dụng UTF-8 cho các tệp văn bản.
- **Thư mục `chuyende/`**: Là thư mục tự sinh, không sửa tay trực tiếp bên trong.
- **Lưu CSV**: Luôn nhớ Ctrl + S tệp CSV trước khi chạy lệnh Push.

---
*Lớp Toán Cá Chép © 2026 · Chuyên đề trọng tâm & Mode Chill*
