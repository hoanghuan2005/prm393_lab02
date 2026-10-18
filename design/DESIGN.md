# DESIGN.md — Design brief và quy ước thiết kế

Tài liệu gốc cho cả prompt Google Stitch và file Figma. Mục "Lịch sử cập nhật" ở cuối ghi lại những gì được bổ sung sau các vòng tinh chỉnh.

## Sản phẩm
Why I Buy? – **Smart Shopping Companion**: trợ lý mua sắm có ý thức trên Android. Giúp người trẻ
lưu món đang thích, cân nhắc với ngân sách tự đặt, đồ đang có và thời điểm sale, tự chọn
**Mua · Chờ · Bỏ qua**, rồi nhìn lại vì sao mình mua. Lấy cảm hứng từ "The Psychology of Money"
(Morgan Housel). Thông điệp: "Hiểu trước khi thay đổi".

*Cập nhật 18/10/2026 theo đặc tả hợp nhất v1.0 (17/10). Bản đầu (đến 14/10) chỉ gồm ghi khoản mua
kèm động cơ và nhìn lại; các quy tắc của bản đầu vẫn áp dụng cho Flow 1–10 trừ khi mục
"Smart Shopping Companion" bên dưới ghi khác.*

## Người dùng
Persona chính (proto-persona, giả định chưa kiểm chứng – xem `ux/persona.md`): Nguyễn Hải Nam,
22 tuổi, sinh viên năm cuối CNTT kiêm thực tập, xem Shopee trên Android, hay gặp flash sale buổi tối,
dùng điện thoại một tay, cận 2 độ, ngại nhập nhiều và không muốn bị phán xét.
Persona phụ: P3 Huy (ngân sách, so sánh, chờ sale), P2 Linh (nhìn lại sau mua), P4 Mai (bị gián đoạn).

## Nền tảng
Android, khung 360 × 800 dp, Material Design 3, light theme. Kênh phụ: Chrome Extension
(popup 360 × 560 px, trang extension 960 × 640 px trên Figma).

## Tone & giọng văn
- Bình tĩnh, ấm áp, trung lập, không phán xét.
- Không cảnh báo đỏ, không chấm điểm người dùng. Ngân sách là mốc tham chiếu người dùng tự đặt; khi
  vượt chỉ ghi chữ trung tính ("Đã vượt 90.000 ₫ so với mốc bạn đặt. App không chặn mua."), không tô đỏ.
- Insight viết dạng quan sát, chỉ dùng số liệu lấy từ dữ liệu người dùng đã ghi: "5 trong 15 khoản tháng này gắn với Khuyến mãi."
- Không thêm thẻ, câu nhắc nhở, khen ngợi hay suy diễn tâm lý ("Bạn có đang thật sự cần?", "Bạn nhận diện được… kịp thời", "Tâm trí bạn…").
- Không dùng ảnh minh họa trang trí.
- Toàn bộ chữ trên giao diện bằng tiếng Việt có đủ dấu, tiền tệ VND (45.000 ₫).

## Từ vựng thống nhất
| Khái niệm | Dùng | Không dùng |
|---|---|---|
| Hành động chính | "Ghi khoản mua" (nút ở Trang chủ, tiêu đề cả 2 bước) | "Nhập chi tiêu mới", "Ghi nhận chi tiêu", "Ghi chép" |
| Lý do mua | "động cơ" | "động lực", "lý do kích hoạt" |
| Một lần mua | "khoản mua" | "giao dịch", "khoản chi" (trên giao diện) |
| Xưng hô | "bạn" | gọi tên người dùng, ngôi thứ ba |
| Danh sách món muốn mua | "Danh sách mong muốn" | "Wishlist", "giỏ hàng" (trên giao diện) |
| Một mục trong danh sách | "món" | "sản phẩm", "đơn hàng" |
| Không mua món nữa | "Bỏ qua" / "Không mua nữa" | "Xóa", "Hủy món" |
| Trạng thái | "Đang cân nhắc" · "Đã mua" · "Bỏ qua" | "Hạ nhiệt", "Đang tĩnh tâm" |
| Ba quyết định (từ 18/10) | **"Mua" · "Chờ" · "Bỏ qua"**, ba nút bình đẳng | "Vẫn mua", "Để sau", "Để mình nghĩ thêm", "Mua ngay" |
| Chờ | Hành động, **không phải trạng thái**: món vẫn Đang cân nhắc, có thêm ngày xem lại ("Đang chờ · xem lại 21/10") | "Khoảng lặng", đếm ngược bắt buộc |
| Giá của món chưa mua | "giá đã ghi", "giá lúc lưu", "giá ghi gần đây", luôn kèm ngày | "giá hiện tại", "giá realtime" |
| Số tiền khi mua | "giá thực trả" / "số tiền thực chi" | "giá sau voucher" (như giá dùng chung) |
| Ngân sách | "ngân sách nhóm", "hạn mức tháng", "phần khả dụng", "mốc bạn đặt" | "số dư", "bạn không đủ tiền" |
| Đợt sale | "đợt sale đã công bố", "đợt sale tiếp theo: 11/11" | "sắp giảm giá", "chắc chắn rẻ hơn" |
| Món đã quyết định không mua | "giá trị món đã quyết định không mua" (GĐ4, tùy chọn) | "tiền đã giữ lại", "tiết kiệm được" |

