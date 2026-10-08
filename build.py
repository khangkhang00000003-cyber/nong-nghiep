# -*- coding: utf-8 -*-
"""Sinh toàn bộ website tĩnh Nông Xanh vào thư mục site/.  Chạy: python3 build.py"""
import json, os, re, shutil, html as H
from html.parser import HTMLParser
import data as D
import art

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
BASE = D.BASE
CAT = {c["slug"]: c for c in D.CATEGORIES}
PROD = {p["slug"]: p for p in D.PRODUCTS}
ART = {a["slug"]: a for a in D.ARTICLES}
esc = lambda s: H.escape(str(s), quote=True)

NAV = [("/cay-giong/", "Cây giống"), ("/hat-giong/", "Hạt giống"), ("/dat-va-phan-bon/", "Đất & phân bón"),
       ("/dung-cu-lam-vuon/", "Dụng cụ"), ("/kien-thuc/", "Kiến thức"), ("/gioi-thieu/", "Giới thiệu"), ("/lien-he/", "Liên hệ")]

KT = dict(slug="kien-thuc", title="Kiến thức nông nghiệp: cách trồng rau, chăm cây | Nông Xanh",
          desc="Bài hướng dẫn trồng rau, chọn đất, lên lịch gieo trồng và chăm sóc cây ăn quả trồng chậu, viết dễ hiểu cho người mới bắt đầu làm vườn.",
          h1="Kiến thức nông nghiệp cho người mới làm vườn")
SM = dict(slug="so-do-trang", title="Sơ đồ trang Nông Xanh – Toàn bộ danh mục và bài viết",
          desc="Sơ đồ trang web Nông Xanh liệt kê đầy đủ danh mục cây giống, hạt giống, đất phân bón, dụng cụ làm vườn và các bài viết kiến thức nông nghiệp.",
          h1="Sơ đồ trang web Nông Xanh")

def vnd(n): return f"{n:,}".replace(",", ".") + "đ"
def u(path): return BASE + path
def write(rel, content, mode="w"):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if mode == "w":
        with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(content)
    else:
        with open(p, "wb") as f: f.write(content)

def jld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"

# ----------------------------------------------------------------- hình ảnh
def make_art():
    d = os.path.join("assets", "img")
    write(f"{d}/logo.svg", art.logo_svg()); write("favicon.svg", art.logo_svg())
    write(f"{d}/hero.svg", art.hero_scene())
    for p in D.PRODUCTS:
        k, a = p["art"]
        fn = {"seed": art.seed_packet, "tree": art.tree_pot, "sack": art.sack, "shears": art.shears, "tools": art.tool_kit}[k]
        write(f"{d}/p-{p['slug']}.svg", art.svg(600, 600, fn(*a), p["alt"]))
    for c in D.CATEGORIES:
        b1, b2 = c["bg"]
        body = {"tree": lambda: art.tree_pot(b1, b2, "#1f8a4c", "#2fa05a", "#ffb020", big=True),
                "seed": lambda: art.seed_packet(b1, b2, "#ef6a5b", "#b91c1c", "tomato"),
                "sack": lambda: art.sack(b1, b2, "#3f7d3a", "#c6f26b", "worm"),
                "tools": lambda: art.tool_kit(b1, b2, "#2f9e44", "#90a4ae")}[c["art"]]()
        write(f"{d}/cat-{c['slug']}.svg", art.svg(600, 600, body, c["name"]))
    for a in D.ARTICLES:
        write(f"{d}/a-{a['slug']}.svg", art.cover(a["c"][0], a["c"][1], a["motif"]))
    # PNG: og-image, apple-touch-icon, logo, favicon.ico
    from PIL import Image, ImageDraw, ImageFont
    sf = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; sn = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    W, Hh = 1200, 630
    im = Image.new("RGB", (W, Hh), "#0e3b2a"); dr = ImageDraw.Draw(im)
    for y in range(Hh):
        t = y / Hh; dr.line([(0, y), (W, y)], fill=(int(14 + 9 * t), int(59 + 80 * t), int(42 + 34 * t)))
    dr.ellipse((820, -120, 1320, 380), fill="#ffc933"); dr.ellipse((860, -80, 1280, 340), fill="#ffd54a")
    for i, (x, y, r, c) in enumerate([(960, 520, 230, "#2fa05a"), (760, 560, 190, "#1f8a4c"), (1140, 540, 170, "#3bb36a")]):
        dr.ellipse((x - r, y - r, x + r, y + r), fill=c)
    dr.rounded_rectangle((70, 70, 150, 150), radius=22, fill="#c6f26b")
    dr.line([(110, 132), (110, 100)], fill="#0e3b2a", width=7)
    dr.polygon([(110, 104), (84, 96), (88, 82), (110, 90)], fill="#0e3b2a"); dr.polygon([(110, 112), (136, 102), (132, 88), (110, 98)], fill="#0e3b2a")
    dr.text((170, 85), "Nông Xanh", font=ImageFont.truetype(sf, 54), fill="white")
    dr.text((70, 230), "Cây giống, hạt giống", font=ImageFont.truetype(sf, 76), fill="white")
    dr.text((70, 330), "& vật tư làm vườn cho mọi nhà", font=ImageFont.truetype(sf, 52), fill="#c6f26b")
    dr.text((70, 470), "Giao hàng toàn quốc  •  Hướng dẫn trồng kèm theo", font=ImageFont.truetype(sn, 30), fill="#d7efe0")
    buf = os.path.join(OUT, "assets", "img"); os.makedirs(buf, exist_ok=True)
    im.save(os.path.join(buf, "og-image.png"), optimize=True)
    def icon(size):
        s = 512; i2 = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d2 = ImageDraw.Draw(i2)
        d2.rounded_rectangle((0, 0, s, s), radius=int(s * .28), fill="#1f8a4c")
        d2.line([(256, 400), (256, 210)], fill="white", width=30)
        d2.polygon([(256, 250), (110, 230), (112, 120), (256, 160)], fill="#c6f26b")
        d2.polygon([(256, 300), (400, 280), (398, 170), (256, 210)], fill="white")
        return i2.resize((size, size), Image.LANCZOS)
    icon(180).save(os.path.join(OUT, "apple-touch-icon.png")); icon(512).save(os.path.join(buf, "logo-512.png"))
    icon(256).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])

