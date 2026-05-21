# -*- coding: utf-8 -*-
with open("03_Outputs/chuyende_02.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Fix q-number
c = c.replace(
    "top: 14px;\n            left: 20px;",
    "top: -18px;\n            left: 20px;"
)

# 2. Add border to question-card and margin-top to avoid clipping
c = c.replace(
    "background: #fff;\n            padding: 48px 20px 20px;\n            border-radius: 24px;",
    "background: #fff;\n            padding: 38px 20px 20px;\n            border-radius: 24px;\n            border: 2px solid var(--primary-blue);\n            margin-top: 20px;"
)

# Also fix the mobile override for question-card padding if any.
# Mobile card padding was changed to `padding: 16px 16px 5px !important;` for cover-card.
# `question-card` had `padding-top: 50px; margin-bottom: 20px;` on mobile. Let's make it `padding-top: 38px; margin-top: 24px;`
c = c.replace(
    "padding-top: 50px; \n                margin-bottom: 20px;",
    "padding-top: 38px; \n                margin-bottom: 20px;\n                margin-top: 24px;"
)

# 3. Change option border to very light blue
c = c.replace(
    "border: 2px solid #e2e8f0;",
    "border: 1px solid rgba(0, 64, 190, 0.15);"
)

# 4. Fix A. B. C. D. spacing (opt-label)
c = c.replace(
    "margin-right: 12px;\n            min-width: 32px;",
    "margin-right: 8px;\n            min-width: auto;"
)

# 5. Fix Cau 13 HTML
old_c13 = '</div><div class="option" data-ans="C" role="button" tabindex="0" aria-label="Phương án C"><div class="opt-label">C.</div> $x=2$</div></div>'
new_c13 = '</div><div class="option" data-ans="C" role="button" tabindex="0" aria-label="Phương án C"><div class="opt-label">C.</div> $\\dfrac{1}{2}$</div><div class="option" data-ans="D" role="button" tabindex="0" aria-label="Phương án D"><div class="opt-label">D.</div> $\\dfrac{7}{9}$</div></div>'
c = c.replace(old_c13, new_c13)

with open("03_Outputs/chuyende_02.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Done")