- **8 động cơ** (đúng tên, đúng thứ tự): Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Không dùng "Giảm giá". Mỗi khoản mua chỉ có **một** chip động cơ, không thêm nhãn phụ.
- **Tiêu đề app bar** (chỉ viết hoa chữ đầu): Trang chủ · Ghi khoản mua (Bước 1/2, Bước 2/2) · Chi tiết khoản mua · Lịch sử · Mô hình · Góc nhìn · Chiêm nghiệm tháng · Cá nhân.

## Phạm vi
- **Trong phạm vi:** ghi khoản mua (số tiền, tên món, thời điểm, động cơ, ghi chú), xem/sửa/xóa, lọc theo động cơ, mô hình theo động cơ và khung giờ, góc nhìn, chiêm nghiệm tháng, nhắc nhở, xuất và xóa dữ liệu.
  **Thêm từ 18/10:** Smart Wishlist lưu qua Android Share / nhập tay / Chrome Extension; Decision Card; Mua · Chờ · Bỏ qua; ngân sách theo nhóm hàng (tùy chọn); nhắc xem lại; giá đã ghi có nguồn và ngày; ghép extension bằng mã 6 số. Các phần GĐ4–GĐ5 (lịch sale, lịch sử giá, so sánh, đồ đang dùng, OCR, gói mua, AI diễn giải) được thiết kế để minh họa lộ trình.
- **Ngoài phạm vi:** cảnh báo đỏ và chặn mua khi vượt ngân sách, chấm điểm người dùng, lời khuyên "nên / không nên mua", "khoảng hạ nhiệt" và đếm ngược bắt buộc, ảnh hóa đơn, danh mục chi tiêu kiểu sổ thu chi, so sánh với người khác, chuỗi ngày (streak), mã giao dịch, đồng bộ ngân hàng, cào dữ liệu Shopee, đọc tài khoản / giỏ hàng / kho voucher Shopee, tự áp mã giảm giá, giá thời gian thực, dự đoán giá, tìm shop rẻ nhất.
- *[Đã thay thế 18/10]* Bản trước ghi "ngân sách" là ngoài phạm vi. Theo góp ý của giảng viên (04:40 trong bản ghi) và đặc tả mục 1.5 #6, ngân sách được đưa vào phạm vi dưới dạng tùy chọn, không cảnh báo đỏ.

## Lưu trữ dữ liệu
Dữ liệu được lưu trên máy và đồng bộ với tài khoản của người dùng khi có mạng. Mất mạng khi lưu → vẫn lưu trên máy và báo "Đã lưu trên máy. Sẽ đồng bộ khi có mạng." Màn Mô hình cần mạng để tổng hợp, nên có trạng thái lỗi "Không tải được mô hình".

## Dữ liệu mẫu (dùng thống nhất trên mọi màn hình)
Hôm nay là Chủ nhật 11/10/2026 (tuần 41, từ 05/10 đến 11/10).

| Khoản mua | Số tiền | Động cơ | Thời điểm | Ghi chú |
|---|---|---|---|---|
| Trà sữa nướng | 45.000 ₫ | Cảm xúc | Hôm nay 23:10 | Khoản đang ghi ở Flow 1 |
| Cơm tấm | 40.000 ₫ | Tiện lợi | Hôm nay 12:15 | |
| Tai nghe Bluetooth | 389.000 ₫ | Khuyến mãi | Hôm qua (10/10) 23:40 | Ghi chú "Thấy flash sale lúc lướt TikTok"; khoản bị xóa ở Flow 3 |
| Sách "Tâm lý học về tiền" | 159.000 ₫ | Mong muốn | 08/10 20:05 | |
| Áo thun | 129.000 ₫ | Khuyến mãi | 07/10 23:55 | |
| Vé xe buýt tháng | 100.000 ₫ | Nhu cầu | 06/10 07:30 | |

- **Trang chủ trước khi lưu:** 817.000 ₫ · 5 khoản · Nhiều nhất: Khuyến mãi (2/5) · Động cơ chính: 40% do Khuyến mãi. Gần đây: Cơm tấm, Tai nghe Bluetooth, Sách.
- **Trang chủ sau khi lưu:** 862.000 ₫ · 6 khoản · Nhiều nhất: Khuyến mãi (2/6) · Động cơ chính: 33% do Khuyến mãi. Gần đây: Trà sữa nướng, Cơm tấm, Tai nghe Bluetooth.
- **Lịch sử:** 6 khoản; nhóm "Hôm nay, 11/10/2026" gồm Trà sữa nướng và Cơm tấm, tổng 85.000 ₫. Sau khi xóa Tai nghe Bluetooth còn 5 khoản.
- **Mô hình, tháng 10:** 15 khoản — Khuyến mãi 5 (33%), Cảm xúc 4 (27%), Tiện lợi 2 (13%), Nhu cầu 2 (13%), Mong muốn 1 (7%), Ảnh hưởng MXH 1 (7%), Quảng cáo 0, Khác 0.
- **Khung giờ:** Sáng 05–11h (2) · Trưa 11–14h (3) · Chiều 14–18h (2) · Tối 18–05h (8).
- **Góc nhìn (3 câu):** "5 trong 15 khoản tháng này gắn với Khuyến mãi." · "8 trong 15 khoản được ghi sau 18:00." · "Cả 4 khoản Cảm xúc đều được ghi sau 22:00."