# ----------------------------------------------------------------- khung trang
ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": BASE + "/#org", "name": D.BRAND, "url": BASE + "/",
       "logo": {"@type": "ImageObject", "url": u("/assets/img/logo-512.png"), "width": 512, "height": 512},
       "email": D.EMAIL, "telephone": D.PHONE_TEL,
       "description": "Cửa hàng cây giống, hạt giống, đất trồng, phân bón và dụng cụ làm vườn cho gia đình."}
FONT = "https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800&display=swap"

def head(path, title, desc, schema, og_img="/assets/img/og-image.png", og_type="website", noindex=False, preload=None):
    canon = u(path)
    assert 50 <= len(title) <= 60, (len(title), title)
    assert 120 <= len(desc) <= 160, (len(desc), desc)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    ga = ""
    if D.GA4_ID:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={D.GA4_ID}"></script>'
              f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{D.GA4_ID}");</script>')
    alt = "" if noindex else (f'<link rel="alternate" hreflang="vi" href="{canon}"><link rel="alternate" hreflang="x-default" href="{canon}">')
    pre = f'<link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ""
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
{alt}
<meta name="theme-color" content="#1f8a4c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{D.BRAND}">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{u(og_img)}">
<meta property="og:image:width" content="{1200 if og_img.endswith('.png') else 1200}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{u(og_img)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONT}">
<link rel="stylesheet" href="/assets/css/style.css">
{pre}
{chr(10).join(jld(s) for s in schema)}
{ga}
</head>'''

def header(active=""):
    items = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{esc(t)}</a></li>' for h, t in NAV)
    return f'''<body>
<a class="skip" href="#main">Bỏ qua và đến nội dung chính</a>
<div class="announce">Miễn phí vận chuyển cho đơn từ {vnd(D.FREE_SHIP)}. Cần tư vấn chọn cây? <a href="/lien-he/">Nhắn cho chúng tôi</a></div>
<header class="site-header"><div class="container bar">
<a class="brand" href="/"><img src="/assets/img/logo.svg" alt="Logo Nông Xanh" width="42" height="42"><span>{D.BRAND}</span></a>
<nav class="nav" aria-label="Menu chính"><ul>{items}</ul></nav>
<button class="cart-btn" type="button" aria-label="Mở giỏ hàng"><span class="cart-label">Giỏ hàng</span> <span class="cart-count" aria-live="polite">0</span></button>
<button class="menu-btn" type="button" aria-label="Mở menu" aria-expanded="false">☰</button>
</div></header>
<main id="main">'''

def footer():
    cats = "".join(f'<li><a href="/{c["slug"]}/">{esc(c["name"])}</a></li>' for c in D.CATEGORIES)
    arts = "".join(f'<li><a href="/kien-thuc/{a["slug"]}/">{esc(a["title"])}</a></li>' for a in D.ARTICLES[:3])
    return f'''</main>
<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><a class="brand" href="/"><img src="/assets/img/logo.svg" alt="Logo Nông Xanh" width="42" height="42"><span>{D.BRAND}</span></a>
<p>Cây giống, hạt giống, đất trồng, phân bón và dụng cụ làm vườn cho gia đình Việt. Có hướng dẫn trồng đi kèm từng sản phẩm.</p></div>
<div><p class="foot-title">Sản phẩm</p><ul>{cats}</ul></div>
<div><p class="foot-title">Kiến thức</p><ul>{arts}<li><a href="/kien-thuc/">Xem tất cả bài viết</a></li></ul></div>
<div><p class="foot-title">Liên hệ</p><ul>
<li>Điện thoại: <a href="tel:{D.PHONE_TEL}">{D.PHONE_DISPLAY}</a></li>
<li>Email: <a href="mailto:{D.EMAIL}">{D.EMAIL}</a></li>
<li>{esc(D.ADDRESS)}</li>
<li><a href="/chinh-sach/">Giao hàng và đổi trả</a></li>
<li><a href="/so-do-trang/">Sơ đồ trang</a></li></ul></div>
</div>
<div class="foot-bottom"><span>© 2026 {D.BRAND}. Bảo lưu mọi quyền.</span><span>Làm vườn xanh, sống nhẹ nhàng.</span></div>
</div></footer>
<div class="drawer-back"></div>
<aside class="drawer" aria-label="Giỏ hàng">
<header><p class="drawer-title">Giỏ hàng của bạn</p><button class="close" type="button" aria-label="Đóng giỏ hàng">×</button></header>
<ul class="cart-items"></ul>
<p class="cart-empty">Giỏ hàng đang trống. Hãy chọn vài gói hạt giống để bắt đầu vườn của bạn.</p>
<footer hidden>
<div class="total-row"><span>Tạm tính</span><span class="cart-total">0đ</span></div>
<p class="ship-note"></p>
<button class="btn btn-primary send-zalo" type="button">Sao chép đơn và gửi qua Zalo</button>
<button class="btn btn-ghost send-mail" type="button">Gửi đơn qua email</button>
</footer></aside>
<div class="toast" role="status" aria-live="polite"></div>
<div class="fab"><a href="tel:{D.PHONE_TEL}" aria-label="Gọi cho Nông Xanh">☎</a></div>
<script>window.NX={{zalo:"{D.ZALO}",email:"{D.EMAIL}",freeShip:{D.FREE_SHIP}}};</script>
<script src="/assets/js/main.js" defer></script>
</body>
</html>'''

def crumbs(items):
    """items: [(tên, đường dẫn)] – phần tử cuối là trang hiện tại."""
    lis = ""
    for i, (n, p) in enumerate(items):
        lis += f'<li><a href="{p}">{esc(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{esc(n)}</li>'
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u(p)} for i, (n, p) in enumerate(items)]}
    return f'<nav class="breadcrumb" aria-label="Đường dẫn"><ol>{lis}</ol></nav>', schema

def page(path, title, desc, body, schema, active="", **kw):
    html = head(path, title, desc, schema, **kw) + header(active) + body + footer()
    rel = path.strip("/") + "/index.html" if path != "/" else "index.html"
    write(rel, html)
    return rel

# ----------------------------------------------------------------- thành phần
def card(p, lazy=True):
    c = CAT[p["cat"]]; href = f'/{p["cat"]}/{p["slug"]}/'; img = f'/assets/img/p-{p["slug"]}.svg'
    badge = f'<span class="badge">-{round((1 - p["price"] / p["old"]) * 100)}%</span>' if p["old"] else ""
    old = f'<s>{vnd(p["old"])}</s>' if p["old"] else ""
    return f'''<article class="p-card">{badge}
