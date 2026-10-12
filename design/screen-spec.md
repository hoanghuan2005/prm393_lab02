# Detailed Screen Specifications

**Project:** Why I Buy? – The Psychology of Money  
**Course:** PRM393 / PRM323 – Mobile UI/UX Design with AI  
**Deliverable:** UI Layout, Hierarchy, States & Constraints for 10 Screens  

---

## Danh mục màn hình hoàn chỉnh

1. [Screen 01: Onboarding Screen](#screen-01-onboarding-screen)
2. [Screen 02: Home Dashboard Screen](#screen-02-home-dashboard-screen)
3. [Screen 03: Add Purchase Screen (Step 1)](#screen-03-add-purchase-screen-step-1)
4. [Screen 04: Purchase Reason Screen (Step 2)](#screen-04-purchase-reason-screen-step-2)
5. [Screen 05: Purchase Detail Screen](#screen-05-purchase-detail-screen)
6. [Screen 06: Purchase History Screen](#screen-06-purchase-history-screen)
7. [Screen 07: Buying Patterns Screen](#screen-07-buying-patterns-screen)
8. [Screen 08: Personal Insights Screen](#screen-08-personal-insights-screen)
9. [Screen 09: Monthly Reflection Screen](#screen-09-monthly-reflection-screen)
10. [Screen 10: Profile & Settings Screen](#screen-10-profile--settings-screen)
11. [Screen 11: Wishlist Overview](#screen-11-wishlist-overview)
12. [Screen 12: Add Wishlist Item](#screen-12-add-wishlist-item)
13. [Screen 13: Wishlist Detail](#screen-13-wishlist-detail)

---

### Screen 01: Onboarding Screen
* **Mục đích:** Giới thiệu định vị ứng dụng, thông điệp cốt lõi *"Understand before you change"* và khơi gợi sự tò mò của người dùng mới về thói quen chi tiêu cá nhân.
* **Bố cục & Phân cấp thị giác:**
  * **Top:** Nút "Bỏ qua" (Text Button, font-caption, góc trên bên phải).
  * **Center:** Illustration dạng vector tối giản mang màu Sage Green thể hiện sự cân bằng giữa lý trí và cảm xúc; Carousel 3 slides giới thiệu (1. Tại sao tôi mua? 2. Nhận diện bẫy cảm xúc. 3. Không phán xét, chỉ thấu hiểu).
  * **Bottom:** Page Indicator (3 dots) và nút Primary Button nổi bật "Bắt đầu khám phá" (chiều cao 52dp, bo góc 24dp).
* **Components sử dụng:** Primary Button, Carousel Indicator, Text Header & Subtitle.
* **Trạng thái (States):**
  * *Slide 1, 2, 3 Active:* Thay đổi nội dung và vị trí dot indicator với hiệu ứng chuyển mượt mà (ease-in-out 300ms).
* **Ràng buộc tương thích (Constraints):** Căn giữa linh hoạt (`Center` + `Flexible Spacer`), padding 24dp trên màn hình 360dp và 32dp trên màn hình 412dp để không bị tràn nội dung.

---

### Screen 02: Home Dashboard Screen
* **Mục đích:** Màn hình chính sau khi mở app; cung cấp bức tranh nhanh về tâm lý chi tiêu tuần hiện tại và là điểm khởi đầu cho hành vi ghi chép.
* **Bố cục & Phân cấp thị giác:**
  * **Header:** Lời chào cá nhân hóa "Chào buổi tối, Nam 👋" kèm câu quote tâm lý trong ngày: *"Tiêu tiền để thể hiện cho người khác thấy bạn có nhiều tiền là cách nhanh nhất để có ít tiền."* (Morgan Housel).
  * **Hero Card (Mindset Breakdown):** Thẻ lớn bo góc 20dp, hiển thị thanh tiến trình tỷ lệ lý do mua sắm tuần này (Ví dụ: 38% Cảm xúc, 32% Nhu cầu, 20% Giảm giá, 10% Tiện lợi).
  * **Quick CTA Button:** Nút nổi bật có icon dấu cộng: "Hôm nay bạn mua gì? – Ghi lại ngay" (Full-width, nền `#2D6A4F`, text trắng).
  * **Recent Reflections:** Danh sách 3 giao dịch ghi nhận gần nhất; mỗi thẻ hiển thị tên món đồ, giá tiền VNĐ và chip lý do tương ứng (ví dụ: `Discount` màu cam ấm, `Emotion` màu đất nung).
  * **Bottom Navigation:** Ghim cố định 5 tab (Home đang kích hoạt).
* **Trạng thái (States):**
  * *Default:* Hiển thị đầy đủ số liệu và danh sách 3 giao dịch.
  * *Empty State:* Người dùng mới chưa có giao dịch nào → Hiển thị hình minh họa ấm cúng kèm lời nhắn: *"Chưa có khoản mua nào được ghi nhận tuần này. Hãy bắt đầu ngay khi bạn có chi tiêu đầu tiên!"* kèm nút "Ghi khoản mua đầu tiên".
  * *Loading:* Skeleton Shimmer hiệu ứng màu xám nhạt (`#EDF2F4`) cho Hero Card và Recent list.
* **Ràng buộc tương thích:** Thẻ Recent items co giãn `width: 100%`, flex wrap cho chip lý do nếu tên món hàng dài trên màn hình 360dp.

---

### Screen 03: Add Purchase Screen (Step 1)
* **Mục đích:** Bước 1 của quy trình ghi nhận: Nhập tên món hàng và giá tiền với ma sát tối thiểu (Zero Friction).
* **Bố cục & Phân cấp thị giác:**
  * **App Bar:** Nút đóng 'X' góc trái, tiêu đề "Ghi nhận khoản mua", chỉ báo bước "Bước 1/2".
  * **Amount Input:** Vùng hiển thị số tiền khổng lồ ở giữa màn hình (font-display-lg 32sp, màu `#1A202C`), đơn vị "₫" ở đuôi. Kèm 3 chip cộng nhanh: `+20k`, `+50k`, `+100k` bên dưới.
  * **Item Input:** Ô Text Field viền xám nhạt bo góc 12dp: "Bạn đã mua món gì?" (ví dụ: Cà phê kem béo, Áo sơ mi Shopee).
  * **Category Icons:** Hàng icon chọn danh mục cơ bản (Ăn uống, Công nghệ, Mua sắm, Đi lại, Giải trí).
  * **Bottom Sticky Bar:** Nút CTA "Tiếp tục: Chọn lý do mua sắm →".
* **Trạng thái (States):**
  * *Default:* Số tiền 0 ₫, nút CTA disabled (nền xám `#CBD5E0`).
  * *Active/Typing:* Số tiền > 0, nút CTA chuyển sang Sage Green (`#2D6A4F`).
  * *Error State:* Người dùng cố tình bấm tiếp mà chưa nhập tên hoặc số tiền = 0 → Ô input đổi viền đỏ `#C53030`, hiện dòng chữ: *"Vui lòng nhập tên món đồ và số tiền hợp lệ"*.
* **Ràng buộc tương thích:** Bàn phím số tự động pop up; bố cục dùng `SingleChildScrollView` tránh lỗi overflow bàn phím trên thiết bị 360dp chiều cao hạn chế.

---

### Screen 04: Purchase Reason Screen (Step 2)
* **Mục đích:** Màn hình trái tim của ứng dụng: Yêu cầu người dùng tự vấn và chọn động cơ tâm lý cốt lõi.
* **Bố cục & Phân cấp thị giác:**
  * **App Bar:** Nút Back '←', tiêu đề "Lý do mua sắm", chỉ báo bước "Bước 2/2".
  * **Prompt Header:** "Điều gì thực sự thôi thúc bạn mua món đồ này?" (font-heading-sm).
  * **Reason Grid (Lưới 2 cột × 4 hàng):** 8 thẻ chọn động cơ tâm lý:
    1. **Nhu cầu (Need):** Vật phẩm thiết yếu, không thể không có.
    2. **Mong muốn (Want):** Sở thích cá nhân, muốn nâng cấp trải nghiệm.
    3. **Khuyến mãi (Discount):** Mua vì thấy giảm giá sốc, flash sale.
    4. **Ảnh hưởng xã hội (Social):** Bạn bè giới thiệu, thấy người khác dùng.
    5. **Quảng cáo (Advertising):** Xem review TikTok, quảng cáo xuất hiện liên tục.
    6. **Cảm xúc (Emotion):** Căng thẳng sau giờ làm, buồn chán, hoặc tự thưởng.
    7. **Tiện lợi (Convenience):** Tiết kiệm thời gian, lười nấu ăn/đi xa.
    8. **Khác (Other):** Nhập lý do tùy chỉnh.
  * **Bottom Sticky Action:** Nút Primary "Lưu góc nhìn chi tiêu" kèm tùy chọn Text Button "Thêm ghi chú chi tiết".
* **Trạng thái (States):**
  * *Unselected:* Các thẻ viền mỏng 1dp xám nhạt, nền trắng.
  * *Selected:* Thẻ được chọn có viền đậm 2dp màu Sage Green `#2D6A4F`, nền đổi sang màu Sage Tint `#D8F3DC`, icon có tick xanh nhỏ.
* **Ràng buộc tương thích:** Lưới dùng `SliverGrid` với tỷ lệ khung hình thẻ (aspectRatio: 1.1), đảm bảo vừa vặn trên cả màn hình 360dp lẫn 412dp mà không bị cắt chữ.

---

### Screen 05: Purchase Detail Screen
* **Mục đích:** Xem lại đầy đủ bối cảnh của một khoản mua, cho phép viết nhật ký cảm xúc ngắn hoặc tải ảnh hóa đơn.
* **Bố cục & Phân cấp thị giác:**
  * **App Bar:** Nút Back '←', tiêu đề "Chi tiết giao dịch", icon thùng rác (xóa) ở góc phải.
  * **Summary Card:** Nền `#FFFFFF`, bo góc 16dp, bóng đổ nhẹ: Tên món hàng, số tiền lớn, ngày giờ chính xác.
  * **Reason Highlight Badge:** Thẻ badge lớn thể hiện lý do mua sắm kèm giải thích định nghĩa tâm lý tương ứng.
  * **Journal Note Section:** Ô ghi chú cảm xúc cá nhân (ví dụ: *"Hôm nay tăng ca đến 21h mệt quá nên đặt trà sữa giải tỏa"*).
  * **Media Attachment:** Khung preview ảnh hóa đơn / sản phẩm chụp nhanh (nếu có).
  * **Action Footer:** Nút "Cập nhật thay đổi" và nút phụ "Đánh giá lại cảm xúc sau 7 ngày".
* **Trạng thái (States):**
  * *View Mode:* Dạng văn bản cố định, chỉ đọc.
  * *Edit Mode:* Các trường chuyển thành input có thể chỉnh sửa trực tiếp.
  * *Delete Confirmation Dialog:* Bấm icon thùng rác hiện modal overlay hỏi xác nhận: *"Bạn có chắc chắn muốn xóa bản ghi này khỏi lịch sử phân tích?"*.
* **Ràng buộc tương thích:** Tự động điều chỉnh cuộn màn hình khi mở rộng ghi chú nhật ký dài.

---

### Screen 06: Purchase History Screen
* **Mục đích:** Quản lý và tra cứu toàn bộ dòng thời gian giao dịch kèm bộ lọc tâm lý chuyên sâu.
* **Bố cục & Phân cấp thị giác:**
  * **Header:** Tiêu đề "Lịch sử mua sắm" kèm thanh tìm kiếm nhanh (Search bar).
  * **Filter Chips Bar:** Thanh cuộn ngang chứa các chip lọc: [Tất cả], [Mua theo cảm xúc], [Săn giảm giá], [Nhu cầu thiết yếu], [Ảnh hưởng MXH].
  * **Timeline List:** Danh sách chia theo nhóm ngày (Hôm nay, Hôm qua, Tuần trước). Mỗi item là một thẻ Purchase Card hoàn chỉnh.
* **Trạng thái (States):**
  * *Populated:* Danh sách cuộn mượt mà với nhiều giao dịch.
  * *Filter Empty:* Khi lọc một lý do mà chưa có giao dịch nào → Hiện illustration kính lúp và text: *"Không tìm thấy khoản mua nào thuộc nhóm 'Ảnh hưởng MXH' trong khoảng thời gian này"*.
  * *Swipe Action:* Vuốt sang trái để hiện nút Quick Delete (nền đỏ dịu).
* **Ràng buộc tương thích:** Dùng `ListView.separated` tối ưu bộ nhớ, kích thước chip đạt chuẩn chạm cao 36dp + margin 6dp = 48dp touch boundary.

---

### Screen 07: Buying Patterns Screen
* **Mục đích:** Trực quan hóa dữ liệu tâm lý học tiêu dùng qua các biểu đồ phân tích đa chiều.
* **Bố cục & Phân cấp thị giác:**
  * **Top Bar:** Tiêu đề "Mô hình hành vi", Dropdown chọn chu kỳ xem (Tuần này / Tháng này / 3 tháng qua).
  * **Primary Chart (Psychological Reason Distribution):** Biểu đồ donut mềm mại thể hiện tỷ trọng 8 lý do mua sắm. Khi chạm vào từng lát bánh sẽ hiển thị số tiền và phần trăm tương ứng.
  * **Trigger Heatmap (Khung giờ bốc đồng):** Biểu đồ cột biểu diễn số lần mua sắm theo khung giờ trong ngày (Sáng, Trưa, Chiều, Đêm muộn).
  * **Takeaway Card:** Khối kết luận màu kem ấm: *"Đêm muộn (22h–1h) là thời điểm bạn dễ đưa ra quyết định mua sắm vì cảm xúc nhất (chiếm 65% tổng số đơn Emotion)."*
* **Trạng thái (States):**
  * *Interactive Tap:* Chạm vào phần "Giảm giá (Discount)" trên donut chart sẽ làm mờ các phần khác và làm nổi bật danh sách các món mua do giảm giá bên dưới.
  * *Data Insufficient:* Dưới 5 giao dịch → Hiện thông báo khuyến khích: *"Ghi nhận thêm ít nhất 3 khoản mua nữa để mở khóa biểu đồ mô hình hành vi chính xác."*
* **Ràng buộc tương thích:** Biểu đồ thiết kế responsive SVG/Canvas vector tự co giãn theo chiều ngang màn hình từ 360dp đến 412dp mà không tràn viền.

---

### Screen 08: Personal Insights Screen
* **Mục đích:** Cung cấp các góc nhìn chiêm nghiệm sâu sắc do AI đúc kết, đóng vai trò như một người bạn tâm giao tài chính.
* **Bố cục & Phân cấp thị giác:**
  * **Header:** "Góc nhìn sâu sắc (Insights)" kèm lời chúc thân mật.
  * **Featured Insight Hero Card:** Thẻ lớn viền vàng hổ phách `#DDA15E`, có icon ngọn đèn: *"Bẫy giảm giá: Trong tháng 10, bạn đã chi 1.200.000₫ cho các món đồ săn sale, nhưng có 60% trong số đó bạn không thực sự cần dùng sau 1 tuần."*
  * **Actionable Advice:** Gợi ý hành động thực tế: *"Quy tắc 72 giờ: Lần tới khi thấy deal giảm giá hời, hãy lưu vào danh sách chờ 3 ngày trước khi thanh toán."*
  * **Community Benchmark:** Thẻ so sánh tương quan ẩn danh: *"68% người trẻ cùng độ tuổi cũng đối mặt với việc chi tiêu cảm xúc vào cuối tuần."*
* **Trạng thái (States):**
  * *New Insight Badge:* Đốm đỏ nhỏ báo hiệu có phân tích mới sau mỗi cuối tuần.
  * *Bookmarked State:* Người dùng có thể nhấn icon ngôi sao để lưu lại lời khuyên yêu thích.
* **Ràng buộc tương thích:** Dạng thẻ Card có thể mở rộng (`ExpansionTile`), thích ứng hoàn hảo với độ phân giải màn hình khác nhau.

---

### Screen 09: Monthly Reflection Screen
* **Mục đích:** Báo cáo tổng kết tháng theo tinh thần *"The Psychology of Money"*, khép lại chu kỳ chi tiêu bằng sự chiêm nghiệm và cam kết mới.
* **Bố cục & Phân cấp thị giác:**
  * **Header:** "Chiêm nghiệm tháng 10/2026" kèm thời lượng đọc ước tính (2 phút đọc).
  * **Storytelling Carousel:** Định dạng lật thẻ như Stories:
    * Thẻ 1: Động cơ lớn nhất tháng này của bạn là gì?
    * Thẻ 2: Khoản mua khiến bạn cảm thấy xứng đáng nhất.
    * Thẻ 3: Khoản mua khiến bạn ước mình đã dừng lại suy nghĩ.
  * **Self-Reflection Rating:** Người dùng tự chấm điểm mức độ thỏa mãn tâm lý với chi tiêu tháng: từ 1 đến 5 sao.
  * **Next Month's Intention:** Khung nhập cam kết ngắn cho tháng sau: *"Tôi sẽ chú ý đến lý do cảm xúc trước khi bấm đặt hàng."*
  * **Share & Export:** Nút "Chia sẻ tóm tắt hành trình" dạng ảnh infographic đẹp mắt để lưu vào ảnh hoặc chia sẻ.
* **Trạng thái (States):**
  * *In Progress:* Đang trả lời các câu hỏi tự vấn từng bước.
  * *Completed:* Hiển thị huy hiệu chiêm nghiệm tháng và lưu trữ vào kho lưu trữ kỷ niệm.
* **Ràng buộc tương thích:** Tối ưu hóa tỷ lệ 16:9 cho từng thẻ Story, tự động căn giữa trên thiết bị dài hoặc ngắn.

---

### Screen 10: Profile & Settings Screen
* **Mục đích:** Quản lý thông tin tài khoản, cài đặt thông báo nhắc nhở nhẹ nhàng (Mindful Nudges) và bảo mật dữ liệu.
* **Bố cục & Phân cấp thị giác:**
  * **Profile Header:** Avatar, tên hiển thị "Nguyễn Hải Nam", email sinh viên, huy hiệu thành viên: *"Mindful Explorer - Tuần thứ 6"*.
  * **Mindful Preferences Section:**
    * *Daily Nudge:* Toggle bật/tắt thông báo nhắc nhở tự hỏi "Why did I buy?" vào lúc 21h mỗi tối.
    * *Cooling-off Period Alert:* Nhắc nhở dừng lại 10 phút trước khi thanh toán đơn hàng online lớn.
  * **Data & Privacy:** Nút "Xuất dữ liệu chi tiêu tâm lý (CSV/PDF)", "Xóa toàn bộ lịch sử", "Đồng bộ đám mây".
  * **App Information:** Phiên bản app v1.0.0, Điều khoản bảo mật, Lời cảm ơn tác giả Morgan Housel.
* **Trạng thái (States):**
  * *Toggle Switches:* Bật (Sage Green) / Tắt (Muted Grey).
  * *Syncing:* Icon xoay tròn thể hiện trạng thái đồng bộ dữ liệu.
* **Ràng buộc tương thích:** Thiết kế danh sách chuẩn `ListTile` của hệ thống, tuân thủ nghiêm ngặt chiều cao tối thiểu 56dp cho mỗi mục menu để dễ dàng thao tác bằng một tay.

---

### Screen 11: Wishlist Overview
* **Mục đích:** Xem những món đang muốn mua và lý do muốn mua, lọc theo trạng thái. Thuộc Flow 6.
* **Bố cục & Phân cấp thị giác:**
  * **App Bar (Nested):** nút Back, tiêu đề "Danh sách mong muốn".
  * **Intro:** thẻ nền surface-container, icon bookmark: "Ghi lại món bạn muốn mua và lý do. Bạn tự quyết định khi nào mua, bỏ qua hay cân nhắc thêm."
  * **Bộ lọc:** 3 Filter chip "Đang cân nhắc (n)", "Đã mua (n)", "Bỏ qua (n)"; chip đang chọn có nền + dấu tích. Ở 360 dp chip xuống hàng (wrap) thay vì bị cắt.
  * **Danh sách:** Wishlist item card (tên, giá dự kiến, chip động cơ, chip trạng thái, ghi chú, ngày thêm).
  * **Thanh đáy:** nút chính "Thêm món" (icon +).
* **Components:** App bar/Nested, Filter chip, Wishlist item card (Status × State Default/Pressed), Motive chip, Wishlist status chip, Empty state (Filter empty), Snackbar, Button/Primary.
* **Trạng thái:** Có dữ liệu (11) · Trống hoàn toàn (11a: "Bạn chưa có món nào đang cân nhắc." + "Thêm món", ẩn thanh đáy) · Bộ lọc trống (11a: "Chưa có món nào trong danh mục này." + "Xem đang cân nhắc") · Đã lưu (11b) · Đã bỏ qua + Hoàn tác (11c) · Sau hoàn tác (11d) · Đã mua (11e). Không bao giờ hiển thị empty state cùng thẻ của bộ lọc khác.
* **Ràng buộc:** số trên chip phải khớp số thẻ; không có nút mua hàng, giỏ hàng hay đồng hồ chờ.

---

### Screen 12: Add Wishlist Item
* **Mục đích:** Lưu một món muốn mua kèm động cơ trong dưới 20 giây. Dùng lại cho "Sửa món mong muốn" (12c).
* **Bố cục & Phân cấp thị giác:**
  * **App Bar (Nested):** Back, "Thêm món mong muốn" (12c: "Sửa món mong muốn").
  * **Thẻ thông tin:** Text field "Tên món đồ (bắt buộc)" (icon túi), Text field "Giá dự kiến (tùy chọn)" (icon hóa đơn), giá hiển thị "650.000 ₫".
  * **Câu hỏi:** "Vì sao bạn muốn mua món này?" + "Chọn một lý do chính. Không có lựa chọn đúng hay sai."
  * **Motive grid:** đúng 8 động cơ, 2 cột × 4 hàng, giống màn 04.
  * **Ghi chú thêm (tùy chọn).**
  * **Thanh đáy:** nút chính "Lưu món" (12c: "Lưu thay đổi").
* **Components:** App bar/Nested, Text field (Default/Error), Motive grid, Button/Primary.
* **Trạng thái:** Trống (12) · Lỗi (12a) · Đã điền hợp lệ (12b) · Sửa (12c).
* **Validation:** tên trống hoặc chỉ khoảng trắng → "Vui lòng nhập tên món đồ để lưu." · giá đã nhập nhưng ≤ 0 → "Vui lòng nhập số tiền lớn hơn 0." · chưa chọn động cơ → "Vui lòng chọn lý do bạn muốn mua món này." Lỗi hiện ngay dưới trường, kèm icon; form hợp lệ không hiện lỗi.
* **Ràng buộc:** nội dung cuộn, nút "Lưu món" luôn hiện trên bàn phím.

---

### Screen 13: Wishlist Detail
* **Mục đích:** Nhìn lại lý do muốn mua và tự quyết định.
* **Bố cục & Phân cấp thị giác:**
  * **App Bar (Nested):** Back, "Chi tiết món mong muốn", icon Sửa (48 dp).
  * **Thẻ tóm tắt:** "MÓN ĐANG CÂN NHẮC", tên món, giá dự kiến (lớn) + "Giá dự kiến · chưa tính vào chi tiêu", chip trạng thái, khối "Lý do muốn mua" với chip động cơ.
  * **Thẻ chi tiết:** "Ngày thêm vào danh sách" (Thứ Sáu, 09/10/2026 · 2 ngày trước), "Ghi chú của bạn".
  * **Thanh đáy:** nút chính "Ghi khoản mua"; nút văn bản "Không mua nữa".
* **Components:** App bar/Nested, Motive chip, Wishlist status chip, Button/Primary, Button/Text, Dialog, Snackbar.
* **Trạng thái:** Đang cân nhắc (13) · Dialog xác nhận bỏ qua (13a, overlay) · Sau khi sửa (13b, snackbar "Đã cập nhật “Bàn phím cơ”") · Đã bỏ qua (13c: overline "MÓN ĐÃ BỎ QUA", chip Bỏ qua, nút chính duy nhất "Đưa về Đang cân nhắc") · Đã mua (13d: overline "MÓN ĐÃ MUA", chip Đã mua, caption "Đã ghi khoản mua 650.000 ₫ vào Lịch sử", ngày mua; chỉ xem — ẩn nút đáy và nút Sửa).
* **Ràng buộc:** không có đếm ngược 48h/72h, không có nhật ký tâm lý bắt buộc, không khóa nút vì thời gian.