### Dữ liệu mẫu – Danh sách mong muốn (Flow 6)

| Món | Giá dự kiến | Động cơ | Ngày thêm | Ghi chú | Trạng thái |
|---|---|---|---|---|---|
| Bàn phím cơ | 650.000 ₫ | Khuyến mãi | 09/10 | "Thấy review trên TikTok, đang có giảm giá." | Đang cân nhắc → Bỏ qua (11c) hoặc Đã mua (11e) |
| Áo khoác | 420.000 ₫ | Mong muốn | 10/10 | "Không chắc có thực sự cần hay không." | Đang cân nhắc |
| Chuột công thái học | 520.000 ₫ | Tiện lợi | 11/10 | "Cổ tay hay mỏi khi code buổi tối." | Món thêm mới ở Flow 6 |
| Bình giữ nhiệt | 180.000 ₫ | Nhu cầu | 05/10 (đã mua) | "Bình cũ bị nứt nắp." | Đã mua |

Giá dự kiến không phải tiền đã chi: không cộng vào tổng tuần, không có câu "tiết kiệm được X đồng".

## Màu
| Token | Giá trị | Dùng cho |
|---|---|---|
| primary | #2E4A9E | Nút chính, tab được chọn |
| on-primary | #FFFFFF | Chữ trên nút chính |
| primary-container | #E3E8F7 | Nền phần tử được chọn |
| background | #F5F6F2 | Nền màn hình |
| surface | #FFFFFF | Card, ô nhập |
| on-surface | #1A2320 | Chữ chính |
| on-surface-variant | #545E59 | Chữ phụ |
| surface-container | #E8F0EB | Nền ô nhập (tonal), chip mặc định, khối tóm tắt, nền bàn phím số, đoạn trống của thanh độ mạnh mật khẩu |
| outline | #8A918A | Viền ô nhập trên thẻ trắng, chip "Bỏ qua", viền switch tắt |
| outline-strong | #7A817B | Viền ô nhập đặt thẳng trên nền #F5F6F2 (≥ 3 : 1, PB-5) |
| error | #B3261E | Lỗi nhập liệu, hành động xóa |
| error-container | #F9DEDC | Nền ô nhập khi lỗi, vòng tròn icon trong dialog nguy hiểm |

Màu động cơ (nền / chữ):
| Động cơ | Nền | Chữ |
|---|---|---|
| Nhu cầu | #E3EEE8 | #1F4D3A |
| Mong muốn | #F3E6F3 | #5E2A5E |
| Khuyến mãi | #FFF3C4 | #6B5200 |
| Ảnh hưởng MXH | #E1EEF8 | #154466 |
| Quảng cáo | #EDE7F8 | #3F2C78 |
| Cảm xúc | #FBEBDC | #7A3A05 |
| Tiện lợi | #E2F1F1 | #135656 |
| Khác | #ECEEE8 | #3E4743 |

## Typography (Be Vietnam Pro)
| Style | Cỡ / dòng (sp) | Độ đậm | Dùng cho |
|---|---|---|---|
| Display | 28 / 36 | 700 | Tiêu đề lớn (Đăng nhập, Xin quyền thông báo), số tiền |
| Title | 20 / 28 | 600 | Tiêu đề app bar, tiêu đề dialog |
| Subtitle | 16 / 24 | 600 | Tiêu đề thẻ |
| Body | 16 / 24 | 400 | Nội dung chính |
| Body Small | 14 / 20 | 400 | Mô tả phụ, ghi chú, dòng lỗi |
| Label | 14 / 20 | 500 | Nhãn ô nhập, link, chữ trên nút |
| Overline | 14 / 20 | 500, viết hoa | Tiêu đề nhóm cài đặt (CÀI ĐẶT NHẮC NHỞ…) |
| Caption | 12 / 16 | 500 | **Chỉ** nhãn thanh tab và mốc thời gian |
| Caption Strong | 12 / 16 | 700 | Nhãn tab đang chọn |

## Khoảng cách, bo góc, elevation
- Spacing: 4 · 8 · 12 · 16 · 24 · 32 dp; lề màn hình 16 dp.
- Bo góc: 8 (nhỏ) · 12 (ô nhập, thẻ động cơ) · 16 (card) · 24 (dialog) · full (nút, chip).
- Elevation: 1 = bóng nhẹ cho card · 2 = dialog, snackbar.