<a class="thumb" href="{href}"><img src="{img}" alt="{esc(p["alt"])}" width="600" height="600"{' loading="lazy"' if lazy else ''}></a>
<div class="p-body"><span class="p-cat">{esc(c["short"])}</span>
<h3><a href="{href}">{esc(p["name"])}</a></h3>
<div class="price"><b>{vnd(p["price"])}</b>{old}</div>
<button class="btn btn-primary btn-sm add-to-cart" type="button" data-id="{p["slug"]}" data-name="{esc(p["name"])}" data-price="{p["price"]}" data-img="{img}">Thêm vào giỏ</button>
</div></article>'''

def post_card(a):
    return f'''<a class="post-card" href="/kien-thuc/{a["slug"]}/">
<img src="/assets/img/a-{a["slug"]}.svg" alt="{esc(a["alt"])}" width="1200" height="630" loading="lazy">
<div><h3>{esc(a["title"])}</h3><p>{esc(a["desc"])}</p><span class="meta">{a["read"]} phút đọc</span></div></a>'''

def cta_block():
    return f'''<section><div class="container"><div class="cta"><div><h2>Chưa biết nên chọn cây nào?</h2>
<p>Cho chúng tôi biết diện tích, lượng nắng và kinh nghiệm của bạn. Chúng tôi sẽ gợi ý cây và vật tư phù hợp.</p></div>
<a class="btn btn-sun" href="https://zalo.me/{D.ZALO}" rel="noopener" target="_blank">Tư vấn miễn phí qua Zalo</a></div></div></section>'''

# ----------------------------------------------------------------- TRANG CHỦ
def build_home():
    feat = [p for p in D.PRODUCTS if p["feat"]][:8]
    cats = "".join(f'''<a class="cat-card" href="/{c["slug"]}/"><div class="arch-sm"><img src="/assets/img/cat-{c["slug"]}.svg" alt="{esc(c["name"])} tại Nông Xanh" width="600" height="600" loading="lazy"></div>
<h3>{esc(c["name"])}</h3><p>{esc(c["tagline"])}</p></a>''' for c in D.CATEGORIES)
    seasons = "".join(f'<div class="season"><h3>{esc(t)}</h3><p>{esc(d)}</p><ul class="tags">{"".join(f"<li>{esc(x)}</li>" for x in tags)}</ul></div>' for t, d, tags in D.SEASONS)
    faq = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in D.FAQS)
    body = f'''
<div class="hero"><div class="container hero-grid">
<div>
<h1>Cây giống, hạt giống và vật tư làm vườn cho mọi nhà</h1>
<p class="lead">Nông Xanh giúp bạn bắt đầu khu vườn từ ban công nhỏ đến mảnh đất rộng. Giống rõ nguồn gốc, đất sạch, dụng cụ bền và hướng dẫn trồng kèm theo từng sản phẩm.</p>
<div class="hero-actions"><a class="btn btn-primary" href="/hat-giong/">Chọn hạt giống</a><a class="btn btn-ghost" href="/cay-giong/">Xem cây giống ăn quả</a></div>
<ul class="chips"><li>Giao hàng toàn quốc</li><li>Có hướng dẫn trồng</li><li>Đổi cây nếu hỏng khi vận chuyển</li></ul>
</div>
<div class="hero-visual"><div class="arch"><img src="/assets/img/hero.svg" alt="Khu vườn xanh với nhà kính, luống rau và cây ăn quả sai trái" width="900" height="1000" fetchpriority="high"></div>
<a class="hero-float" href="/hat-giong/ca-chua-cherry/"><img src="/assets/img/p-ca-chua-cherry.svg" alt="Gói hạt giống cà chua cherry" width="54" height="54"><div><strong>Hạt giống cà chua cherry</strong><span>Từ {vnd(29000)}</span></div></a></div>
</div></div>
<div class="furrow" aria-hidden="true"></div>

<section class="trust"><div class="container"><ul>
<li><span class="ico" aria-hidden="true">🌱</span><div><strong>Giống rõ nguồn gốc</strong><span>Mỗi sản phẩm đều ghi rõ đặc điểm và thời gian thu hoạch dự kiến.</span></div></li>
<li><span class="ico" aria-hidden="true">🚚</span><div><strong>Giao hàng toàn quốc</strong><span>Cây được đóng bầu và bọc cẩn thận. Miễn phí vận chuyển từ {vnd(D.FREE_SHIP)}.</span></div></li>
<li><span class="ico" aria-hidden="true">📖</span><div><strong>Hướng dẫn từng bước</strong><span>Cách gieo, trồng, tưới và bón phân ngay trên trang sản phẩm.</span></div></li>
<li><span class="ico" aria-hidden="true">🔄</span><div><strong>Hỗ trợ đổi cây</strong><span>Báo trong 24 giờ nếu cây hỏng khi vận chuyển để được đổi mới.</span></div></li>
</ul></div></section>

