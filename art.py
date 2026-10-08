# -*- coding: utf-8 -*-
"""Sinh toàn bộ hình minh hoạ SVG (nhẹ, sắc nét, có thể thay bằng ảnh thật WebP sau)."""
import math, random, html as _h

def svg(w, h, body, title=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img"><title>{_h.escape(title)}</title>{body}</svg>')

def leaf(x, y, size, rot, fill, dark=None):
    d = dark or fill
    return (f'<g transform="translate({x} {y}) rotate({rot})">'
            f'<path d="M0 0 C {size*0.55} {-size*0.35}, {size*0.9} {-size*0.1}, {size} 0 '
            f'C {size*0.9} {size*0.1}, {size*0.55} {size*0.35}, 0 0 Z" fill="{fill}"/>'
            f'<path d="M{size*0.08} 0 L{size*0.85} 0" stroke="{d}" stroke-width="3" stroke-linecap="round" opacity=".35"/></g>')

def backdrop(bg1, bg2, w=600, h=600, r=0):
    return (f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient></defs>'
            f'<rect width="{w}" height="{h}" rx="{r}" fill="url(#bg)"/>')

def ground(w=600, h=600, color="#0000001a"):
    return f'<ellipse cx="{w/2}" cy="{h-70}" rx="170" ry="22" fill="{color}"/>'

def pot(cx, base_y, w, h, fill, rim):
    top = base_y - h
    return (f'<path d="M{cx-w/2} {top} L{cx+w/2} {top} L{cx+w*0.38} {base_y} L{cx-w*0.38} {base_y} Z" fill="{fill}"/>'
            f'<rect x="{cx-w/2-10}" y="{top-24}" width="{w+20}" height="30" rx="10" fill="{rim}"/>')

# ---------- cây trồng ----------
def tree_pot(bg1, bg2, canopy, canopy2, fruit=None, potc="#c8794a", rim="#a85f36", big=False):
    b = backdrop(bg1, bg2) + ground()
    b += pot(300, 500, 210, 130, potc, rim)
    b += '<path d="M300 372 C 296 320, 304 270, 300 215" stroke="#6b4a2f" stroke-width="14" stroke-linecap="round" fill="none"/>'
    r = 120 if big else 105
    b += f'<circle cx="300" cy="190" r="{r}" fill="{canopy}"/>'
    b += f'<circle cx="225" cy="230" r="{r*0.62}" fill="{canopy2}"/><circle cx="375" cy="225" r="{r*0.66}" fill="{canopy2}"/>'
    b += f'<circle cx="300" cy="130" r="{r*0.55}" fill="{canopy}" opacity=".9"/>'
    random.seed(7)
    if fruit:
        for (x, y) in [(250, 170), (340, 150), (300, 225), (210, 235), (385, 230), (330, 195)]:
            b += f'<circle cx="{x}" cy="{y}" r="{16 if big else 13}" fill="{fruit}"/><circle cx="{x-4}" cy="{y-5}" r="4" fill="#ffffff" opacity=".45"/>'
    return b

def sapling_pot(bg1, bg2, leafc, leafc2, potc="#d98c5f", rim="#b8693f"):
    b = backdrop(bg1, bg2) + ground()
    b += pot(300, 500, 190, 120, potc, rim)
    b += '<path d="M300 376 C 300 330, 296 290, 300 220" stroke="#4d8a3a" stroke-width="10" stroke-linecap="round" fill="none"/>'
    for i, (x, y, rot, s) in enumerate([(300, 330, -150, 95), (300, 310, -30, 100), (300, 270, -160, 85), (300, 255, -20, 90), (300, 225, -120, 80), (300, 215, -60, 80)]):
        b += leaf(x, y, s, rot, leafc if i % 2 == 0 else leafc2, "#0e3b2a")
    return b

# ---------- hạt giống ----------
def seed_packet(bg1, bg2, packet, accent, plant="tomato"):
    b = backdrop(bg1, bg2) + ground()
    b += f'<g transform="rotate(-6 300 300)">'
    b += f'<rect x="170" y="110" width="260" height="360" rx="16" fill="{packet}"/>'
    zig = "".join(f'<path d="M{170+i*26} 110 l13 -22 l13 22 z" fill="{packet}"/>' for i in range(10))
    b += zig
    b += f'<rect x="170" y="110" width="260" height="34" rx="6" fill="#00000022"/>'
    b += '<rect x="196" y="190" width="208" height="210" rx="105" fill="#ffffffee"/>'
    if plant == "tomato":
        b += '<circle cx="262" cy="320" r="34" fill="#ef4444"/><circle cx="332" cy="330" r="30" fill="#f87171"/>'
        b += '<path d="M250 292 l12 -12 l12 12 l-12 6z M320 304 l12 -12 l12 12 l-12 6z" fill="#2f9e44"/>'
        b += '<path d="M300 280 C 300 250 300 240 300 230" stroke="#2f9e44" stroke-width="7" fill="none"/>'
    elif plant == "lettuce":
        for rot, c in [(-110, "#7bd25a"), (-70, "#58b83e"), (-90, "#9be16e"), (-130, "#58b83e"), (-50, "#7bd25a")]:
            b += leaf(300, 360, 110, rot, c, "#1f6b2a")
        b += '<circle cx="300" cy="352" r="16" fill="#4aa332"/>'
    elif plant == "basil":
        for rot, c in [(-120, "#3fae49"), (-60, "#2e9a3d"), (-90, "#56c15a"), (-150, "#2e9a3d"), (-30, "#3fae49")]:
            b += leaf(300, 355, 95, rot, c, "#14532d")
        b += '<path d="M300 355 L300 385" stroke="#14532d" stroke-width="7" stroke-linecap="round"/>'
    b += f'<rect x="196" y="418" width="208" height="14" rx="7" fill="{accent}"/>'
    b += '</g>'
    # hạt rải
    for x, y, r in [(110, 470, -20), (150, 505, 30), (460, 490, 15), (500, 450, -40), (420, 520, 60)]:
        b += f'<ellipse cx="{x}" cy="{y}" rx="9" ry="5" fill="#8a5a2b" transform="rotate({r} {x} {y})"/>'
    return b

# ---------- đất & phân ----------
def sack(bg1, bg2, color, accent, kind="soil"):
    b = backdrop(bg1, bg2) + ground()
    b += f'<path d="M185 150 C 170 220, 160 380, 180 485 L420 485 C 440 380, 430 220, 415 150 Z" fill="{color}"/>'
    b += f'<path d="M185 150 C 230 120, 370 120, 415 150 C 380 175, 220 175, 185 150Z" fill="#00000026"/>'
    b += f'<path d="M200 135 q100 -45 200 0" stroke="{color}" stroke-width="20" fill="none" stroke-linecap="round"/>'
    b += '<rect x="215" y="230" width="170" height="170" rx="85" fill="#ffffffee"/>'
    if kind == "soil":
        b += '<path d="M232 372 Q300 330 368 372 Z" fill="#6b4226"/><path d="M300 345 C 300 320 300 305 300 285" stroke="#2f9e44" stroke-width="8" fill="none" stroke-linecap="round"/>'
        b += leaf(300, 300, 48, -150, "#4cb050") + leaf(300, 300, 48, -30, "#68c76a")
    else:
        # trùn quế + lá
        b += '<path d="M240 340 q15 -28 30 0 t30 0 t30 0" stroke="#b5651d" stroke-width="12" fill="none" stroke-linecap="round"/>'
        b += leaf(300, 300, 52, -140, "#4cb050") + leaf(300, 300, 52, -40, "#68c76a")
    b += f'<rect x="215" y="418" width="170" height="14" rx="7" fill="{accent}"/>'
    return b

# ---------- dụng cụ ----------
def shears(bg1, bg2, handle, blade):
    b = backdrop(bg1, bg2) + ground()
    b += f'<g transform="rotate(35 300 300)">'
    b += f'<path d="M300 300 L300 90 Q 330 90 330 140 L 312 300 Z" fill="{blade}"/>'
    b += f'<path d="M300 300 L300 120 Q 270 110 272 150 L 288 300 Z" fill="#cfd8dc"/>'
    b += f'<rect x="272" y="296" width="14" height="40" rx="7" fill="#546e7a"/>'
    b += f'<path d="M288 330 C 250 420, 230 480, 260 520 C 290 540, 300 480, 305 360 Z" fill="{handle}"/>'
    b += f'<path d="M315 330 C 350 420, 372 480, 342 520 C 312 540, 300 480, 300 360 Z" fill="{handle}" opacity=".85"/>'
    b += '<circle cx="300" cy="312" r="10" fill="#37474f"/></g>'
    return b

def tool_kit(bg1, bg2, handle, metal):
    b = backdrop(bg1, bg2) + ground()
    # xẻng nhỏ
    b += f'<g transform="rotate(-12 200 300)"><path d="M200 120 C 150 120, 140 210, 200 250 C 260 210, 250 120, 200 120 Z" fill="{metal}"/>'
    b += f'<rect x="190" y="245" width="20" height="170" rx="10" fill="{handle}"/></g>'
    # cào
    b += f'<g transform="rotate(8 330 300)"><rect x="300" y="120" width="70" height="26" rx="8" fill="{metal}"/>'
    b += "".join(f'<rect x="{304+i*17}" y="140" width="9" height="55" rx="4" fill="{metal}"/>' for i in range(4))
    b += f'<rect x="326" y="190" width="18" height="225" rx="9" fill="{handle}"/></g>'
    # găng tay
    b += f'<path d="M420 330 q10 -70 40 -60 q10 5 6 25 l6 -55 q12 -5 18 8 l4 48 l6 -40 q14 -4 16 10 l-2 48 l10 -30 q14 0 12 14 q-6 70 -40 100 q-40 20 -72 -20z" fill="#facc15" transform="translate(-10 40)"/>'
    return b

# ---------- cảnh hero ----------
def hero_scene():
    w, h = 900, 1000
    b = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9f5e4"/><stop offset="1" stop-color="#f2fbdc"/></linearGradient></defs>'
         f'<rect width="{w}" height="{h}" fill="url(#sky)"/>')
    b += '<circle cx="660" cy="230" r="110" fill="#ffd54a"/><circle cx="660" cy="230" r="150" fill="#ffd54a" opacity=".22"/>'
    # mây
    b += '<g fill="#ffffff" opacity=".9"><ellipse cx="190" cy="190" rx="90" ry="28"/><ellipse cx="250" cy="170" rx="60" ry="30"/><ellipse cx="740" cy="410" rx="80" ry="22"/></g>'
    # đồi
    b += '<path d="M0 520 C 200 440, 420 470, 900 400 L900 1000 L0 1000Z" fill="#8fd694"/>'
    b += '<path d="M0 620 C 260 540, 520 600, 900 520 L900 1000 L0 1000Z" fill="#5fc176"/>'
    # luống cây
    for i in range(7):
        y = 640 + i * 52
        sc = 0.55 + i * 0.12
        b += f'<path d="M-20 {y} Q450 {y-40*sc} 920 {y}" stroke="#2f9e5a" stroke-width="{10*sc+4}" fill="none" opacity=".55"/>'
        for j in range(6 + i):
            x = 60 + j * (780 / (5 + i))
            b += leaf(x, y - 4, 26 * sc + 10, -120, "#1d7a43") + leaf(x, y - 4, 26 * sc + 10, -60, "#2fa05a")
    # nhà kính
    b += '<g transform="translate(70 360)"><path d="M0 160 L0 70 Q150 -30 300 70 L300 160Z" fill="#ffffff" opacity=".55" stroke="#ffffff" stroke-width="4"/>'
    b += '<path d="M100 160 L100 40 M200 160 L200 40 M0 100 L300 100" stroke="#ffffff" stroke-width="3" opacity=".9"/></g>'
    # cây to giữa
    b += '<path d="M450 760 C 440 650, 462 560, 450 470" stroke="#5b3d22" stroke-width="22" stroke-linecap="round" fill="none"/>'
    b += '<circle cx="450" cy="400" r="150" fill="#1f8a4c"/><circle cx="350" cy="470" r="95" fill="#2fa05a"/><circle cx="560" cy="465" r="100" fill="#2fa05a"/><circle cx="450" cy="300" r="95" fill="#3bb36a"/>'
    for x, y in [(400, 380), (500, 340), (450, 450), (350, 480), (565, 470), (480, 400)]:
        b += f'<circle cx="{x}" cy="{y}" r="19" fill="#ffb020"/><circle cx="{x-6}" cy="{y-7}" r="5" fill="#fff" opacity=".5"/>'
    return svg(w, h, b, "Khu vườn xanh với nhà kính và cây ăn quả")

