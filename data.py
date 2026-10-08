# -*- coding: utf-8 -*-
"""Toàn bộ nội dung website. Sửa ở đây rồi chạy lại: python3 build.py"""

# ====================== CẤU HÌNH – HÃY SỬA CÁC DÒNG NÀY ======================
BASE = "https://tranthiquynhnhu0901-hue.github.io"   # không có dấu / ở cuối
BRAND = "Nông Xanh"
PHONE_DISPLAY = "0900 000 000"        # <-- thay số thật
PHONE_TEL = "+84900000000"            # <-- thay số thật (định dạng +84...)
ZALO = "0900000000"                   # <-- số Zalo thật
EMAIL = "lienhe@nongxanh.vn"          # <-- thay email thật
ADDRESS = "Số 1, đường Nông Nghiệp, TP. Hồ Chí Minh"   # <-- thay địa chỉ thật
GA4_ID = ""                           # <-- dán mã G-XXXXXXXXXX để bật Google Analytics
TODAY = "2026-10-08"
FREE_SHIP = 500000
# ============================================================================

CATEGORIES = [
    dict(slug="cay-giong", name="Cây giống ăn quả", short="Cây giống",
         title="Cây giống ăn quả: bưởi, chanh, ổi ghép | Nông Xanh",
         desc="Cây giống bưởi da xanh, chanh không hạt, ổi lê Đài Loan khỏe, rõ nguồn gốc. Kèm hướng dẫn trồng chậu và trồng đất. Giao hàng toàn quốc.",
         h1="Cây giống ăn quả khỏe, rễ tốt, dễ trồng",
         tagline="Cây ghép đã qua chọn lọc, đóng bầu cẩn thận để đến tay bạn vẫn tươi.",
         art="tree", bg=("#fff7d6", "#ffeaa1"),
         intro=["Cây giống là khoản đầu tư dài hạn nhất của một khu vườn, nên chọn đúng cây ngay từ đầu sẽ tiết kiệm cho bạn nhiều năm chăm sóc. Tại Nông Xanh, mọi cây giống ăn quả đều là cây ghép hoặc chiết từ cây mẹ đã cho trái ổn định, bầu đất còn nguyên và bộ rễ được kiểm tra trước khi đóng gói.",
                "Bạn có thể trồng xuống đất nếu có sân vườn, hoặc trồng chậu lớn trên sân thượng, ban công nhiều nắng. Mỗi sản phẩm đều có hướng dẫn trồng ngay trên trang để bạn làm theo từng bước."],
         guide=[("Chọn cây theo không gian", "Sân vườn rộng phù hợp với bưởi da xanh. Ban công hoặc sân thượng nên chọn chanh không hạt hoặc ổi lê vì tán gọn và dễ tạo hình trong chậu."),
                ("Chọn cây theo thời điểm", "Mùa mưa là lúc tốt nhất để trồng cây giống ngoài đất vì cây ít mất nước. Mùa khô vẫn trồng được nếu bạn che nắng 1 đến 2 tuần đầu và tưới đều."),
                ("Kiểm tra cây khi nhận hàng", "Cây khỏe có lá xanh đều, thân thẳng, vết ghép liền và bầu đất không vỡ. Nếu cây có dấu hiệu héo hoặc hỏng, hãy chụp ảnh và báo lại trong 24 giờ để được hỗ trợ đổi cây.")]),
    dict(slug="hat-giong", name="Hạt giống rau & gia vị", short="Hạt giống",
         title="Hạt giống rau, cà chua, húng quế dễ trồng | Nông Xanh",
         desc="Hạt giống cà chua cherry, xà lách romaine, húng quế nảy mầm đều, đóng gói kín, có hướng dẫn gieo. Phù hợp trồng chậu, khay và vườn nhỏ.",
         h1="Hạt giống rau, gia vị nảy mầm đều, dễ gieo",
         tagline="Gói nhỏ, giá nhẹ, đủ để bạn bắt đầu một luống rau hoặc vài chậu ban công.",
         art="seed", bg=("#e2f6e8", "#c8eed3"),
         intro=["Hạt giống là cách bắt đầu rẻ nhất và dễ nhất cho người mới làm vườn. Chỉ với một gói hạt, một khay đất và vài tuần kiên nhẫn, bạn đã có rau sạch tự trồng ngay tại nhà.",
                "Các giống ở Nông Xanh được chọn vì dễ thích nghi với khí hậu Việt Nam, nảy mầm nhanh và cho thu hoạch sớm. Mỗi gói đều ghi ngày đóng gói, hướng dẫn gieo và thời gian thu hoạch dự kiến."],
         guide=[("Gieo hạt vào đúng mùa", "Rau ăn lá như xà lách thích thời tiết mát. Cà chua và húng quế ưa nắng ấm nên gieo khi trời không quá lạnh và không có mưa kéo dài."),
                ("Bảo quản hạt chưa dùng", "Gấp kín miệng gói, để trong hộp khô ráo, tránh nắng và nơi ẩm. Hạt giữ được lâu hơn khi bảo quản ở nhiệt độ mát và ổn định."),
                ("Gieo ít, tỉa sớm", "Gieo thưa hơn bạn nghĩ và tỉa bớt cây yếu khi có 2 lá thật. Cây có đủ chỗ sẽ khỏe hơn và ít sâu bệnh hơn.")]),
    dict(slug="dat-va-phan-bon", name="Đất trồng & phân bón", short="Đất & phân bón",
         title="Đất trồng & phân bón hữu cơ cho vườn nhà | Nông Xanh",
         desc="Đất trồng cây trộn sẵn xơ dừa, phân trùn quế hữu cơ giúp đất tơi xốp, giữ ẩm tốt. Dùng cho rau, hoa và cây ăn quả trồng chậu.",
         h1="Đất sạch và phân hữu cơ cho cây lớn nhanh",
         tagline="Nền đất tốt giúp bạn bớt phải chữa bệnh cho cây về sau.",
         art="sack", bg=("#eaf6e4", "#d7edcd"),
         intro=["Phần lớn cây trồng chậu thất bại không phải vì giống xấu mà vì đất nén chặt, úng nước hoặc thiếu dinh dưỡng. Một loại đất thoáng, giữ ẩm vừa phải và giàu mùn hữu cơ sẽ giải quyết gần hết các vấn đề này.",
                "Đất trộn sẵn của Nông Xanh dùng xơ dừa đã xử lý để giữ ẩm, kết hợp phân trùn quế để cung cấp dinh dưỡng chậm. Phân trùn quế nguyên chất dùng bón lót hoặc bón thúc đều an toàn cho rễ."],
         guide=[("Dùng bao nhiêu đất cho một chậu", "Đổ đất đến cách miệng chậu khoảng 3 cm để khi tưới nước không tràn. Chậu càng lớn thì đất càng ít bị khô nhanh."),
                ("Bón phân thế nào cho đúng", "Bón ít và đều tốt hơn bón nhiều một lần. Rải phân quanh gốc, cách thân 5 đến 10 cm rồi tưới nhẹ để phân ngấm dần."),
                ("Nhận biết đất đã kiệt", "Đất bị chai cứng, nước chảy thẳng qua chậu hoặc cây lá vàng dù tưới đủ là dấu hiệu cần thay một phần đất và bổ sung phân hữu cơ.")]),
    dict(slug="dung-cu-lam-vuon", name="Dụng cụ làm vườn", short="Dụng cụ",
         title="Dụng cụ làm vườn: kéo cắt tỉa, bộ xẻng mini | Nông Xanh",
         desc="Kéo cắt tỉa cành sắc bén, bộ dụng cụ làm vườn mini kèm găng tay, bền và nhẹ tay. Đủ đồ nghề để chăm sân thượng, ban công và vườn nhỏ.",
         h1="Dụng cụ làm vườn gọn tay, bền và dễ dùng",
         tagline="Chọn đúng dụng cụ giúp công việc nhẹ hơn và cây ít bị tổn thương.",
         art="tools", bg=("#fff4d6", "#ffe7a8"),
         intro=["Bạn không cần cả một kho đồ nghề để làm vườn tốt. Một chiếc kéo cắt tỉa sắc và một bộ xẻng, cào nhỏ đã đủ cho hầu hết công việc ở sân thượng và ban công.",
                "Dụng cụ ở Nông Xanh được chọn theo tiêu chí: cầm vừa tay, lưỡi bằng thép không gỉ dễ vệ sinh và giá hợp lý cho người mới bắt đầu."],
         guide=[("Giữ lưỡi kéo luôn sắc", "Vết cắt gọn giúp cành mau liền và ít nhiễm bệnh. Lau sạch nhựa sau mỗi lần dùng và tra một ít dầu vào trục kéo mỗi tháng."),
                ("Vệ sinh dụng cụ giữa các cây", "Lau lưỡi bằng cồn khi chuyển từ cây bệnh sang cây khỏe để tránh lây lan mầm bệnh."),
                ("Bảo quản nơi khô ráo", "Rửa sạch đất, lau khô rồi cất ở chỗ thoáng. Dụng cụ để ngoài mưa nắng sẽ nhanh gỉ và hỏng.")]),
]