<section><div class="container">
<div class="section-head"><h2>Mua sắm theo nhu cầu làm vườn</h2><p>Bốn nhóm sản phẩm đủ để bạn đi từ hạt giống đầu tiên đến cây ăn quả cho trái.</p></div>
<div class="cat-grid">{cats}</div></div></section>

<section class="bg-mint"><div class="container">
<div class="section-head"><h2>Sản phẩm nổi bật</h2><p>Những lựa chọn được khách hàng mới bắt đầu làm vườn mua nhiều nhất.</p></div>
<div class="product-grid">{"".join(card(p) for p in feat)}</div></div></section>

<section><div class="container">
<div class="section-head"><h2>Gieo trồng đúng mùa để vườn khỏe hơn</h2><p>Chọn đúng thời điểm giúp cây lên đều, ít sâu bệnh và đỡ tốn công chăm sóc. Đây là gợi ý chung, bạn nên điều chỉnh theo thời tiết nơi mình sống.</p></div>
<div class="season-grid">{seasons}</div>
<p style="margin-top:1.5rem"><a href="/kien-thuc/lich-gieo-trong-rau-theo-mua/">Đọc lịch gieo trồng rau chi tiết</a></p></div></section>

<section class="bg-forest"><div class="container">
<div class="section-head"><h2>Từ hạt giống đến mâm cơm trong bốn bước</h2></div>
<ol class="steps">
<li><h3>Chọn giống phù hợp</h3><p>Dựa vào lượng nắng, kích thước chậu và thời gian bạn có mỗi ngày.</p></li>
<li><h3>Chuẩn bị đất tốt</h3><p>Đất tơi xốp và giàu mùn giúp rễ khỏe, cây ít bệnh ngay từ đầu.</p></li>
<li><h3>Gieo trồng và chăm sóc</h3><p>Tưới đúng lúc, bón phân vừa đủ và tỉa cành khi cần.</p></li>
<li><h3>Thu hoạch và chia sẻ</h3><p>Hái đúng độ chín rồi giữ lại hạt hoặc cây con cho vụ sau.</p></li>
</ol></div></section>

<section><div class="container">
<div class="section-head"><h2>Kiến thức nông nghiệp dễ hiểu</h2><p>Các bài hướng dẫn được viết theo trải nghiệm thực tế của người trồng tại nhà.</p></div>
<div class="post-grid">{"".join(post_card(a) for a in D.ARTICLES)}</div>
<p style="margin-top:1.5rem"><a href="/kien-thuc/">Xem tất cả bài viết kiến thức</a></p></div></section>

<section class="bg-mint"><div class="container narrow faq">
<h2>Câu hỏi thường gặp</h2>{faq}</div></section>

{cta_block()}'''
    schema = [ORG,
              {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": D.BRAND, "inLanguage": "vi", "publisher": {"@id": BASE + "/#org"}},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in D.FAQS]}]
    page("/", "Nông Xanh | Cây giống, hạt giống & vật tư nông nghiệp",
         "Mua cây giống ăn quả, hạt giống rau, đất trồng, phân bón hữu cơ và dụng cụ làm vườn tại Nông Xanh. Giao hàng toàn quốc, có hướng dẫn trồng kèm theo.",
         body, schema, preload="/assets/img/hero.svg")

# ----------------------------------------------------------------- DANH MỤC
def build_categories():
    for c in D.CATEGORIES:
        path = f'/{c["slug"]}/'; items = [p for p in D.PRODUCTS if p["cat"] == c["slug"]]
        bc, bcs = crumbs([("Trang chủ", "/"), (c["name"], path)])
        others = "".join(f'<li><a href="/{o["slug"]}/">{esc(o["name"])}</a></li>' for o in D.CATEGORIES if o["slug"] != c["slug"])
        rel_arts = {p["article"] for p in items}
        posts = "".join(post_card(ART[s]) for s in rel_arts)
        guide = "".join(f'<article><h3>{esc(t)}</h3><p>{esc(d)}</p></article>' for t, d in c["guide"])
        body = f'''
<div class="page-hero"><div class="container">{bc}<h1>{esc(c["h1"])}</h1><p class="lead">{esc(c["tagline"])}</p></div></div>
<section><div class="container">
<h2>Tất cả sản phẩm {esc(c["name"].lower())}</h2>
<div class="product-grid">{"".join(card(p, lazy=False) for p in items)}</div></div></section>
<section class="bg-mint"><div class="container narrow prose">
<h2>Giới thiệu {esc(c["name"].lower())} tại Nông Xanh</h2>{"".join(f"<p>{esc(x)}</p>" for x in c["intro"])}</div></section>
<section><div class="container"><div class="section-head"><h2>Lời khuyên khi chọn mua</h2></div><div class="cat-split">{guide}</div></div></section>
<section class="bg-mint"><div class="container"><div class="section-head"><h2>Bài viết hữu ích</h2></div><div class="post-grid">{posts}</div></div></section>
<section><div class="container narrow prose"><h2>Khám phá danh mục khác</h2><ul>{others}</ul></div></section>
{cta_block()}'''
        schema = [bcs, {"@context": "https://schema.org", "@type": "CollectionPage", "name": c["title"], "url": u(path), "inLanguage": "vi",
                        "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": u(f'/{p["cat"]}/{p["slug"]}/'), "name": p["name"]} for i, p in enumerate(items)]}}]
        page(path, c["title"], c["desc"], body, schema, active=path)

# ----------------------------------------------------------------- SẢN PHẨM
def build_products():
    for p in D.PRODUCTS:
        c = CAT[p["cat"]]; path = f'/{p["cat"]}/{p["slug"]}/'; img = f'/assets/img/p-{p["slug"]}.svg'
        bc, bcs = crumbs([("Trang chủ", "/"), (c["name"], f'/{c["slug"]}/'), (p["name"], path)])
        specs = "".join(f'<tr><th scope="row">{esc(k)}</th><td>{esc(v)}</td></tr>' for k, v in p["specs"])
        guide = "".join(f'<h3>{esc(t)}</h3><p>{esc(d)}</p>' for t, d in p["guide"])
        related = [x for x in D.PRODUCTS if x["cat"] == p["cat"] and x["slug"] != p["slug"]]
        related += [x for x in D.PRODUCTS if x["cat"] != p["cat"] and x["feat"]]
        related = related[:4]
        old = f'<s>{vnd(p["old"])}</s>' if p["old"] else ""
        a = ART[p["article"]]
        body = f'''