## Quy tắc component
- Mỗi màn hình có **tối đa một** nút chính (filled, primary, cao 56 dp), ghim ở thanh đáy
  ngay trên thanh điều hướng vì Nam thao tác một tay. Màn chỉ để xem (Lịch sử, Mô hình, Cá nhân)
  có thể không có nút chính. Hành động phụ dùng nút Tonal (nền nhạt), Text hoặc viền, không tô đặc.
  Nội dung cuộn phía sau, nút luôn hiện trong khung 800 dp.
- Vùng chạm tối thiểu 48 × 48 dp; chữ nội dung tối thiểu 14 sp.
- Độ tương phản chữ tối thiểu 4.5:1 (Nam cận và hay dùng trong phòng tối).
- Động cơ luôn hiển thị **icon + tên**, không chỉ dùng màu.
- Biểu đồ luôn có nhãn chữ và phần trăm.
- Thanh điều hướng dưới 5 tab: Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân.
  Tab được chọn có nền pill + chữ đậm, không chỉ đổi màu.
- Lỗi nhập liệu hiển thị ngay dưới ô nhập, kèm icon và cách sửa.
- Hành động xóa luôn có dialog xác nhận (nêu tên khoản mua) và snackbar hoàn tác 5 giây.
- Sau khi lưu có snackbar "Đã lưu “…”" kèm "Hoàn tác" 5 giây (cùng component với snackbar xóa).
- Thẻ động cơ chỉ gồm icon + tên (không có dòng mô tả); thẻ được chọn có nền, viền và dấu tích.
- Tên món được xuống tối đa 2 dòng, không cắt bằng "…".
- Mỗi màn hình có dữ liệu cần thiết kế đủ trạng thái: loading, trống, lỗi. Mỗi trạng thái là
  một khung riêng, giống hệt màn gốc (cùng app bar, thẻ, thứ tự, tab đang chọn), chỉ khác phần
  thay đổi; trong Figma dùng chung component.
- Danh sách mong muốn không có thời gian chờ bắt buộc, đồng hồ đếm ngược hay nhật ký nhiều bước; nút "Ghi khoản mua" không bao giờ bị khóa vì thời gian.
- Trạng thái món luôn là chip icon + chữ (Đang cân nhắc: bookmark · Đã mua: check-circle · Bỏ qua: archive).
- "Không mua nữa" không phải hành động phá hủy: dialog dùng nút primary (không dùng màu error), và có snackbar hoàn tác 5 giây.
- Tên món xuống tối đa 2 dòng; chỉ khi vượt 2 dòng mới cắt bằng "…" (thẻ Danh sách mong muốn).

## Smart Shopping Companion – quy tắc thiết kế (18/10/2026)

Nguồn: đặc tả hợp nhất v1.0 mục 1.3, 4, 6.5, 7, 8, 10.2. Token màu, chữ, khoảng cách, bo góc giữ nguyên như các mục trên; không thêm màu cảnh báo.

### Nguyên tắc
1. **Người dùng luôn là người quyết định.** Quy tắc và AI chỉ nêu dữ kiện, nói rõ khi thiếu dữ liệu, không nói "nên" hay "không nên mua". Ba nút Mua · Chờ · Bỏ qua **bằng nhau về độ nổi bật**, luôn hiện và luôn bấm được.
2. **Wishlist ≠ chi tiêu.** Chỉ khoản mua đã lưu (giá thực trả) mới được cộng vào "đã chi". "Mua" là ý định; món chỉ thành Đã mua khi khoản mua lưu thành công. Chờ và Bỏ qua không tạo khoản chi.
3. **Không thúc ép mua.** Không chặn mua, không đếm ngược bắt buộc, không "Mua ngay kẻo lỡ", không đỏ làm cảnh báo đạo đức. Thời gian cân nhắc **gợi ý mặc định 3 ngày** (chỉnh 0–14), không khóa nút Mua, bỏ qua với động cơ Nhu cầu.
4. **Mọi mức giá có nguồn, ngày, phân loại và trạng thái xác nhận.** Không hứa món sẽ giảm, không quảng bá giá thời gian thực.
5. **Thu thập tối thiểu, minh bạch.** Không cào Shopee, không đọc cookie, giỏ hàng, kho voucher hay đơn mua. Người dùng xuất và xóa được dữ liệu.

### Smart Wishlist
- Ba trạng thái Đang cân nhắc · Đã mua · Bỏ qua; lọc theo trạng thái; Hoàn tác 5 giây khi Bỏ qua.
- Mỗi thẻ món hiện: tên (tối đa 2 dòng), giá đã ghi kèm ngày, nhãn so giá (Price tag), động cơ, ưu tiên (sao), "Lúc lưu … · đã chờ n ngày".
- Nhãn nguồn lưu: chia sẻ từ Shopee · máy tính (extension) · nhập tay. Giá luôn **không bắt buộc**; không bao giờ điền 0 ₫ thay cho "chưa có giá".
- Món trùng (cùng sản phẩm, cùng phân loại) không tạo bản mới, chỉ "Cập nhật giá" (19d).