# art: (hàm, tham số) – xem art.py
PRODUCTS = [
    dict(slug="ca-chua-cherry", cat="hat-giong", name="Hạt giống cà chua cherry", price=29000, old=35000,
         title="Hạt giống cà chua cherry, gói tiện lợi | Nông Xanh",
         desc="Hạt giống cà chua cherry cho quả nhỏ, ngọt, sai quả, hợp trồng chậu và giàn ban công. Có hướng dẫn gieo và chăm sóc chi tiết đi kèm.",
         short="Cà chua cherry quả nhỏ, vị ngọt, ra chùm đều. Hợp trồng chậu lớn hoặc làm giàn ở ban công.",
         art=("seed", ("#fff1f0", "#ffe0dc", "#ef6a5b", "#b91c1c", "tomato")), alt="Gói hạt giống cà chua cherry màu đỏ",
         specs=[("Loại", "Hạt giống rau ăn quả"), ("Gieo đến nảy mầm", "Khoảng 5 đến 10 ngày"), ("Thu hoạch", "Khoảng 70 đến 90 ngày kể từ khi gieo"), ("Ánh sáng", "Nắng đủ 6 đến 8 giờ mỗi ngày"), ("Kiểu trồng", "Chậu từ 20 lít hoặc luống có giàn")],
         body=["Cà chua cherry là lựa chọn rất đáng thử cho người mới làm vườn. Cây ra quả sớm, quả nhỏ vừa miệng và ăn sống rất ngọt. Mỗi cây có thể cho nhiều chùm quả liên tục trong nhiều tuần nếu được chăm đều.",
               "Hạt được đóng gói kín, tách ẩm và ghi rõ ngày đóng gói. Bạn nên gieo trong khay đất tơi xốp trước, sau đó chuyển ra chậu khi cây có 3 đến 4 lá thật."],
         guide=[("Gieo hạt", "Gieo sâu khoảng 0,5 cm vào đất ẩm, giữ nơi sáng nhưng không nắng gắt. Hạt sẽ nảy mầm sau 5 đến 10 ngày."),
                ("Chuyển ra chậu", "Khi cây cao khoảng 10 cm và có 3 đến 4 lá thật, chuyển sang chậu 20 lít trở lên có lỗ thoát nước. Cắm cọc hoặc dựng giàn ngay từ đầu."),
                ("Chăm sóc đến thu hoạch", "Tưới đều vào gốc, tránh làm ướt lá. Khi cây ra hoa, bón thêm phân giàu kali. Hái quả khi chuyển hoàn toàn sang màu đỏ.")],
         article="cach-trong-ca-chua-cherry-tai-nha", feat=True),
    dict(slug="xa-lach-romaine", cat="hat-giong", name="Hạt giống xà lách romaine", price=22000, old=None,
         title="Hạt giống xà lách romaine giòn ngọt, dễ gieo | Nông Xanh",
         desc="Hạt giống xà lách romaine lá dày, giòn, ít đắng, dễ gieo trong khay hoặc thùng xốp. Thu hoạch nhanh, hợp vườn rau trên sân thượng.",
         short="Xà lách romaine lá dày, giòn và ngọt, thu hoạch nhanh chỉ sau vài tuần.",
         art=("seed", ("#eafbe0", "#d6f5c0", "#58b83e", "#2f6f1a", "lettuce")), alt="Gói hạt giống xà lách romaine màu xanh lá",
         specs=[("Loại", "Hạt giống rau ăn lá"), ("Gieo đến nảy mầm", "Khoảng 2 đến 7 ngày"), ("Thu hoạch", "Khoảng 35 đến 50 ngày kể từ khi gieo"), ("Ánh sáng", "Nắng nhẹ, tránh nắng gắt buổi trưa"), ("Kiểu trồng", "Khay, thùng xốp hoặc luống nông")],
         body=["Xà lách romaine có lá dài, gân to và giòn, rất hợp làm salad hoặc cuốn thịt nướng. Đây là loại rau ăn lá thu hoạch nhanh nên giúp bạn có thành quả sớm và dễ giữ động lực làm vườn.",
               "Xà lách ưa mát nên đạt chất lượng tốt nhất khi trồng vào mùa nhiệt độ dịu. Nếu trồng mùa nóng, hãy che lưới giảm nắng và tưới sáng sớm."],
         guide=[("Gieo hạt", "Rải hạt thưa trên mặt đất ẩm rồi phủ lớp đất mỏng khoảng 0,3 cm. Hạt xà lách cần ánh sáng nên không phủ quá dày."),
                ("Tỉa và giãn cây", "Khi cây có 3 đến 4 lá, tỉa để các cây cách nhau 15 đến 20 cm. Cây tỉa có thể ăn như rau mầm."),
                ("Thu hoạch", "Cắt cả cây sát gốc khi đủ lớn hoặc hái lá ngoài trước để cây tiếp tục ra lá mới.")],
         article="lich-gieo-trong-rau-theo-mua", feat=True),
    dict(slug="hung-que", cat="hat-giong", name="Hạt giống húng quế", price=19000, old=None,
         title="Hạt giống húng quế thơm, dễ trồng chậu | Nông Xanh",
         desc="Hạt giống húng quế lá xanh, thơm đậm, mọc nhanh, trồng được quanh năm trong chậu nhỏ. Thích hợp làm gia vị cho bếp nhà bạn mỗi ngày.",
         short="Húng quế thơm đậm, mọc khỏe, hái liên tục. Một chậu nhỏ ở cửa sổ bếp là đủ dùng.",
         art=("seed", ("#e2f6e8", "#c8eed3", "#2e9a3d", "#14532d", "basil")), alt="Gói hạt giống húng quế màu xanh đậm",
         specs=[("Loại", "Hạt giống rau gia vị"), ("Gieo đến nảy mầm", "Khoảng 5 đến 10 ngày"), ("Thu hoạch", "Từ khoảng 30 đến 45 ngày kể từ khi gieo"), ("Ánh sáng", "Nắng đủ, ưa ấm"), ("Kiểu trồng", "Chậu nhỏ từ 2 đến 5 lít")],
         body=["Húng quế là loại rau gia vị gần như không thể thiếu trong bếp Việt. Trồng tại nhà giúp bạn luôn có lá tươi thơm để ăn phở, bún, gỏi hoặc làm pesto.",
               "Cây thích nắng ấm và đất thoát nước tốt. Hãy bấm ngọn thường xuyên để cây đâm nhiều nhánh và kéo dài thời gian thu hoạch."],
         guide=[("Gieo hạt", "Gieo hạt trên mặt đất ẩm và phủ lớp đất rất mỏng. Giữ ẩm nhẹ, không để úng nước."),
                ("Bấm ngọn", "Khi cây cao 15 cm, bấm bỏ phần ngọn trên cặp lá thật. Việc này giúp cây bụi và nhiều lá hơn."),
                ("Cắt hoa", "Nhìn thấy nụ hoa thì cắt đi để cây tập trung ra lá và giữ vị thơm lâu hơn.")],
         article="lich-gieo-trong-rau-theo-mua", feat=False),
    dict(slug="buoi-da-xanh", cat="cay-giong", name="Cây giống bưởi da xanh", price=85000, old=99000,
         title="Cây giống bưởi da xanh ghép, rễ khỏe, dễ trồng | Nông Xanh",
         desc="Cây giống bưởi da xanh ghép từ cây mẹ cho trái ổn định, bầu đất nguyên, rễ khỏe. Kèm hướng dẫn trồng và chăm sóc cho vườn nhà.",
         short="Cây ghép bầu đất nguyên, bộ rễ khỏe. Phù hợp trồng đất ở sân vườn rộng hoặc chậu lớn.",
         art=("tree", ("#fff7d6", "#ffeaa1", "#1f8a4c", "#2fa05a", "#9ad94a", "#c8794a", "#a85f36", True)), alt="Cây bưởi da xanh giống trồng trong chậu với quả xanh",
         specs=[("Loại", "Cây giống ghép"), ("Chiều cao khi giao", "Khoảng 40 đến 60 cm"), ("Cho trái", "Khoảng 2 đến 3 năm tùy chăm sóc"), ("Ánh sáng", "Nắng đủ cả ngày"), ("Kiểu trồng", "Đất vườn hoặc chậu từ 50 cm")],
         body=["Bưởi da xanh được ưa chuộng nhờ múi hồng, ít hạt và vị ngọt thanh. Cây ghép cho trái sớm hơn cây trồng từ hạt và giữ được đặc tính của cây mẹ.",
               "Cây cần nhiều nắng, đất thoát nước tốt và bón phân định kỳ. Nếu trồng chậu, hãy chọn chậu đường kính từ 50 cm để rễ có chỗ phát triển."],
         guide=[("Chuẩn bị hố trồng", "Đào hố rộng 50 cm, sâu 50 cm. Trộn đất mặt với phân hữu cơ hoai mục rồi để vài ngày trước khi trồng."),
                ("Trồng cây", "Rạch nhẹ bầu, đặt cây sao cho vết ghép nằm cao hơn mặt đất. Lấp đất vừa kín rễ, nén nhẹ rồi tưới đẫm."),
                ("Chăm sóc năm đầu", "Tưới khi mặt đất khô, bón phân 30 đến 45 ngày một lần. Tỉa chồi mọc dưới vết ghép để cây không bị hút dinh dưỡng.")],
         article="cach-cham-soc-cay-an-qua-trong-chau", feat=True),
    dict(slug="chanh-khong-hat", cat="cay-giong", name="Cây giống chanh không hạt", price=55000, old=None,
         title="Cây giống chanh không hạt, trồng chậu sai quả | Nông Xanh",
         desc="Cây giống chanh không hạt tán gọn, ra trái quanh năm khi chăm tốt, rất hợp trồng chậu ban công. Bầu đất nguyên, đóng gói cẩn thận.",
         short="Chanh không hạt tán gọn, thơm vỏ, cho trái nhiều lứa. Chọn số một cho ban công và sân thượng.",
         art=("tree", ("#e6f7e3", "#d0f0c8", "#2a8f45", "#3aa557", "#c6f26b", "#c8794a", "#a85f36", False)), alt="Cây chanh không hạt trồng chậu với quả xanh lục",
         specs=[("Loại", "Cây giống ghép"), ("Chiều cao khi giao", "Khoảng 35 đến 50 cm"), ("Cho trái", "Khoảng 1,5 đến 2 năm tùy chăm sóc"), ("Ánh sáng", "Nắng đủ 6 giờ trở lên"), ("Kiểu trồng", "Chậu từ 40 cm hoặc đất vườn")],
         body=["Chanh không hạt có tán nhỏ, dễ tạo hình và cho trái nhiều lứa trong năm. Quả to, vỏ mỏng, nhiều nước nên rất tiện cho bếp gia đình.",
               "Cây thích hợp trồng chậu nhờ bộ rễ gọn. Đặt chậu nơi nhiều nắng, tưới đều nhưng không để chậu đọng nước."],
         guide=[("Chọn chậu và đất", "Chọn chậu có lỗ thoát nước, đường kính từ 40 cm. Dùng đất tơi xốp trộn xơ dừa và phân hữu cơ để rễ thoáng."),
                ("Tưới và bón phân", "Tưới khi lớp đất mặt khô khoảng 2 đến 3 cm. Bón phân hữu cơ chu kỳ 30 đến 45 ngày."),
                ("Tỉa cành tạo tán", "Tỉa cành khô, cành sâu bệnh và các nhánh mọc chen sau mỗi đợt thu hoạch để tán thông thoáng.")],
         article="cach-cham-soc-cay-an-qua-trong-chau", feat=True),
    dict(slug="oi-le-dai-loan", cat="cay-giong", name="Cây giống ổi lê Đài Loan", price=45000, old=None,
         title="Cây giống ổi lê Đài Loan ghép, ra quả sớm | Nông Xanh",
         desc="Cây giống ổi lê Đài Loan ghép, quả to, giòn, ít hạt, ra quả sớm sau khi trồng. Phù hợp trồng chậu và trồng đất. Giao hàng toàn quốc.",
         short="Ổi lê quả to, giòn, ít hạt, cho trái sớm. Dễ chăm hơn nhiều loại cây ăn quả khác.",
         art=("tree", ("#fff0f3", "#ffd9e1", "#2f9e44", "#46b25a", "#d7e86a", "#c8794a", "#a85f36", False)), alt="Cây ổi lê Đài Loan trồng chậu với quả vàng xanh",
         specs=[("Loại", "Cây giống ghép"), ("Chiều cao khi giao", "Khoảng 35 đến 50 cm"), ("Cho trái", "Khoảng 8 đến 12 tháng sau khi trồng"), ("Ánh sáng", "Nắng đủ cả ngày"), ("Kiểu trồng", "Chậu từ 40 cm hoặc đất vườn")],
         body=["Ổi lê Đài Loan được nhiều gia đình lựa chọn nhờ quả to, thịt giòn và ít hạt. Cây sinh trưởng nhanh và cho trái sớm nên rất thích hợp với người mới trồng cây ăn quả.",
               "Để quả đẹp, hãy bón phân cân đối, tỉa bớt quả khi còn nhỏ và bao quả bằng túi giấy hoặc túi lưới để hạn chế sâu đục quả."],
         guide=[("Trồng cây", "Trồng nơi nhiều nắng, đất thoát nước. Đặt cây sao cho cổ rễ ngang mặt đất, tránh chôn quá sâu."),
                ("Bón phân", "Giai đoạn cây con ưu tiên đạm và mùn hữu cơ. Khi cây ra hoa đậu quả, tăng dần lượng kali."),
                ("Tỉa và bao quả", "Mỗi chùm giữ lại 1 đến 2 quả đẹp nhất, bao quả sớm để quả sạch và ít sâu hại.")],
         article="cach-cham-soc-cay-an-qua-trong-chau", feat=True),
    dict(slug="dat-trong-cay-tron-san", cat="dat-va-phan-bon", name="Đất trồng cây trộn sẵn 20 dm³", price=49000, old=None,
         title="Đất trồng cây trộn sẵn xơ dừa, phân trùn quế | Nông Xanh",
         desc="Đất trồng cây trộn sẵn xơ dừa đã xử lý và phân trùn quế, tơi xốp, thoát nước tốt, giữ ẩm vừa phải. Đổ vào chậu là gieo trồng được ngay.",
         short="Đất sạch trộn sẵn xơ dừa và phân trùn quế. Đổ vào chậu là gieo trồng được ngay.",
         art=("sack", ("#f6ede2", "#ecdcc6", "#8b5a34", "#2f9e44", "soil")), alt="Bao đất trồng cây trộn sẵn xơ dừa và phân trùn quế",
         specs=[("Loại", "Giá thể trộn sẵn"), ("Thể tích", "20 dm³ mỗi bao"), ("Thành phần", "Xơ dừa đã xử lý, phân trùn quế, đất sạch"), ("Phù hợp", "Rau, hoa, cây ăn quả trồng chậu"), ("Bảo quản", "Nơi khô ráo, tránh mưa nắng")],
         body=["Đất trộn sẵn giúp bạn bỏ qua khâu phối trộn mất công. Hỗn hợp tơi xốp, thoát nước tốt nhưng vẫn giữ đủ ẩm cho rễ, phù hợp với phần lớn cây rau, hoa và cây ăn quả trồng chậu.",
               "Xơ dừa đã được xử lý để giảm chát, kết hợp phân trùn quế cung cấp dinh dưỡng chậm nên cây ít bị sốc phân."],
         guide=[("Cách dùng", "Đổ đất vào chậu đến cách miệng khoảng 3 cm, tưới ẩm đều rồi mới gieo hạt hoặc trồng cây."),
                ("Bổ sung dinh dưỡng", "Sau khoảng 1 đến 2 tháng, bổ sung thêm phân hữu cơ hoặc phân trùn quế quanh gốc."),
                ("Tái sử dụng đất", "Đất cũ có thể trộn thêm một nửa đất mới và phân hữu cơ để tái sử dụng cho vụ sau.")],
         article="cach-chon-dat-trong-cay-trong-chau", feat=True),
    dict(slug="phan-trun-que-2kg", cat="dat-va-phan-bon", name="Phân trùn quế hữu cơ 2 kg", price=55000, old=65000,
         title="Phân trùn quế hữu cơ 2 kg, bón rau và cây ăn quả | Nông Xanh",
         desc="Phân trùn quế hữu cơ dạng viên mịn, ít mùi, an toàn cho rễ, giúp đất tơi xốp và cây phát triển khỏe. Gói 2 kg dùng cho nhiều chậu.",
         short="Phân trùn quế mịn, ít mùi, bón cho rau, hoa và cây ăn quả. Dùng để bón lót hoặc bón thúc.",
         art=("sack", ("#eaf6e4", "#d7edcd", "#3f7d3a", "#c6f26b", "worm")), alt="Bao phân trùn quế hữu cơ màu xanh lá",
         specs=[("Loại", "Phân hữu cơ"), ("Khối lượng", "2 kg mỗi gói"), ("Dạng", "Mịn, tơi, ít mùi"), ("Phù hợp", "Rau, hoa, cây ăn quả"), ("Bảo quản", "Nơi khô ráo, đậy kín sau khi dùng")],
         body=["Phân trùn quế giàu mùn hữu cơ, giúp cải tạo đất và giữ ẩm tốt. Phân tác động chậm, ít gây cháy rễ nên rất hợp cho người mới.",
               "Bạn có thể trộn trực tiếp vào đất khi trồng hoặc rải quanh gốc để bón thúc định kỳ."],
         guide=[("Bón lót", "Trộn khoảng 1 phần phân với 4 đến 5 phần đất rồi mới trồng cây."),
                ("Bón thúc", "Rải một lớp mỏng quanh gốc, cách thân 5 đến 10 cm, xới nhẹ rồi tưới nước. Lặp lại sau 30 đến 45 ngày."),
                ("Lưu ý", "Không để phân tiếp xúc trực tiếp với thân cây non. Đóng kín bao sau khi dùng để phân không bị ẩm mốc.")],
         article="cach-chon-dat-trong-cay-trong-chau", feat=True),
    dict(slug="keo-cat-tia-canh", cat="dung-cu-lam-vuon", name="Kéo cắt tỉa cành thép không gỉ", price=89000, old=None,
         title="Kéo cắt tỉa cành thép không gỉ, cầm êm tay | Nông Xanh",
         desc="Kéo cắt tỉa cành lưỡi thép không gỉ sắc bén, tay cầm chống trượt, cắt gọn cành nhỏ và cuống quả. Dụng cụ cần có cho người làm vườn.",
         short="Lưỡi thép không gỉ sắc bén, tay cầm chống trượt, cắt gọn cành nhỏ và cuống quả.",
         art=("shears", ("#e6f2ff", "#cfe4fb", "#ef6c2f", "#90a4ae")), alt="Kéo cắt tỉa cành tay cầm màu cam lưỡi thép",
         specs=[("Loại", "Kéo cắt tỉa"), ("Chất liệu lưỡi", "Thép không gỉ"), ("Cắt được", "Cành nhỏ đến khoảng 15 mm"), ("Tay cầm", "Chống trượt, có khóa an toàn"), ("Phù hợp", "Cây ăn quả, hoa, cây cảnh")],
         body=["Kéo cắt tỉa là dụng cụ dùng nhiều nhất trong vườn. Vết cắt sạch và gọn giúp cành mau liền và hạn chế nhiễm bệnh, tốt hơn nhiều so với dùng dao hoặc kéo văn phòng.",
               "Lò xo trợ lực giúp mở lưỡi nhẹ nhàng nên tay đỡ mỏi khi làm lâu."],
         guide=[("Cắt đúng cách", "Cắt xéo khoảng 45 độ, ngay trên mắt chồi hướng ra ngoài tán để cành mới mọc về hướng thoáng."),
                ("Vệ sinh sau khi dùng", "Lau nhựa và đất bằng khăn ẩm, lau cồn khi chuyển sang cây khác, rồi lau khô."),
                ("Bảo dưỡng", "Tra một giọt dầu vào trục kéo mỗi tháng để lưỡi luôn trơn và êm.")],
         article="cach-cham-soc-cay-an-qua-trong-chau", feat=False),
    dict(slug="bo-dung-cu-mini", cat="dung-cu-lam-vuon", name="Bộ dụng cụ làm vườn mini 4 món", price=129000, old=149000,
         title="Bộ dụng cụ làm vườn mini 4 món kèm găng tay | Nông Xanh",
         desc="Bộ dụng cụ làm vườn mini gồm xẻng, cào, xới đất và găng tay chống trượt. Nhỏ gọn, nhẹ, đủ dùng cho ban công, sân thượng và chậu cây.",
         short="Xẻng, cào, xới đất và găng tay trong một bộ. Nhỏ gọn, nhẹ, rất hợp ban công và sân thượng.",
         art=("tools", ("#fff4d6", "#ffe7a8", "#2f9e44", "#90a4ae")), alt="Bộ dụng cụ làm vườn mini gồm xẻng cào và găng tay vàng",
         specs=[("Loại", "Bộ dụng cụ mini"), ("Số món", "4 món: xẻng, cào, xới đất, găng tay"), ("Chất liệu", "Thép carbon sơn tĩnh điện, cán nhựa"), ("Phù hợp", "Chậu cây, ban công, sân thượng"), ("Bảo quản", "Lau khô sau khi dùng")],
         body=["Bộ dụng cụ gọn nhẹ này đủ cho các công việc cơ bản như xới đất, trộn phân, thay chậu và vun gốc. Cán cầm ôm tay, găng tay chống trượt giúp bạn làm vườn thoải mái hơn.",
               "Đây là món quà rất hợp cho người mới bắt đầu hoặc người thân thích trồng cây."],
         guide=[("Xới đất", "Dùng cào nhỏ xới nhẹ lớp mặt để đất thoáng, tránh làm đứt rễ non."),
                ("Thay chậu", "Dùng xẻng nhỏ nới đất quanh mép chậu rồi nhấc cây ra cùng bầu đất nguyên."),
                ("Vệ sinh", "Rửa dụng cụ bằng nước sạch, lau khô và cất nơi thoáng sau mỗi lần dùng.")],
         article="cach-chon-dat-trong-cay-trong-chau", feat=False),
]

