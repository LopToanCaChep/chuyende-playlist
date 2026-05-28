import os

file_path = r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\03_Outputs\chuyende_05.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Tìm vị trí bắt đầu của theory-content
start_tag = '<div class="theory-text" id="theory-content"'
start_idx = content.find(start_tag)

if start_idx == -1:
    print("❌ Không tìm thấy thẻ theory-content")
    exit(1)

# Tìm thẻ đóng </div> tương ứng của theoryModal
# Đoạn cuối của modal lý thuyết là:
# f(x) nghịch biến trên từ hàng 11 đến 20 tức là \displaystyle x \in\left(\frac{\pi}{4} ; \frac{\pi}{2}\right)
#         </div>
#     </div>
# </div>
# </div>

end_marker = 'nghịch biến trên từ hàng 11 đến 20 tức là \\displaystyle x \\in\\left(\\frac{\\pi}{4} ; \\frac{\\pi}{2}\\right)</p>\n        </div>'
end_idx = content.find(end_marker)

if end_idx == -1:
    # Thử tìm với \r\n (Windows line ending)
    end_marker = 'nghịch biến trên từ hàng 11 đến 20 tức là \\displaystyle x \\in\\left(\\frac{\\pi}{4} ; \\frac{\\pi}{2}\\right)</p>\r\n        </div>'
    end_idx = content.find(end_marker)

if end_idx == -1:
    # Thử tìm đoạn ngắn hơn
    end_marker = 'nghịch biến trên từ hàng 11 đến 20 tức là'
    end_idx = content.find(end_marker)
    if end_idx != -1:
        # Tìm thẻ đóng </div> đầu tiên sau đoạn này
        div_close = content.find('</div>', end_idx)
        end_theory_idx = div_close + len('</div>')
    else:
        print("❌ Không tìm thấy end marker")
        exit(1)
else:
    end_theory_idx = end_idx + len(end_marker)

# Đoạn thay thế mới (12 trang ảnh đã crop lề trắng):
replacement = """<div class="theory-text" id="theory-content" style="font-size:16px; line-height:1.8; color:#334155; padding: 10px 0;">
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966857/chuyende_05/a7dtjqakttrt0lswngpq.png" alt="Lý thuyết trang 1">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966867/chuyende_05/se11xhw1x6hvmvnfycds.png" alt="Lý thuyết trang 2">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966870/chuyende_05/flhvdk5zrnsbhns0p3jj.png" alt="Lý thuyết trang 3">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966872/chuyende_05/saobpkwi6rshqoygwiyg.png" alt="Lý thuyết trang 4">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966874/chuyende_05/yfzonjwqix5yedynrubl.png" alt="Lý thuyết trang 5">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966877/chuyende_05/asbvdjaghybkzu7xgd8m.png" alt="Lý thuyết trang 6">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966880/chuyende_05/vtk8e3udkgeblgafuugb.png" alt="Lý thuyết trang 7">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966882/chuyende_05/ky30gctamw7x0palxvyq.png" alt="Lý thuyết trang 8">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966885/chuyende_05/v8pjvdl9vmnpggsq6ikw.png" alt="Lý thuyết trang 9">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966859/chuyende_05/uyloe5prw14tg7mdoakv.png" alt="Lý thuyết trang 10">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966862/chuyende_05/qkuempzqksqoz6qtqpra.png" alt="Lý thuyết trang 11">
            </div>
            <div class="img-wrap">
                <img src="https://res.cloudinary.com/dud32vrhg/image/upload/v1779966864/chuyende_05/qcg6r9dh12c7vusdagtr.png" alt="Lý thuyết trang 12">
            </div>
        </div>"""

new_content = content[:start_idx] + replacement + content[end_theory_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Thay thế lý thuyết chuyên đề 5 thành công!")