### Ngân sách theo nhóm
- Nhóm ngân sách là **nhóm hàng**, tách khỏi 8 động cơ. Mặc định 6 nhóm: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác; người dùng đổi tên, thêm, bớt.
- Hạn mức tháng do người dùng tự khai, bỏ qua được. **Không đồng bộ ngân hàng.**
- Đã chi = tổng giá thực trả của khoản mua đã ghi trong nhóm, trong tháng. Còn lại = hạn mức − đã chi.
- Phần khả dụng cho Wishlist: `khaDung = max(0, conLai − duPhong) × (1 − bienDo)`; biên độ an toàn mặc định 10%. Người mới chưa đủ 30 ngày dữ liệu: `duPhong = 0` kèm ghi chú.
- Luôn có "Vì sao con số này?" hiện đúng công thức với số của người dùng (31c).
- Thanh ngân sách dùng màu trung tính; "đã vượt" là chữ, không tô đỏ (31b).

### Decision Card
| Khối | Nội dung | Khi thiếu dữ liệu |
|---|---|---|
| Giá | Giá mới nhất + nguồn + ngày + phân loại; so với giá lúc lưu nếu "so được" | "Cần cập nhật giá" + Xác nhận lại giá · Mở link (28b) |
| Ngân sách | "Món này chiếm khoảng 44% phần khả dụng (864.000 ₫)" | "Chưa thiết lập ngân sách… App không tính phần trăm khi chưa có hạn mức" + Thiết lập · Để sau (28a) |
| Đồ đang có | "Bạn đã ghi có 1 tai nghe đang dùng" | Ẩn khối |
| Món cùng nhóm | "Bạn đang cân nhắc thêm 2 món cùng nhóm" + So sánh | Ẩn khối |
| Thời điểm | "Đợt 11.11 còn 4 ngày (đã xác nhận)"; chỉ đợt đã công bố | Ẩn khối |
| Quyết định | Mua (ghi khoản mua điền sẵn) · Chờ (3 ngày · đến đợt sale · tự chọn) · Bỏ qua (Hoàn tác 5 giây) | Luôn hiện và luôn bấm được |

**Nhãn tóm tắt** (Rules Engine v1, đặc tả 7.4): chỉ dùng các nhãn trung tính "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Có thể cân nhắc bỏ", "Trong ngân sách", "Chưa đủ dữ liệu". **Không có nhãn "Nên mua", "Nên chờ", "Hợp lý để mua".** *(Figma 18/10 đang dùng "Hợp lý để mua", "Nên chờ", "Cân nhắc bỏ" ở Verdict tag – xem `design-decisions.md` QĐ-N3.)*

### Giá, voucher và dữ liệu
**Ba loại giá** (đặc tả 10.2):

| Loại | Lưu ở | Dùng cho | Không dùng cho |
|---|---|---|---|
| Giá tham khảo | Bản ghi giá (PriceSnapshot) mới nhất | Decision Card, so sánh, thông báo | Không cộng vào chi tiêu |
| Giá lịch sử | Chuỗi bản ghi giá | Lịch sử giá, "thấp nhất đã ghi" | Không coi là giá hiện tại |
| Giá thực trả | Khoản mua (đã trừ voucher, không gồm phí vận chuyển) | Đã chi, ngân sách, Lịch sử, Mô hình | — |

**So sánh giá:**
- Lõi là giá **người dùng ghi hoặc xác nhận**. Mỗi bản ghi có: loại giá (giá đơn · khoảng giá · Flash Sale), phân loại (ví dụ "Đen"), nguồn (bạn gõ · chia sẻ · ảnh chụp · extension), ngày ghi, trạng thái xác nhận. Giá tự động ở trạng thái "chưa xác nhận" cho tới khi người dùng xác nhận một chạm.
- **Độ mới:** ≤ 3 ngày là "mới" (được dùng để so, thông báo, Decision Card); 4–7 ngày hiện kèm ngày; > 7 ngày là "cũ", hiện nhãn ngày và nút "Xác nhận lại".
- **Chỉ so khi "so được":** cùng loại giá (Flash Sale chỉ so với Flash Sale), cùng phân loại, giá đơn không so với khoảng giá.
- Đây là **so lịch sử giá của cùng một món**, không phải tìm shop rẻ nhất.
- **Dữ liệu bất thường phải kiểm tra, không tự loại:** không tự xem mọi mức chênh hơn 30% là giá sai (Flash Sale có thể chênh nhiều). Ngưỡng 30% chỉ áp cho giá người khác ghi ở GĐ5.
- **Giá người khác ghi (giá cộng đồng):** chỉ là định hướng GĐ5 – ẩn danh, có đồng ý, cùng phân loại, ≤ 3 ngày, ≥ 2 người. Chỉ hiện nhãn tham khảo, người dùng phải xác nhận. **Không gửi thông báo đẩy dựa trên giá cộng đồng.**

