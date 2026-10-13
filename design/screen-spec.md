# Screen Specification — Why I Buy?

**Project:** Why I Buy? – lấy cảm hứng từ "The Psychology of Money"
**Course:** PRM323 – Lab 2

Mỗi màn hình: dùng để làm gì, hiển thị nội dung gì (từ trên xuống), thuộc flow nào, có những khung trạng thái nào, và ý đồ thiết kế. Nội dung khớp với page `03 Final UI` trong Figma; ảnh từng khung ở [`assets/figma/`](../assets/figma/). Token và quy tắc component xem [`DESIGN.md`](DESIGN.md); cách dựng bằng Flutter xem [`handoff/flutter-handoff.md`](../handoff/flutter-handoff.md).

## Danh mục màn hình

| # | Màn hình | Cấp | Flow | Khung trạng thái | Ảnh |
|---|---|---|---|---|---|
| 00a | Đăng nhập | Gốc | 7 | — | [00a](../assets/figma/00a-login.png) |
| 00b | Đăng ký | Gốc | 7 | — | [00b](../assets/figma/00b-register.png) |
| 01 | Onboarding | Gốc (lần đầu) | 1, 7 | — | [01](../assets/figma/01-onboarding.png) |
| 02 | Trang chủ | Tab 1 | 1, 2, 6 | trống, sau khi lưu, ngoại tuyến, lối vào Danh sách mong muốn | [02](../assets/figma/02-home.png) |
| 03 | Ghi khoản mua – Bước 1/2 | Lồng | 1, 3, 6 | lỗi, sửa, điền sẵn từ Danh sách mong muốn | [03](../assets/figma/03-add-purchase-step1.png) |
| 04 | Ghi khoản mua – Bước 2/2 | Lồng | 1, 3, 6 | đang lưu, giải thích động cơ, sửa, điền sẵn | [04](../assets/figma/04-purchase-reason.png) |
| 05 | Chi tiết khoản mua | Lồng | 3 | dialog xóa | [05](../assets/figma/05-purchase-detail.png) |
| 06 | Lịch sử | Tab 2 | 3, 4 | không có kết quả, sau khi xóa, chọn tháng, tháng 9/2026 | [06](../assets/figma/06-history.png) |
| 07 | Mô hình | Tab 3 | 2, 4 | đang tải, lỗi, chưa đủ dữ liệu, tháng 9/2026, Tuần | [07](../assets/figma/07-patterns.png) |
| 08 | Góc nhìn | Tab 4 | 2 | đã lưu chiêm nghiệm | [08](../assets/figma/08-insights.png) |
| 09 | Chiêm nghiệm tháng | Lồng | 2 | — | [09](../assets/figma/09-monthly-reflection.png) |
| 10 | Cá nhân | Tab 5 | 5 | xác nhận xóa toàn bộ, đã xuất dữ liệu | [10](../assets/figma/10-profile.png) |
| 11 | Danh sách mong muốn | Lồng | 6 | 11a–11e | [11](../assets/figma/11-wishlist-overview.png) |
| 12 | Thêm món mong muốn | Lồng | 6 | 12a–12c | [12](../assets/figma/12-add-item.png) |
| 13 | Chi tiết món mong muốn | Lồng | 6 | 13a–13d | [13](../assets/figma/13-wishlist-detail.png) |

Quy ước chung cho mọi màn: một nút chính (filled, cao 56 dp) ghim ở đáy, ngay trên thanh điều hướng; tab gốc có logo bên trái và avatar (→ Cá nhân) bên phải app bar; màn lồng có nút Back và không có thanh điều hướng.

---

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

### 01 Onboarding
- **Mục đích:** giới thiệu app làm gì trong một màn, rồi để người dùng bắt đầu ngay.
- **Nội dung:** icon app · overline "NHẬT KÝ ĐỘNG CƠ MUA SẮM" · "Why I Buy?" · "Ghi lại lý do của mỗi khoản mua để hiểu thói quen chi tiêu của chính bạn. Không chấm điểm, không phán xét." · thẻ 3 dòng: ghi số tiền, tên món và động cơ / xem động cơ và khung giờ theo tuần, tháng / đọc quan sát từ dữ liệu của chính bạn · nút chính "Bắt đầu" · "Dữ liệu được lưu trên máy của bạn."
- **Flow:** 1 (lần đầu), 7. "Bắt đầu" → Đăng nhập.
- **Ý đồ:** một màn thay cho carousel nhiều trang (bớt thao tác); 3 dòng tương ứng 3 tab chính để người dùng biết trước sẽ thấy gì; không ảnh minh họa trang trí (DESIGN.md).

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

### 08 Góc nhìn
- **Mục đích:** đọc vài quan sát trung tính rút ra từ chính dữ liệu đã ghi.
- **Nội dung:** app bar "Góc nhìn" · "THÁNG 10/2026 · Góc nhìn" + "Những quan sát trung tính, tổng hợp từ các khoản bạn đã ghi trong tháng." · thẻ "THÁNG 10 · NHÌN LẠI — 15 khoản đã ghi" · 3 thẻ quan sát: "5 trong 15 khoản tháng này gắn với Khuyến mãi." [Động cơ], "8 trong 15 khoản được ghi sau 18:00." [Khung giờ], "Cả 4 khoản Cảm xúc đều được ghi sau 22:00." [Cảm xúc] · nút chính "Mở chiêm nghiệm tháng" · thanh điều hướng.
- **Flow:** 2.
- **Trạng thái:** `– đã lưu chiêm nghiệm` (snackbar "Đã lưu chiêm nghiệm tháng 10").
- **Ý đồ:** chỉ quan sát kiểm chứng được, không lời khuyên, không số liệu bịa (Nielsen #2; giọng văn trong DESIGN.md).

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