ARTICLES = [
    dict(slug="cach-trong-ca-chua-cherry-tai-nha", motif="tomato", c=("#ffe4de", "#ffc9bf"),
         title="Cách trồng cà chua cherry tại nhà từ hạt đến thu hoạch",
         desc="Hướng dẫn trồng cà chua cherry trong chậu từ gieo hạt, chuyển cây, làm giàn, bón phân đến thu hoạch. Phù hợp cho người mới bắt đầu.",
         h1="Cách trồng cà chua cherry tại nhà từ hạt đến thu hoạch",
         read=6, related=["ca-chua-cherry", "dat-trong-cay-tron-san", "phan-trun-que-2kg"], alt="Ảnh bìa bài hướng dẫn trồng cà chua cherry với những quả cà chua đỏ",
         body="""
<p>Cà chua cherry là loại rau ăn quả dễ thành công nhất khi trồng chậu. Cây cho quả liên tục, ăn sống rất ngọt và trông rất đẹp trên ban công. Bài viết này đi qua từng bước để bạn trồng thành công ngay từ vụ đầu tiên.</p>
<h2>Chuẩn bị trước khi gieo</h2>
<h3>Chọn chỗ đặt chậu</h3>
<p>Cà chua cần nắng từ 6 đến 8 giờ mỗi ngày. Hãy chọn vị trí đón nắng buổi sáng và đầu giờ chiều, có gió nhẹ để lá mau khô sau khi tưới.</p>
<h3>Chọn chậu và đất</h3>
<p>Chậu nên có dung tích từ 20 lít trở lên và có lỗ thoát nước. Dùng đất tơi xốp trộn xơ dừa và phân hữu cơ hoai mục để rễ phát triển tốt.</p>
<h2>Gieo hạt và chuyển cây</h2>
<h3>Gieo hạt vào khay</h3>
<p>Ngâm hạt trong nước ấm khoảng 4 đến 6 giờ để hạt nhanh nảy mầm. Gieo sâu khoảng 0,5 cm vào khay đất ẩm. Sau 5 đến 10 ngày hạt sẽ lên mầm.</p>
<h3>Chuyển ra chậu</h3>
<p>Khi cây có 3 đến 4 lá thật, thường sau 3 đến 4 tuần, hãy chuyển ra chậu lớn. Chôn sâu hơn một chút để thân cây mọc thêm rễ phụ giúp cây vững hơn.</p>
<h2>Chăm sóc đến lúc thu hoạch</h2>
<h3>Tưới nước đều tay</h3>
<p>Tưới vào gốc, tránh làm ướt lá để hạn chế nấm bệnh. Giữ độ ẩm đất đều vì lúc khô lúc ướt thất thường dễ làm quả bị thối đít.</p>
<h3>Làm giàn và tỉa chồi</h3>
<p>Cắm cọc hoặc dựng giàn ngay khi chuyển cây ra chậu. Với giống leo cao, tỉa bớt các chồi mọc ở nách lá để cây tập trung nuôi quả.</p>
<h3>Bón phân</h3>
<p>Giai đoạn cây con ưu tiên mùn hữu cơ. Khi cây ra hoa, bổ sung phân giàu kali để quả ngọt và chắc. Bón ít, chia nhiều lần sẽ an toàn hơn bón một lần thật nhiều.</p>
<h2>Thu hoạch và bảo quản</h2>
<p>Hái quả khi chuyển hoàn toàn sang màu đỏ. Hái thường xuyên sẽ kích thích cây ra thêm chùm mới. Quả hái về nên để nơi thoáng mát, không cần cho vào tủ lạnh nếu dùng trong vài ngày.</p>
<h2>Những lỗi người mới hay gặp</h2>
<ul>
<li>Đặt chậu nơi thiếu nắng nên cây vống và ít quả.</li>
<li>Tưới quá nhiều làm úng rễ, lá vàng từ dưới lên.</li>
<li>Không làm giàn sớm khiến thân đổ khi quả nặng.</li>
</ul>
""" ),
    dict(slug="cach-chon-dat-trong-cay-trong-chau", motif="soil", c=("#efe6da", "#e2cfb4"),
         title="Cách chọn đất trồng cây trong chậu: công thức và mẹo",
         desc="Đất tốt quyết định cây có khỏe hay không. Tìm hiểu cách chọn, phối trộn đất trồng chậu cho rau, hoa và cây ăn quả, kèm công thức dễ làm.",
         h1="Cách chọn đất trồng cây trong chậu: công thức và mẹo",
         read=5, related=["dat-trong-cay-tron-san", "phan-trun-que-2kg", "bo-dung-cu-mini"], alt="Ảnh bìa bài viết về đất trồng cây với đống đất và mầm non",
         body="""
<p>Nhiều người thay đổi giống cây, thay đổi phân bón mà vẫn thất bại vì quên mất yếu tố nền tảng: đất. Cây trồng chậu sống trong một thể tích đất rất nhỏ nên chất lượng đất ảnh hưởng đến cây nhiều hơn khi trồng ngoài vườn.</p>
<h2>Một loại đất tốt cần những gì</h2>
<h3>Tơi xốp và thoát nước</h3>
<p>Rễ cần oxy để hô hấp. Đất bị nén chặt hoặc đọng nước sẽ khiến rễ thối, lá vàng và cây chậm lớn.</p>
<h3>Giữ ẩm vừa phải</h3>
<p>Đất quá thoát nước sẽ khô nhanh và bắt bạn tưới liên tục. Xơ dừa và mùn hữu cơ giúp giữ ẩm mà vẫn thoáng khí.</p>
<h3>Giàu mùn hữu cơ</h3>
<p>Mùn hữu cơ cung cấp dinh dưỡng chậm và nuôi vi sinh vật có lợi trong đất. Phân trùn quế và phân hữu cơ hoai mục là những lựa chọn quen thuộc.</p>
<h2>Công thức phối trộn đơn giản</h2>
<p>Với phần lớn cây rau và cây ăn quả trồng chậu, bạn có thể bắt đầu từ công thức sau rồi điều chỉnh theo thực tế:</p>
<ul>
<li>40 phần đất sạch hoặc đất thịt nhẹ.</li>
<li>30 phần xơ dừa đã xử lý.</li>
<li>20 phần phân hữu cơ hoai mục hoặc phân trùn quế.</li>
<li>10 phần trấu hun hoặc đá perlite để tăng độ thoáng.</li>
</ul>
<p>Nếu không muốn mất công phối trộn, đất trộn sẵn là lựa chọn nhanh và ổn định hơn.</p>
<h2>Độ pH và khi nào cần quan tâm</h2>
<p>Hầu hết các loại rau phát triển tốt ở khoảng pH 6 đến 6,8. Cây có múi và ổi chịu được đất hơi chua hơn. Nếu cây vàng lá dù đã tưới và bón đủ, hãy thử đo pH bằng bút đo hoặc giấy quỳ.</p>
<h2>Chăm sóc đất theo thời gian</h2>
<h3>Xới nhẹ mặt đất</h3>
<p>Sau vài tuần, mặt đất thường bị đóng váng. Dùng cào nhỏ xới nhẹ để nước và không khí thấm xuống.</p>
<h3>Bổ sung phân định kỳ</h3>
<p>Sau 1 đến 2 tháng, rải thêm một lớp phân hữu cơ mỏng quanh gốc. Đến cuối vụ, thay một phần đất cũ bằng đất mới để cây vụ sau có nền tốt.</p>
<h2>Những điều cần tránh</h2>
<ul>
<li>Dùng thuần đất đồi hoặc đất sét vì dễ đóng cứng.</li>
<li>Dùng phân tươi chưa hoai mục vì có thể làm cháy rễ.</li>
<li>Dùng chậu không có lỗ thoát nước.</li>
</ul>
""" ),
    dict(slug="lich-gieo-trong-rau-theo-mua", motif="calendar", c=("#dff3ff", "#bfe6fb"),
         title="Lịch gieo trồng rau theo mùa cho người mới làm vườn",
         desc="Gợi ý lịch gieo trồng rau ăn lá, rau ăn quả và rau gia vị theo mùa ở Việt Nam. Hiểu đúng mùa vụ để rau lên khỏe, ít sâu bệnh.",
         h1="Lịch gieo trồng rau theo mùa cho người mới làm vườn",
         read=5, related=["xa-lach-romaine", "hung-que", "ca-chua-cherry"], alt="Ảnh bìa bài viết lịch gieo trồng rau với tờ lịch và ô ngày màu vàng",
         body="""
<p>Gieo đúng mùa là cách tiết kiệm công sức nhất trong làm vườn. Cùng một loại rau, gieo đúng thời điểm sẽ lên khỏe, ít sâu bệnh và cho thu hoạch ngon hơn rất nhiều. Dưới đây là gợi ý để bạn bắt đầu, bạn nên điều chỉnh theo thời tiết thực tế của từng địa phương.</p>
<h2>Hiểu mùa vụ ở các vùng miền</h2>
<h3>Miền Nam</h3>
<p>Khí hậu chia thành hai mùa rõ rệt: mùa mưa (khoảng tháng 5 đến tháng 10) và mùa khô (khoảng tháng 11 đến tháng 4). Mùa mưa cần chú ý thoát nước và phòng nấm bệnh. Mùa khô cần tưới đều và che nắng gắt.</p>
<h3>Miền Bắc và miền Trung</h3>
<p>Miền Bắc có bốn mùa nên rau ưa mát thường trồng vào thu đông và đông xuân, còn rau ưa nóng trồng vào xuân hè. Miền Trung cần lưu ý thêm mùa mưa bão và gió nóng.</p>
<h2>Gợi ý rau theo nhóm</h2>
<h3>Rau ăn lá</h3>
<p>Xà lách, cải xanh, cải ngọt thích thời tiết mát nên hợp vụ đông xuân ở miền Bắc và mùa khô ở miền Nam. Rau muống, mồng tơi, rau dền chịu nóng tốt nên trồng quanh năm, nhất là mùa hè.</p>
<h3>Rau ăn quả</h3>
<p>Cà chua, ớt, dưa leo, mướp cần nhiều nắng và nhiệt độ ấm. Hãy gieo khi trời ổn định, tránh giai đoạn mưa kéo dài khi cây ra hoa.</p>
<h3>Rau gia vị</h3>
<p>Húng quế, ngò rí, tía tô trồng được gần như quanh năm, chỉ cần nắng đủ và đất thoát nước tốt.</p>
<h2>Lịch làm vườn đơn giản theo tuần</h2>
<ul>
<li>Tuần 1: chuẩn bị đất, chậu và gieo hạt vào khay.</li>
<li>Tuần 2 đến 3: tưới ẩm đều, tỉa bớt cây yếu.</li>
<li>Tuần 4: chuyển cây con ra chậu hoặc luống.</li>
<li>Tuần 5 trở đi: bón phân loãng, kiểm tra sâu bệnh, bắt đầu thu hoạch rau lá.</li>
</ul>
<h2>Mẹo để vụ đầu tiên thành công</h2>
<p>Bắt đầu với 2 đến 3 loại dễ trồng thay vì cố gắng trồng nhiều loại cùng lúc. Ghi lại ngày gieo, ngày bón phân để lần sau điều chỉnh. Trồng xen húng quế cạnh rau ăn quả cũng là cách quen thuộc để vườn đẹp và thơm hơn.</p>
""" ),
    dict(slug="cach-cham-soc-cay-an-qua-trong-chau", motif="tree", c=("#fff3c9", "#ffe28a"),
         title="Cách chăm sóc cây ăn quả trồng chậu: chanh, ổi, bưởi",
         desc="Hướng dẫn chăm cây ăn quả trồng chậu cho người mới: chọn chậu, tưới nước, bón phân, tỉa cành và phòng sâu bệnh cho chanh, ổi và bưởi.",
         h1="Cách chăm sóc cây ăn quả trồng chậu: chanh, ổi, bưởi",
         read=7, related=["chanh-khong-hat", "oi-le-dai-loan", "keo-cat-tia-canh"], alt="Ảnh bìa bài viết chăm sóc cây ăn quả trồng chậu với cây quả vàng cam",
         body="""
<p>Không có sân vườn vẫn có thể trồng cây ăn quả. Chanh, ổi và một số giống bưởi nhỏ hoàn toàn sống tốt trong chậu lớn trên ban công hoặc sân thượng. Điều quan trọng là bạn chăm đúng cách ngay từ đầu.</p>
<h2>Chọn chậu và vị trí</h2>
<h3>Kích thước chậu</h3>
<p>Chọn chậu có đường kính từ 40 đến 50 cm trở lên, có lỗ thoát nước ở đáy. Chậu quá nhỏ sẽ làm cây còi cọc và đất khô rất nhanh.</p>
<h3>Ánh sáng</h3>
<p>Cây ăn quả cần ít nhất 6 giờ nắng mỗi ngày để ra hoa và đậu quả. Nếu ban công thiếu nắng, hãy ưu tiên đặt cây ở vị trí đón nắng sáng.</p>
<h2>Tưới nước và bón phân</h2>
<h3>Tưới khi đất cần</h3>
<p>Dùng ngón tay thử độ ẩm: nếu lớp đất sâu 2 đến 3 cm đã khô thì tưới đẫm cho nước chảy ra lỗ đáy. Tránh tưới ít nhưng nhiều lần vì rễ sẽ nằm nông.</p>
<h3>Bón phân định kỳ</h3>
<p>Bón phân hữu cơ hoặc phân trùn quế 30 đến 45 ngày một lần. Giai đoạn ra hoa đậu quả cần tăng lượng kali và bổ sung vi lượng. Bón ít, đều đặn sẽ tốt hơn bón mạnh một lần.</p>
<h2>Tỉa cành và tạo tán</h2>
<p>Sau mỗi đợt thu hoạch, cắt bỏ cành khô, cành sâu bệnh và cành mọc chen vào trong tán. Tán thông thoáng giúp cây nhận đủ nắng và ít sâu bệnh hơn. Dùng kéo sắc, cắt xéo và lau sạch lưỡi kéo sau khi dùng.</p>
<h2>Phòng trừ sâu bệnh</h2>
<h3>Sâu vẽ bùa và rệp sáp</h3>
<p>Cây có múi như chanh và bưởi hay bị sâu vẽ bùa ở lá non. Cắt bỏ lá bị hại nặng và thường xuyên kiểm tra mặt dưới lá. Rệp sáp có thể lau bằng bông thấm nước xà phòng loãng.</p>
<h3>Thối rễ</h3>
<p>Đa số do đọng nước. Hãy kiểm tra lỗ thoát nước và giảm lượng tưới khi trời mưa nhiều.</p>
<h2>Khi nào cây cho trái</h2>
<p>Thời gian cho trái phụ thuộc giống, cách chăm sóc và điều kiện nắng. Ổi lê thường cho trái sớm nhất, kế đến là chanh, còn bưởi cần nhiều thời gian hơn. Kiên nhẫn và chăm đều là bí quyết quan trọng nhất.</p>
""" ),
]