<div class="container" style="padding-top:1.6rem">{bc}
<div class="pdp">
<div class="pdp-img"><img src="{img}" alt="{esc(p["alt"])}" width="600" height="600" fetchpriority="high"></div>
<div>
<p class="p-cat"><a href="/{c["slug"]}/">{esc(c["name"])}</a></p>
<h1>{esc(p["name"])}</h1>
<div class="price"><b>{vnd(p["price"])}</b>{old}</div>
<p>{esc(p["short"])}</p>
<div class="buy-row"><div class="qty"><button type="button" data-act="dec" aria-label="Giảm số lượng">−</button><input value="1" inputmode="numeric" aria-label="Số lượng"><button type="button" data-act="inc" aria-label="Tăng số lượng">+</button></div>
<button class="btn btn-primary add-to-cart" type="button" data-id="{p["slug"]}" data-name="{esc(p["name"])}" data-price="{p["price"]}" data-img="{img}">Thêm vào giỏ hàng</button>
<a class="btn btn-ghost" href="https://zalo.me/{D.ZALO}" target="_blank" rel="noopener">Hỏi qua Zalo</a></div>
<p class="notice">Miễn phí vận chuyển cho đơn từ {vnd(D.FREE_SHIP)}. Nếu sản phẩm bị hỏng khi vận chuyển, hãy báo trong 24 giờ để được hỗ trợ. Xem <a href="/chinh-sach/">chính sách giao hàng và đổi trả</a>.</p>
</div></div></div>
<section class="bg-mint"><div class="container narrow prose">
<h2>Thông tin sản phẩm</h2><table class="tbl"><tbody>{specs}</tbody></table>
<h2>Mô tả chi tiết</h2>{"".join(f"<p>{esc(x)}</p>" for x in p["body"])}
<h2>Hướng dẫn sử dụng và chăm sóc</h2>{guide}
<p>Muốn tìm hiểu kỹ hơn? Đọc bài <a href="/kien-thuc/{a["slug"]}/">{esc(a["title"])}</a>.</p></div></section>
<section><div class="container"><div class="section-head"><h2>Sản phẩm bạn có thể quan tâm</h2></div>
<div class="product-grid">{"".join(card(x) for x in related)}</div></div></section>'''
        offer = {"@type": "Offer", "url": u(path), "priceCurrency": "VND", "price": str(p["price"]), "priceValidUntil": "2027-12-31",
                 "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition", "seller": {"@id": BASE + "/#org"}}
        prod = {"@context": "https://schema.org", "@type": "Product", "name": p["name"], "image": [u(img)], "description": p["desc"], "sku": p["slug"],
                "brand": {"@type": "Brand", "name": D.BRAND}, "category": c["name"], "offers": offer}
        page(path, p["title"], p["desc"], body, [bcs, prod], active=f'/{c["slug"]}/', og_img=img.replace(".svg", ".svg"), og_type="product") if False else \
        page(path, p["title"], p["desc"], body, [bcs, prod], active=f'/{c["slug"]}/', og_type="website")

# ----------------------------------------------------------------- KIẾN THỨC
def build_knowledge():
    path = "/kien-thuc/"; bc, bcs = crumbs([("Trang chủ", "/"), ("Kiến thức", path)])
    body = f'''
<div class="page-hero"><div class="container">{bc}<h1>{esc(KT["h1"])}</h1><p class="lead">Hướng dẫn trồng rau, chọn đất, lên lịch gieo trồng và chăm cây ăn quả, viết bằng ngôn ngữ đời thường.</p></div></div>
<section><div class="container"><h2>Bài viết mới nhất</h2><div class="post-grid">{"".join(post_card(a) for a in D.ARTICLES)}</div></div></section>
<section class="bg-mint"><div class="container narrow prose"><h2>Bắt đầu từ đâu?</h2>
<p>Nếu bạn là người mới, hãy đọc bài về <a href="/kien-thuc/cach-chon-dat-trong-cay-trong-chau/">cách chọn đất trồng cây trong chậu</a> trước, sau đó xem <a href="/kien-thuc/lich-gieo-trong-rau-theo-mua/">lịch gieo trồng rau theo mùa</a>. Khi đã quen tay, bạn có thể thử <a href="/kien-thuc/cach-trong-ca-chua-cherry-tai-nha/">trồng cà chua cherry</a> hoặc <a href="/kien-thuc/cach-cham-soc-cay-an-qua-trong-chau/">chăm cây ăn quả trồng chậu</a>.</p>
<p>Bạn cũng có thể xem ngay <a href="/hat-giong/">hạt giống</a>, <a href="/cay-giong/">cây giống</a> và <a href="/dat-va-phan-bon/">đất, phân bón</a> để chuẩn bị cho vụ đầu tiên.</p></div></section>
{cta_block()}'''
    schema = [bcs, {"@context": "https://schema.org", "@type": "CollectionPage", "name": KT["title"], "url": u(path), "inLanguage": "vi"}]
    page(path, KT["title"], KT["desc"], body, schema, active=path)

    for a in D.ARTICLES:
        path = f'/kien-thuc/{a["slug"]}/'; img = f'/assets/img/a-{a["slug"]}.svg'
        bc, bcs = crumbs([("Trang chủ", "/"), ("Kiến thức", "/kien-thuc/"), (a["h1"], path)])
        rel_p = "".join(card(PROD[s]) for s in a["related"])
        others = "".join(post_card(x) for x in D.ARTICLES if x["slug"] != a["slug"])
        body = f'''
