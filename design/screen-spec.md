# Screen Specification — Why I Buy?

**Project:** Why I Buy? – lấy cảm hứng từ "The Psychology of Money"
**Course:** PRM323 – Lab 2

> **Cập nhật 18/10/2026:** các màn F11–F13 (19–31, EXT, X2–X5) và bảng **ánh xạ mã màn đặc tả 17/10 ↔ Figma 18/10** ở cuối file, mục "Smart Shopping Companion – màn F11–F13". Figma hiện hành: `Why I Buy ver2` (`VaPYFxfpx14tnQmOMSgdjP`). Ảnh hiện hành của mọi khung: [`assets/figma/ver2/`](../assets/figma/ver2/) (18/10); ảnh ở `assets/figma/` là của file cũ (Flow 1–10, 14/10).

Mỗi màn hình: dùng để làm gì, hiển thị nội dung gì (từ trên xuống), thuộc flow nào, có những khung trạng thái nào, và ý đồ thiết kế. Nội dung khớp với page `03 Final UI` trong Figma; ảnh từng khung ở [`assets/figma/`](../assets/figma/). Token và quy tắc component xem [`DESIGN.md`](DESIGN.md); cách dựng bằng Flutter xem [`handoff/flutter-handoff.md`](../handoff/flutter-handoff.md).

## Danh mục màn hình

| # | Màn hình | Cấp | Flow | Khung trạng thái | Ảnh |
|---|---|---|---|---|---|
| 00 | Splash | Gốc (mọi lần mở app) | 7 | — | — |
| 00a | Đăng nhập | Gốc | 7 | — | [00a](../assets/figma/00a-login.png) |
| 00b | Đăng ký | Gốc | 7 | — | [00b](../assets/figma/00b-register.png) |
| — | Quên mật khẩu | Gốc | 7 | — | — |
| 01 | Onboarding | Gốc (lần đầu) | 1, 7 | — | [01](../assets/figma/01-onboarding.png) |
| 00 Hub | Trang chủ tổng hợp | Tab 1 | 1, 6, 7, 8, 9 | chưa ghi hôm nay; các trạng thái của 02 | — |
| 02 | Trang chủ | Tab 1 | 1, 2, 6 | trống, sau khi lưu, ngoại tuyến, lối vào Danh sách mong muốn, lối vào Trước khi mua | [02](../assets/figma/02-home.png) |
| 03 | Ghi khoản mua – Bước 1/2 | Lồng | 1, 3, 6 | lỗi, sửa, điền sẵn từ Danh sách mong muốn | [03](../assets/figma/03-add-purchase-step1.png) |
| 04 | Ghi khoản mua – Bước 2/2 | Lồng | 1, 3, 6 | đang lưu, giải thích động cơ, sửa, điền sẵn | [04](../assets/figma/04-purchase-reason.png) |
| 05 | Chi tiết khoản mua | Lồng | 3 | dialog xóa | [05](../assets/figma/05-purchase-detail.png) |
| 05 | Khoản mua đã lưu | Lồng | 1, 8 | — | — |
| 05a | Xin quyền thông báo | Lồng | 1, 5 | — | — |
| 06 | Lịch sử | Tab 2 | 3, 4 | không có kết quả, sau khi xóa, chọn tháng, tháng 9/2026 | [06](../assets/figma/06-history.png) |
| 07 | Mô hình | Tab 3 | 2, 4, 8, 10 | đang tải, lỗi, chưa đủ dữ liệu, tháng 9/2026, Tuần; phiên bản có AI | [07](../assets/figma/07-patterns.png) |
| 08 | Góc nhìn | Tab 4 | 2, 10 | đã lưu chiêm nghiệm; phiên bản có AI (và đã lưu chiêm nghiệm) | [08](../assets/figma/08-insights.png) |
| 08b | Chi tiết mô hình mua sắm | Lồng | 8, 9, 10 | AI đang phân tích – mô hình (08a) | — |
| 08c | Nhận định AI về khoản mua | Lồng | 8, 10 | AI đang phân tích – khoản vừa lưu (08a); khung "khoản vừa lưu" | — |
| 09 | Chiêm nghiệm tháng | Lồng | 2, 10 | — | [09](../assets/figma/09-monthly-reflection.png) |
| 10 | Cá nhân | Tab 5 | 5, 7 | xác nhận xóa toàn bộ, đã xuất dữ liệu, chưa cấp quyền thông báo, xác nhận đăng xuất | [10](../assets/figma/10-profile.png) |
| 10a | Tài khoản | Lồng | 7 | xác nhận xóa tài khoản, sau khi đổi mật khẩu | — |
| 10b | Đổi mật khẩu | Lồng | 7 | — | — |
| 11 | Danh sách mong muốn | Lồng | 6 | 11a–11e | [11](../assets/figma/11-wishlist-overview.png) |
| 12 | Thêm món mong muốn | Lồng | 6 | 12a–12c | [12](../assets/figma/12-add-item.png) |
| 13 | Chi tiết món mong muốn | Lồng | 6 | 13a–13d | [13](../assets/figma/13-wishlist-detail.png) |
| 14 | Trước khi mua – Bước 1/3 | Lồng | 9 | — | — |
| 15 | Trước khi mua – Bước 2/3 | Lồng | 9 | — | — |
| 16 | Trước khi mua – Bước 3/3 | Lồng | 9 | chỉ hiện khi chọn Khuyến mãi ở 15 | — |
| 18 | Nhận định trước khi mua | Lồng | 9 | AI đang phân tích – trước khi mua (17) | — |

Ảnh của các màn này (xuất từ Figma ver2 ngày 18/10) ở [`assets/figma/ver2/`](../assets/figma/ver2/): `00-splash.png`, `quen-mat-khau.png`, `00-trang-chu-tong-hop-hub.png`, `05-khoan-mua-da-luu.png`, `05a-xin-quyen-thong-bao.png`, `08b-…`, `08c-…`, `10a-tai-khoan.png`, `10b-doi-mat-khau.png`, `14-…` đến `18-…`. Vị trí trên page `03 Final UI` (Splash ở section "Màn hình chính"; Quên mật khẩu, Hub, 10a, 10b ở section "Flow 7 – Tài khoản"; 05a, 05 Khoản mua đã lưu, 08b, 08c, 14–18 ở section "Flow 8–10 – AI (Góc nhìn AI, Trước khi mua)").

Quy ước chung cho mọi màn: một nút chính (filled, cao 56 dp) ghim ở đáy, ngay trên thanh điều hướng; tab gốc có logo bên trái và avatar (→ Cá nhân) bên phải app bar; màn lồng có nút Back và không có thanh điều hướng.

---

### 00 Splash
- **Mục đích:** điểm vào mỗi lần mở app; hiện thương hiệu trong lúc app kiểm tra đã đăng nhập hay chưa. Thuộc Flow 7.
- **Bố cục & phân cấp thị giác:**
  - **Nền:** color/primary phủ cả khung 360 × 800.
  - **Giữa màn:** Logo (App icon) và wordmark "Why I Buy?".
  - Không app bar, không thanh điều hướng, không có phần tử bấm được.
- **Components:** App icon.
- **Trạng thái:** chỉ một trạng thái. Prototype: sau 0,8 giây chuyển Dissolve 300 ms sang 01 Onboarding.
- **Điều hướng:** chưa đăng nhập → 00a Đăng nhập (lần đầu → 01 Onboarding); đã đăng nhập → 00 Hub. Prototype chỉ nối nhánh lần đầu.
- **Ràng buộc:** không có nút, không xin quyền ở màn này; chỉ giữ trong lúc kiểm tra phiên đăng nhập (mục tiêu ≤ 0,8 giây, xem handoff mục 8.4).

### 00a Đăng nhập
- **Mục đích:** cho người đã có tài khoản vào app và đồng bộ dữ liệu giữa các máy.
- **Nội dung:** "← Quay lại" · logo + "Why I Buy?" · "Chào bạn trở lại" · "Tiếp tục hiểu mình qua những khoản mua, từng chút một." · ô Email, ô Mật khẩu · "Quên mật khẩu?" · nút chính "Đăng nhập" · "Chưa có tài khoản? Đăng ký" · thẻ nhắc giá trị sản phẩm "Hiểu mình, không phán xét".
- **Flow:** 7 (bắt đầu). Đăng nhập xong → 02.
- **Ý đồ:** chỉ 2 trường để không tạo rào cản; giọng chào ấm, nhắc lại lời hứa "không phán xét" vì persona từng bỏ app do cảm giác bị đánh giá.