FAQS = [
    ("Tôi có thể đặt hàng như thế nào?", "Bạn thêm sản phẩm vào giỏ hàng trên website, sau đó bấm nút gửi đơn qua Zalo. Nhân viên sẽ xác nhận đơn, phí vận chuyển và thời gian giao với bạn trong vòng vài giờ làm việc."),
    ("Cây giống có được giao đi toàn quốc không?", "Có. Cây được đóng bầu, bọc giấy và đặt trong thùng chuyên dụng để hạn chế dập nát. Thời gian giao thay đổi theo khu vực, thường từ 1 đến 5 ngày."),
    ("Nếu cây đến nơi bị héo hoặc hỏng thì sao?", "Bạn hãy chụp ảnh hoặc quay video lúc mở hàng và báo cho chúng tôi trong vòng 24 giờ. Shop sẽ hỗ trợ đổi cây mới hoặc hoàn tiền theo chính sách đổi trả."),
    ("Người mới làm vườn nên bắt đầu từ đâu?", "Hãy bắt đầu với hạt giống rau dễ trồng như xà lách, húng quế và một chậu đất trộn sẵn. Khi quen tay, bạn có thể thử cà chua hoặc cây ăn quả trồng chậu."),
    ("Có hướng dẫn trồng và chăm sóc đi kèm không?", "Có. Mỗi sản phẩm đều có hướng dẫn trồng ngay trên trang, ngoài ra bạn có thể đọc thêm các bài hướng dẫn chi tiết trong mục kiến thức nông nghiệp."),
]