<div class="container narrow" style="padding-top:1.6rem">{bc}<h1>{esc(a["h1"])}</h1>
<p class="meta">Cập nhật {D.TODAY[8:10]}/{D.TODAY[5:7]}/{D.TODAY[:4]} • {a["read"]} phút đọc • Bởi đội ngũ {D.BRAND}</p>
<div class="article-cover"><img src="{img}" alt="{esc(a["alt"])}" width="1200" height="630" fetchpriority="high"></div>
<article class="prose">{a["body"]}</article></div>
<section class="bg-mint"><div class="container"><div class="section-head"><h2>Sản phẩm dùng cho bài viết này</h2></div><div class="product-grid">{rel_p}</div></div></section>
<section><div class="container"><div class="section-head"><h2>Bài viết khác bạn có thể thích</h2></div><div class="post-grid">{others}</div></div></section>'''
        art_s = {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["desc"], "inLanguage": "vi",
                 "image": [u(img)], "datePublished": D.TODAY, "dateModified": D.TODAY, "mainEntityOfPage": u(path),
                 "author": {"@type": "Organization", "name": D.BRAND, "url": BASE + "/"}, "publisher": {"@id": BASE + "/#org"}}
        page(path, a["title"], a["desc"], body, [bcs, art_s, ORG], active="/kien-thuc/", og_type="article")

# ----------------------------------------------------------------- TRANG TĨNH
def build_static():
    # Giới thiệu
    path = "/gioi-thieu/"; pg = D.PAGES[0]; bc, bcs = crumbs([("Trang chủ", "/"), ("Giới thiệu", path)])
    body = f'''<div class="page-hero"><div class="container">{bc}<h1>{esc(pg["h1"])}</h1><p class="lead">Chúng tôi tin rằng ai cũng có thể trồng được một thứ gì đó, chỉ cần có đúng giống, đúng đất và đúng hướng dẫn.</p></div></div>
<section><div class="container narrow prose">
<h2>Câu chuyện của Nông Xanh</h2>
<p>Nông Xanh bắt đầu từ một ban công nhỏ và rất nhiều lần trồng thất bại. Chúng tôi nhận ra phần lớn người mới làm vườn không thiếu nhiệt huyết, họ chỉ thiếu thông tin đúng lúc: chọn giống nào, gieo khi nào, đất phải thế nào.</p>
<p>Vì vậy, mỗi sản phẩm tại Nông Xanh đều đi kèm hướng dẫn rõ ràng, và các bài kiến thức được viết từ chính trải nghiệm trồng tại nhà.</p>
<h2>Cam kết của chúng tôi</h2>
<h3>Giống rõ ràng, mô tả trung thực</h3><p>Chúng tôi ghi rõ thời gian nảy mầm, thời gian thu hoạch dự kiến và điều kiện trồng. Kết quả thực tế còn phụ thuộc vào thời tiết và cách chăm sóc nên chúng tôi không hứa hẹn quá mức.</p>
<h3>Đóng gói cẩn thận</h3><p>Cây giống được giữ bầu đất, bọc giấy và đặt trong thùng chuyên dụng để hạn chế dập nát khi vận chuyển.</p>
<h3>Hỗ trợ sau bán hàng</h3><p>Nếu cây gặp vấn đề, bạn có thể gửi ảnh qua Zalo để được tư vấn cách xử lý hoặc hỗ trợ đổi theo chính sách.</p>
<h2>Bạn có thể bắt đầu ngay</h2>
<p>Hãy xem <a href="/hat-giong/">hạt giống</a> nếu muốn thử nhanh, hoặc <a href="/cay-giong/">cây giống ăn quả</a> nếu bạn muốn một dự án dài hơi. Cần giúp đỡ? <a href="/lien-he/">Liên hệ với chúng tôi</a>.</p>
</div></section>'''
    page(path, pg["title"], pg["desc"], body, [bcs, {"@context": "https://schema.org", "@type": "AboutPage", "name": pg["title"], "url": u(path)}, ORG], active=path)

    # Liên hệ
    path = "/lien-he/"; pg = D.PAGES[1]; bc, bcs = crumbs([("Trang chủ", "/"), ("Liên hệ", path)])
    body = f'''<div class="page-hero"><div class="container">{bc}<h1>{esc(pg["h1"])}</h1><p class="lead">Gọi, nhắn Zalo hoặc gửi email. Chúng tôi trả lời trong giờ làm việc.</p></div></div>