**Voucher:**
- App **không đọc** tài khoản hay kho voucher Shopee, **không tự áp mã**, không có ô nhập mã.
- Khi Mua: ghi **giá thực trả** + chip **"Có dùng mã giảm giá"**. App chỉ nói "bạn trả thấp hơn giá lúc lưu X%", không đánh giá người dùng đã dùng mã tối ưu chưa.
- **Nhóm chốt 18/10 (QĐ-N5):** lịch sử giá **có** loại giá "Sau voucher" (Figma 30a, 30b), bên cạnh Giá niêm yết và Flash Sale. Giá sau voucher là giá **cá nhân**: hiển thị song song với giá niêm yết; **không** tính vào "Thấp nhất", **không** dùng để so tăng/giảm với giá niêm yết, **không** dùng làm mức giá chung và **không bao giờ** đưa vào giá cộng đồng. Đây là điểm khác với đặc tả hợp nhất 6.5 (chỉ có giá đơn · khoảng giá · Flash Sale), theo đề xuất trong báo cáo của Khoa.
- Gợi ý voucher nâng cao là roadmap, chưa hứa hoạt động.

**Quy đổi giá ra giờ làm (nhóm chốt giữ, 18/10):** người dùng có thể tự nhập "Thu nhập mỗi giờ (không bắt buộc)" ở 26 Nhắc nhở & ngưỡng; khi có, Chi tiết món (13 v3) hiện thêm dòng trung tính "≈ 9 giờ làm việc · Bạn là người quyết định." Không nhập thì ẩn dòng này. Con số chỉ là phép chia giá cho thu nhập mỗi giờ người dùng tự khai, không suy đoán thu nhập, không đánh giá "đắt" hay "rẻ". Không có trong đặc tả hợp nhất v1.0 – là quyết định bổ sung của nhóm.

**Kiến trúc** (đặc tả mục 3, 6): app Flutter là sản phẩm chính; Chrome Extension là kênh phụ; backend đề xuất Firebase. Không dựa vào cào dữ liệu, API Shopee chưa được cấp quyền hay dữ liệu giả. Rules Engine tính con số; AI chỉ diễn giải ở giai đoạn sau và không được tạo số mới.

### Ngôn ngữ (microcopy)
- **Dùng:** "Bạn đã ghi…", "Giá ghi ngày…", "Có thể…", "Chưa đủ dữ liệu", "Đợt sale đã công bố", "Bạn là người quyết định".
- **Tránh:** "Nên mua", "Nên chờ", "Không nên mua", "Mua ngay kẻo lỡ", "Chắc chắn giảm", "Giá đang realtime", "Tiết kiệm được" / "Tiền đã giữ lại" (khi chỉ là bỏ món), "Bạn có thật sự cần không?".
- Thông báo đẩy: không emoji, không dấu "!", không gửi 22:00–08:00 và lúc 0:00; tối đa 1 thông báo mỗi món mỗi ngày, 3 mỗi người mỗi ngày; gom nhiều món vào một thông báo.

### Trạng thái bắt buộc cho màn mới
- **Thiếu dữ liệu:** thiếu giá (19c, 13h, 28b), thiếu ngân sách (28a, 31), chưa có món (11a v3, 21a, 24b), chưa đủ dữ liệu cho gói mua (22c).
- **Lỗi:** link không phải Shopee (19e), OCR không đọc được (20b), mã ghép sai / hết hạn (X4, 25c), liên kết bị hủy (EXT-8).
- **Offline và đồng bộ:** "Đã lưu trên máy; sẽ đồng bộ khi có mạng"; extension "Chỉ trên máy · chưa liên kết" (X2), "Chưa đồng bộ được 1 món… Thử lại" (X2a). Chỉ báo "đã đồng bộ" khi server xác nhận.
- **Đang tải → kết quả:** 19a → 19; EXT-3 "Đang đọc trang…".
- Mọi trạng thái có icon và chữ, không chỉ dùng màu. Mọi lỗi có lối ra và không làm mất thông tin đã nhập.

### Dữ liệu mô phỏng cho màn mới
Mọi màn có số liệu giá, ngân sách, mã ghép phải có nhãn **"Dữ liệu mô phỏng"**. Đặc tả mục 11.5 đề xuất một bộ dữ liệu dùng chung: tai nghe Bluetooth 420.000 ₫ (Công nghệ, Khuyến mãi), áo Lovito 250.000 ₫ (Thời trang, Đen – M), kính cường lực 180.000 ₫; ngân sách Công nghệ 1.000.000 ₫/tháng; đợt 11.11 đã xác nhận; mã ghép 482 913.
*Hiện trạng Figma 18/10:* cùng món "Tai nghe Bluetooth" đang có giá khác nhau giữa các màn (225.000 ₫ lúc lưu 250.000 ₫ ở 11 v3, 13 v3, 19d, EXT; 378.000 ₫ lúc lưu 420.000 ₫ ở 28–30b, X2, X3); nhãn "Dữ liệu mô phỏng" mới có ở 28–31, 30b, X2, X3. Cần thống nhất trên Figma.

## Bổ sung theo checklist.design/mobile (13/10/2026)

Nhóm đối chiếu thiết kế với checklist.design/mobile và chỉ làm phần lớn các mục áp dụng được
(kết quả review: 98,2%, xem báo cáo). Các quy ước mới:

