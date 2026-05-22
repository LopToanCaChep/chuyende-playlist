# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"c:\Users\huyds\OneDrive\2. PARA\1 - Projects\CaChep_Ecosystem\02_Distribution\List_Chuyende_Web\template\chuyende_template.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Tìm đoạn từ /* ── Theory Heading System đến </style>
ts = content.find("/* ── Theory Heading System")
te = content.find("</style>", ts)

if ts >= 0 and te >= 0:
    print(content[ts:te])
else:
    print("❌ Không tìm thấy đoạn CSS")
