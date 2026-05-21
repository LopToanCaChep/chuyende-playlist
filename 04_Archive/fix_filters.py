# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add per-filter active color CSS after the generic .filter-tab.active block
css_insert = """
.filter-tab[data-filter="12"].active{background:#fef08a;color:#ca8a04;border-color:#fef08a;box-shadow:0 4px 12px rgba(202,138,4,.25)}
.filter-tab[data-filter="11"].active{background:#e0f2fe;color:#0284c7;border-color:#e0f2fe;box-shadow:0 4px 12px rgba(2,132,199,.25)}
.filter-tab[data-filter="10"].active{background:#dcfce7;color:#16a34a;border-color:#dcfce7;box-shadow:0 4px 12px rgba(22,163,74,.25)}
.filter-tab[data-filter="dsgt"].active{background:#f3e8ff;color:#7e22ce;border-color:#f3e8ff;box-shadow:0 4px 12px rgba(126,34,206,.2)}
.filter-tab[data-filter="hinh"].active{background:#fee2e2;color:#dc2626;border-color:#fee2e2;box-shadow:0 4px 12px rgba(220,38,38,.2)}
.filter-tab[data-filter="xstk"].active{background:#f1f5f9;color:#475569;border-color:#f1f5f9;box-shadow:0 4px 12px rgba(71,85,105,.2)}
.hub-filters .divider{width:1px;height:28px;background:var(--cc-line);flex-shrink:0;align-self:center}
"""
# Insert after ".filter-tab.active{...}"
content = content.replace(
    "border-color:var(--cc-yellow);box-shadow:0 4px 12px rgba(247, 200, 0, 0.3);\n}\n",
    "border-color:var(--cc-yellow);box-shadow:0 4px 12px rgba(247, 200, 0, 0.3);\n}" + css_insert
)

# 2. Add 3 subject filter buttons + divider in HTML
old_filters = """    <button class="filter-tab" data-filter="10">L\u1edbp 10</button>
  </div>"""
new_filters = """    <button class="filter-tab" data-filter="10">L\u1edbp 10</button>
    <div class="divider"></div>
    <button class="filter-tab" data-filter="dsgt">\u0110S-GT</button>
    <button class="filter-tab" data-filter="hinh">H\u00ecnh</button>
    <button class="filter-tab" data-filter="xstk">XS-TK</button>
  </div>"""
content = content.replace(old_filters, new_filters)

# 3. Update renderList to support subject filtering
old_js = """function renderList(filter = 'all') {
  const filtered = filter === 'all'
    ? CHUYENDE
    : CHUYENDE.filter(e => e.grade === filter);"""
new_js = """const _subjectMap = {'dsgt':'Đại số - Giải tích','hinh':'Hình học','xstk':'Thống kê - Xác suất'};
function renderList(filter = 'all') {
  let filtered;
  if (filter === 'all') filtered = CHUYENDE;
  else if (_subjectMap[filter]) filtered = CHUYENDE.filter(e => e.subject === _subjectMap[filter]);
  else filtered = CHUYENDE.filter(e => e.grade === filter);"""
content = content.replace(old_js, new_js)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done! Filters updated.")