**Icon mới** (24 × 24, nét 2 px, màu color/on-surface): `eye`, `eye-off` (hiện / ẩn mật khẩu),
`logout` (Đăng xuất).

**Component mới / thay đổi**
- **Password strength**: 3 mức Yếu / Trung bình / Mạnh, đặt ngay dưới ô Mật khẩu (Đăng ký,
  Đổi mật khẩu). Màu đoạn: Yếu = error, Trung bình = motive/khuyen-mai/on, Mạnh = primary.
  Luôn có nhãn chữ "Độ mạnh: …", không chỉ dựa vào màu.
- **Dialog** có 2 loại: *Danger* (xóa, không hoàn tác; icon và nút màu error) và *Default*
  (xác nhận thường như Đăng xuất; icon và nút màu primary). Luôn có nút "Hủy" dạng text.
- **Text field**: ô mật khẩu ẩn icon bên trái, icon bên phải là eye-off / eye. Dòng lỗi ở
  trạng thái Error tự xuống hàng, đi kèm icon cảnh báo.
- **App icon**: adaptive icon 108 dp, vùng an toàn 66 dp, nền primary, ký hiệu chart-search
  màu trắng. Hai dạng: vuông bo góc và tròn. Dùng chung cho icon app, Splash và mẫu thông báo.

**Quy tắc**
- **Splash** chỉ có logo và tên app trên nền primary, không có nút, tự chuyển sau khoảng 0,8 giây.
- **Xin quyền thông báo**: không hỏi lúc mở app. Chỉ hỏi sau khi người dùng lưu khoản mua đầu
  tiên, trên một màn riêng (05a), có mẫu thông báo thật và nút "Để sau". Nếu người dùng từ chối,
  Cá nhân hiện dòng "Chưa cấp quyền thông báo · Mở cài đặt".
- **Tài khoản**:
  - Muốn đổi mật khẩu phải nhập mật khẩu hiện tại. Nút "Lưu" bị khóa đến khi nhập đủ 3 ô.
  - "Xóa tài khoản" nằm ở nhóm riêng cuối màn Tài khoản, chữ đỏ, có dialog Danger.
    Thao tác này khác "Xóa toàn bộ dữ liệu" ở Cá nhân (chỉ xóa khoản mua, giữ tài khoản).
- **Cá nhân**: thẻ tài khoản ở đầu màn. Cuối màn có nhóm "Hỗ trợ & thông tin" (Gửi góp ý,
  Điều khoản sử dụng, Chính sách quyền riêng tư), nút "Đăng xuất" (Tonal) và dòng "Phiên bản 1.0.0".
- **Thanh tab** ẩn ở màn cấp sâu: Ghi khoản mua, Chi tiết, Tài khoản, Đổi mật khẩu,
  Xin quyền thông báo.
- **Chính tả**: dùng "Xóa" (không dùng "Xoá") cho thống nhất toàn bộ giao diện.

## Danh sách màn hình
00 Splash · 01 Onboarding · 00a Đăng nhập · 00b Đăng ký · Quên mật khẩu · 00 Trang chủ tổng hợp (Hub) ·
02 Trang chủ · 03 Ghi khoản mua – Bước 1/2 · 04 Ghi khoản mua – Bước 2/2 · 05 Chi tiết khoản mua ·
05 Khoản mua đã lưu · 05a Xin quyền thông báo · 06 Lịch sử · 07 Mô hình (có AI) · 08 Góc nhìn (có AI) ·
08b Chi tiết mô hình mua sắm · 08c Nhận định AI về khoản mua · 09 Chiêm nghiệm tháng ·
10 Cá nhân · 10a Tài khoản · 10b Đổi mật khẩu · 11–13 Danh sách mong muốn ·
14–16 Trước khi mua – Bước 1/3 đến 3/3 · 18 Nhận định trước khi mua

Trong Figma, Splash và Trang chủ tổng hợp cùng mang số 00. Khi nhắc tới, luôn ghi kèm tên
("00 Splash", "00 Hub") để không nhầm. Mã 05a, 10a, 10b chỉ dùng cho màn mới (Xin quyền thông báo,
Tài khoản, Đổi mật khẩu). Các khung trạng thái cũ gọi theo tên khung Figma, ví dụ
"05 Chi tiết khoản mua – dialog xóa", "10 Cá nhân – xác nhận xóa toàn bộ".

**Khung trạng thái:** 02 trống · 02 sau khi lưu · 02 ngoại tuyến · 02 vừa tạo tài khoản ·
Hub chưa ghi hôm nay · 03 lỗi số tiền · 03 đang nhập số tiền (bàn phím số) · 04 đang lưu ·
05 dialog xóa · 06 không có kết quả · 06 sau khi xóa · 07 đang tải · 07 lỗi · 07 chưa đủ dữ liệu ·
Đăng nhập – lỗi · 10 chưa cấp quyền thông báo · 10 xác nhận đăng xuất · 10 xác nhận xóa toàn bộ ·
10a xác nhận xóa tài khoản · 10b đã đổi mật khẩu · 02 lối vào Trước khi mua ·
08a AI đang phân tích – khoản vừa lưu · 08a AI đang phân tích – mô hình · 17 AI đang phân tích – trước khi mua ·
08 đã lưu chiêm nghiệm (có AI).

