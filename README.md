# Nông Xanh – Website cây giống, hạt giống & vật tư nông nghiệp

## 1. Đưa lên GitHub Pages (quan trọng để robots.txt và sitemap.xml đạt xanh)
Báo cáo SEOquake kiểm tra `https://tranthiquynhnhu0901-hue.github.io/robots.txt` và `/sitemap.xml` ở **gốc tên miền**.
Vì vậy website phải nằm ở repo có tên đúng là **`tranthiquynhnhu0901-hue.github.io`** (không phải repo con như `shopthethao`).

1. Tạo repo `tranthiquynhnhu0901-hue.github.io` (Public).
2. Giải nén file zip, upload **toàn bộ nội dung bên trong thư mục `site/`** lên gốc repo (có `index.html`, `robots.txt`, `sitemap.xml`, `404.html`, `assets/`...).
3. Settings → Pages → Source: Deploy from a branch → `main` / `(root)`.
4. Đợi 1–2 phút rồi mở https://tranthiquynhnhu0901-hue.github.io/

## 2. Việc BẮT BUỘC phải sửa (đang là dữ liệu mẫu)
Mở `data.py`, sửa khối CẤU HÌNH ở đầu file rồi chạy `python3 build.py`:
- `PHONE_DISPLAY`, `PHONE_TEL`, `ZALO`, `EMAIL`, `ADDRESS`: thông tin liên hệ thật.
- `GA4_ID`: mã Google Analytics dạng `G-XXXXXXXXXX` (để trống thì chưa bật theo dõi).
- Giá, thông số, chính sách giao hàng / đổi trả trong `data.py` và trang `/chinh-sach/` là nội dung mẫu, hãy chỉnh theo đúng thực tế shop.

## 3. Đối chiếu với báo cáo SEOquake
| Mục trong báo cáo | Cách website xử lý |
|---|---|
| Title 50–60 ký tự | Mọi trang đều 50–60 ký tự, từ khóa chính ở đầu (script build tự kiểm tra) |
| Meta description | Mọi trang 120–160 ký tự |
| Heading | Mỗi trang đúng 1 H1, có H2/H3 phân cấp |
| ALT | Mọi ảnh đều có alt mô tả |
| Canonical | Có trên mọi trang |
| Sitemap / Robots | `sitemap.xml` (24 URL) và `robots.txt` có dòng Sitemap |
| Favicon | `favicon.svg`, `favicon.ico`, `apple-touch-icon.png` |
| Schema.org | Organization, WebSite, FAQPage, Product, Article, BreadcrumbList, CollectionPage |
| Open Graph / Twitter Card | Có đủ trên mọi trang, ảnh 1200x630 |
| Hreflang | `vi` và `x-default` tự tham chiếu |
| Encoding | UTF-8 (`<meta charset="utf-8">` đặt đầu `<head>`). Lỗi font mất dấu ở báo cáo cũ do file lưu không phải UTF-8, hãy luôn lưu UTF-8 |
| Google Analytics | Điền `GA4_ID` |
| HSTS | GitHub Pages **không cho tự thêm header**. Muốn có HSTS: đặt Cloudflare (miễn phí) phía trước và bật HSTS. Đây là mục nâng cao, không ảnh hưởng thứ hạng đáng kể |
| HTTP Status "Pending" | Lỗi tạm của công cụ, chạy lại sau khi site online |

## 4. Sau khi online
1. Đăng ký **Google Search Console** → thêm property → gửi `https://tranthiquynhnhu0901-hue.github.io/sitemap.xml`.
2. Thay ảnh minh họa SVG bằng ảnh thật định dạng **WebP** (< 150 KB mỗi ảnh), giữ nguyên tên file hoặc sửa trong `build.py`.
3. Mỗi tuần viết thêm 1 bài trong mục Kiến thức (thêm vào `ARTICLES` trong `data.py`).

## 5. Cấu trúc URL
```
/                                  Trang chủ
/cay-giong/  /hat-giong/  /dat-va-phan-bon/  /dung-cu-lam-vuon/     4 danh mục
/<danh-muc>/<san-pham>/            10 trang sản phẩm
/kien-thuc/  /kien-thuc/<bai>/     Blog + 4 bài
/gioi-thieu/  /lien-he/  /chinh-sach/  /so-do-trang/
```