SEASONS = [
    ("Mùa mưa (tháng 5 đến 10)", "Ưu tiên rau chịu nóng ẩm như rau muống, mồng tơi, rau dền và húng quế. Trồng cây giống ăn quả xuống đất rất thuận lợi vì cây ít mất nước. Chú ý thoát nước và phòng nấm bệnh.", ["Rau muống", "Mồng tơi", "Húng quế", "Cây giống ăn quả"]),
    ("Mùa khô và mát (tháng 11 đến 4)", "Thời điểm tốt cho xà lách, cải xanh, cà chua cherry và các loại rau ưa mát. Cần tưới đều và che nắng gắt buổi trưa cho cây con.", ["Xà lách", "Cải xanh", "Cà chua cherry", "Ớt"]),
    ("Quanh năm trong nhà và ban công", "Rau gia vị và rau mầm trồng được hầu như quanh năm nếu có đủ ánh sáng và đất thoát nước tốt. Đây là cách bắt đầu nhẹ nhàng nhất.", ["Húng quế", "Rau mầm", "Tía tô", "Ngò rí"]),
]

PAGES = [
    dict(slug="gioi-thieu", title="Giới thiệu Nông Xanh – Đồng hành cùng người làm vườn", desc="Nông Xanh cung cấp cây giống, hạt giống, đất trồng và dụng cụ làm vườn cho gia đình. Tìm hiểu câu chuyện, cam kết và cách chúng tôi làm việc.", h1="Nông Xanh – người bạn đồng hành của mọi khu vườn"),
    dict(slug="lien-he", title="Liên hệ Nông Xanh – Tư vấn chọn cây giống và hạt giống", desc="Liên hệ Nông Xanh qua điện thoại, Zalo hoặc email để được tư vấn chọn cây giống, hạt giống, đất trồng và dụng cụ phù hợp với vườn của bạn.", h1="Liên hệ để được tư vấn chọn cây và hạt giống"),
    dict(slug="chinh-sach", title="Chính sách giao hàng và đổi trả cây giống | Nông Xanh", desc="Thông tin về phí vận chuyển, thời gian giao, cách đóng gói và chính sách đổi trả cây giống, hạt giống, đất và dụng cụ tại Nông Xanh.", h1="Chính sách giao hàng và đổi trả"),
]