<section><div class="container"><div class="cols-2">
<div class="contact-card"><h2>Thông tin liên hệ</h2>
<p><strong>Điện thoại:</strong> <a href="tel:{D.PHONE_TEL}">{D.PHONE_DISPLAY}</a></p>
<p><strong>Zalo:</strong> <a href="https://zalo.me/{D.ZALO}" target="_blank" rel="noopener">Nhắn tin cho Nông Xanh</a></p>
<p><strong>Email:</strong> <a href="mailto:{D.EMAIL}">{D.EMAIL}</a></p>
<p><strong>Địa chỉ:</strong> {esc(D.ADDRESS)}</p>
<p><strong>Giờ làm việc:</strong> 8:00 đến 18:00, thứ Hai đến thứ Bảy</p></div>
<div class="contact-card"><h2>Để được tư vấn nhanh hơn</h2><p>Hãy cho chúng tôi biết:</p>
<ul><li>Bạn trồng ở đâu: ban công, sân thượng hay vườn đất.</li><li>Khu vực có nắng bao nhiêu giờ mỗi ngày.</li><li>Bạn muốn trồng để ăn, để bán hay để làm cảnh.</li><li>Ngân sách dự kiến cho đợt trồng đầu tiên.</li></ul></div>
</div></div></section>
<section class="bg-mint"><div class="container narrow prose"><h2>Cách đặt hàng</h2>
<p>Chọn sản phẩm, bấm thêm vào giỏ, rồi chọn gửi đơn qua Zalo hoặc email. Chúng tôi sẽ xác nhận đơn, phí vận chuyển và thời gian giao. Xem thêm <a href="/chinh-sach/">chính sách giao hàng và đổi trả</a>.</p></div></section>'''
    ctc = {"@context": "https://schema.org", "@type": "ContactPage", "name": pg["title"], "url": u(path)}
    page(path, pg["title"], pg["desc"], body, [bcs, ctc, ORG], active=path)

    # Chính sách
    path = "/chinh-sach/"; pg = D.PAGES[2]; bc, bcs = crumbs([("Trang chủ", "/"), ("Chính sách", path)])
    body = f'''<div class="page-hero"><div class="container">{bc}<h1>{esc(pg["h1"])}</h1><p class="lead">Thông tin rõ ràng để bạn yên tâm khi đặt mua cây giống và vật tư làm vườn.</p></div></div>
<section><div class="container narrow prose">
<h2>Phí và thời gian vận chuyển</h2>
<p>Đơn hàng từ {vnd(D.FREE_SHIP)} được miễn phí vận chuyển. Với đơn nhỏ hơn, phí vận chuyển phụ thuộc khu vực và được báo khi xác nhận đơn. Thời gian giao thông thường từ 1 đến 5 ngày tùy địa chỉ nhận hàng.</p>
<h2>Cách đóng gói</h2>
<h3>Cây giống</h3><p>Cây được giữ bầu đất, bọc giấy và đặt trong thùng chuyên dụng. Khi nhận hàng, hãy mở thùng ngay, tưới nhẹ và đặt cây nơi râm mát 1 đến 2 ngày trước khi đưa ra nắng.</p>
<h3>Hạt giống, đất và dụng cụ</h3><p>Hạt giống được đóng gói kín. Đất, phân bón và dụng cụ được đóng trong bao và hộp chắc chắn để tránh rách vỡ.</p>
<h2>Đổi trả</h2>
<p>Khi nhận hàng, bạn nên quay video lúc mở thùng. Nếu sản phẩm bị hư hỏng, sai mẫu hoặc cây bị héo do vận chuyển, hãy báo cho chúng tôi trong vòng 24 giờ kèm hình ảnh hoặc video. Chúng tôi sẽ đổi sản phẩm mới hoặc hoàn tiền sau khi xác nhận.</p>
<p>Cây bị chết do chăm sóc không đúng cách sau khi nhận không nằm trong phạm vi đổi trả, nhưng chúng tôi vẫn sẵn sàng tư vấn để bạn trồng lại tốt hơn.</p>
<h2>Thanh toán</h2>
<p>Bạn có thể thanh toán khi nhận hàng hoặc chuyển khoản theo hướng dẫn khi xác nhận đơn.</p>
<p>Còn thắc mắc? <a href="/lien-he/">Liên hệ với chúng tôi</a>.</p>
</div></section>'''
    page(path, pg["title"], pg["desc"], body, [bcs], active=path)

    # Sơ đồ trang (HTML sitemap)
    path = "/so-do-trang/"; bc, bcs = crumbs([("Trang chủ", "/"), ("Sơ đồ trang", path)])
    blocks = ""
    for c in D.CATEGORIES:
        li = "".join(f'<li><a href="/{c["slug"]}/{p["slug"]}/">{esc(p["name"])}</a></li>' for p in D.PRODUCTS if p["cat"] == c["slug"])
        blocks += f'<h2><a href="/{c["slug"]}/">{esc(c["name"])}</a></h2><ul>{li}</ul>'
    li = "".join(f'<li><a href="/kien-thuc/{a["slug"]}/">{esc(a["h1"])}</a></li>' for a in D.ARTICLES)
    blocks += f'<h2><a href="/kien-thuc/">Kiến thức nông nghiệp</a></h2><ul>{li}</ul>'
    blocks += '<h2>Thông tin</h2><ul><li><a href="/gioi-thieu/">Giới thiệu</a></li><li><a href="/lien-he/">Liên hệ</a></li><li><a href="/chinh-sach/">Chính sách giao hàng và đổi trả</a></li></ul>'
    body = f'''<div class="page-hero"><div class="container">{bc}<h1>{esc(SM["h1"])}</h1><p class="lead">Tất cả trang của Nông Xanh trong một nơi.</p></div></div>
<section><div class="container narrow prose"><ul><li><a href="/">Trang chủ</a></li></ul>{blocks}</div></section>'''
    page(path, SM["title"], SM["desc"], body, [bcs], active="")

    # 404
    h = head("/404.html", "Không tìm thấy trang | Nông Xanh – Cây giống, hạt giống", "Trang bạn tìm không tồn tại hoặc đã được chuyển đi. Hãy quay lại trang chủ Nông Xanh để xem cây giống, hạt giống và dụng cụ làm vườn.", [], noindex=True)
    b = '''<section><div class="container narrow prose" style="text-align:center;padding:3rem 0"><h1>Không tìm thấy trang này</h1><p>Có thể đường dẫn đã thay đổi. Hãy thử một trong các lối đi bên dưới.</p>
