# -*- coding: utf-8 -*-

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update CSS: remove old arrow background styling
old_arrow_css = """  width:36px;height:36px;border-radius:50%;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  background:var(--cc-yellow);color:var(--cc-blue-deep);
  font-size:18px;font-weight:900;
  transition:all .3s ease;"""

new_arrow_css = """  width:36px;height:36px;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  background:none;border:none;border-radius:0;
  transition:all .3s ease;"""

c = c.replace(old_arrow_css, new_arrow_css)

# 2. Add hover rule for img swap - insert before ".exam-row:hover .exam-arrow"
hover_css = """.exam-arrow img{width:36px;height:36px;object-fit:contain;transition:opacity .2s}
.exam-arrow .arrow-hover{display:none}
.exam-row:hover .arrow-default{display:none}
.exam-row:hover .arrow-hover{display:block}
"""

c = c.replace(
    ".exam-row:hover .exam-arrow",
    hover_css + ".exam-row:hover .exam-arrow"
)

# 3. Replace text arrow with img in JS template
c = c.replace(
    '<div class="exam-arrow">\u2192</div>',
    '<div class="exam-arrow"><img class="arrow-default" src="Pic/arrow_1.png" alt=""><img class="arrow-hover" src="Pic/arrow.png" alt=""></div>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Done! Arrow images updated.")
