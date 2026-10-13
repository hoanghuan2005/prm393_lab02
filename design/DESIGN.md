# DESIGN.md — Design brief và quy ước thiết kế

Tài liệu gốc cho cả prompt Google Stitch và file Figma. Mục "Lịch sử cập nhật" ở cuối ghi lại những gì được bổ sung sau các vòng tinh chỉnh.

## Sản phẩm
Why I Buy? — ứng dụng di động giúp người trẻ ghi nhanh khoản mua và gắn động cơ
tâm lý, lấy cảm hứng từ "The Psychology of Money" (Morgan Housel).
Thông điệp: "Hiểu trước khi thay đổi".

## Người dùng
Nguyễn Hải Nam, 22 tuổi, sinh viên năm cuối ngành CNTT kiêm thực tập sinh,
thu nhập 6–9 triệu/tháng. Hay đặt đồ ăn khuya và chốt flash sale sau 22h,
dùng điện thoại một tay, cận 2 độ. Đã bỏ các app chi tiêu vì nhập lâu và
cảm giác tội lỗi khi thấy cảnh báo đỏ.

## Nền tảng
Android, khung 360 × 800 dp, Material Design 3, light theme.

## Tone & giọng văn
- Bình tĩnh, ấm áp, trung lập, không phán xét.
- Không cảnh báo đỏ, không "vượt ngân sách", không chấm điểm người dùng.
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
| Trạng thái | "Đang cân nhắc" · "Đã mua" · "Bỏ qua" | "Chờ", "Hạ nhiệt", "Đang tĩnh tâm" |

- **8 động cơ** (đúng tên, đúng thứ tự): Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Không dùng "Giảm giá". Mỗi khoản mua chỉ có **một** chip động cơ, không thêm nhãn phụ.
- **Tiêu đề app bar** (chỉ viết hoa chữ đầu): Trang chủ · Ghi khoản mua (Bước 1/2, Bước 2/2) · Chi tiết khoản mua · Lịch sử · Mô hình · Góc nhìn · Chiêm nghiệm tháng · Cá nhân.

## Phạm vi
- **Trong phạm vi:** ghi khoản mua (số tiền, tên món, thời điểm, động cơ, ghi chú), xem/sửa/xóa, lọc theo động cơ, mô hình theo động cơ và khung giờ, góc nhìn, chiêm nghiệm tháng, nhắc nhở, xuất và xóa dữ liệu.
- **Ngoài phạm vi:** ngân sách và cảnh báo vượt mức, chấm điểm người dùng, lời khuyên, "khoảng hạ nhiệt", ảnh hóa đơn hoặc ảnh khoản mua, danh mục chi tiêu, so sánh với người khác, chuỗi ngày (streak), mã giao dịch.

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
05a Xin quyền thông báo · 06 Lịch sử · 07 Mô hình · 08 Góc nhìn · 09 Chiêm nghiệm tháng ·
10 Cá nhân · 10a Tài khoản · 10b Đổi mật khẩu · 11–13 Danh sách mong muốn · 14–18 Trước khi mua (AI)

Trong Figma, Splash và Trang chủ tổng hợp cùng mang số 00. Khi nhắc tới, luôn ghi kèm tên
("00 Splash", "00 Hub") để không nhầm. Mã 05a, 10a, 10b chỉ dùng cho màn mới (Xin quyền thông báo,
Tài khoản, Đổi mật khẩu). Các khung trạng thái cũ gọi theo tên khung Figma, ví dụ
"05 Chi tiết khoản mua – dialog xóa", "10 Cá nhân – xác nhận xóa toàn bộ".

**Khung trạng thái:** 02 trống · 02 sau khi lưu · 02 ngoại tuyến · 02 vừa tạo tài khoản ·
Hub chưa ghi hôm nay · 03 lỗi số tiền · 03 đang nhập số tiền (bàn phím số) · 04 đang lưu ·
05 dialog xóa · 06 không có kết quả · 06 sau khi xóa · 07 đang tải · 07 lỗi · 07 chưa đủ dữ liệu ·
Đăng nhập – lỗi · 10 chưa cấp quyền thông báo · 10 xác nhận đăng xuất · 10 xác nhận xóa toàn bộ ·
10a xác nhận xóa tài khoản · 10b đã đổi mật khẩu.

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