<p><a class="btn btn-primary" href="/">Về trang chủ</a> <a class="btn btn-ghost" href="/hat-giong/">Xem hạt giống</a></p></div></section>'''
    write("404.html", h + header() + b + footer())

# ----------------------------------------------------------------- SITEMAP, ROBOTS
def build_seo_files():
    urls = [("/", "1.0", "weekly")]
    urls += [(f'/{c["slug"]}/', "0.9", "weekly") for c in D.CATEGORIES]
    urls += [(f'/{p["cat"]}/{p["slug"]}/', "0.8", "weekly") for p in D.PRODUCTS]
    urls += [("/kien-thuc/", "0.8", "weekly")] + [(f'/kien-thuc/{a["slug"]}/', "0.7", "monthly") for a in D.ARTICLES]
    urls += [("/gioi-thieu/", "0.5", "yearly"), ("/lien-he/", "0.5", "yearly"), ("/chinh-sach/", "0.4", "yearly"), ("/so-do-trang/", "0.3", "monthly")]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p, pr, cf in urls:
        xml += f'  <url><loc>{u(p)}</loc><lastmod>{D.TODAY}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>\n'
    xml += "</urlset>\n"
    write("sitemap.xml", xml)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write(".nojekyll", "")
    return urls

# ----------------------------------------------------------------- KIỂM TRA (giống tiêu chí SEOquake)
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.h = {}; s.imgs = []; s.links = []; s.text = []; s.skip = 0; s.title = ""; s.in_title = False; s.meta = {}; s.canon = None; s.ld = []; s.in_ld = False; s.lang = None
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "html": s.lang = a.get("lang")
        if t in ("h1", "h2", "h3", "h4"): s.h[t] = s.h.get(t, 0) + 1
        if t == "img": s.imgs.append(a)
        if t == "a" and a.get("href"): s.links.append(a["href"])
        if t == "title": s.in_title = True
        if t == "meta":
            k = a.get("name") or a.get("property")
            if k: s.meta[k] = a.get("content", "")
        if t == "link" and a.get("rel") == "canonical": s.canon = a["href"]
        if t == "script": s.skip += 1; s.in_ld = a.get("type") == "application/ld+json"
        if t == "style": s.skip += 1
    def handle_endtag(s, t):
        if t == "title": s.in_title = False
        if t in ("script", "style"): s.skip -= 1; s.in_ld = False
    def handle_data(s, d):
        if s.in_title: s.title += d
        elif s.in_ld: s.ld.append(d)
        elif s.skip == 0: s.text.append(d)

def validate(urls):
    problems = []; rows = []
    files = set()
    for r, _, fs in os.walk(OUT):
        for f in fs: files.add(os.path.relpath(os.path.join(r, f), OUT).replace(os.sep, "/"))
    def exists(href):
        href = href.split("#")[0].split("?")[0]
        if not href.startswith("/"): return True
        if href.endswith("/"): return href.lstrip("/") + "index.html" in files or href == "/"
        return href.lstrip("/") in files
    for p, _, _ in urls:
        rel = "index.html" if p == "/" else p.strip("/") + "/index.html"
        raw = open(os.path.join(OUT, rel), encoding="utf-8").read()
        q = P(); q.feed(raw)
        words = len(re.findall(r"\w+", " ".join(q.text), flags=re.UNICODE))
        ratio = len(" ".join(q.text).encode()) / len(raw.encode()) * 100
        d = q.meta.get("description", "")
        checks = {
            "title 50-60": 50 <= len(q.title) <= 60, "desc 120-160": 120 <= len(d) <= 160, "1 H1": q.h.get("h1") == 1,
            "H2>=1": q.h.get("h2", 0) >= 1, "alt đủ": all(i.get("alt") for i in q.imgs), "canonical": q.canon == u(p),
            "lang vi": q.lang == "vi", "viewport": "viewport" in q.meta, "OG": all(k in q.meta for k in ("og:title", "og:description", "og:image", "og:url")),
            "Twitter": "twitter:card" in q.meta, "schema": len(q.ld) > 0, "robots index": "index" in q.meta.get("robots", "") and "noindex" not in q.meta.get("robots", ""),
        }
        for s in q.ld:
            try: json.loads(s)
            except Exception as e: checks["JSON-LD hợp lệ"] = False
        bad_links = [h for h in q.links if not exists(h)]
        if bad_links: checks["link nội bộ không lỗi"] = False
        for k, v in checks.items():
            if not v: problems.append((p, k, bad_links if k.startswith("link") else ""))
        rows.append((p, len(q.title), len(d), words, round(ratio, 1), dict(q.h), len(q.imgs), len(q.links)))
    return rows, problems

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets", "css")); os.makedirs(os.path.join(OUT, "assets", "js"))
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copy(os.path.join(here, "static", "style.css"), os.path.join(OUT, "assets", "css", "style.css"))
    shutil.copy(os.path.join(here, "static", "main.js"), os.path.join(OUT, "assets", "js", "main.js"))
    make_art(); build_home(); build_categories(); build_products(); build_knowledge(); build_static()
    urls = build_seo_files()
    rows, problems = validate(urls)
    print(f"{'URL':58} T   D   từ   text%  H  ảnh link")
    for r in rows: print(f"{r[0]:58} {r[1]:<3} {r[2]:<3} {r[3]:<4} {r[4]:<5} {r[5]} {r[6]} {r[7]}")
    print("\nTổng số URL trong sitemap:", len(urls))
    print("VẤN ĐỀ:" , problems if problems else "không có – tất cả trang đạt")

if __name__ == "__main__":
    main()
