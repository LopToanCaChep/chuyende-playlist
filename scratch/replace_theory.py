import os

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_06.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Tìm vị trí bắt đầu của theory-content
start_tag = '<div class="theory-text" id="theory-content"'
start_idx = content.find(start_tag)

if start_idx == -1:
    print("Không tìm thấy thẻ theory-content")
    exit(1)

# Tìm thẻ đóng </div> tương ứng
# Thẻ đóng </div> nằm ngay trước thẻ đóng </div class="modal-content"> hoặc </div> của modal
# Ở đây ta biết sau theory-content là </div> đóng của nó, tiếp đến là đóng modal-content, tiếp đến đóng modal-overlay
# Vì bên trong theory-content cũ có rất nhiều </div> của các bảng biểu, ta tìm thẻ đóng </div> dựa trên cấu trúc file:
# Ngay sau theory-content kết thúc là:
#         </div>
#     </div>
# </div>
# </div>

# Hãy tìm đoạn kết thúc:
# <p class="theory-text">7. Tổng thành tích</p>
#         </div>
#     </div>
# </div>
# </div>
end_marker = '<p class="theory-text">7. Tổng thành tích</p>\n        </div>'
end_idx = content.find(end_marker)

if end_idx == -1:
    # Thử tìm với \r\n (Windows line ending)
    end_marker = '<p class="theory-text">7. Tổng thành tích</p>\r\n        </div>'
    end_idx = content.find(end_marker)

if end_idx == -1:
    print("Không tìm thấy end marker")
    exit(1)

# Vị trí đóng của theory-content chính là sau chữ </div>
end_theory_idx = end_idx + len(end_marker)

# Đoạn thay thế mới:
replacement = """<div class="theory-text" id="theory-content" style="font-size:16px; line-height:1.8; color:#334155; padding: 10px 0;">
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779965474/chuyende_06/ksb6dc4rrjmgoqgyltkj.png" alt="Lý thuyết 1">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779965477/chuyende_06/xlanlvudwgpm3ujixtxb.png" alt="Lý thuyết 2">
            </div>
        </div>"""

new_content = content[:start_idx] + replacement + content[end_theory_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Thay thế lý thuyết thành công!")