**Màn hướng Smart Shopping Companion (Figma ver2, 18/10; mã theo tên frame Figma):**
11 v3 Danh sách mong muốn · 13 v3 Chi tiết món · 19 Lưu món (bottom sheet từ Chia sẻ) · 20 Lấy giá từ ảnh chụp ·
21 Danh sách cho đợt sale · 22 Gói mua · 23 So sánh món cùng loại · 24 Đồ đang dùng · 25 Liên kết extension ·
25b Thiết bị đã liên kết · 26 Nhắc nhở & ngưỡng · 27 Hỏi mức hài lòng (dialog) · 28 Decision Card · 30b Lịch sử giá ·
31 Ngân sách theo nhóm · EXT Popup extension (EXT-1…EXT-8) · X2 Trang danh sách · X3 Decision Card bảng cạnh ·
X4 Liên kết thiết bị · X5 Cài đặt & quyền riêng tư.

**Khung trạng thái mới:** 11a v3 trống · 11f đang trong thời gian chờ · 13g cảnh báo giá gốc · 13h cần giá ·
19a đang lấy thông tin · 19b có giá ghi gần đây · 19c thiếu giá · 19d món đã lưu · 19e link không phải Shopee ·
19f nhắc món tương tự · 19g đã lưu · 20a đã nhận giá · 20b không tìm thấy giá · 21a chưa có món · 22a–22c phương án gói mua ·
24a thêm đồ · 24b trống · 25c mã hết hạn · 25e dialog hủy liên kết · 25f xác nhận thiết bị · 27a sau khi chọn ·
28a chưa thiết lập ngân sách · 28b giá cũ · 28c có món cùng nhóm · 29 Chờ (bottom sheet) · 29a đã đặt nhắc ·
30 xác nhận giá (bottom sheet) · 30a gõ giá (bottom sheet) · 31a đã đặt · 31b đã vượt · 31c "Vì sao con số này?" ·
X2a lỗi đồng bộ · X4 mã sai · X4a liên kết thành công.

Mã màn trên Figma (18/10) khác bảng mã của đặc tả hợp nhất (17/10) và vẫn dùng hậu tố chữ thay cho số phân cấp
(02.1, 19.1); bảng ánh xạ ở `design/screen-spec.md` mục "Ánh xạ mã màn". **Nhóm chốt 18/10: dùng mã màn theo tên frame Figma** (19a, 28, 31c…) trong repo, slide và prototype; bảng mã của đặc tả 17/10 chỉ dùng để đối chiếu. Có thể đổi lại nếu giảng viên yêu cầu cách đánh mã phân cấp.

## Lịch sử cập nhật
- 11/10/2026: bản đầu tiên, dùng làm brief cho prompt P1.
- 12/10/2026: sau R1–R3, bổ sung từ vựng thống nhất, phạm vi, lưu trữ dữ liệu, dữ liệu mẫu và khung giờ;
  quy tắc giọng văn (không khuyên bảo, không ảnh trang trí); nút chính ghim đáy 56 dp; snackbar
  hoàn tác sau khi lưu; thẻ động cơ chỉ icon + tên; quy tắc khung trạng thái. Lý do xem
  [`ai/ai-design-log.md`](../ai/ai-design-log.md) và [`design-decisions.md`](design-decisions.md).
- 12/10/2026 (sau Flow 6 và vòng phản biện PB): đồng bộ thang chữ với Figma (Label 14 sp, thêm Overline,
  Caption, Caption strong; đã sửa 33 lớp chữ 12 → 14 sp); thêm token surface-container, error-container,
  outline-strong (PB-5); thêm màn 00a Đăng nhập, 00b Đăng ký (Flow 7); thống nhất mốc "sau 22h" với persona (PB-14).
- 13/10/2026: đối chiếu checklist.design/mobile; thêm Splash, icon app, Xin quyền thông báo,
  Tài khoản / Đổi mật khẩu / Xóa tài khoản / Đăng xuất, trạng thái lỗi đăng nhập, Password strength,
  Dialog Default; quy tắc "tối đa một nút chính"; đồng bộ bảng typography và màu với Figma.
- 18/10/2026: chuyển định vị sang Smart Shopping Companion theo đặc tả hợp nhất v1.0; đưa ngân sách vào phạm vi
  (tùy chọn, không cảnh báo đỏ); thêm từ vựng Mua · Chờ · Bỏ qua, giá đã ghi / giá thực trả; thêm mục quy tắc
  Smart Wishlist, ngân sách, Decision Card, giá – voucher – dữ liệu, microcopy, trạng thái bắt buộc; liệt kê màn F11–F13
  theo Figma ver2. Token không đổi. Figma ver2 có thêm biến `price/lower/bg`, `price/lower/on` (chưa đo tương phản).