def cover(c1, c2, motif, w=1200, h=630):
    b = backdrop(c1, c2, w, h)
    b += '<circle cx="1000" cy="130" r="80" fill="#ffd54a" opacity=".85"/>'
    b += f'<path d="M0 470 C 300 400, 700 500, {w} 420 L{w} {h} L0 {h}Z" fill="#ffffff" opacity=".28"/>'
    b += f'<path d="M0 520 C 350 470, 750 560, {w} 500 L{w} {h} L0 {h}Z" fill="#0e3b2a" opacity=".16"/>'
    if motif == "tomato":
        for x, y, r in [(420, 330, 78), (610, 360, 70), (520, 250, 62)]:
            b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ef4444"/><circle cx="{x-r*0.3}" cy="{y-r*0.3}" r="{r*0.18}" fill="#fff" opacity=".4"/>'
            b += leaf(x, y - r + 4, 40, -150, "#2f9e44") + leaf(x, y - r + 4, 40, -30, "#2f9e44")
    elif motif == "soil":
        b += '<path d="M330 470 Q600 290 870 470 Z" fill="#6b4226"/><path d="M600 330 L600 250" stroke="#2f9e44" stroke-width="12" stroke-linecap="round"/>'
        b += leaf(600, 270, 110, -150, "#4cb050") + leaf(600, 270, 110, -30, "#68c76a")
    elif motif == "calendar":
        b += '<rect x="380" y="150" width="440" height="330" rx="28" fill="#fff"/><rect x="380" y="150" width="440" height="80" rx="28" fill="#1f8a4c"/>'
        for r in range(3):
            for c in range(5):
                b += f'<rect x="{410+c*76}" y="{260+r*68}" width="52" height="44" rx="10" fill="{"#ffd54a" if (r,c) in [(1,2),(2,4)] else "#e8f5ec"}"/>'
    else:
        b += '<path d="M600 520 C 596 440, 604 380, 600 320" stroke="#5b3d22" stroke-width="18" stroke-linecap="round" fill="none"/>'
        b += '<circle cx="600" cy="250" r="120" fill="#1f8a4c"/><circle cx="510" cy="300" r="75" fill="#2fa05a"/><circle cx="690" cy="300" r="78" fill="#2fa05a"/><circle cx="600" cy="170" r="70" fill="#3bb36a"/>'
        for x, y in [(560, 240), (650, 215), (600, 300), (520, 310), (690, 305)]:
            b += f'<circle cx="{x}" cy="{y}" r="16" fill="#ffb020"/>'
    return svg(w, h, b, "Ảnh bìa bài viết")

def logo_svg():
    b = ('<rect width="64" height="64" rx="18" fill="#1f8a4c"/>'
         '<path d="M32 50 C 32 40, 32 34, 32 26" stroke="#fff" stroke-width="4" stroke-linecap="round" fill="none"/>'
         '<path d="M32 30 C 20 30, 14 22, 14 14 C 24 14, 32 18, 32 30Z" fill="#c6f26b"/>'
         '<path d="M32 36 C 44 36, 50 28, 50 20 C 40 20, 32 24, 32 36Z" fill="#ffffff"/>')
    return svg(64, 64, b, "Nông Xanh")
