# -*- coding: utf-8 -*-
with open("03_Outputs/chuyende_02.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Reduce q-content margin-bottom from 24px to 10px
c = c.replace(
    "margin-bottom: 24px;\n            padding: 0 4px;",
    "margin-bottom: 10px;\n            padding: 0 4px;"
)

# 2. Reduce options-grid gap from 12px to 8px, margin-top from 20px to 10px
c = c.replace(
    "gap: 12px;\n            margin-top: 20px;\n        }\n\n        @media (max-width: 600px)",
    "gap: 8px;\n            margin-top: 10px;\n        }\n\n        @media (max-width: 600px)"
)

# 3. Reduce option padding from 16px 18px to 12px 14px
c = c.replace(
    "padding: 16px 18px;\n            font-weight: 600;\n            font-size: 16px;",
    "padding: 12px 14px;\n            font-weight: 600;\n            font-size: 16px;"
)

# 4. Reduce question-card padding-top and margin-bottom on mobile
c = c.replace(
    "min-height: 60vh;\n                padding-top: 60px; \n                margin-bottom: 40px;",
    "min-height: auto;\n                padding-top: 50px; \n                margin-bottom: 20px;"
)

# 5. Reduce solution margin-top from 24px to 12px, padding from 20px to 14px
c = c.replace(
    "margin-top: 24px;\n            padding: 20px;",
    "margin-top: 12px;\n            padding: 14px;"
)

# 6. Reduce question-card base padding-top from 60px to 48px
c = c.replace(
    "padding: 60px 24px 30px;\n            border-radius: 24px;",
    "padding: 48px 20px 20px;\n            border-radius: 24px;"
)

with open("03_Outputs/chuyende_02.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Done - spacing reduced")