### 00b Đăng ký
- **Mục đích:** tạo tài khoản mới.
- **Nội dung:** "← Quay lại" · logo · "Tạo tài khoản" · "Bắt đầu hành trình hiểu thói quen mua sắm của bạn, theo cách nhẹ nhàng." · 4 ô: Họ tên ("Tên bạn muốn được gọi"), Email, Mật khẩu, Xác nhận mật khẩu · gợi ý "Mật khẩu có ít nhất 8 ký tự." · nút chính "Tạo tài khoản" · "Đã có tài khoản? Đăng nhập".
- **Flow:** 7. Tạo xong → quay về Đăng nhập.
- **Ý đồ:** nêu quy tắc mật khẩu trước khi người dùng nhập (Nielsen #5, phòng lỗi) thay vì chỉ báo lỗi sau.

### Quên mật khẩu
- **Mục đích:** gửi liên kết đặt lại mật khẩu cho người không nhớ mật khẩu. Thuộc Flow 7 (nhánh phục hồi).
- **Bố cục & phân cấp thị giác:**
  - **Đầu màn:** nút "Quay lại".
  - **Nội dung khôi phục:** wordmark "Why I Buy?" · tiêu đề "Quên mật khẩu" · mô tả "Nhập email bạn dùng để đăng ký. Chúng mình sẽ gửi liên kết để bạn đặt lại mật khẩu." · ô "Email" (placeholder "Nhập email của bạn") · nút chính "Gửi liên kết đặt lại" · nút chữ "Quay lại Đăng nhập".
  - **Cuối màn:** thẻ "Hiểu mình, không phán xét" / "Mỗi khoản mua là một dịp để lắng nghe chính bạn." (giống Đăng nhập).
- **Components:** Text field (Default, Focused), Button/Primary/Large, Button/Text/Medium.
- **Trạng thái:** mặc định; chạm ô Email → Focused (prototype). Lỗi email, đang gửi, đã gửi *(đề xuất, chưa có khung trong Figma)*: lỗi dùng cùng mẫu với `Đăng nhập – lỗi` (viền đỏ, icon, câu hướng dẫn dưới ô); đang gửi: nút Loading; đã gửi: về Đăng nhập kèm snackbar "Đã gửi liên kết tới email của bạn".
- **Điều hướng:** "Quay lại", "Gửi liên kết đặt lại" và "Quay lại Đăng nhập" đều → Đăng nhập (prototype).
- **Ràng buộc:** chỉ một ô nhập; nút và link ≥ 48 dp.

### 01 Onboarding
- **Mục đích:** giới thiệu app làm gì trong một màn, rồi để người dùng bắt đầu ngay.
- **Nội dung:** icon app · overline "NHẬT KÝ ĐỘNG CƠ MUA SẮM" · "Why I Buy?" · "Ghi lại lý do của mỗi khoản mua để hiểu thói quen chi tiêu của chính bạn. Không chấm điểm, không phán xét." · thẻ 3 dòng: ghi số tiền, tên món và động cơ / xem động cơ và khung giờ theo tuần, tháng / đọc quan sát từ dữ liệu của chính bạn · nút chính "Bắt đầu" · "Dữ liệu được lưu trên máy của bạn."
- **Flow:** 1 (lần đầu), 7. "Bắt đầu" → Đăng nhập.
- **Ý đồ:** một màn thay cho carousel nhiều trang (bớt thao tác); 3 dòng tương ứng 3 tab chính để người dùng biết trước sẽ thấy gì; không ảnh minh họa trang trí (DESIGN.md).

### 00 Trang chủ tổng hợp (Hub)
- **Mục đích:** tab 1 sau khi đăng nhập. Hub là màn 02 Trang chủ có thêm lối vào Flow 6 (Danh sách mong muốn) và Flow 9 (Trước khi mua). Thuộc Flow 1, 6, 7, 8, 9.
- **Bố cục & phân cấp thị giác:**
  - **App bar (tab):** "Trang chủ", logo bên trái, avatar bên phải.
  - **Nội dung (cuộn):** "Chào bạn," → thẻ **Tổng quan tuần** ("TỔNG QUAN TUẦN", chip "Hôm nay, 11/10", "817.000 ₫", "Tuần này: 5 khoản · 817.000 ₫", "Nhiều nhất: Khuyến mãi (2/5)", "Động cơ chính · 40% do Khuyến mãi") → thẻ "Danh sách mong muốn" / "2 món đang cân nhắc" → thẻ **Trước khi mua** ("Dừng lại một chút. Vài câu hỏi nhanh giúp bạn hiểu điều gì đứng sau một lần mua.", "Hiểu trước khi thay đổi.", nút Tonal "Trước khi mua") → "Khoản mua gần đây" (badge 3) + "Xem tất cả" → 3 dòng khoản mua: Cơm tấm · Tiện lợi · Hôm nay 12:15 · 40.000 ₫ / Tai nghe Bluetooth · Khuyến mãi · Hôm qua 23:40 · 389.000 ₫ / Sách “Tâm lý học về tiền” · Mong muốn · 08/10 20:05 · 159.000 ₫.
  - **Thanh đáy:** nút chính "Ghi khoản mua" + thanh điều hướng (Trang chủ).
- **Components:** App bar/Tab, Weekly summary card, Wishlist entry, Before You Buy entry, Button (Tonal Medium, Primary Large), Purchase row, Motive chip, Navigation bar.
- **Điều hướng (prototype):** thẻ Danh sách mong muốn → 11 · "Trước khi mua" → 14 Trước khi mua – Bước 1/3 · "Xem tất cả" → 06 Lịch sử · dòng khoản mua → 05 Chi tiết khoản mua (đúng khoản được chạm) · "Ghi khoản mua" → 03 · avatar → 10 Cá nhân · các tab → 06, 07, 08, 10.
- **Trạng thái:** chưa ghi hôm nay (khung `00 Trang chủ (Hub) – chưa ghi hôm nay`, dòng "Hôm nay bạn chưa ghi khoản nào"). Trống, ngoại tuyến, sau khi lưu: dùng các khung của 02 (xem mục 02 bên dưới).
- **Ràng buộc:** "Ghi khoản mua" là nút chính duy nhất; nút "Trước khi mua" dùng kiểu Tonal để không cạnh tranh. Nội dung cuộn phía sau thanh đáy, nút luôn hiện.

### 02 Trang chủ
- **Mục đích:** xem nhanh tuần này và ghi khoản mua mới bằng một chạm.
- **Nội dung:** app bar "Trang chủ" · "Chào bạn," · thẻ **Tổng quan tuần**: chip "Hôm nay, 11/10", tổng 817.000 ₫, "Tuần này: 5 khoản · 817.000 ₫", "Nhiều nhất: Khuyến mãi (2/5)", khối "Động cơ chính — 40% do Khuyến mãi" với thanh màu xếp chồng · (thẻ "Danh sách mong muốn · 2 món đang cân nhắc" khi có món) · "Khoản mua gần đây (3)" + "Xem tất cả" · 3 dòng khoản mua (icon động cơ, tên, chip động cơ, giờ, số tiền) · nút chính "Ghi khoản mua" · thanh điều hướng 5 tab.
- **Flow:** 1 (bắt đầu, kết thúc), 2 (bắt đầu), 6 (bắt đầu).
- **Trạng thái:** `02 Trang chủ – trống` (0 ₫, "Chưa có dữ liệu", empty state "Chưa có khoản mua nào tuần này") · `– sau khi lưu` (862.000 ₫ · 6 khoản, snackbar "Đã lưu “Trà sữa nướng” · Hoàn tác") · `– ngoại tuyến` (snackbar "Đã lưu trên máy. Sẽ đồng bộ khi có mạng.") · `– lối vào Danh sách mong muốn`.
- **Ý đồ:** nút "Ghi khoản mua" là hành động chính duy nhất, ghim ở vùng ngón cái (Nam dùng một tay). Không có cảnh báo vượt ngân sách hay màu đỏ; thẻ tổng quan chỉ nêu số đếm và động cơ.

### 03 Ghi khoản mua – Bước 1/2
- **Mục đích:** nhập số tiền, tên món và thời điểm trong vài giây.
- **Nội dung:** app bar "← Ghi khoản mua" · chấm tiến trình + chip "Bước 1/2: Thông tin khoản chi" · thẻ **Số tiền thực chi** (nhãn "Bắt buộc"): 45.000 ₫ cỡ lớn + nút xóa, 3 chip "+20.000 ₫ / +50.000 ₫ / +100.000 ₫" · thẻ: "Tên món đồ hoặc dịch vụ" (Trà sữa nướng), "Thời điểm chi tiêu" (Hôm nay 23:10 – Chủ Nhật, 11/10/2026) · nút chính "Tiếp tục" + "Bước tiếp theo: chọn động cơ của khoản mua".
- **Flow:** 1 (bước 1, nhánh lỗi), 3 (sửa), 6 (điền sẵn).
- **Trạng thái:** `03 … (lỗi)` (0 ₫: ô nền đỏ nhạt, "Vui lòng nhập số tiền lớn hơn 0 ₫", nút "Tiếp tục" bị khóa) · `03 Sửa khoản mua – Bước 1/2` · `03 … (từ danh sách mong muốn)` (banner "Điền sẵn từ Danh sách mong muốn: “Bàn phím cơ”…").
- **Ý đồ:** tách form thành 2 bước để mỗi màn ít trường (mục tiêu ≤ 25 giây); thời điểm mặc định là "bây giờ" nên thường không cần chạm; lỗi hiện ngay dưới ô và khóa nút (Nielsen #5, #9) thay vì popup.

### 04 Ghi khoản mua – Bước 2/2
- **Mục đích:** gắn đúng một động cơ cho khoản vừa nhập.
- **Nội dung:** app bar "← Ghi khoản mua" + nút "?" · "BƯỚC 2/2 · Nhận diện động cơ" · khối "KHOẢN CHI VỪA NHẬP — Trà sữa nướng · 45.000 ₫" · "Vì sao bạn mua?" + "Chọn động cơ gần nhất với lúc bạn quyết định mua." · lưới 2 × 4 thẻ động cơ (icon + tên), Cảm xúc đang chọn · "Ghi chú thêm (tùy chọn)" · nút chính "Lưu".
- **Flow:** 1 (bước 2), 3 (sửa), 6 (động cơ chọn sẵn).
- **Trạng thái:** `– Bước 2/2 (đang lưu)` (nút "Đang lưu…") · `– giải thích động cơ` (bottom sheet "Các động cơ nghĩa là gì?" với 8 định nghĩa một dòng) · `04 Sửa khoản mua – Bước 2/2` ("Lưu thay đổi") · `– Bước 2/2 (từ danh sách mong muốn)`.
- **Ý đồ:** thẻ có icon để nhận ra thay vì nhớ (Nielsen #6); bỏ dòng mô tả trong thẻ để cả lưới và nút Lưu nằm gọn trong 800 dp, phần giải thích chuyển vào nút "?" (Nielsen #10).

### 05 Chi tiết khoản mua
- **Mục đích:** xem lại đầy đủ một khoản, sửa hoặc xóa.
- **Nội dung:** app bar "← Chi tiết khoản mua" + nút xóa (đỏ) · thẻ: "MỤC ĐÃ CHI TIÊU", Tai nghe Bluetooth, 389.000 ₫, khối "Động cơ" (Khuyến mãi) · thẻ: "Thời gian ghi nhận — Hôm qua 23:40 — Thứ Bảy, 10/10/2026", "Ghi chú của bạn — “Thấy flash sale lúc lướt TikTok”" · nút chính "Sửa".
- **Flow:** 3.
- **Trạng thái:** `05 … – dialog xóa` ("Xóa khoản mua này?" / "“Tai nghe Bluetooth” sẽ bị xóa khỏi lịch sử. Bạn có 5 giây để hoàn tác." / Hủy · Xóa).
- **Ý đồ:** "Sửa" là hành động chính vì thường gặp hơn xóa; xóa đặt ở app bar, có dialog nêu tên khoản và hoàn tác 5 giây (Nielsen #3, #5).

### 05a Xin quyền thông báo
- **Mục đích:** xin đúng một quyền (thông báo) để gửi lời nhắc ghi khoản mua mỗi tối. Thuộc Flow 1, 5.
- **Bố cục & phân cấp thị giác:**
  - **Đầu màn:** icon trong vòng tròn.
  - **Nội dung:** tiêu đề "Để Why I Buy? nhắc bạn mỗi tối?" · mô tả "Một lời nhắc lúc 21:00 giúp bạn ghi lại khoản mua trong ngày khi còn nhớ rõ lý do." · khung xem trước thông báo (App icon, "Why I Buy? · 21:00", "Hôm nay bạn có mua gì không? Ghi lại trong 10 giây.").
  - **Khối hành động (cuối màn):** nút chính "Bật nhắc nhở" · nút chữ "Để sau" · chú thích "Bạn có thể đổi giờ nhắc trong Cá nhân."
- **Components:** App icon, Button/Primary/Large, Button/Text/Medium.
- **Điểm vào:** sau lần lưu khoản mua **đầu tiên** (Flow 1); từ nút Tonal "Mở cài đặt" trong thẻ "Thông báo đang tắt" ở `10 Cá nhân – chưa cấp quyền thông báo` (thêm ở vòng R4-2).
- **Trạng thái:** chỉ một khung. Prototype nhớ lựa chọn "Để sau" bằng biến `thong-bao/da-tu-choi`, để tab Cá nhân hiện đúng trạng thái chưa cấp quyền.
- **Ràng buộc:** không hỏi quyền lúc mở app; một màn chỉ xin một quyền; "Để sau" không chặn người dùng. Hành vi trên Android xem handoff mục 8.5.

### 06 Lịch sử
- **Mục đích:** xem lại các khoản theo kỳ và lọc theo động cơ.
- **Nội dung:** app bar "Lịch sử" · bộ chọn kỳ "< Tuần này · 05/10 – 11/10 / 6 khoản · 862.000 ₫ ˅ >" · hàng chip lọc "Tất cả (6)", "Nhu cầu (1)", "Mong muốn…" · nhóm theo ngày ("Hôm nay, 11/10/2026 — 85.000 ₫": Trà sữa nướng, Cơm tấm; "Hôm qua…": Tai nghe Bluetooth; "08/10/2026": Sách…) · thanh điều hướng.
- **Flow:** 3 (bắt đầu, kết thúc), 4.
- **Trạng thái:** `– không có kết quả` ("Chưa có khoản nào gắn Quảng cáo" + "Xóa bộ lọc") · `– sau khi xóa` (5 khoản · 473.000 ₫ + snackbar "Đã xóa “Tai nghe Bluetooth” · Hoàn tác") · `– chọn tháng` (bottom sheet "Xem theo tháng": chọn năm, 12 ô tháng, tháng chưa có dữ liệu bị mờ, nút "Xem tháng 9/2026") · `– tháng 9/2026` (11 khoản · 1.254.000 ₫, banner "Xem mô hình động cơ tháng 9 ›").
- **Ý đồ:** nhóm theo ngày kèm tổng ngày để dễ nhớ lại; chip có số lượng nên biết trước bộ lọc có kết quả hay không; bộ lọc trống luôn có lối thoát "Xóa bộ lọc" (không ngõ cụt).

### 07 Mô hình
- **Mục đích:** thấy động cơ nào chiếm nhiều nhất và hay mua vào khung giờ nào.
- **Nội dung:** app bar "Mô hình" · segmented "Tuần | Tháng" · bộ chọn kỳ "Tháng 10/2026 · 15 khoản" · thẻ "TỔNG QUAN CHU KỲ — Tháng 10/2026: 15 khoản" · "Động cơ chi tiêu · 8 động cơ": 8 dòng icon + tên + "5 (33%)" + thanh % (Khuyến mãi 5, Cảm xúc 4, Tiện lợi 2, Nhu cầu 2, Mong muốn 1, Ảnh hưởng MXH 1, Quảng cáo 0, Khác 0) · "Khung giờ chi tiêu": Sáng 2 · Trưa 3 · Chiều 2 · Tối 8 · thanh điều hướng.
- **Flow:** 2, 4.
- **Trạng thái:** `– đang tải` (skeleton giữ đúng khung) · `– lỗi` ("Không tải được mô hình", nguyên nhân + trấn an dữ liệu, "Thử lại") · `– chưa đủ dữ liệu` ("Bạn đã ghi 3 khoản. Ghi thêm 2 khoản để xem mô hình." + "Ghi khoản mua") · `– tháng 9/2026` · `– Tuần` (Tuần 41: 6 khoản).
- **Ý đồ:** dùng danh sách thanh ngang có số và phần trăm thay cho biểu đồ tròn, để đọc được cả khi không phân biệt màu (WCAG 1.4.1) và ở 360 dp; động cơ 0 khoản vẫn hiện để không ngầm "chấm điểm".
- **Phiên bản có AI** (khung `07 Mô hình (có AI)`, phiên bản hiện tại của 07, Flow 10): giữ nguyên nội dung trên (Tuần / **Tháng**, "Tháng 10/2026 · 15 khoản", 8 động cơ, 4 khung giờ), thêm nút Primary "Để AI phân tích" → `08a AI đang phân tích – mô hình` (tự chuyển) → 08b Chi tiết mô hình mua sắm.

### 08 Góc nhìn
- **Mục đích:** đọc vài quan sát trung tính rút ra từ chính dữ liệu đã ghi.
- **Nội dung:** app bar "Góc nhìn" · "THÁNG 10/2026 · Góc nhìn" + "Những quan sát trung tính, tổng hợp từ các khoản bạn đã ghi trong tháng." · thẻ "THÁNG 10 · NHÌN LẠI — 15 khoản đã ghi" · 3 thẻ quan sát: "5 trong 15 khoản tháng này gắn với Khuyến mãi." [Động cơ], "8 trong 15 khoản được ghi sau 18:00." [Khung giờ], "Cả 4 khoản Cảm xúc đều được ghi sau 22:00." [Cảm xúc] · nút chính "Mở chiêm nghiệm tháng" · thanh điều hướng.
- **Flow:** 2.
- **Trạng thái:** `– đã lưu chiêm nghiệm` (snackbar "Đã lưu chiêm nghiệm tháng 10").
- **Ý đồ:** chỉ quan sát kiểm chứng được, không lời khuyên, không số liệu bịa (Nielsen #2; giọng văn trong DESIGN.md).
- **Phiên bản có AI** (khung `08 Góc nhìn (có AI)`, phiên bản hiện tại của 08, Flow 10): app bar "Góc nhìn" · "THÁNG 10/2026" · dòng mạch "Dữ liệu mua sắm → Nhận định AI → Chiêm nghiệm" · thẻ **AI nhận thấy** ("Khuyến mãi là một trong những động cơ bạn chọn nhiều nhất." · "5/15 khoản gắn với Khuyến mãi. Cảm xúc xuất hiện 4 lần." · "Gợi mở: Điều gì khiến một ưu đãi có giá trị với bạn?" · nút chữ "Xem chi tiết" → 08c) · thẻ **Mô hình mua sắm (AI)** (Khuyến mãi 5/15; Cảm xúc 4/15; "Ghi vào buổi tối · 8/15 – Nhiều khoản được ghi vào buổi tối — không nhất thiết là mua vào buổi tối." · nút "Xem mô hình của tôi" → 08b) · thẻ **Chiêm nghiệm tháng** ("Tháng 10/2026 · 15 khoản đã ghi" · "Khuyến mãi xuất hiện nhiều nhất (5/15), tiếp theo là Cảm xúc (4/15)." · "Gợi mở: Tháng tới bạn muốn để ý điều gì?" · nút "Mở chiêm nghiệm tháng" → 09) · thanh điều hướng. Components: App bar/Tab, Button/Text/Medium, AI pattern card, Snackbar/Saved, Navigation bar. Trạng thái: `08 Góc nhìn – đã lưu chiêm nghiệm (có AI)` (snackbar "Đã lưu chiêm nghiệm tháng 10").

### 09 Chiêm nghiệm tháng
- **Mục đích:** tự đánh giá mức hài lòng với tháng và đặt một điều muốn để ý tháng sau.
- **Nội dung:** app bar "← Chiêm nghiệm tháng" · thẻ "Tháng 10/2026: 15 khoản chi" + thanh màu xếp chồng + lưới chip động cơ có số · thẻ "Mức độ hài lòng của bạn" + thang 1–5 ("Không hài lòng" … "Rất hài lòng") · thẻ "Mục tiêu cho tháng 11" (ô nhập) · nút chính "Lưu chiêm nghiệm" · nút chữ "Để sau".
- **Flow:** 2 (kết thúc).
- **Ý đồ:** người dùng tự chấm, app không chấm; có "Để sau" để không ép (Nielsen #3).

### 10 Cá nhân
- **Mục đích:** bật / tắt nhắc nhở, xuất và xóa dữ liệu.
- **Nội dung:** app bar "Cá nhân" · thẻ "Bạn — Dữ liệu cá nhân trên máy này" · "CÀI ĐẶT NHẮC NHỞ": "Nhắc ghi khoản mua" (21:00 mỗi tối, bật), "Nhắc chiêm nghiệm hằng tháng" (ngày cuối tháng, bật) · "CÀI ĐẶT DỮ LIỆU": "Xuất dữ liệu" (CSV), "Xóa toàn bộ dữ liệu" (chữ đỏ) · ghi chú "Dữ liệu được lưu trên máy và đồng bộ với tài khoản của bạn khi có mạng." · thanh điều hướng.
- **Flow:** 5.
- **Trạng thái:** `– xác nhận xóa toàn bộ` (dialog, nêu rõ "Không thể hoàn tác") · `– đã xuất dữ liệu` (snackbar "Đã lưu “whyibuy-10-2026.csv” vào Tải xuống").
- **Ý đồ:** nhắc nhở là lời nhắc trung tính, người dùng tự bật; xóa toàn bộ không hoàn tác được nên bắt buộc dialog (Nielsen #5).

### 10a Tài khoản
- **Mục đích:** xem email, đổi mật khẩu hoặc xóa tài khoản. Thuộc Flow 7.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** Back, "Tài khoản".
  - **Thẻ thông tin:** "Email" · "minhanh@gmail.com" (chỉ hiển thị) · "Đổi mật khẩu" · "Cập nhật mật khẩu đăng nhập" (chevron → 10b).
  - **Nhóm nguy hiểm (tách riêng ở cuối màn):** "Xóa tài khoản" · "Xóa vĩnh viễn tài khoản và mọi khoản mua đã đồng bộ", chữ màu error.
- **Components:** App bar/Nested, Card, Dialog (Type=Danger), Snackbar (Type=Saved), Button/Text/Medium, Button/Danger/Medium.
- **Trạng thái:** mặc định (10a) · xác nhận xóa (`10a Tài khoản – xác nhận xóa`: scrim 40% + dialog "Xóa tài khoản?" / "Tài khoản và toàn bộ khoản mua của bạn sẽ bị xóa vĩnh viễn, không thể khôi phục." / nút chữ "Hủy" · nút Danger "Xóa tài khoản" bên phải) · sau khi đổi mật khẩu (khung `10b Đổi mật khẩu – đã lưu`: nội dung 10a kèm snackbar "Đã đổi mật khẩu").
- **Điều hướng:** đến từ thẻ tài khoản ở 10 Cá nhân. Back → 10. Xóa tài khoản xong → 00a Đăng nhập.
- **Ràng buộc:** "Xóa tài khoản" khác "Xóa toàn bộ dữ liệu" ở 10 (chỉ xóa khoản mua, giữ tài khoản); không có hoàn tác nên bắt buộc dialog Danger.

### 10b Đổi mật khẩu
- **Mục đích:** đổi mật khẩu đăng nhập, phải nhập mật khẩu hiện tại. Thuộc Flow 7.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** Back, "Đổi mật khẩu".
  - **Form:** ô "Mật khẩu hiện tại" (placeholder "Nhập mật khẩu đang dùng") · ô "Mật khẩu mới" · thanh độ mạnh "Độ mạnh: Trung bình · Thêm ký tự để mạnh hơn" · ô "Nhập lại mật khẩu mới".
  - **Thanh đáy:** nút chính "Lưu" (Disabled trong khung mẫu).
- **Components:** App bar/Nested, Text field (ô mật khẩu có icon eye / eye-off), Password strength (Level=Trung bình), Button/Primary/Large (Disabled).
- **Trạng thái:** đang nhập (10b, nút Lưu Disabled) · đã lưu: về 10a kèm snackbar "Đã đổi mật khẩu" (khung `10b Đổi mật khẩu – đã lưu`).
- **Validation:** nút "Lưu" chỉ bật khi đủ 3 ô và ô mới trùng ô nhập lại (handoff mục 8.1). Câu lỗi cho mật khẩu hiện tại sai hoặc nhập lại chưa khớp *(đề xuất, chưa có khung trong Figma)*: "Mật khẩu hiện tại chưa đúng.", "Mật khẩu nhập lại chưa khớp."
- **Điều hướng:** đến từ 10a. Back → 10a. Lưu thành công → 10a.

---

### 11 Danh sách mong muốn (Wishlist Overview)
- **Mục đích:** xem những món đang muốn mua và lý do muốn mua, lọc theo trạng thái. Thuộc Flow 6.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** nút Back, tiêu đề "Danh sách mong muốn".
  - **Intro:** thẻ nền surface-container, icon bookmark: "Ghi lại món bạn muốn mua và lý do. Bạn tự quyết định khi nào mua, bỏ qua hay cân nhắc thêm."
  - **Bộ lọc:** 3 chip "Đang cân nhắc (n)", "Đã mua (n)", "Bỏ qua (n)"; chip đang chọn có nền + dấu tích. Ở 360 dp chip xuống hàng (wrap) thay vì bị cắt.
  - **Danh sách:** thẻ món (tên, giá dự kiến, chip động cơ, chip trạng thái, ghi chú, ngày thêm).
  - **Thanh đáy:** nút chính "Thêm món" (icon +).
- **Components:** App bar/Nested, Filter chip, Wishlist item card (Status × State Default/Pressed), Motive chip, Wishlist status chip, Empty state (Filter empty), Snackbar, Button/Primary.
- **Trạng thái:** có dữ liệu (11) · trống hoàn toàn (11a: "Bạn chưa có món nào đang cân nhắc." + "Thêm món", ẩn thanh đáy) · bộ lọc trống (11a: "Chưa có món nào trong danh mục này." + "Xem đang cân nhắc") · đã lưu (11b) · đã bỏ qua + Hoàn tác (11c) · sau hoàn tác (11d) · đã mua (11e). Không bao giờ hiển thị empty state cùng thẻ của bộ lọc khác.
- **Ràng buộc:** số trên chip phải khớp số thẻ; không có nút mua hàng, giỏ hàng hay đồng hồ chờ.

### 12 Thêm món mong muốn (Add Wishlist Item)
- **Mục đích:** lưu một món muốn mua kèm động cơ trong dưới 20 giây. Dùng lại cho "Sửa món mong muốn" (12c).
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** Back, "Thêm món mong muốn" (12c: "Sửa món mong muốn").
  - **Thẻ thông tin:** ô "Tên món đồ (bắt buộc)" (icon túi), ô "Giá dự kiến (tùy chọn)" (icon hóa đơn), giá hiển thị "650.000 ₫".
  - **Câu hỏi:** "Vì sao bạn muốn mua món này?" + "Chọn một lý do chính. Không có lựa chọn đúng hay sai."
  - **Lưới động cơ:** đúng 8 động cơ, 2 cột × 4 hàng, giống màn 04.
  - **Ghi chú thêm (tùy chọn).**
  - **Thanh đáy:** nút chính "Lưu món" (12c: "Lưu thay đổi").
- **Components:** App bar/Nested, Text field (Default/Error), Motive grid, Button/Primary.
- **Trạng thái:** trống (12) · lỗi (12a) · đã điền hợp lệ (12b) · sửa (12c).
- **Validation:** tên trống hoặc chỉ khoảng trắng → "Vui lòng nhập tên món đồ để lưu." · giá đã nhập nhưng ≤ 0 → "Vui lòng nhập số tiền lớn hơn 0." · chưa chọn động cơ → "Vui lòng chọn lý do bạn muốn mua món này." Lỗi hiện ngay dưới trường, kèm icon; form hợp lệ không hiện lỗi.
- **Ràng buộc:** nội dung cuộn, nút "Lưu món" luôn hiện trên bàn phím.

### 13 Chi tiết món mong muốn (Wishlist Detail)
- **Mục đích:** nhìn lại lý do muốn mua và tự quyết định.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** Back, "Chi tiết món mong muốn", icon Sửa (48 dp).
  - **Thẻ tóm tắt:** "MÓN ĐANG CÂN NHẮC", tên món, giá dự kiến (lớn) + "Giá dự kiến · chưa tính vào chi tiêu", chip trạng thái, khối "Lý do muốn mua" với chip động cơ.
  - **Thẻ chi tiết:** "Ngày thêm vào danh sách" (Thứ Sáu, 09/10/2026 · 2 ngày trước), "Ghi chú của bạn".
  - **Thanh đáy:** nút chính "Ghi khoản mua"; nút văn bản "Không mua nữa".
- **Components:** App bar/Nested, Motive chip, Wishlist status chip, Button/Primary, Button/Text, Dialog, Snackbar.
- **Trạng thái:** đang cân nhắc (13) · dialog xác nhận bỏ qua (13a, overlay) · sau khi sửa (13b, snackbar "Đã cập nhật “Bàn phím cơ”") · đã bỏ qua (13c: overline "MÓN ĐÃ BỎ QUA", chip Bỏ qua, nút chính duy nhất "Đưa về Đang cân nhắc") · đã mua (13d: overline "MÓN ĐÃ MUA", chip Đã mua, caption "Đã ghi khoản mua 650.000 ₫ vào Lịch sử", ngày mua; chỉ xem — ẩn nút đáy và nút Sửa).
- **Ràng buộc:** không có đếm ngược 48h/72h, không có nhật ký tâm lý bắt buộc, không khóa nút vì thời gian.

---

Các màn dưới đây thuộc Flow 8–10 (AI và Trước khi mua), nằm ở section "Flow 8–10 – AI (Góc nhìn AI, Trước khi mua)" của page `03 Final UI`. Tên màn giữ đúng tên khung Figma. Hai trạng thái đang tải `08a AI đang phân tích` và `17 AI đang phân tích – trước khi mua` được mô tả trong màn đích của chúng.

### 05 Khoản mua đã lưu
- **Mục đích:** xác nhận khoản vừa lưu và mời người dùng xem nhận định ở Góc nhìn. Thuộc Flow 1 (sau khi lưu), Flow 8 (bắt đầu).
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** "Đã lưu khoản mua".
  - **Xác nhận:** "Khoản mua đã được lưu" · "Một khoảnh khắc để nhận biết." · dòng khoản mua Trà sữa nướng · Cảm xúc · Hôm nay · 45.000 ₫ · "Động cơ đã chọn: Cảm xúc".
  - **Thẻ dẫn hướng:** "Nhận định của bạn ở Góc nhìn" / "Nhận định AI và chiêm nghiệm nằm ở Góc nhìn. Xem điều gì đúng với bạn." · "Hiểu trước khi thay đổi."
  - **Thanh đáy:** nút chính "Mở Góc nhìn" · nút Tonal "Về Trang chủ".
- **Components:** App bar/Nested, Purchase row, Motive chip, Button/Primary/Large, Button/Tonal/Medium.
- **Điều hướng:** đến từ 04 sau khi lưu. "Mở Góc nhìn" → `08a AI đang phân tích – khoản vừa lưu` → 08c. "Về Trang chủ" → `02 Trang chủ – sau khi lưu` (snackbar "Đã lưu"). Lần lưu đầu tiên và chưa cấp quyền → 05a (Flow 1).
- **Ràng buộc:** không khen, không đánh giá khoản vừa lưu; chỉ nhắc lại động cơ người dùng đã chọn.

### 08b Chi tiết mô hình mua sắm
- **Mục đích:** đọc phân tích AI về các động cơ đã ghi trong tháng. Thuộc Flow 8, 9, 10.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** "Chi tiết mô hình".
  - **Đầu trang:** "Mô hình mua sắm của bạn" · "Tháng 10/2026 · 15 khoản".
  - **Động cơ phổ biến nhất:** overline "ĐỘNG CƠ PHỔ BIẾN NHẤT" · "Khuyến mãi · 5/15" · "Khuyến mãi là động cơ bạn chọn nhiều nhất, chiếm khoảng một phần ba số khoản trong tháng."
  - **3 thẻ nhận định:** Khuyến mãi 5/15 · Cảm xúc 4/15 · Nhu cầu 2 · Tiện lợi 2.
  - **Phần còn lại:** "Mong muốn: 1 · Ảnh hưởng MXH: 1 · Quảng cáo: 0. Đây là động cơ bạn đã ghi, không phải dự đoán về bạn."
  - **Gợi mở:** "Điều gì khiến một ưu đãi có giá trị với bạn?"
  - **Thanh đáy:** nút chính "Xem mô hình của tôi".
- **Components:** App bar/Nested, Insight card, Button/Primary/Large.
- **Trạng thái:** đang tải (`08a AI đang phân tích – mô hình`: "AI đang phân tích", "Đang xem kỹ hơn", "Đang tổng hợp các động cơ bạn đã ghi trong tháng này.", "Tháng 10/2026 · 15 khoản", skeleton, "Đang so sánh các động cơ bạn đã chọn…", tự chuyển) · có kết quả (08b). Lỗi hoặc mất mạng *(đề xuất, chưa có khung trong Figma)*: Empty / Error state có "Thử lại", giống `07 Mô hình – lỗi`.
- **Điều hướng:** từ 07 Mô hình (có AI) qua 08a; từ thẻ "Mô hình mua sắm (AI)" ở 08; chạm thẻ nhận định ở 08c, 18. "Xem mô hình của tôi" → 07 Mô hình (có AI).
- **Ràng buộc:** chỉ nêu số đếm từ dữ liệu đã ghi (ví dụ "5/15"); luôn có một câu "Gợi mở"; không khuyên, không dự đoán.

### 08c Nhận định AI về khoản mua
- **Mục đích:** đọc nhận định AI về một khoản mua cụ thể. Có 2 khung cùng nội dung, khác điểm vào: `08c Nhận định AI về khoản vừa lưu` (Flow 8) và `08c Nhận định AI về khoản mua` (Flow 10).
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** "Nhận định AI về khoản mua".
  - **Khối AI:** "AI nhận thấy" · dòng khoản mua Trà sữa nướng · Cảm xúc · 45.000 ₫ · "Bạn đã chọn Cảm xúc." · "Một món quen thuộc đôi khi giúp tâm trạng khá hơn một chút. Điều đó có thể đúng với khoản này — hoặc không. Chỉ bạn biết lúc đó thế nào."
  - **2 thẻ nhận định:** "Bạn gắn ly trà này với cảm xúc lúc đó, hơn là một nhu cầu thiết thực." (tag "Động cơ bạn chọn") · "Sự quen thuộc có thể là một phần khiến món này hấp dẫn." (tag "Một tín hiệu dễ chịu có thể có").
  - **Gợi mở:** "Bạn mong ly trà giúp mình cảm thấy thế nào?" · "Đây là gợi ý để nhìn lại, không phải chẩn đoán hay phán xét."
  - **Thanh đáy:** nút chính "Đã hiểu" · nút Tonal "Xem mô hình của tôi".
- **Components:** App bar/Nested, Purchase row, Motive chip, Insight card, Button/Primary/Large, Button/Tonal/Medium.
- **Trạng thái:** đang tải (`08a AI đang phân tích – khoản vừa lưu`: "AI đang phân tích", "Đang xem kỹ hơn", "Đang nhìn lại động cơ bạn chọn: Cảm xúc.", "Trà sữa nướng · 45.000 ₫", skeleton, "Đang xem động cơ bạn đã chọn…", "Hiểu trước khi thay đổi.", tự chuyển sau 1,5 giây) · có kết quả (08c). Lỗi hoặc mất mạng *(đề xuất, chưa có khung trong Figma)*: Empty / Error state có "Thử lại".
- **Điều hướng:** Flow 8: từ 05 Khoản mua đã lưu qua 08a; "Đã hiểu" → 00 Hub. Flow 10: từ "Xem chi tiết" ở 08; "Đã hiểu" → 08 Góc nhìn. Cả hai: "Xem mô hình của tôi" → 07 Mô hình (có AI); chạm thẻ nhận định → 08b.
- **Ràng buộc:** chỉ dựa trên động cơ người dùng đã chọn; luôn có câu "Gợi mở" và câu chốt "không phải chẩn đoán hay phán xét".

### 14 Trước khi mua – Bước 1/3
- **Mục đích:** ghi lại món đang cân nhắc trước khi trả lời câu hỏi. Bước này không ghi khoản mua. Thuộc Flow 9.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** "Trước khi mua".
  - **Đầu bước:** "BƯỚC 1/3" · "Bạn đang cân nhắc món gì?" · "Bắt đầu với món bạn đang cân nhắc. Bước này không ghi khoản mua."
  - **Form:** ô "Tên món" (Tai nghe Bluetooth) · ô "Giá dự kiến (không bắt buộc)" (389.000 ₫).
  - **Thẻ giới thiệu:** "Một chút để hiểu mình" / "Tiếp theo, bạn sẽ xem vì sao mình muốn món này và điều gì thu hút bạn. Không có câu trả lời đúng hay sai." · "AI chỉ gợi ý để nhìn lại. Quyết định vẫn là của bạn."
  - **Thanh đáy:** nút chính "Tiếp tục".
- **Components:** App bar/Nested, Step header, Text field, Button/Primary/Large.
- **Trạng thái:** đã điền (14). Tên trống *(đề xuất, chưa có khung trong Figma)*: nút "Tiếp tục" khóa, lỗi dưới ô theo mẫu Text field/Error.
- **Điều hướng:** đến từ nút "Trước khi mua" ở 00 Hub hoặc `02 Trang chủ – lối vào Trước khi mua`. "Tiếp tục" → 15.
- **Ràng buộc:** giá dự kiến không bắt buộc, không cộng vào chi tiêu.

### 15 Trước khi mua – Bước 2/3
- **Mục đích:** chọn động cơ và tác động bên ngoài của món đang cân nhắc. Thuộc Flow 9.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** "Câu hỏi nhanh".
  - **Đầu bước:** "BƯỚC 2/3" · "Điều gì đứng sau lựa chọn?" · "Tai nghe Bluetooth · 389.000 ₫".
  - **Câu 1:** "Vì sao bạn muốn món này?" ("Chọn động cơ gần nhất với cảm nhận của bạn.") – 4 thẻ: Nhu cầu, Mong muốn, Cảm xúc, Khác.
  - **Câu 2:** "Điều gì tác động đến lần mua này?" ("Chọn tác động rõ nhất.") – 4 thẻ: Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Không có.
  - "Không có câu trả lời đúng hay sai." · **Thanh đáy:** nút chính "Tiếp tục".
- **Components:** App bar/Nested, Step header, Motive card (Default/Selected), Button/Primary/Large.
- **Trạng thái:** khung mẫu đang chọn Mong muốn + Khuyến mãi.
- **Điều hướng:** từ 14. "Tiếp tục" → 16 nếu câu 2 chọn Khuyến mãi; nếu không → `17 AI đang phân tích – trước khi mua` → 18.
- **Ràng buộc:** mỗi câu chọn một thẻ; thẻ có icon + tên, thẻ được chọn có nền, viền và dấu tích.

### 16 Trước khi mua – Bước 3/3
- **Mục đích:** tách sức hút của món đồ khỏi ưu đãi. Chỉ hiện khi câu 2 ở 15 chọn Khuyến mãi. Thuộc Flow 9.
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** "Câu hỏi về khuyến mãi".
  - **Đầu bước:** "BƯỚC 3/3" · "Thử bỏ qua ưu đãi" · "Tai nghe Bluetooth" · "389.000 ₫ · Mong muốn + Khuyến mãi".
  - **Câu hỏi:** "Không có khuyến mãi, bạn vẫn muốn món này chứ?" ("Hãy nghĩ về món đồ, tách khỏi ưu đãi.") – 3 lựa chọn: "Có, vẫn muốn", "Chưa chắc", "Không".
  - "Chưa chắc cũng không sao. Câu trả lời giúp gợi ý sát hơn." · **Thanh đáy:** nút chính "Xem nhận định".
- **Components:** App bar/Nested, Step header, Motive card, Button/Primary/Large.
- **Điều hướng:** từ 15. "Xem nhận định" → `17 AI đang phân tích – trước khi mua` → 18.
- **Ràng buộc:** "Chưa chắc" là lựa chọn hợp lệ, không bị coi là câu trả lời sai.

### 18 Nhận định trước khi mua
- **Mục đích:** đọc nhận định AI từ các câu trả lời, rồi tự quyết định. Thuộc Flow 9 (kết thúc).
- **Bố cục & phân cấp thị giác:**
  - **App bar (lồng):** "Nhận định trước khi mua".
  - **Đầu trang:** "Rõ hơn một chút trước khi mua" · "Tai nghe Bluetooth" · "389.000 ₫ · Dựa trên câu trả lời của bạn".
  - **2 thẻ nhận định:** "Bạn chọn Mong muốn: món này hấp dẫn bạn, hơn là một nhu cầu bạn đã xác định." (tag Mong muốn) · "Bạn chọn Khuyến mãi và chưa chắc sẽ muốn nó khi đủ giá. Ưu đãi là một phần sức hút." (tag Khuyến mãi).
  - **Tóm tắt:** "Câu trả lời cho thấy cả món đồ lẫn ưu đãi đều quan trọng với bạn. Đây là gợi ý từ điều bạn chia sẻ, không phải dự đoán việc bạn sẽ làm."
  - **Gợi mở:** "Không có khuyến mãi, điều gì khiến tai nghe này đáng mua với bạn?" · "Không có lựa chọn đúng hay sai. Quyết định là của bạn."
  - **Thanh đáy:** nút chính "Để mình nghĩ thêm" · nút Tonal "Vẫn mua".
- **Components:** App bar/Nested, Insight card, Button/Primary/Large, Button/Tonal/Medium.
- **Trạng thái:** đang tải (`17 AI đang phân tích – trước khi mua`: "AI đang phân tích", "Đang xem kỹ hơn", "Đang nhìn lại Mong muốn, Khuyến mãi và câu trả lời “Chưa chắc”.", "Tai nghe Bluetooth · 389.000 ₫", skeleton, "Đang kết nối các câu trả lời của bạn…", tự chuyển sau 1,5 giây) · có kết quả (18). Lỗi hoặc mất mạng *(đề xuất, chưa có khung trong Figma)*: Empty / Error state có "Thử lại".
- **Điều hướng:** "Để mình nghĩ thêm" → về Trang chủ, không ghi gì. "Vẫn mua" → 03 Ghi khoản mua – Bước 1/2 (sang Flow 1). Chạm thẻ nhận định → 08b.
- **Ràng buộc:** Flow 9 không tạo khoản mua nếu người dùng không chọn "Vẫn mua". Nút chính là "Để mình nghĩ thêm", nhưng cả hai lựa chọn đều trung lập, không có lời khuyên nên mua hay không.

---

## Smart Shopping Companion – màn F11–F13 (Figma ver2, 18/10/2026)

Nguồn: tên frame, chữ hiển thị và dây nối prototype đọc trực tiếp từ file Figma `VaPYFxfpx14tnQmOMSgdjP` ngày 18/10 (page 03, section "Flow 11–12 – Danh sách chờ v3…", "Extension trình duyệt – popup 8 trạng thái", "[MỚI · 18/10] Bổ sung theo đặc tả 11.3…"). Quy tắc sản phẩm theo đặc tả hợp nhất v1.0 (17/10). Ảnh 1× của mọi khung (kể cả biến thể) ở [`assets/figma/ver2/`](../assets/figma/ver2/) (xuất ngày 18/10); chưa kiểm tra bố cục ở 412 dp.

### Ánh xạ mã màn: đặc tả 17/10 ↔ Figma 18/10

Repo dùng **mã Figma** (nhóm chốt ngày 18/10, để khớp prototype); cột "Đặc tả" chỉ để đối chiếu với đặc tả hợp nhất 17/10.

| Đặc tả 17/10 (mục 11.3) | Tên trong đặc tả | Mã trên Figma 18/10 | Trạng thái thiết kế | Ghi chú lệch |
|---|---|---|---|---|
| 19 · 19.1–19.5 | Lưu từ chia sẻ (bottom sheet) | 19, 19a–19g | Đã thiết kế; 19a, 19, 19g, 19e nối prototype | Figma dùng hậu tố chữ; thêm 19a đang lấy, 19b có giá gần đây, 19f nhắc món tương tự. 19.2 ≈ 19c, 19.3 ≈ 19e, 19.4 ≈ 19d, 19.5 ≈ 19g |
| 20 · 20.1–20.5 | Decision Card | **28**, 28a, 28b, 28c | Đã thiết kế; 28 nối prototype | Figma số **20** là "Lấy giá từ ảnh chụp". Không có biến thể "20.3 thiếu giá" riêng: gần nhất là 28b (giá cũ) và 13h (cần giá) |
| 21 · 21.1–21.2 | Chờ – chọn thời điểm xem lại | **29**, 29a | Đã thiết kế, nối prototype | Figma số **21** là "Danh sách cho đợt sale" |
| 22 · 22.1–22.3 | Cập nhật giá và lịch sử giá | **30**, 30a, 30b | Đã thiết kế, nối prototype (F12) | Figma số **22** là "Gói mua" (đặc tả: GĐ5) |
| 23 · 23.1–23.3 + giải thích | Ngân sách theo nhóm | **31**, 31a, 31b, 31c | Đã thiết kế; chỉ 31c nối prototype | Figma số **23** là "So sánh món cùng loại" |
| 24 · 24.1–24.3 | Hồ sơ mua sắm | 24, 24a, 24b "Đồ đang dùng" | Đã thiết kế, chưa nối | Figma chỉ có đồ đang dùng (tên, loại, tình trạng, số lượng); chưa có phong cách và thương hiệu hay dùng |
| 25 · 25.1–25.4 | Thiết bị đã liên kết và mã ghép | 25, 25c, 25f, 25b, 25e | Đã thiết kế; 25, 25f, 25b, 25e nối prototype | Khớp nội dung |
| 26 · 26.1–26.3 | Lịch sale và Danh sách cho đợt sale | **21**, 21a, Thông báo đẩy – 3 mẫu | Đã thiết kế, nối prototype (F12) | Figma số **26** là "Nhắc nhở & ngưỡng" (cài đặt) |
| 27 · 27.1–27.2 | Hỏi mức hài lòng | 27, 27a | Đã thiết kế, chưa nối | Khớp |
| — (A-17, GĐ4) | Lấy giá từ ảnh chụp | 20, 20a, 20b | Đã thiết kế; 20, 20a nối prototype | Đặc tả không đánh mã màn |
| — (A-19, GĐ5) | Gói mua vừa ngân sách | 22, 22a, 22b, 22c | Đã thiết kế, chưa nối | Đặc tả: chỉ chạy khi người dùng yêu cầu |
| — (A-15, GĐ4) | So sánh các món cùng nhóm | 23 | Đã thiết kế, chưa nối | — |
| — | Cài đặt nhắc và ngưỡng | 26 | Đã thiết kế, chưa nối | Mặc định thời gian chờ **7 ngày** (đặc tả: 3 ngày) |
| X1 (400 × 600) | Popup Lưu nhanh | EXT-1 … EXT-8 (360 × 560) | Đã thiết kế, **chưa nối prototype** | Theo bản 8 trạng thái của Kiệt; EXT-1 chặn lưu khi chưa liên kết (đặc tả 5.2: không chặn) |
| X2–X5 | Trang Wishlist · Decision Card bảng cạnh · Ghép thiết bị · Cài đặt | X2, X2a, X3, X4, X4a, X5 (960 × 640) | Đã thiết kế; X2, X3, X4, X4a, X5 nối prototype | X2a chưa nối; X4 chưa có trạng thái nhập mã ban đầu |
| 11 (sửa) | Wishlist: nhãn nguồn, giá kèm ngày | 11 v3, 11a v3, 11f | Đã thiết kế; 11 v3 nối prototype | Chưa thấy nhãn nguồn lưu trên thẻ 11 v3 (13 v3 có "từ extension") |
| 13 (sửa) | Lối vào Decision Card, Mua · Chờ · Bỏ qua, lịch sử giá | 13 v3, 13g, 13h | Đã thiết kế, chưa nối | Nút ghi "Chờ đợt sau" (28 ghi "Chờ") |
| 14–16 (sửa) | Điền sẵn từ món, chip "Có mã giảm giá" | 14, 15, 16 (bản cũ) | **Chưa sửa** | — |
| 18 (sửa) | Đổi "Vẫn mua / Để mình nghĩ thêm" thành Mua · Chờ · Bỏ qua | 18 (bản cũ) | **Chưa sửa** | — |
| 03/04 từ Wishlist (sửa) | Giá thực trả + chip "Có dùng mã giảm giá" | 03 … (từ danh sách mong muốn) | **Một phần** | Có "Số tiền thực chi"; chưa có chip "Có dùng mã giảm giá" |
| 10 Cá nhân (sửa) | Lối vào Ngân sách, Hồ sơ, Thiết bị | 10 Cá nhân – bản sửa | **Chưa sửa** | Không có hàng Ngân sách, Đồ đang dùng, Liên kết extension, Nhắc nhở & ngưỡng |
| 02.1, 11.2 … (đánh mã phân cấp, mục 11.2) | — | Vẫn dùng hậu tố chữ (02a, 19a) | **Không áp dụng** | Nhóm chốt 18/10: dùng mã theo Figma; đổi lại nếu giảng viên yêu cầu |

### Danh mục màn mới

| Mã Figma | Màn hình | Cấp | Flow | Khung trạng thái | Ảnh |
|---|---|---|---|---|---|
| 11 v3 | Danh sách mong muốn – v3 | Lồng | F11, F12 | 11a v3 trống, 11f đang chờ | [11 v3](../assets/figma/ver2/11-danh-sach-mong-muon-v3-nhan-gia-nhan-dinh.png) |
| 13 v3 | Chi tiết món – v3 | Lồng | F11, F12 | 13g cảnh báo giá gốc, 13h cần giá | [13 v3](../assets/figma/ver2/13-chi-tiet-mon-v3-gia-nhan-dinh-mua-cho-bo.png) |
| 19 | Lưu món – bottom sheet | Điểm vào (Android Share) | F11 | 19a–19g | [19](../assets/figma/ver2/19-luu-mon-bottom-sheet-tu-nut-chia-se.png) |
| 20 | Lấy giá từ ảnh chụp | Lồng | F11 | 20a, 20b | [20](../assets/figma/ver2/20-lay-gia-tu-anh-chup-buoc-1-chon-anh.png) |
| 21 | Danh sách cho đợt sale | Lồng | F12 | 21a | [21](../assets/figma/ver2/21-danh-sach-cho-dot-sale-11-11.png) |
| 22 | Gói mua | Lồng | — (GĐ5) | 22a, 22b, 22c | [22](../assets/figma/ver2/22-goi-mua-ke-hoach-cho-11-11.png) |
| 23 | So sánh món cùng loại | Lồng | — (GĐ4) | — | [23](../assets/figma/ver2/23-so-sanh-mon-cung-loai-3-tai-nghe.png) |
| 24 | Đồ đang dùng | Lồng | — (GĐ4) | 24a thêm, 24b trống | [24](../assets/figma/ver2/24-do-dang-dung.png) |
| 25 | Liên kết extension | Lồng | F13 | 25c hết hạn, 25f xác nhận | [25](../assets/figma/ver2/25-lien-ket-extension.png) |
| 25b | Thiết bị đã liên kết | Lồng | F13 | 25e dialog hủy liên kết | [25b](../assets/figma/ver2/25b-thiet-bi-da-lien-ket.png) |
| 26 | Nhắc nhở & ngưỡng | Lồng | — | — | [26](../assets/figma/ver2/26-nhac-nho-va-nguong.png) |
| 27 | Hỏi mức hài lòng (dialog trên Trang chủ) | Dialog | — (GĐ4) | 27a | [27](../assets/figma/ver2/27-hoi-muc-hai-long-chua-chon.png) |
| 28 | Decision Card | Lồng | F11, F12 | 28a, 28b, 28c, 29, 29a, 30, 30a | [28](../assets/figma/ver2/28-decision-card-du-du-lieu.png) |
| 30b | Lịch sử giá | Lồng | F12 | — | [30b](../assets/figma/ver2/30b-lich-su-gia-nhieu-lan-ghi.png) |
| 31 | Ngân sách theo nhóm | Lồng | F11 (31c) | 31a, 31b, 31c | [31](../assets/figma/ver2/31-ngan-sach-theo-nhom-chua-dat.png) |
| EXT | Popup extension | Extension | F13 | EXT-1 … EXT-8 | [EXT](../assets/figma/ver2/ext-1-chua-lien-ket.png) |
| X2 | Extension – Trang danh sách | Extension | F13 | X2a lỗi đồng bộ | [X2](../assets/figma/ver2/x2-extension-trang-danh-sach-mong-muon-chi-tren-may.png) |
| X3 | Extension – Decision Card bảng cạnh | Extension | F13 | — | [X3](../assets/figma/ver2/x3-extension-decision-card-bang-canh-side-panel.png) |
| X4 | Extension – Liên kết thiết bị | Extension | F13 | X4 mã sai, X4a thành công | [X4](../assets/figma/ver2/x4-extension-lien-ket-thiet-bi-ma-sai.png) |
| X5 | Extension – Cài đặt & quyền riêng tư | Extension | F13 | — | [X5](../assets/figma/ver2/x5-extension-cai-dat-va-quyen-rieng-tu.png) |

### 19 Lưu món – bottom sheet (từ nút Chia sẻ)
- **Mục đích:** lưu món đang xem trên app Shopee vào Smart Wishlist mà không mở cả app; mục tiêu dưới 20 giây (KPI-01). Thuộc F11.
- **Bố cục & phân cấp thị giác:**
  - **Nền:** app Shopee mờ phía sau ("App Shopee đang mở phía sau"); bottom sheet "Lưu vào danh sách mong muốn".
  - **Món:** tên tự điền "Tai nghe Bluetooth TWS chống ồn" (sửa được) · link gọn `shopee.vn/product/<shopId>/<itemId>`.
  - **Giá:** "Giá đang thấy (không bắt buộc)", ô nhập kèm "₫", nút "Lấy giá từ ảnh chụp" và "Bỏ qua".
  - **Lý do:** "Vì sao muốn mua? (chọn 1, không bắt buộc)" – 8 chip động cơ.
  - **Phụ:** "Nhóm: Công nghệ" · "Ưu tiên ★★★★☆" · "Đợt sale Shopee tiếp theo: 11/11".
  - **Nút chính:** "Lưu".
- **Components:** Bottom sheet, Text field, Motive chip, Button (Primary, Text).
- **Trạng thái:** 19a đang lấy thông tin (ô giá "Đang lấy thông tin…") · 19 đủ thông tin · 19b có giá ghi gần đây ("Giá ghi gần đây: 250.000 ₫ (2 ngày trước). Đúng giá bạn thấy không?" + "Đúng giá này" · "Không, sửa giá") · 19c thiếu giá ("Giá không bắt buộc. Bạn có thể cập nhật khi đến đợt sale.") · 19d món đã lưu ("Đã có trong danh sách… Không tạo bản trùng." + "Cập nhật giá" · "Xem món trong danh sách") · 19e link không phải Shopee ("Hiện chỉ hỗ trợ Shopee. Bạn vẫn có thể lưu thủ công, nhưng app sẽ không nhắc sale." + "Lưu thủ công") · 19f nhắc món tương tự · 19g đã lưu (snackbar "Đã lưu vào danh sách mong muốn · Hoàn tác").
- **Điều hướng:** 19a tự chuyển sang 19 → "Lưu" → 19g → chạm snackbar → 11 v3; "Lấy giá từ ảnh chụp" → 20.
- **Ràng buộc:** giá không bao giờ là 0 ₫ khi trống; lưu được khi offline; mất mạng không báo "đã đồng bộ". **Xung đột câu chữ:** 19f hỏi "Bạn có thật sự cần thêm không?" — trái quy tắc giọng văn (DESIGN.md) và quyết định 1; đặc tả 7.2 gợi ý "Bạn đã ghi có … Bạn muốn thay hay mua thêm?".

### 20 Lấy giá từ ảnh chụp (GĐ4, tùy chọn)
- **Mục đích:** lấy giá từ ảnh chụp màn hình người dùng tự chọn, luôn để người dùng xác nhận. Thuộc F11.
- **Bố cục:** "Bước 1/2 · Chọn ảnh chụp màn hình có giá" + hướng dẫn + "Cho món: …" + "Chọn ảnh" + "App chỉ đọc ảnh bạn chọn" → "Bước 2/2 · Kiểm tra giá nhận được": ảnh có khoanh số, ô "Giá" sửa được, "Số khác trong ảnh · chạm để chọn lại" (chip 250.000 ₫ / 12.000 ₫ / 199.000 ₫), "Dùng giá này" · "Chọn ảnh khác".
- **Components:** App bar/Nested, Button, Filter chip (Default/Selected), Text field.
- **Trạng thái:** 20 chưa chọn ảnh · 20a đã nhận giá · 20b không tìm thấy giá ("Chọn ảnh khác" · "Gõ giá").
- **Ràng buộc:** không tự quét thư viện ảnh; giá chỉ lưu sau khi người dùng xác nhận; phí vận chuyển không tính vào giá.

### 11 Danh sách mong muốn – v3
- **Mục đích:** xem các món đang cân nhắc kèm giá đã ghi và nhãn, lọc theo trạng thái. Thuộc F11, F12.
- **Bố cục:** app bar "Danh sách mong muốn" · 3 chip lọc "Đang cân nhắc (3) · Đã mua (1) · Bỏ qua (0)" · dải "Đợt sale tiếp theo: 11/11" + "Lập kế hoạch mua" · gợi ý "Bạn đang cân nhắc 3 tai nghe. So sánh?" · thẻ món (Wishlist item card v3: tên, giá, ngày, Price tag, Verdict tag, động cơ, ưu tiên, "Lúc lưu … · đã chờ n ngày") · nút "Thêm món".
- **Components:** Filter chip, Wishlist item card v3, Price tag, Verdict tag, Motive chip, Button.
- **Trạng thái:** có dữ liệu · 11a v3 trống ("Chưa có món nào đang cân nhắc." + hướng dẫn dùng Chia sẻ) · 11f món đang trong thời gian chờ ("Đang chờ · còn 4 ngày").
- **Ràng buộc:** giá trong Wishlist không cộng vào đã chi. **Xung đột:** Verdict tag "Hợp lý để mua" trái đặc tả 7.4 (QĐ-N3).

### 13 Chi tiết món – v3
- **Mục đích:** xem giá, lịch sử ghi giá và nhận định của một món, rồi quyết định. Thuộc F11, F12 (chưa nối prototype).
- **Bố cục:** "MÓN ĐANG CÂN NHẮC" · tên · giá + "Giá ghi 2 ngày trước · từ extension" · khối Giá (Lúc lưu / Mới nhất / Thấp nhất, "4 lần ghi giá · extension, bạn nhập, ảnh chụp") · khối nhận định ("Hợp lý để mua… vẫn trong ngân sách Công nghệ (còn 864.000 ₫)", "≈ 9 giờ làm việc · Bạn là người quyết định.") · nút "Mua · ghi khoản mua" · "Chờ đợt sau" · "Bỏ qua".
- **Trạng thái:** 13 v3 · 13g cảnh báo giá gốc ("Giá gốc có thể cao bất thường…") · 13h cần giá ("Chưa có giá trong 3 ngày qua nên app chưa so được với lúc lưu.").
- **Quy đổi giờ làm:** nhóm chốt giữ (18/10); dòng "≈ 9 giờ làm việc" chỉ hiện khi người dùng đã nhập thu nhập mỗi giờ ở 26.
- **Xung đột cần nhóm quyết:** nhãn "Nên chờ" (13g) và "Hợp lý để mua"; nút "Chờ đợt sau" khác nhãn "Chờ" ở 28.

### 28 Decision Card
- **Mục đích:** gom dữ kiện để người dùng tự quyết Mua · Chờ · Bỏ qua. Thuộc F11, F12.
- **Bố cục:** app bar "Cân nhắc trước khi mua" · overline "ĐANG CÂN NHẮC · ĐÃ LƯU 2 NGÀY" · tên món + nhãn "Dữ liệu mô phỏng" · **khối Giá** ("Thấp hơn lúc lưu 10%", "378.000 ₫", "Bạn ghi 18/10 · từ ảnh chụp · Đen. Lúc lưu 420.000 ₫.") · **khối Ngân sách** ("Ngân sách Công nghệ · tháng 10 – Món này chiếm khoảng 44% phần khả dụng (864.000 ₫)." + "Vì sao con số này?") · **khối Đồ đang có** ("Bạn đã ghi có 1 tai nghe đang dùng" + tag "Sắp hỏng") · **khối Thời điểm** ("Đợt 11.11 còn 4 ngày (đã xác nhận)") · 3 nút "Mua · ghi khoản mua" · "Chờ" · "Bỏ qua".
- **Components:** App bar/Nested, Card, Price tag, Condition tag, Button, Bottom sheet.
- **Trạng thái:** 28 đủ dữ liệu · 28a chưa thiết lập ngân sách · 28b giá cũ ("Bạn ghi 12 ngày trước · giá này không dùng để so tăng/giảm", "Xác nhận lại giá" · "Mở link") · 28c có món cùng nhóm ("So sánh 3 món →") · 29 Chờ (bottom sheet "Chờ và xem lại khi nào?": "Sau 3 ngày – Xem lại vào Thứ Tư, 21/10" · "Đến đợt sale 11.11 – nhắc lúc 20:00 tối 10/11"; "Chờ không tạo khoản chi. Bạn vẫn có thể bấm Mua bất cứ lúc nào.") · 29a đã đặt nhắc (snackbar "Đã đặt nhắc xem lại 21/10 · Hoàn tác") · 30, 30a cập nhật giá (bottom sheet).
- **Điều hướng (prototype):** Back · "Vì sao con số này?" → 31c · Mua → 03 · Chờ → 29 → 29a · Bỏ qua → 11 v3 · chạm khối Giá → 30b (F12).
- **Ràng buộc:** ba nút bằng nhau, luôn bấm được; không phần trăm khi chưa có ngân sách; không so giá cũ hơn 3 ngày. **Lỗi prototype:** Mua mở 03 điền sẵn "Bàn phím cơ"; Bỏ qua không có Hoàn tác.

### 30 Cập nhật giá · 30b Lịch sử giá
- **Mục đích:** ghi giá người dùng đang thấy cho một món và xem các lần ghi. Thuộc F12.
- **Bố cục 30 (bottom sheet):** "Giá ghi gần đây · 2 ngày trước – 378.000 ₫ · Đen. Đúng giá bạn đang thấy không?" · "Đúng giá này" · "Lấy giá từ ảnh chụp" · "Gõ giá" · "Giá luôn không bắt buộc. Bạn có thể bỏ qua."
- **Bố cục 30a (bottom sheet):** ô "Giá (₫)" 359.000, "Chỉ dùng số", chip "Loại giá": Giá niêm yết · Sau voucher · Flash Sale; "Phân loại: Đen · ngày ghi: hôm nay"; "Lưu giá".
- **Bố cục 30b:** tóm tắt Lúc lưu 420.000 ₫ · Mới nhất 378.000 ₫ · Thấp nhất 359.000 ₫; danh sách lần ghi (ngày · loại giá · nguồn); chú thích "Chỉ giá ghi trong 3 ngày, cùng phân loại và cùng loại giá mới được dùng để so tăng/giảm… Dữ liệu mô phỏng."
- **Ràng buộc:** giá > 0, số nguyên VND. Loại giá "Sau voucher" **được giữ** (nhóm chốt 18/10, QĐ-N5) nhưng không tính vào "Thấp nhất" và không so với giá niêm yết. **Cần sửa Figma:** 30b đang lấy giá "Sau voucher" 359.000 ₫ làm "Thấp nhất".

### 31 Ngân sách theo nhóm
- **Mục đích:** đặt hạn mức tháng cho từng nhóm hàng và xem phần khả dụng. Lối vào từ 10 Cá nhân **chưa có trên Figma**.
- **Bố cục:** "THÁNG 10/2026 · CÒN 14 NGÀY" · mỗi nhóm: tên, "40.000 ₫ / 1.000.000 ₫", "Còn lại 960.000 ₫ · khả dụng cho danh sách chờ 864.000 ₫" · nhóm chưa đặt "Đặt hạn mức →" · "Vì sao con số này?" · ghi chú "Đã chi chỉ gồm khoản mua bạn đã ghi. Món trong danh sách mong muốn không được cộng vào. Dữ liệu mô phỏng." · "Thêm nhóm".
- **Trạng thái:** 31 chưa đặt ("Ngân sách là mốc tham chiếu bạn tự đặt… App không đồng bộ ngân hàng và không chặn mua.") · 31a đã đặt · 31b đã vượt ("Đã vượt 90.000 ₫ so với mốc bạn đặt. App không chặn mua.", màu trung tính) · 31c bottom sheet công thức (hạn mức − đã chi − dự phòng, "Chưa đủ 30 ngày dữ liệu…").
- **Ràng buộc:** không dùng màu đỏ khi vượt; công thức khớp DESIGN.md mục Ngân sách.

### 21 Danh sách cho đợt sale – 11/11 (GĐ4)
- **Mục đích:** gom các món đang chờ cho một đợt sale đã công bố để người dùng cập nhật giá rồi quyết định. Thuộc F12.
- **Bố cục:** "Mai là 11/11 · 3 món đang chờ" · "Mở từng món trên Shopee, rồi cập nhật giá bạn thấy." · tiến độ "Đã cập nhật giá 1/3 món" · mỗi món: tên, Price tag, "Lúc lưu … · vừa cập nhật / Chưa có giá mới", "Mở trên Shopee" · "Cập nhật giá" · khối "Gợi ý gói mua cho 11/11 – Hiện khi đã có giá mới cho từ 2 món trở lên".
- **Trạng thái:** 21 có món · 21a chưa có món ("Món bạn chọn 'Chờ · đến đợt sale' sẽ hiện ở đây. App sẽ không gửi nhắc khi danh sách trống." + "Mở danh sách mong muốn").
- **Ràng buộc:** không nói món sẽ rẻ hơn. Thông báo đẩy kèm theo (khung "Thông báo đẩy – 3 mẫu") có quy tắc in trên frame: không emoji, không "!", không gửi 22:00–08:00 và lúc 0h, tối đa 3 thông báo mỗi ngày. **Cần chỉnh:** câu "có thể được giảm giá" trong thông báo.

### 22 Gói mua (GĐ5) · 23 So sánh món cùng loại (GĐ4)
- **22:** ba phương án "Cân bằng · Cần thiết trước · Giữ lại nhiều hơn"; mỗi gói có danh sách món, tổng, "Thấp hơn tổng giá lúc lưu …", "Còn lại nhóm Công nghệ … (đã chừa 10% an toàn)", câu chốt "Đây là gợi ý. Bạn quyết định món nào sẽ mua." · 22c chưa đủ dữ liệu ("Cập nhật giá cho ít nhất 2 món…").
- **23:** bảng 3 tai nghe (giá hiện tại, động cơ, ưu tiên, đã chờ, nhận định) · "Giữ món phù hợp nhất và bỏ 2 món còn lại?" · "Giữ 1, bỏ 2" · "Để sau".
- **Xung đột cần quyết:** đặc tả 7.5 chỉ cho gói mua chạy khi người dùng yêu cầu và không hiện điểm thô; 22 nhắc "điểm phù hợp cao nhất"; 22a hoãn món theo động cơ ("Các món lưu vì Khuyến mãi, Cảm xúc, Quảng cáo được hoãn"); 22b và 23 dùng "Tiền đã giữ lại" (đặc tả 7.8 đã đổi thành chỉ số trung tính); 23 gợi ý "bỏ 2 món" là thúc đẩy một lựa chọn.

### 24 Đồ đang dùng (GĐ4) · 26 Nhắc nhở & ngưỡng · 27 Hỏi mức hài lòng (GĐ4)
- **24:** nhóm theo loại (Tai nghe 2 món, Áo thun 5 món, Giày 3 món), mỗi đồ có tên, ghi chú, Condition tag (Tốt · Sắp hỏng · Đã hỏng), số lượng · 24a form thêm đồ (tên, loại, tình trạng, số lượng, ghi chú) · 24b trống ("Ghi lại đồ bạn đang có để app nhận ra khi bạn định mua trùng.").
- **26:** "Mức nhắc sale" (Chỉ đợt lớn / Mọi đợt), "Nhắc lúc 20:00 tối hôm trước. Không nhắc lúc 0h.", "Thời gian chờ − 7 ngày +", "Biên độ an toàn 10% (0–30%)", "Thu nhập mỗi giờ (không bắt buộc)" để quy đổi giá ra giờ làm.
- **27:** dialog trên Trang chủ "Bạn có hài lòng với tai nghe đã mua 7 ngày trước?" (1–5) + "Bỏ qua" · 27a cảm ơn kèm nhận xét theo động cơ.
- **Xung đột cần quyết:** 26 mặc định 7 ngày (đặc tả: 3 ngày, chỉnh 0–14); câu ở 26 "Trước khi gợi ý mua, món mới lưu ở trạng thái 'Đang chờ'" mâu thuẫn với "Chờ không phải trạng thái" và "app không gợi ý mua"; "Thu nhập mỗi giờ" và quy đổi giờ làm không có trong đặc tả nhưng nhóm chốt giữ (18/10), luôn không bắt buộc. Trang chủ ở 27 có thẻ "Tiền đã giữ lại · 1.240.000 ₫ · Nhờ chờ và bỏ bớt" (đặc tả 7.8). Tag "Đã hỏng" dùng màu error; chữ trên các tag cỡ 12 sp (quy tắc chữ nội dung ≥ 14 sp).

### 25 Liên kết extension · 25b Thiết bị đã liên kết
- **Mục đích:** ghép extension trên máy tính với tài khoản bằng mã 6 số, có xác nhận trên điện thoại; xem và hủy thiết bị. Thuộc F13.
- **Bố cục 25:** mô tả · "Mã liên kết 482 913" · "Hết hạn sau 04:59" · "Mã dùng một lần. Không chia sẻ mã cho người khác." · 3 bước cài và nhập mã · "Thiết bị đã liên kết (1)" · "Tạo mã mới".
- **Trạng thái:** 25c mã hết hạn · 25f dialog "Liên kết với Chrome trên Windows? Một máy tính vừa nhập mã 482 913 lúc 21:05. Nếu không phải bạn, chọn Từ chối và tạo mã mới." (Từ chối · Đồng ý) · 25b danh sách ("Chrome – Windows · dùng lần cuối hôm nay · liên kết 16/10", "Huỷ liên kết") · 25e dialog overlay "Huỷ liên kết Chrome – Windows?" (Giữ liên kết · Huỷ liên kết).
- **Ràng buộc:** lỗi mã không lộ tài khoản; hết hạn 5 phút; hủy liên kết không xóa dữ liệu chưa đồng bộ trên máy tính. **Thiếu:** lối vào từ 10 Cá nhân.

### EXT Popup extension (EXT-1 … EXT-8, 360 × 560)
- **Mục đích:** lưu nhanh món đang xem trên shopee.vn khi người dùng bấm icon. Thuộc F13 (chưa nối prototype).
- **Trạng thái:** EXT-1 chưa liên kết ("Nhập mã 6 số từ app…" + "Liên kết") · EXT-2 không phải trang sản phẩm ("Mở một sản phẩm trên shopee.vn để lưu") · EXT-3 đang đọc trang · EXT-4 đủ thông tin (tên, "Phân loại: Đen", 225.000 ₫, 8 động cơ, "Nhóm ngân sách: Công nghệ", "Lưu vào danh sách") · EXT-5 thiếu giá ("Không đọc được giá trên trang. Bạn có thể bỏ qua.") · EXT-6 đã lưu trước đó (lúc lưu / trên trang bây giờ, "Cập nhật giá" · "Mở app") · EXT-7 đã lưu · EXT-8 liên kết bị hủy ("Liên kết đã bị huỷ, vui lòng nhập mã mới.").
- **Xung đột:** EXT-1 không cho lưu khi chưa liên kết, trái đặc tả 5.2 (chưa liên kết chỉ là dải thông báo nhỏ, không chặn lưu) và quyết định 21 (extension không cần đăng nhập để lưu). EXT-4 hiện giá đọc từ trang; theo đặc tả, đọc giá tự động (EX-10) là thử nghiệm có cổng, giá đọc được phải ở trạng thái "chưa xác nhận". Chân popup hiện tên tài khoản ("Đang lưu vào tài khoản: Tâm").

### X2 – X5 Trang extension (960 × 640)
- **X2 Trang danh sách:** menu trái (Danh sách mong muốn · Liên kết thiết bị · Cài đặt & quyền riêng tư) · dải trạng thái "Chỉ trên máy · chưa liên kết – Món lưu trên máy này sẽ được đồng bộ sau khi bạn liên kết với app Android." · danh sách món (ngày lưu, ngày ghi giá, Price tag) · "Liên kết với app" · "Xuất dữ liệu" · "Dữ liệu mô phỏng". **X2a:** "Đã liên kết · Chrome – Windows" + "Chưa đồng bộ được 1 món vì mất kết nối. Món vẫn được giữ trên máy này." + "Thử lại"; món "Chờ đồng bộ".
- **X3 Decision Card bảng cạnh:** cạnh trang Shopee minh họa ("không phải dữ liệu thật"): giá, ngân sách, đợt sale, nút "Mua · mở form trên điện thoại" · "Chờ" · "Bỏ qua", "Bạn luôn là người quyết định."
- **X4 Liên kết thiết bị:** ô 6 số; X4 mã sai ("Mã không đúng hoặc đã hết hạn. Bạn còn 3 lần thử. Có thể tạo mã mới trên app.") · X4a thành công ("2 món đang chờ đã được đồng bộ").
- **X5 Cài đặt & quyền riêng tư:** "Extension đọc gì? Chỉ đọc trang sản phẩm Shopee đang mở, và chỉ khi bạn bấm icon… Không đọc giỏ hàng, đơn mua, kho voucher hay cookie đăng nhập." · công tắc "Đồng bộ với app Android", "Lưu ảnh sản phẩm" · "Xuất dữ liệu (JSON)" · "Xoá dữ liệu trên máy này".
- **Ràng buộc:** bàn phím Tab / Enter / Esc dùng được, phóng to 200% không mất nội dung (TC-19, chưa kiểm).
