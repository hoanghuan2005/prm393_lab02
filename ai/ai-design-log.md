# AI Design Log

**Project:** Why I Buy?
**Course:** PRM323 – Cross-Platform Application Development

## Khai báo công cụ AI
| Công cụ | Mục đích |
|---|---|
| Claude (claude.ai, Cowork) | Soạn nháp persona, user flow, DESIGN.md, prompt Stitch; giao diện tham chiếu; soạn prompt tinh chỉnh R1–R3 và hỗ trợ đối chiếu ảnh khi nhận xét output Stitch (tôi kiểm tra lại và tự quyết định từng mục) |
| Google Stitch | Sinh UI ban đầu và các vòng lặp |
| Claude (claude.ai + Figma connector), 12/10/2026 | Phản biện ảnh Stitch của Flow 6; dựng Flow 6 trực tiếp trong file Figma (component, Final UI, wireframe, sơ đồ user flow, prototype) theo master prompt của tôi; soạn nội dung tài liệu Flow 6. Tôi kiểm tra lại từng màn và tự quyết định giữ / sửa / bỏ. |
| Claude (Claude Code, desktop app), 12/10/2026 | Rà repo và file Figma theo đề bài; chụp lại toàn bộ khung Final UI từ Figma vào `assets/figma/`; chạy vòng phản biện bằng AI (mục PB bên dưới, một agent Claude riêng chỉ đọc ảnh và tài liệu); soạn lại `handoff/flutter-handoff.md`, `design/screen-spec.md`, `design/design-decisions.md`, README cho khớp Figma; soạn nháp quyết định cho từng phát hiện để tôi duyệt. |
| Claude (Cowork, Figma MCP) | Đối chiếu checklist.design/mobile, lập kế hoạch prompt theo giai đoạn, dựng component/wireframe/Final UI/user flow/prototype trực tiếp trong Figma qua Plugin API, AI review theo checklist (nhóm duyệt và xác nhận từng giai đoạn) |

---

## P1 — Prompt đầu tiên (Flow 1)
**Ngày:** 11/10/2026
**Công cụ:** Google Stitch, chế độ Mobile
**Prompt (nguyên văn):**

```
Design a mobile app (Android, 360x800 dp, Material 3, light theme) called "Why I Buy?" — a non-judgmental purchase-reflection app inspired by Morgan Housel's "The Psychology of Money".

User: Nam, 22, final-year IT student and intern in Vietnam. He often orders late-night food and buys flash-sale items after 11 pm, uses his phone one-handed, and is near-sighted. He quit expense apps because logging was slow and red over-budget warnings made him feel guilty.
Main task: log a purchase and tag its psychological motive in under 25 seconds.

Screens:
1. Onboarding – headline "Hiểu trước khi thay đổi", short subtitle, one primary button "Bắt đầu".
2. Home Dashboard – weekly summary (number of purchases, total in VND, most common motive), one primary button "Ghi khoản mua" in the lower half, list of 3 recent purchases, bottom navigation with 5 tabs: Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân.
3. Add Purchase, step 1 of 2 – large amount field in VND, item name field, date/time row, primary button "Tiếp tục". Also show an error variant: amount "0" with inline error message under the field.
4. Purchase Reason, step 2 of 2 – title "Vì sao bạn mua?", 8 selectable motive cards in a 2-column grid, each with icon and label: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác; optional note field; primary button "Lưu".
5. Home Dashboard after saving – same as screen 2 with a snackbar "Đã lưu" and the new purchase at the top of the recent list.

Style: calm and clean. Background #F5F6F2, primary indigo #2E4A9E, text #1A2320, secondary text #545E59, error #B3261E. Font Be Vietnam Pro. 16 dp side margins, 8 dp spacing grid, 12–16 dp corner radius, soft low elevation. Tone: warm and neutral, never judgmental — no red overspending warnings.

Constraints: all UI text in Vietnamese; exactly one primary action per screen; touch targets at least 48 dp; body text at least 14 sp; text contrast at least 4.5:1; motives always shown with icon + label, never by color alone; selected tab shown with a pill background and bold label.
```

**Kết quả:** Stitch sinh 5 màn hình và 1 bảng design system.

| Màn hình | Ảnh |
|---|---|
| Toàn cảnh | ![](../assets/stitch/stitch1/Screenshot%202026-10-11%20140005.png) |
| Design system do Stitch tạo | ![](../assets/stitch/stitch1/v1-00-design-system.png) |
| 01 Onboarding | ![](../assets/stitch/stitch1/v1-01-onboarding.png) |
| 02 Home Dashboard | ![](../assets/stitch/stitch1/v1-02-home.png) |
| 03 Add Purchase (biến thể lỗi) | ![](../assets/stitch/stitch1/v1-03-add-purchase-error.png) |
| 04 Purchase Reason | ![](../assets/stitch/stitch1/v1-04-purchase-reason.png) |
| 05 Home sau khi lưu | ![](../assets/stitch/stitch1/v1-05-home-saved.png) |

**Phản hồi của Stitch (nguyên văn, chưa kiểm chứng):**

> Bộ thiết kế hoàn chỉnh cho ứng dụng "Why I Buy?" (Android, kích thước chuẩn 360x800 dp, Material 3, light theme) đã được hoàn thiện đáp ứng toàn bộ các tiêu chí và persona người dùng Nam (22 tuổi):
>
> 1. Phân tích & Giải pháp thiết kế cho Persona Nam:
> Thao tác một tay & Tốc độ < 25 giây: Toàn bộ các nút hành động chính (CTA) và lưới chọn nhanh đều được bố trí ở nửa dưới màn hình trong tầm với của ngón tay cái, kèm các chip gợi ý nhanh (+20k, +50k...).
> Độ rõ nét cho mắt cận: Font Be Vietnam Pro với cỡ chữ lớn, tương phản cao (trên 4.5:1), trường nhập số tiền hiển thị nổi bật dễ nhận biết.
> Tâm lý phi phán xét (Non-judgmental): Lấy cảm hứng từ cuốn "The Psychology of Money" của Morgan Housel. Không có bất kỳ thanh cảnh báo màu đỏ hay âm báo tiêu cực nào tạo cảm giác tội lỗi khi chi tiêu ngoài kế hoạch/đêm muộn; thay vào đó là sự ghi nhận khách quan về động cơ tâm lý.
>
> 2. Danh sách 5 màn hình đã thiết kế:
> Onboarding – Hiểu trước khi thay đổi: Tiêu đề chính "Hiểu trước khi thay đổi", phụ đề giải thích tinh tế. 3 điểm cam kết: Ghi chép nhanh dưới 25s, không phán xét, thấu hiểu tâm lý. Nút chính duy nhất: "Bắt đầu".
> Trang chủ – Tổng quan & Ghi khoản mua: Thẻ tổng kết tuần: Số khoản mua (14 khoản), Tổng tiền (2.450.000 ₫), Động cơ chính (Khuyến mãi 38%). Nút hành động chính nổi bật ở nửa dưới: "Ghi khoản mua mới". Danh sách 3 khoản mua gần nhất với đầy đủ Icon + Nhãn động cơ rõ ràng. Thanh điều hướng 5 tab chuẩn Material 3: Trang chủ (đang chọn với pill background & in đậm), Lịch sử, Mô hình, Góc nhìn, Cá nhân.
> Nhập chi tiêu – Bước 1/2 (kèm trạng thái lỗi): Ô nhập số tiền lớn bằng VNĐ, ô tên món đồ, dòng chọn ngày giờ ("Hôm nay, 23:45"). Hiển thị trực quan biến thể trạng thái lỗi hợp lệ: Khi số tiền là "0", thông báo lỗi nội dòng màu #B3261E: "⚠️ Vui lòng nhập số tiền lớn hơn 0 ₫ để tiếp tục." Nút chính: "Tiếp tục".
> Động cơ mua – Bước 2/2 (Vì sao bạn mua?): Tiêu đề "Vì sao bạn mua?". Lưới 2 cột gồm 8 thẻ động cơ tâm lý (có đầy đủ icon + nhãn): Nhu cầu, Mong muốn, Khuyến mãi (đang chọn), Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Khung nhập ghi chú tâm trạng tùy chọn. Nút chính: "Lưu khoản mua".
> Trang chủ sau khi lưu (kèm Snackbar): Hiển thị Snackbar ở đáy: "✓ Đã lưu khoản mua thành công" kèm nút "Hoàn tác". Thẻ tổng kết tuần tự động cập nhật (+1 khoản, +65.000 ₫). Khoản mua mới vừa lưu được đưa lên vị trí đầu tiên trong danh sách gần đây.
>
> Thông số kỹ thuật & Thiết kế: Tone & Theme: Nền #F5F6F2, màu chủ đạo Indigo #2E4A9E, chữ chính #1A2320, chữ phụ #545E59, màu lỗi #B3261E. Quy cách: Bo góc 12–16 dp, lề 16 dp, lưới 8 dp, mục tiêu chạm tối thiểu 48 dp

**Nhận xét của tôi (đối chiếu với ảnh):**
- Được:
  - Toàn bộ chữ là tiếng Việt, đủ dấu, dùng font Be Vietnam Pro như DESIGN.md.
  - 01 Onboarding: đúng một nút chính "Bắt đầu", thông điệp "Hiểu trước khi thay đổi" rõ ràng, 3 cam kết khớp pain point của Nam.
  - 04 Purchase Reason: lưới 2 cột đủ 8 động cơ, mỗi thẻ có icon + tên + mô tả; thẻ được chọn có nền khác màu và dấu tích, không chỉ dựa vào màu.
  - 03 Add Purchase: lỗi số tiền hiển thị ngay dưới ô nhập, có icon và câu hướng dẫn cách sửa.
  - Không có cảnh báo đỏ hay câu chữ về "vượt ngân sách" ở Trang chủ.
  - Màu chính #2E4A9E, chữ #1A2320, chữ phụ #545E59 được dùng đúng.

- Chưa được:
  - 02 Home Dashboard: động cơ chính ghi "Giảm giá 38%" thay vì "Khuyến mãi"; danh sách gần đây có nhãn ngoài bộ 8 động cơ như "Đồ ăn đêm • Cảm xúc", "Khuyến mãi (Flash sale)", "Nhu cầu phát triển" → không nhất quán tên gọi 
  - 03 và 04: tiêu đề màn là "Nhập Chi Tiêu Mới" trong khi Trang chủ dùng "Ghi khoản mua"; màn 04 dùng "Chọn động lực kích hoạt" thay vì "động cơ" → cùng một khái niệm có nhiều tên 
  - 03 Add Purchase (biến thể lỗi): số tiền đang là 0 và đã báo lỗi nhưng nút "Tiếp tục" vẫn hiển thị như đang bấm được → thiếu phòng ngừa lỗi 
  - 03 Add Purchase: thẻ "Bạn có đang thật sự cần? Các khoản chi sau 23:00 thường xuất phát từ áp lực học tập hoặc sự mệt mỏi…" mang tính phán đoán và gợi cảm giác tội lỗi, trái với triết lý không phán xét và pain point của Nam; thẻ còn xuất hiện trước khi Nam chọn động cơ nên có thể làm Nam chọn lệch.
  - 03 Add Purchase: chip "Thêm nhanh" (+20k, +50k, +100k, +200k) và chip gợi ý tên món trông thấp hơn nhiều so với 48dp; dãy chip gợi ý bị cắt ở mép phải.
  - 02 Home Dashboard: nút chính "Ghi khoản mua mới" bị xuống 2 dòng và chen thêm chữ "Ngay lúc này" cùng mũi tên; nút nằm khoảng giữa màn hình chứ không ở nửa dưới như yêu cầu (Nam dùng một tay).
  - 02 Home Dashboard: tên món trong danh sách bị cắt nhiều ("Cơm tấm đêm & Tr…", "Tai nghe chống ồ…", "Sách 'The Psychol…").
  - 02 Home Dashboard: thẻ "Khoảng hạ nhiệt 24h" là một tính năng không có trong phạm vi và cạnh tranh với hành động chính 
  - 02 Home Dashboard: nhãn thanh điều hướng rất nhỏ, và khó nhận ra tab "Trang chủ" đang được chọn (không thấy nền pill như yêu cầu).
  - Nhiều chữ phụ trông nhỏ hơn 14sp: mô tả dưới tên động cơ ở 04, dòng phụ trong thẻ cam kết ở 01, các dòng chú thích nhỏ ở cuối màn 04 và 01.
  - 05 Home sau khi lưu: biểu đồ các ngày trong tuần (T2–CN) chỉ phân biệt bằng kích thước và màu chấm, không có số liệu → truyền thông tin chỉ bằng hình/màu.
  - 05 Home sau khi lưu: bố cục và nhãn khác hẳn màn 02 dù prompt yêu cầu "giống màn 2" ("Tổng chi tiêu đã ghi" thành "Tổng chi tiêu đã nhận diện", "Số khoản mua" thành "Số lần ra quyết định") → không nhất quán giữa hai trạng thái của cùng một màn.
  - 04 và 05: khoản đang ghi ở bước 2 là "Cà phê phễu pha thủ công", nhưng khoản mới ở Trang chủ sau khi lưu lại là "Trà sữa nướng & Bánh tráng" → dữ liệu không liên tục giữa các bước.
  - 02, 03, 04: theo tỷ lệ ảnh, các màn dài hơn khung 800dp; ở màn 04, nút "Lưu khoản mua" nằm dưới cùng nên trên máy 360×800 Nam phải cuộn mới thấy nút chính.
  - Design system: Stitch tự thêm màu Tertiary #5C6A4D (xanh rêu) không có trong DESIGN.md, dùng #545E59 (màu chữ phụ) làm màu Secondary, và không thể hiện màu nền #F5F6F2 cùng màu lỗi #B3261E trong bảng màu.

---

## P2 — Prompt thứ hai (Flow 2, Flow 3)
**Ngày:** 11/10/2026
**Công cụ:** Google Stitch, chế độ Mobile, cùng project với P1
**Prompt (nguyên văn):**

```
Using the same style and design system as the existing screens, add these screens for "Why I Buy?" (all text in Vietnamese, same constraints):
1. Purchase History – motive filter chips, purchases grouped by day with daily total; each row shows motive icon, item name, motive label, time, amount. Also an empty variant for a filter with no results: icon, message, button "Xóa bộ lọc". Bottom navigation with "Lịch sử" selected.
2. Purchase Detail – large amount, item name, date, motive chip, note, delete icon in the app bar, button "Sửa".
3. Delete confirmation dialog over Purchase Detail – "Xóa khoản mua này?", buttons "Hủy" and a red "Xóa".
4. Purchase History after deletion – snackbar "Đã xóa" with action "Hoàn tác".
5. Buying Patterns – tabs "Tuần / Tháng", horizontal bars per motive with icon, label, count and percentage, a 4-column chart of purchase time (Sáng, Trưa, Chiều, Tối). Also a skeleton loading variant and an error variant with plain-language cause and a "Thử lại" button. Bottom navigation with "Mô hình" selected.
6. Personal Insights – 3 insight cards written as neutral observations, button "Mở chiêm nghiệm tháng". Bottom navigation with "Góc nhìn" selected.
7. Monthly Reflection – summary of the month by motive, satisfaction rating 1–5, goal input for next month, primary button "Lưu chiêm nghiệm", text button "Để sau".
8. Profile & Settings – profile card, toggles "Nhắc ghi khoản mua" and "Nhắc chiêm nghiệm hằng tháng", rows "Xuất dữ liệu" and a red "Xóa toàn bộ dữ liệu". Bottom navigation with "Cá nhân" selected.
```

**Kết quả:** Stitch sinh 8 khung màn hình. Các biến thể trạng thái trống, loading và lỗi không được tách thành khung riêng mà nằm ở cuối khung Lịch sử và khung Mô hình; tôi chụp riêng các phần đó.

| Màn hình | Ảnh |
|---|---|
| Toàn cảnh | ![](../assets/stitch/stitch2/v2-00-overview.png) |
| 06 Purchase History | ![](../assets/stitch/stitch2/v2-06-history.png) |
| 06 Purchase History (trống, phần cuối của cùng khung 06) | ![](../assets/stitch/stitch2/v2-06-history.png) |
| 06 Purchase History (sau khi xóa) | ![](../assets/stitch/stitch2/v2-06c-history-undo.png) |
| 05 Purchase Detail | ![](../assets/stitch/stitch2/v2-05-detail.png) |
| 05 Dialog xác nhận xóa | ![](../assets/stitch/stitch2/v2-05b-delete-dialog.png) |
| 07 Buying Patterns | ![](../assets/stitch/stitch2/v2-07-patterns.png) |
| 07 Buying Patterns (skeleton loading và lỗi, phần cuối khung 07) | ![](../assets/stitch/stitch2/v2-07-patterns2.png) |
| 08 Personal Insights | ![](../assets/stitch/stitch2/v2-08-insights.png) |
| 09 Monthly Reflection | ![](../assets/stitch/stitch2/v2-09-reflection.png) |
| 10 Profile & Settings | ![](../assets/stitch/stitch2/v2-10-settings.png) |

**Phản hồi của Stitch (nguyên văn, chưa kiểm chứng):**

> Danh sách chi tiết 8 màn hình vừa hoàn thiện:
>
> **1. Lịch sử chi tiêu & Bộ lọc:**
> Thanh bộ lọc động cơ dạng chip lướt ngang (Tất cả (15), Khuyến mãi (6), Cảm xúc (4)...).
> Danh sách chi tiêu gom nhóm theo ngày (Hôm nay 24/10, Hôm qua 23/10, Thứ hai 21/10) kèm tổng tiền từng ngày rõ nét.
> Mỗi hàng hiển thị đầy đủ: icon động cơ, tên món đồ, nhãn động cơ, giờ phát sinh, và số tiền.
> Tích hợp sẵn biến thể Empty State khi bộ lọc không có kết quả với thông báo nhẹ nhàng và nút "Xóa bộ lọc".
> Thanh điều hướng đáy active tại tab Lịch sử với pill background.
>
> **2. Chi tiết khoản mua:**
> Header hiển thị số tiền lớn 65.000 ₫ rõ ràng, tên món đồ kèm huy hiệu "Chi tiêu ngoài giờ cao điểm 🌙".
> Thẻ động cơ kích hoạt (🏷️ Khuyến mãi) và khung trích dẫn tâm trạng khi mua đồ.
> Thẻ gợi ý suy ngẫm nhẹ nhàng không phán xét.
> Nút icon thùng rác 🗑️ trên thanh App Bar và nút hành động chính ở nửa dưới: "Sửa khoản mua".
>
> **3. Hộp thoại xác nhận xóa:**
> Modal Dialog chuẩn Material 3 hiển thị trên nền mờ của màn hình Chi tiết.
> Tiêu đề "Xóa khoản mua này?", nội dung giải thích bình an (thông báo có thể hoàn tác ngay).
> Nút bấm với vùng chạm tối thiểu 48dp: nút chữ "Hủy" và nút cảnh báo màu đỏ "Xóa" (#B3261E).
>
> **4. Lịch sử sau khi xóa (Snackbar):**
> Khoản mua vừa xóa được gỡ khỏi danh sách đầu ngày.
> Snackbar nổi phía trên Bottom Bar: thông báo "Đã xóa khoản mua 'Trà sữa nướng & Bánh tráng'" cùng nút hành động tương phản "Hoàn tác".
>
> **5. Mô hình chi tiêu (kèm Loading & Lỗi):**
> Chuyển đổi tab "Tuần / Tháng".
> Biểu đồ thanh ngang (Horizontal bars) trực quan cho từng động cơ (Khuyến mãi 40%, Cảm xúc 27%, Tiện lợi 13%...).
> Biểu đồ 4 cột khung giờ chi tiêu (Sáng, Trưa, Chiều, Tối), làm nổi bật khung giờ cao điểm đêm muộn của Nam (22h - 04h).
> Trình bày trực quan biến thể Skeleton Loading (hiệu ứng khung tải) và biến thể Báo lỗi kết nối với ngôn ngữ thân thiện, nút "Thử lại".
> Tab Mô hình được kích hoạt ở thanh điều hướng.
>
> **6. Góc nhìn cá nhân:**
> 3 thẻ nhận định tâm lý được viết dưới dạng quan sát trung lập, thấu cảm (không phán xét hay khiển trách):
> Chi tiêu sau 23:00 thường gắn với khuyến mãi.
> Khoảng dừng 15 phút giúp giảm 40% mua bốc đồng.
> Cảm giác tiết kiệm thúc đẩy chi tiêu.
> Nút hành động chính lớn ở đáy: "Mở chiêm nghiệm tháng →".
> Tab Góc nhìn được kích hoạt.
>
> **7. Chiêm nghiệm tháng:**
> Tổng kết động cơ tháng (6.850.000 ₫ với 38 khoản mua).
> Thang đo mức độ hài lòng/bình an từ 1 đến 5 với các nút tròn dễ chạm.
> Ô nhập mục tiêu & định hướng cho tháng tiếp theo với nội dung gợi ý sâu sắc.
> Nút chính "Lưu chiêm nghiệm" và nút phụ "Để sau".
>
> **8. Cá nhân & Cài đặt:**
> Thẻ hồ sơ của Nam Nguyễn kèm thông điệp triết lý tiền bạc từ Morgan Housel.
> Công tắc bật/tắt (Switch toggles): "Nhắc ghi khoản mua" (23:30) và "Nhắc chiêm nghiệm hằng tháng".
> Các hàng thao tác: "Xuất dữ liệu cá nhân" (CSV/JSON) và hàng màu đỏ "Xóa toàn bộ dữ liệu".
> Tab Cá nhân được kích hoạt.

**Nhận xét**
- Được:
  - Thanh điều hướng ở 06 Lịch sử, 07 Mô hình, 08 Góc nhìn, 10 Cá nhân có tab đang chọn với nền pill rõ ràng (đã khắc phục so với 02 Home ở v1).
  - 05 Dialog xóa: hiển thị dạng overlay trên nền tối, nút "Xóa" màu đỏ có cả icon và chữ, nút "Hủy" tách biệt.
  - 07 Mô hình: thanh ngang theo động cơ có đủ icon + tên + số khoản + phần trăm; biểu đồ khung giờ có nhãn phần trăm và khung giờ cụ thể, không chỉ dựa vào màu.
  - 07 Trạng thái lỗi: nêu nguyên nhân bằng ngôn ngữ dễ hiểu ("do kết nối mạng gián đoạn"), trấn an dữ liệu vẫn an toàn, có nút "Thử lại" và lựa chọn "Xem dữ liệu ngoại tuyến".
  - 06 Trạng thái trống: có icon, thông báo và một hành động "Xóa bộ lọc".
  - 09 Chiêm nghiệm tháng: thang 1–5 có nhãn ở hai đầu ("Rất bồn chồn" / "Rất bình an & chủ động"), có cả nút chính "Lưu chiêm nghiệm" và lối thoát "Để sau".
  - 10 Cá nhân: mỗi công tắc có dòng mô tả; hàng "Xóa toàn bộ dữ liệu" có màu đỏ, icon và câu giải thích hậu quả.

- Chưa được:
  - Tiêu đề và phụ đề app bar mất dấu tiếng Việt: "Chi Tiet Chi Tieu" (05), "Phan Chieu Thang" (09), và phụ đề "Lich Su", "Mo Hinh", "Goc Nhin", "Ca Nhan" dưới logo → vi phạm ràng buộc "toàn bộ chữ tiếng Việt" và gây khó đọc.
  - 06 sau khi xóa: không có snackbar và nút "Hoàn tác"; chỉ có thẻ "Bạn vừa điều chỉnh nhật ký…" ở phía trên, không nói rõ khoản nào đã bị xóa → Nam không thể khôi phục khi xóa nhầm và không biết chuyện gì vừa xảy ra 
  - 05 Dialog hứa "Thông báo hoàn tác sẽ hiển thị trong 5 giây" và "Bạn vẫn có thể hoàn tác", nhưng màn sau khi xóa không có hoàn tác → giao diện hứa một điều rồi không thực hiện. Dòng phụ "Hành động không làm mất dữ liệu vĩnh viễn" cũng mâu thuẫn với nút "Xóa".
  - 05 Dialog: màn Chi tiết phía sau dialog có bố cục khác hẳn màn 05 (giờ "15:42" thay vì "23:45", có nút "Chỉnh sửa" và thùng rác ở đáy) → cùng một màn nhưng hai phiên bản khác nhau 
  - 05 Chi tiết: không có icon xóa trên app bar như yêu cầu (chỉ có menu ⋮); hành động phụ "Xác nhận & Đóng" không rõ dùng để làm gì.
  - Nhiều nhận định có số liệu không có nguồn và không phải quan sát từ dữ liệu của Nam: 08 "Khoảng dừng 15 phút giúp giảm 40% mua bốc đồng", "75% các đơn hàng đặt sau 23h…"; 07 "giúp hoãn 75% chi tiêu bốc đồng"; 09 "+12% hài lòng" → trái với yêu cầu "quan sát trung lập" và định hướng khách quan của app.
  - Số liệu mâu thuẫn giữa các màn: 07 ghi "8/15 khoản diễn ra từ 22h–04h", 08 ghi "75% đơn sau 23h" và "8 trên 10 đơn hàng đồ ăn đêm"; 06 sau khi xóa ghi tuần này 630.000 ₫ và động cơ chủ đạo "Cảm xúc", trong khi 05 Home (v1) ghi tuần này 2.515.000 ₫ và "Khuyến mãi (37%)".
  - Stitch tự thêm các tính năng ngoài phạm vi: "Khoảng hạ nhiệt 24h" (08), bộ lọc "Ngủ quá đêm" (07), "danh sách cần thiết từ đầu tuần" (08), ảnh đính kèm khoản mua (05). Thẻ 08 còn tự mâu thuẫn: tiêu đề nói "15 phút" nhưng nội dung nói "24h".
  - Giọng văn chuyển từ quan sát sang khuyên bảo và chấm điểm: 05 "Lần tới, bạn có thể thử đợi 10 phút trước khi thanh toán"; 09 "Bạn đang giữ nhịp kiểm soát rất tích cực"; 09 ô mục tiêu được điền sẵn nội dung do app viết thay Nam → trái với thông điệp "Hiểu trước khi thay đổi".
  - 07 và 08: các câu diễn giải tâm lý như "Tâm trí bạn có xu hướng tìm kiếm niềm vui nhanh vào đêm muộn…", "tâm trí có xu hướng tìm kiếm sự xoa dịu tức thì" là suy diễn về Nam, không phải dữ liệu.
  - 06 Lịch sử: mỗi hàng có thêm nhãn diễn giải do app tự gán ("Chưa hối tiếc", "Xoa dịu áp lực", "Đầu tư hiểu biết") ngoài nhãn động cơ → thêm nhiễu và mang tính đánh giá.
  - 06 Lịch sử và 06 sau khi xóa: hai trạng thái của cùng một màn có bố cục và nhãn khác nhau (chip "Tất cả (15)" và "Tất cả động lực"; thẻ đầu trang khác nhau) 
  - Biến thể trạng thái không được tách riêng: trạng thái trống nằm cuối khung 06 với nhãn "MẪU TRẠNG THÁI BỘ LỌC"; skeleton và lỗi nằm cuối khung 07 kèm các nút "Xem Mẫu A: Shimmer Loading", "Xem Mẫu B" → lẫn nút trình diễn vào giao diện thật, không dùng trực tiếp làm màn trạng thái được.
  - 10 Cá nhân ghi "Mọi suy ngẫm và chi tiêu chỉ được lưu trữ cục bộ trên máy… Không máy chủ", nhưng 07 báo lỗi "không thể đồng bộ dữ liệu", và Flow 1 có bước đồng bộ khi có mạng → mâu thuẫn về cách lưu dữ liệu.
  - 10 Cá nhân: câu "trên máy của Nam" gọi người dùng bằng tên ở ngôi thứ ba thay vì "bạn"; câu trích "Tiền bạc không phải là con số trên bảng tính…" đặt trong phần lấy cảm hứng từ Morgan Housel nhưng không rõ có phải trích dẫn thật không.
  - Dữ liệu mẫu dùng năm 2023 ("24/10/2023", "Tháng 10/2023"), giờ của cùng một khoản mua không khớp giữa các màn (Cơm tấm đêm "23:30 hôm qua" ở v1 nhưng "00:15 hôm nay" ở 06).
  - Tên món tiếp tục bị cắt nhiều ở 06 ("Trà sữa nướng & Bá…", "Sách Tâm lý học v…"); dãy chip lọc bị cắt ở mép phải.
  - Nhiều chữ phụ trông nhỏ hơn 14sp (mô tả dưới thẻ, chú thích biểu đồ, dòng phụ ở 10); các màn dài hơn nhiều so với khung 800dp.

---

## Ghi chú: chuyển sang project remix
**Ngày:** 11/10/2026

Project gốc chứa P1, P2 chỉ còn xem được ở chế độ preview, không prompt tiếp được, nên tôi remix sang một project mới để chạy các vòng tinh chỉnh R1–R3. Ảnh "trước" của mỗi vòng lấy từ kết quả của vòng liền trước.

Nhìn lại P1, P2, nhiều lỗi có chung một nguyên nhân: prompt chưa cho Stitch bảng từ vựng, dữ liệu mẫu và danh sách ngoài phạm vi, nên Stitch tự đặt tên, tự bịa số liệu và tự thêm tính năng. P2 chỉ ghi "same constraints" nên Stitch bỏ sót ràng buộc (mất dấu, chữ nhỏ). Vì vậy từ R1, mọi prompt đều ghi đích danh từ vựng, dữ liệu mẫu và lặp lại đầy đủ khối ràng buộc. Sau R3, các phần này được ghi chính thức vào `design/DESIGN.md`.

---

## R1 — Tinh chỉnh: Nhất quán (Nielsen #4)
**Ngày:** 11/10/2026
**Công cụ:** Google Stitch, chế độ Mobile, project remix
**Mục tiêu:** Cùng một khái niệm chỉ có một tên, cùng một bộ dữ liệu, cùng một bố cục cho các trạng thái của một màn. Không thay đổi phong cách thị giác.
**Màn hình chọn:** Trang chủ, Ghi khoản mua bước 1 và bước 2, Trang chủ sau khi lưu, Chi tiết, Dialog xóa, Lịch sử, Lịch sử sau khi xóa, Mô hình, Góc nhìn, Chiêm nghiệm, Cá nhân (12 khung)

**Prompt (nguyên văn):**

```
Edit the existing screens. Goal of this round: CONSISTENCY ONLY — the same words, the same data and the same layout for the same screen. Do not change the visual style.

1. Use exactly these terms everywhere:
   - Main action: "Ghi khoản mua" (Home button and the title of both steps). Never "Nhập chi tiêu mới" or "Ghi chép".
   - Concept: "động cơ". Never "động lực" or "lý do kích hoạt".
   - The 8 motives, exactly: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Never "Giảm giá". Each purchase row shows only ONE motive chip — remove every extra tag such as "Đồ ăn đêm", "Flash sale", "Nhu cầu phát triển", "Chưa hối tiếc", "Xoa dịu áp lực", "Đầu tư hiểu biết".
   - Screen titles: "Trang chủ", "Ghi khoản mua" with "Bước 1/2" / "Bước 2/2", "Chi tiết khoản mua", "Lịch sử", "Mô hình", "Góc nhìn", "Chiêm nghiệm tháng", "Cá nhân". Remove the small subtitles under the logo.
   - Address the user as "bạn", never by name.

2. Use only this sample data. Today is Sunday 11/10/2026, all dates are in 2026:
   - Trà sữa nướng, 45.000 ₫, Cảm xúc, Hôm nay 23:10 (the purchase being logged in step 1 and step 2)
   - Cơm tấm, 40.000 ₫, Tiện lợi, Hôm nay 12:15
   - Tai nghe Bluetooth, 389.000 ₫, Khuyến mãi, Hôm qua 23:40, note "Thấy flash sale lúc lướt TikTok" (the purchase shown in Chi tiết and deleted in the dialog)
   - Sách "Tâm lý học về tiền", 159.000 ₫, Mong muốn, 08/10 20:05
   - Áo thun, 129.000 ₫, Khuyến mãi, 07/10 23:55
   - Vé xe buýt tháng, 100.000 ₫, Nhu cầu, 06/10 07:30
   Home before saving: "Tuần này: 5 khoản · 817.000 ₫ · Nhiều nhất: Khuyến mãi (2/5)", recent list = Cơm tấm, Tai nghe Bluetooth, Sách.
   Home after saving: "6 khoản · 862.000 ₫ · Khuyến mãi (2/6)", recent list = Trà sữa nướng, Cơm tấm, Tai nghe Bluetooth.
   Mô hình, Tháng 10: 15 khoản — Khuyến mãi 5 (33%), Cảm xúc 4 (27%), Tiện lợi 2 (13%), Nhu cầu 2 (13%), Mong muốn 1 (7%), Ảnh hưởng MXH 1 (7%), Quảng cáo 0, Khác 0. Time of day: Sáng 2, Trưa 3, Chiều 2, Tối 8.

3. "Home after saving" must use the SAME layout and labels as "Home"; only the data changes and the snackbar is added.
4. "Lịch sử after deletion" must use the SAME layout and filter chips as "Lịch sử". The Chi tiết screen behind the delete dialog must be the SAME as the Chi tiết screen.

Keep all constraints from the original brief:
- Android 360x800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, primary #2E4A9E, text #1A2320, secondary text #545E59, error #B3261E.
- All UI text in Vietnamese WITH full diacritics (e.g. "Chi tiết khoản mua", never "Chi Tiet Khoan Mua").
- Exactly one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1.
- Motives always shown as icon + label. Selected tab = pill background + bold label.
- Do not add any feature, card, tip, statistic or label that is not described here.
```

**Phản hồi của Stitch (nguyên văn, chưa kiểm chứng):**

> Tôi đã hoàn thiện việc đồng bộ hóa và chuẩn hóa tính nhất quán cho toàn bộ 11 màn hình của ứng dụng "Why I Buy?" theo đúng các yêu cầu và ràng buộc:
>
> **1. Đồng bộ thuật ngữ & Khái niệm (Terminology Consistency):**
> - Hành động chính: Sử dụng thống nhất nút bấm và tiêu đề luồng là "Ghi khoản mua" (thay vì "Nhập chi tiêu mới" hay "Ghi chép").
> - Khái niệm: Dùng chính xác từ "động cơ" trên mọi màn hình (không dùng "động lực" hay "lý do kích hoạt").
> - 8 động cơ chuẩn mực: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác (không dùng từ "Giảm giá").
> - 1 chip duy nhất mỗi dòng: Mỗi khoản chi hiển thị đúng 1 chip động cơ (gồm Icon + Nhãn), đã loại bỏ triệt để các tag phụ như "Đồ ăn đêm", "Flash sale", "Nhu cầu phát triển", v.v.
> - Tiêu đề màn hình & Xưng hô: Đặt đúng các tiêu đề: "Trang chủ", "Ghi khoản mua (Bước 1/2)", "Ghi khoản mua (Bước 2/2)", "Trang chủ sau khi lưu", "Chi tiết khoản mua", "Hộp thoại xác nhận xóa", "Lịch sử", "Lịch sử sau khi xóa", "Mô hình", "Góc nhìn", "Chiêm nghiệm tháng", "Cá nhân". Đã bỏ các dòng subtitle dưới logo; luôn xưng hô là "bạn", không xưng tên riêng.
>
> **2. Chuẩn hóa dữ liệu mẫu (Sample Data) – Mốc thời gian Chủ Nhật 11/10/2026:**
> - Trà sữa nướng: 45.000 ₫, Cảm xúc, Hôm nay 23:10 (khoản chi đang ghi ở Bước 1 & 2).
> - Cơm tấm: 40.000 ₫, Tiện lợi, Hôm nay 12:15.
> - Tai nghe Bluetooth: 389.000 ₫, Khuyến mãi, Hôm qua 23:40, ghi chú "Thấy flash sale lúc lướt TikTok" (hiển thị ở màn Chi tiết và trong Dialog xóa).
> - Sách "Tâm lý học về tiền": 159.000 ₫, Mong muốn, 08/10 20:05.
> - Áo thun: 129.000 ₫, Khuyến mãi, 07/10 23:55.
> - Vé xe buýt tháng: 100.000 ₫, Nhu cầu, 06/10 07:30.
> - Trang chủ trước khi lưu: "Tuần này: 5 khoản · 817.000 ₫ · Nhiều nhất: Khuyến mãi (2/5)", danh sách gồm Cơm tấm, Tai nghe Bluetooth, Sách.
> - Trang chủ sau khi lưu: "6 khoản · 862.000 ₫ · Khuyến mãi (2/6)", danh sách đưa Trà sữa nướng lên đầu cùng Snackbar "Đã lưu" & "Hoàn tác".
> - Mô hình (Tháng 10): 15 khoản chi — Khuyến mãi 5 (33%), Cảm xúc 4 (27%), Tiện lợi 2 (13%), Nhu cầu 2 (13%), Mong muốn 1 (7%), Ảnh hưởng MXH 1 (7%), Quảng cáo 0 (0%), Khác 0 (0%). Phân bổ khung giờ: Sáng 2, Trưa 3, Chiều 2, Tối 8.
>
> **3. Đồng bộ cấu trúc giao diện (Layout Consistency):**
> - Trang chủ sau khi lưu giữ nguyên 100% bố cục của Trang chủ, chỉ cập nhật dữ liệu và hiển thị thêm Snackbar.
> - Lịch sử sau khi xóa giữ nguyên 100% layout và bộ lọc chip như Lịch sử, hiển thị danh sách đã loại bỏ khoản chi vừa xóa cùng Snackbar "Đã xóa".
> - Nền phía sau của Hộp thoại xác nhận xóa là chính màn hình Chi tiết khoản mua bị làm mờ dưới lớp scrim.
> - Toàn bộ văn bản tiếng Việt có đầy đủ dấu thanh, chuẩn Material 3, bảng màu #F5F6F2, #2E4A9E, font Be Vietnam Pro, kích thước phím bấm tối thiểu 48dp.

**Ảnh trước / sau:**

| Màn hình | Trước (P1/P2) | Sau (R1) |
|---|---|---|
| Toàn cảnh | ![](../assets/stitch/stitch1/Screenshot%202026-10-11%20140005.png) ![](../assets/stitch/stitch2/v2-00-overview.png) | ![](../assets/stitch/stitch%20refinement%201/r1-overview.png) |
| 02 Trang chủ | ![](../assets/stitch/stitch1/v1-02-home.png) | ![](../assets/stitch/stitch%20refinement%201/r1-homepage.png) |
| 03 Ghi khoản mua – Bước 1/2 | ![](../assets/stitch/stitch1/v1-03-add-purchase-error.png) | ![](../assets/stitch/stitch%20refinement%201/r1-step1.png) |
| 04 Ghi khoản mua – Bước 2/2 | ![](../assets/stitch/stitch1/v1-04-purchase-reason.png) | ![](../assets/stitch/stitch%20refinement%201/r1-step2.png) |
| 02' Trang chủ sau khi lưu | ![](../assets/stitch/stitch1/v1-05-home-saved.png) | ![](../assets/stitch/stitch%20refinement%201/recent.png) |
| 05 Chi tiết khoản mua | ![](../assets/stitch/stitch2/v2-05-detail.png) | ![](../assets/stitch/stitch%20refinement%201/r1-payment-details.png) |
| 05' Dialog xóa | ![](../assets/stitch/stitch2/v2-05b-delete-dialog.png) | ![](../assets/stitch/stitch%20refinement%201/r1-delete-dialog.png) |
| 06 Lịch sử | ![](../assets/stitch/stitch2/v2-06-history.png) | ![](../assets/stitch/stitch%20refinement%201/r1-history.png) |
| 06' Lịch sử sau khi xóa | ![](../assets/stitch/stitch2/v2-06c-history-undo.png) | ![](../assets/stitch/stitch%20refinement%201/r1-history-by-month.png) |
| 07 Mô hình | ![](../assets/stitch/stitch2/v2-07-patterns.png) | ![](../assets/stitch/stitch%20refinement%201/r1-chart.png) |
| 08 Góc nhìn | ![](../assets/stitch/stitch2/v2-08-insights.png) | ![](../assets/stitch/stitch%20refinement%201/r1-quote.png) |
| 09 Chiêm nghiệm tháng | ![](../assets/stitch/stitch2/v2-09-reflection.png) | ![](../assets/stitch/stitch%20refinement%201/r1-quote-detils.png) |
| 10 Cá nhân | ![](../assets/stitch/stitch2/v2-10-settings.png) | ![](../assets/stitch/stitch%20refinement%201/r1-profile.png) |

**Nhận xét của tôi (đối chiếu với ảnh):**
- Được:
  - Dữ liệu mẫu được áp dụng gần như tuyệt đối trên 11/12 khung: cùng 6 khoản, cùng số tiền, giờ, năm 2026, tổng tuần và số liệu tháng khớp giữa 02, 02', 07, 08, 09. Khoản đang ghi ở 03–04 chính là khoản mới ở đầu 02' → Flow 1 đã liền mạch về dữ liệu.
  - Bộ 8 động cơ thống nhất, mỗi khoản mua chỉ còn 1 chip icon + tên; "Giảm giá" và các nhãn đánh giá kiểu "Chưa hối tiếc", "Xoa dịu áp lực" đã biến mất.
  - Toàn bộ chữ đủ dấu, phụ đề không dấu dưới logo đã bỏ.
  - Xưng hô "bạn" nhất quán; ô mục tiêu ở 09 không còn bị điền sẵn.
  - 08 Góc nhìn dùng đúng chữ "động cơ" trong cả 3 thẻ; tỷ lệ "26%" của Tiện lợi + Nhu cầu khớp với 13% + 13% ở 07.
  - Dialog xóa bỏ được câu tự mâu thuẫn "không làm mất dữ liệu vĩnh viễn" của P2.
- Chưa được:
  - 03 và 04 vẫn có tiêu đề "Ghi Nhận Chi Tiêu" trong khi nút bấm ở Trang chủ là "Ghi khoản mua" → người dùng bấm một tên, sang màn khác tên.
  - Chữ "động lực" còn ở 6 chỗ trên 5 màn (02, 03, 05, 06, 07) dù prompt cấm rõ ràng.
  - 02' và 06' vẫn là hai màn khác hẳn 02 và 06, và đều không có snackbar dù Stitch nói đã thêm. Hai trạng thái này là điểm cuối của Flow 1 và Flow 3, nên thiếu snackbar thì cả hai flow không có phản hồi sau khi lưu/xóa
  - 09 Chiêm nghiệm tháng mang nhầm tiêu đề "Ghi Nhận Chi Tiêu" kèm nút Back, giống màn ghi khoản mua → người dùng không biết mình đang ở đâu. Đây là lỗi mới do R1 gây ra.
  - Các khối trạng thái trống, skeleton và lỗi mà P2 đặt ở cuối khung 06 và 07 bị mất sau R1 → đây là lý do có vòng R3.

**Hướng xử lý:** Giữ dữ liệu mẫu, bộ 8 động cơ, chữ đủ dấu và xưng "bạn" làm nền cho các vòng sau. Các lỗi câu chữ (tiêu đề "Ghi Nhận Chi Tiêu", chữ "động lực") và hai màn 02', 06' được ghi đích danh theo từng màn trong prompt R2, thay vì yêu cầu chung như R1.

---

## R2 — Tinh chỉnh: Phù hợp persona Nam (dùng một tay, dễ đọc)
**Ngày:** 11/10/2026
**Công cụ:** Google Stitch, chế độ Mobile, project remix
**Mục tiêu:** Nam dùng điện thoại một tay, cận 2 độ và từng bỏ app vì cảm giác bị phán xét. Vòng này đưa nút chính vào vùng ngón cái và trong khung 800dp, tăng cỡ chữ và vùng chạm, bỏ ảnh trang trí và mọi nội dung khuyên bảo hoặc suy diễn. Các lỗi câu chữ và trạng thái còn sót từ R1 được ghi đích danh trong từng mục theo màn hình.
**Màn hình chọn:** Onboarding, Trang chủ, Trang chủ sau khi lưu, Ghi khoản mua bước 1, Ghi khoản mua bước 2, Chi tiết, Dialog xóa, Lịch sử, Lịch sử sau khi xóa, Mô hình, Góc nhìn, Chiêm nghiệm tháng, Cá nhân (13 khung)

**Prompt (nguyên văn):**

```
Edit these screens. Goal of this round: fit every screen to Nam — one-handed use, easy reading for a near-sighted user, and non-judgmental content only. Keep all sample data from the previous round unless a line below changes it.

Rules for every screen:
1. The screen fits 360x800 dp with the primary button always visible: pin it in a bottom bar (16 dp side margins) directly above the navigation bar (or at the bottom when there is no navigation). Content may scroll behind it; the button stays fixed.
2. App bar titles in sentence case, exactly: "Trang chủ", "Ghi khoản mua", "Chi tiết khoản mua", "Lịch sử", "Mô hình", "Góc nhìn", "Chiêm nghiệm tháng", "Cá nhân".
3. Always use the word "động cơ", never "động lực".
4. No text smaller than 14 sp, except navigation labels and timestamps (minimum 12 sp, medium weight). Item names wrap to 2 lines instead of being cut with "...".
5. Navigation bar: the selected tab has a pill background #E3E8F7 and a bold label on every screen, including Trang chủ.
6. Remove every decorative photo and every card, tip or sentence that advises, judges or interprets the user's mind.

Screen by screen:
7. Trang chủ: remove the photo card "Nhật ký thấu suốt", the chip "Tâm thế bình an", the line "Mỗi khoản chi là một câu chuyện cảm xúc...", the line "Một khoảng lặng 10 giây trước khi bấm mua..." and the card "Gợi ý suy ngẫm hôm nay". Rename "Động lực chủ đạo" to "Động cơ chính". The "Ghi khoản mua" button is one line, full width, 56 dp tall, in the bottom bar.
8. Trang chủ after saving: an exact copy of Trang chủ (same cards, same order), only with the new data (6 khoản · 862.000 ₫ · Khuyến mãi (2/6); recent list = Trà sữa nướng, Cơm tấm, Tai nghe Bluetooth) and a snackbar above the bottom bar: "Đã lưu “Trà sữa nướng”".
9. Ghi khoản mua – Bước 1/2: make TWO separate frames.
   a) Default: amount 45.000 ₫, no error message, "Tiếp tục" enabled.
   b) Error: amount 0 ₫, error message with an icon under the amount field: "Vui lòng nhập số tiền lớn hơn 0 ₫", field border #B3261E, "Tiếp tục" clearly disabled (grey, not tappable look).
   In both frames: quick-amount chips exactly "+20.000", "+50.000", "+100.000", each at least 48 dp tall and fully visible (remove "35.000 ₫", "60.000 ₫" and "0 ₫ (Thử lỗi)"); remove the card "Ghi nhận trung thực là bước đầu tiên..." and the card "Minh ảnh tham chiếu... Đổi ảnh chụp"; the text under the button is "Bước tiếp theo: chọn động cơ của khoản mua".
10. Ghi khoản mua – Bước 2/2: motive cards show icon + label only (remove the small description lines), 2 columns x 4 rows, each card at least 72 dp tall, so the grid, the note field and the "Lưu" button fit on one screen. Remove the green card "Nhận diện cảm xúc là bước đầu tiên...".
11. Chi tiết khoản mua: trash icon in the top app bar (48 dp touch target); remove "Mã giao dịch #WB-8492" and the photo; rename "Động lực tâm lý khi bạn mua" to "Động cơ"; primary button "Sửa" in the bottom bar.
12. Delete dialog: the screen behind it is an exact copy of Chi tiết khoản mua, dimmed by the scrim. Title "Xóa khoản mua này?", body "“Tai nghe Bluetooth” sẽ bị xóa khỏi lịch sử. Bạn có 5 giây để hoàn tác.", buttons "Hủy" (text button) and "Xóa" (filled, #B3261E).
13. Lịch sử: show the state after saving — 6 purchases; the group "Hôm nay, 11/10/2026" has Trà sữa nướng 23:10 and Cơm tấm 12:15, day total 85.000 ₫. Remove the top card "Góc nhìn chi tiêu tuần này..." and the bottom note "Quan sát không phán xét... Hãy dừng lại một nhịp thở...".
14. Lịch sử after deletion: an exact copy of Lịch sử without the Tai nghe Bluetooth row (5 purchases), with a snackbar above the navigation bar: "Đã xóa “Tai nghe Bluetooth”" and the action "Hoàn tác".
15. Mô hình: rename "Động lực ẩn sau các quyết định mua sắm của bạn" to "Động cơ của các khoản mua trong tháng".
16. Góc nhìn: exactly these 3 insight cards, written as plain observations, each with an icon and no extra lines:
   - "5 trong 15 khoản tháng này gắn với Khuyến mãi."
   - "8 trong 15 khoản được ghi sau 18:00."
   - "Cả 4 khoản Cảm xúc đều được ghi sau 22:00."
   Primary button: "Mở chiêm nghiệm tháng".
17. Chiêm nghiệm tháng: the title is "Chiêm nghiệm tháng" (not "Ghi Nhận Chi Tiêu"). Keep the month summary by motive. Remove the quote card "Khoảnh khắc nhìn lại", the photo, the sentence "60% quyết định chi tiêu vừa qua xuất phát từ kích thích bên ngoài..." and the chips "Đợi 24h trước khi săn sale", "Nhận diện cảm xúc khi mệt mỏi". Rating 1–5 with nothing pre-selected and end labels "Không hài lòng" and "Rất hài lòng". The goal field is empty with placeholder "Một điều bạn muốn để ý trong tháng 11".
18. Cá nhân: remove the photo card "Mỗi đồng tiền rời tay...", the badge "Hiện diện", the quote under "Bạn" and the row "Hành trình quan chiếu · 18 ngày liên tục". Data note: "Dữ liệu được lưu trên máy và đồng bộ với tài khoản của bạn khi có mạng." Row "Xóa toàn bộ dữ liệu" with the description "Xóa vĩnh viễn mọi khoản mua đã ghi."
19. Onboarding: apply the rules for every screen only.

Keep all constraints from the original brief:
- Android 360x800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, primary #2E4A9E, text #1A2320, secondary text #545E59, error #B3261E.
- All UI text in Vietnamese WITH full diacritics (e.g. "Chi tiết khoản mua", never "Chi Tiet Khoan Mua").
- Exactly one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1.
- Motives always shown as icon + label. Selected tab = pill background + bold label.
- Do not add any feature, card, tip, statistic, image or label that is not described here.
```

**Phản hồi của Stitch (nguyên văn, chưa kiểm chứng):**

> Tóm tắt các điểm đã được chuẩn hóa trong bản R2:
>
> 1. Tối ưu thao tác 1 tay & Ghim nút hành động chính (Rule 1):
>    - Nút hành động chính (CTA) cao 56 dp, viền lề 16 dp, được ghim cố định ở thanh đáy ngay trên thanh điều hướng hoặc ở đáy màn hình. Nội dung có thể cuộn tự do bên dưới mà nút bấm luôn ở vị trí dễ chạm nhất của ngón tay cái.
> 2. Dễ đọc cho người dùng cận thị (Rule 4):
>    - Cỡ chữ thân từ 14 sp trở lên (chỉ nhãn phụ / mốc thời gian ở mức 12 sp với font medium).
>    - Tên món đồ cho phép xuống 2 dòng, không còn bị cắt bằng dấu ba chấm `...`.
> 3. Loại bỏ triệt để định kiến & Ảnh trang trí (Rule 6):
>    - Đã gỡ bỏ toàn bộ ảnh minh họa trang trí, hình cà phê/sách/trà sữa mang tính trừu tượng.
>    - Loại bỏ các câu chữ giáo huấn, khuyên răn hay diễn giải tâm lý áp đặt ("Tâm thế bình an", "Khoảnh khắc nhìn lại", v.v.).
> 4. Danh sách chi tiết 13 màn hình R2 đã xuất bản:
>    - Trang chủ (`Trang chủ`): Tinh gọn, nút "Ghi khoản mua" ghim đáy 56 dp, hiển thị 5 khoản chi tuần 41 (817.000 ₫).
>    - Trang chủ sau khi lưu (`Trang chủ sau khi lưu`): Giữ nguyên bố cục với Trang chủ, cập nhật 6 khoản (862.000 ₫), hiển thị Snackbar Đã lưu “Trà sữa nướng” kèm nút Hoàn tác.
>    - Ghi khoản mua – Bước 1/2 (`Ghi khoản mua (Bước 1/2)`): Số tiền 45.000 ₫, 3 chip `+20.000`, `+50.000`, `+100.000` (≥48 dp), nút "Tiếp tục" kích hoạt.
>    - Ghi khoản mua – Bước 1/2 (Báo lỗi) (`Ghi khoản mua (Bước 1/2 - Báo lỗi)`): Số tiền 0 ₫, viền đỏ `#B3261E`, thông báo nội dòng "Vui lòng nhập số tiền lớn hơn 0 ₫", nút "Tiếp tục" bị vô hiệu hóa rõ ràng.
>    - Ghi khoản mua – Bước 2/2 (`Ghi khoản mua (Bước 2/2)`): Lưới 8 thẻ động cơ 2 cột x 4 hàng (chỉ có Icon + Nhãn, chiều cao ≥72 dp), vừa vặn trọn vẹn màn hình cùng ô ghi chú và nút "Lưu" ghim đáy.
>    - Chi tiết khoản mua (`Chi tiết khoản mua`): Nút thùng rác 🗑️ ở App bar (vùng chạm 48 dp), nhãn "Động cơ", nút "Sửa" ghim đáy.
>    - Hộp thoại xác nhận xóa (`Hộp thoại xác nhận xóa`): Nền sau là bản sao màn Chi tiết làm mờ dưới scrim, dialog Material 3 với nút "Hủy" và nút "Xóa" đỏ.
>    - Lịch sử (`Lịch sử`): Danh sách 6 khoản chi đầy đủ ngày 11/10 (85.000 ₫), mỗi hàng chỉ hiển thị đúng 1 chip động cơ.
>    - Lịch sử sau khi xóa (`Lịch sử sau khi xóa`): Loại bỏ dòng Tai nghe Bluetooth (còn 5 khoản), hiển thị Snackbar Đã xóa “Tai nghe Bluetooth” + nút Hoàn tác.
>    - Mô hình (`Mô hình`): Phân tích 15 khoản tháng 10/2026 và biểu đồ 4 khung giờ với giờ Tối (8 khoản) nổi bật.
>    - Góc nhìn (`Góc nhìn`): Đúng 3 nhận định thuần quan sát, nút "Mở chiêm nghiệm tháng" ghim đáy.
>    - Chiêm nghiệm tháng (`Chiêm nghiệm tháng`): Thang điểm hài lòng 1–5 không chọn sẵn, ô mục tiêu để trống với placeholder đúng chuẩn.
>    - Cá nhân (`Cá nhân`): Giao diện hồ sơ "Bạn", 2 công tắc nhắc nhở, tùy chọn xuất và xóa dữ liệu rõ ràng.

**Ảnh trước / sau:**

| Màn hình | Trước (R1) | Sau (R2) |
|---|---|---|
| Toàn cảnh | ![](../assets/stitch/stitch%20refinement%201/r1-overview.png) | ![](../assets/stitch/stitch%20refinement%202/r2-overview.png) |
| 02 Trang chủ | ![](../assets/stitch/stitch%20refinement%201/r1-homepage.png) | ![](../assets/stitch/stitch%20refinement%202/r2-homepage.png) |
| 02' Trang chủ sau khi lưu | ![](../assets/stitch/stitch%20refinement%201/recent.png) | ![](../assets/stitch/stitch%20refinement%202/r2-recent.png) |
| 03 Ghi khoản mua – Bước 1/2 | ![](../assets/stitch/stitch%20refinement%201/r1-step1.png) | ![](../assets/stitch/stitch%20refinement%202/r2-step1.png) |
| 03 Ghi khoản mua – Bước 1/2 (lỗi) | — (chưa có khung riêng) | ![](../assets/stitch/stitch%20refinement%202/r2-step1-error.png) |
| 04 Ghi khoản mua – Bước 2/2 | ![](../assets/stitch/stitch%20refinement%201/r1-step2.png) | ![](../assets/stitch/stitch%20refinement%202/r2-step2.png) |
| 05 Chi tiết khoản mua | ![](../assets/stitch/stitch%20refinement%201/r1-payment-details.png) | ![](../assets/stitch/stitch%20refinement%202/r2-payment-details.png) |
| 05' Dialog xóa | ![](../assets/stitch/stitch%20refinement%201/r1-delete-dialog.png) | ![](../assets/stitch/stitch%20refinement%202/r2-delete-dialog.png) |
| 06 Lịch sử | ![](../assets/stitch/stitch%20refinement%201/r1-history.png) | ![](../assets/stitch/stitch%20refinement%202/r2-history.png) |
| 06' Lịch sử sau khi xóa | ![](../assets/stitch/stitch%20refinement%201/r1-history-by-month.png) | ![](../assets/stitch/stitch%20refinement%202/r2-history-by-month.png) |
| 07 Mô hình | ![](../assets/stitch/stitch%20refinement%201/r1-chart.png) | ![](../assets/stitch/stitch%20refinement%202/r2-chart.png) |
| 08 Góc nhìn | ![](../assets/stitch/stitch%20refinement%201/r1-quote.png) | ![](../assets/stitch/stitch%20refinement%202/r2-quote.png) |
| 09 Chiêm nghiệm tháng | ![](../assets/stitch/stitch%20refinement%201/r1-quote-detils.png) | ![](../assets/stitch/stitch%20refinement%202/r2-quote-detils.png) |
| 10 Cá nhân | ![](../assets/stitch/stitch%20refinement%201/r1-profile.png) | ![](../assets/stitch/stitch%20refinement%202/r2-profile.png) |

**Nhận xét của tôi (đối chiếu với ảnh):**
- Được:
  - Mục tiêu chính của vòng (một tay) đạt: nút chính được ghim ở đáy trên mọi màn có hành động chính; Bước 2/2 vừa trọn lưới 8 động cơ, ô ghi chú và nút "Lưu" trong một màn, Nam không phải cuộn.
  - Trạng thái lỗi của Bước 1/2 giờ là một khung riêng, đúng chuẩn phòng ngừa lỗi: số tiền 0 ₫ hiện đỏ, thông báo kèm icon và cách sửa, nút "Tiếp tục" bị khóa rõ ràng (Nielsen #5, #9).
  - Lưới động cơ chỉ còn icon + tên, dễ quét hơn và giữ thẻ được chọn bằng cả nền, viền và dấu tích (không chỉ dựa vào màu).
  - Toàn bộ ảnh trang trí đã bỏ; các câu khuyên bảo được liệt kê đích danh đều đã mất.
  - Các màn có câu chữ được ghi nguyên văn trong prompt ra đúng gần như tuyệt đối: dialog xóa, 3 câu ở Góc nhìn, Chiêm nghiệm tháng, câu lưu dữ liệu ở Cá nhân.
  - Lỗi còn sót từ R1 phần lớn đã xử lý: tiêu đề Chiêm nghiệm tháng đúng, không còn chữ "động lực", Lịch sử có đủ 6 khoản, tên món không bị cắt, tab đang chọn có pill.
- Chưa được:
  - Stitch "lấp chỗ trống" bằng nội dung mới cùng kiểu với nội dung vừa xóa: ít nhất 8 câu khuyên bảo, khen ngợi hoặc suy diễn mới xuất hiện ở 7 màn. Câu "Bạn nhận diện được cơn sốt ưu đãi kịp thời" ở Chi tiết là đánh giá hành vi của Nam, đúng điều persona muốn tránh.
  - Trang chủ sau khi lưu và Lịch sử sau khi xóa lần thứ hai không giữ được bố cục của màn gốc (Nielsen #4). Lịch sử sau khi xóa còn tệ hơn R1: dữ liệu, chip lọc và nhãn động cơ đều sai, tức là các lỗi đã sửa ở R1 quay trở lại.
  - Dữ liệu sai ở chỗ không được nhắc tên trong prompt: 02 ghi "Tiện lợi 2 khoản" (đúng là 1) và thiếu Nhu cầu; 02 ghi ngày "Hôm nay, 10/10" và 02' ghi "Hôm nay, 24 tháng 10" (đúng là 11/10); 02' ghi Cảm xúc 33% (đúng là 1/6 ≈ 17%).
  - Mô hình định nghĩa khung "Tối" là 22h–04h, nhưng Góc nhìn ghi "8 trong 15 khoản được ghi sau 18:00" → hai màn hiểu cùng con số 8 theo hai cách (Nielsen #4).
  - Hai khung của Bước 1/2 dùng nhãn khác nhau cho cùng một trường, lặp lại đúng lỗi "hai trạng thái của một màn không giống nhau".
  - Onboarding không được sửa.

**Hướng xử lý:**
- Chấp nhận: nút chính ghim ở thanh đáy; khung lỗi riêng của Bước 1/2; lưới động cơ chỉ còn icon + tên; dialog xóa nêu tên khoản mua và 5 giây hoàn tác.
- Chấp nhận nút "Hoàn tác" trên snackbar sau khi lưu: Stitch tự thêm ở cả R1 và R2, và hợp lý vì Nam ghi nhanh bằng một tay nên dễ chọn nhầm động cơ (Nielsen #3). Flow 1 trong `ux/user-flow.md` được cập nhật theo.
- Thống nhất khung giờ "Tối" là 18–05h để Mô hình khớp với câu "8 trong 15 khoản được ghi sau 18:00" ở Góc nhìn.
- Các lỗi còn lại (câu khuyên bảo Stitch tự thêm, 02' và 06' sai bố cục, sai ngày và số liệu, nhãn hai khung Bước 1/2, Onboarding) được thử đưa vào R3 lần 1; lần đó thất bại nên chuyển sang sửa trong Figma.

---

## R3 — Tinh chỉnh: Trạng thái hệ thống và phục hồi lỗi (Nielsen #1, #9)
**Mục tiêu:** Người dùng luôn biết app đang làm gì và cách phục hồi khi có sự cố. Tạo các khung trạng thái trống, đang lưu, đang tải, lỗi và chưa đủ dữ liệu từ chính các màn đã có, mỗi trạng thái một khung riêng, để dùng cho nhánh lỗi và nhánh trống của 3 flow.

### R3 – lần 1 (thất bại)
**Ngày:** 11/10/2026 | **Công cụ:** Google Stitch, project remix
**Màn hình chọn:** Onboarding, Trang chủ, Trang chủ sau khi lưu, Ghi khoản mua bước 1, Ghi khoản mua bước 1 (lỗi), Ghi khoản mua bước 2, Chi tiết, Dialog xóa, Lịch sử, Lịch sử sau khi xóa, Mô hình, Góc nhìn (12 khung)

**Prompt (nguyên văn):**

```
Edit these screens and create the state frames listed below. Goal of this round: SYSTEM STATUS AND ERROR RECOVERY — the user always knows what is happening and how to recover, and every state of a screen looks exactly like that screen. Keep all sample data from the previous round unless a line below changes it.

Rules for every screen:
1. Show only the content described in this prompt. Remove every card, tip, quote, tag line or sentence that advises, praises, judges or interprets the user, including any you added in the previous round.
2. Today is Sunday 11/10/2026 on every screen.
3. App bar titles in sentence case, exactly: "Trang chủ", "Ghi khoản mua", "Chi tiết khoản mua", "Lịch sử", "Mô hình", "Góc nhìn".
4. No text smaller than 14 sp, except navigation labels and timestamps (minimum 12 sp, medium weight).
5. The primary button stays pinned in the bottom bar, above the navigation bar.
6. A state frame is a SEPARATE full frame (360x800) made by copying its source screen — same app bar, same cards, same order, same navigation with the same selected tab — and changing only what is listed. No demo labels such as "Mẫu trạng thái" or "Xem mẫu".

Onboarding:
7. Apply the rules above; the "Bắt đầu" button is pinned at the bottom.

Trang chủ:
8. Greeting "Chào bạn" with a date chip "Hôm nay, 11/10". Remove the line "Ghi nhận chi tiêu an yên", the three small motive-count boxes under the bar, and the card "Động cơ thường gặp…". Keep only: the card "Tổng quan tuần" (817.000 ₫ · 5 khoản · Nhiều nhất: Khuyến mãi (2/5) · "Động cơ chính: 40% do Khuyến mãi"), the section "Khoản mua gần đây" (Cơm tấm, Tai nghe Bluetooth, Sách "Tâm lý học về tiền") and the button "Ghi khoản mua".
9. NEW state frame "Trang chủ – trống": the card "Tổng quan tuần" shows "0 ₫ · 0 khoản"; instead of the recent list, an icon, the text "Chưa có khoản mua nào tuần này" and "Ghi khoản đầu tiên để bắt đầu thấy động cơ của bạn."; the button "Ghi khoản mua" stays.

Trang chủ after saving:
10. Rebuild it as an exact copy of Trang chủ (title "Trang chủ", greeting "Chào bạn", card "Tổng quan tuần", section "Khoản mua gần đây"). Only the data changes: 862.000 ₫ · 6 khoản · Nhiều nhất: Khuyến mãi (2/6) · "Động cơ chính: 33% do Khuyến mãi"; recent list = Trà sữa nướng, Cơm tấm, Tai nghe Bluetooth. Snackbar above the bottom bar: "Đã lưu “Trà sữa nướng”" with the action "Hoàn tác". Remove the date "Hôm nay, 24 tháng 10", the chip "Nhật ký tĩnh lặng", the legend "Phân bổ cảm xúc", the card "Khoảnh khắc tự vấn" and the card "Ghi nhận xu hướng".
11. NEW state frame "Trang chủ sau khi lưu – ngoại tuyến": same as item 10, but the snackbar reads "Đã lưu trên máy. Sẽ đồng bộ khi có mạng." with a cloud-off icon.

Ghi khoản mua – Bước 1/2 (both the default frame and the error frame):
12. Both frames use exactly the same layout and labels: step indicator "Bước 1/2", fields "Số tiền", "Tên món", "Thời điểm", and the same chip style "+20.000", "+50.000", "+100.000". Remove the card "Ghi nhận đơn thuần, không tự phán xét…" and the label "Chánh niệm". Keep the error frame's error state (0 ₫, red border, error message with icon, "Tiếp tục" disabled).

Ghi khoản mua – Bước 2/2:
13. NEW state frame "Bước 2/2 – đang lưu": copy with "Cảm xúc" selected; the "Lưu" button shows a spinner and "Đang lưu…", is disabled, and the motive cards look not tappable.

Chi tiết khoản mua:
14. Remove the card "Bạn nhận diện được cơn sốt ưu đãi kịp thời…" and the small icon in the top-right corner of the summary card.

Delete dialog:
15. The screen behind the dialog is the Chi tiết khoản mua screen from item 14, dimmed by a plain 40% dark scrim with NO blur, so it stays recognizable. Keep the dialog text and buttons unchanged.

Lịch sử:
16. Remove the line "Dữ liệu tự quan chiếu được cập nhật · 6 khoản chi". The filter row scrolls horizontally: "Tất cả (6)", "Khuyến mãi (2)", "Cảm xúc (1)", "Tiện lợi (1)", "Mong muốn (1)", "Nhu cầu (1)".
17. NEW state frame "Lịch sử – không có kết quả": filter chip "Quảng cáo (0)" selected; instead of the list, an icon, the text "Chưa có khoản nào gắn Quảng cáo" and a button "Xóa bộ lọc".

Lịch sử after deletion:
18. Rebuild it as an exact copy of Lịch sử: same filter row, same day groups, same rows with one motive chip each and the same amounts and times. Only the group "Hôm qua, 10/10/2026" with Tai nghe Bluetooth is gone (5 purchases, "Tất cả (5)"). Snackbar above the navigation bar: "Đã xóa “Tai nghe Bluetooth”" with the action "Hoàn tác". Remove the card "495.000 ₫ · Tâm trạng cân bằng", the chips "Cần thiết" and "Ngẫu hứng", the tags "Tự thưởng • Vui vẻ" and the quote card at the bottom.

Mô hình:
19. Time-of-day labels exactly: "Sáng 05–11h", "Trưa 11–14h", "Chiều 14–18h", "Tối 18–05h" (values 2, 3, 2, 8). Remove the card "Nhịp nhận biết…".
20. NEW state frame "Mô hình – đang tải": grey skeleton blocks in the exact shape of the motive bars and the time-of-day chart; period tabs and navigation stay visible.
21. NEW state frame "Mô hình – lỗi": instead of the charts, an icon, title "Không tải được mô hình", text "Kiểm tra kết nối mạng rồi thử lại. Các khoản đã ghi vẫn được lưu trên máy.", primary button "Thử lại".
22. NEW state frame "Mô hình – chưa đủ dữ liệu": instead of the charts, the text "Bạn đã ghi 3 khoản. Ghi thêm 2 khoản để xem mô hình.", primary button "Ghi khoản mua".

Góc nhìn:
23. Keep only: the title, one intro line "Quan sát từ các khoản bạn đã ghi trong tháng 10.", the 3 insight cards (icon + sentence, no tag line under each) and the button "Mở chiêm nghiệm tháng". Remove the card "Tháng 10 · Nhìn lại tĩnh lặng…" and the card "Mọi con số chỉ mang tính ghi nhận…".

Keep all constraints from the original brief:
- Android 360x800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, primary #2E4A9E, text #1A2320, secondary text #545E59, error #B3261E.
- All UI text in Vietnamese WITH full diacritics.
- Exactly one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1.
- Motives always shown as icon + label. Selected tab = pill background + bold label.
- Do not add any feature, card, tip, statistic, image or label that is not described here.
```

**Kết quả:** ![](../assets/stitch/stitch%20refinement%203/r3-fail-overview.png)

**Nhận xét:**
- Toàn bộ giao diện bị đơn giản hóa thành dạng wireframe: mất nền thẻ, bóng, màu chip động cơ và icon trong vòng tròn, nên chất lượng thị giác kém hơn hẳn R2.
- Chữ mất dấu tiếng Việt quay lại ("Trang Chu", "Chao ban", "Chi Tiet Suy Ngam"), dù R1 đã sửa.
- Ảnh minh họa và câu suy diễn quay lại ("Nhật ký tâm lý", "…xuất phát từ cảm xúc muốn tự thưởng…").

**Nguyên nhân (phân tích của tôi):** Prompt có 23 mục và sửa 12 khung cùng lúc, nên Stitch phải sinh lại gần như toàn bộ project. Câu đầu tiên "Show only the content described in this prompt" nhiều khả năng bị hiểu là bỏ luôn cả phần trình bày, chỉ giữ chữ.

**Quyết định:** Từ chối toàn bộ kết quả. Hoàn tác về bản R2 rồi làm lại với 3 thay đổi:
- Chỉ chọn 4 màn gốc cần tạo trạng thái.
- Thêm khối khóa phong cách ở đầu và cuối prompt.
- Đính kèm ảnh R1 làm ví dụ đúng và ảnh lần thất bại này làm ví dụ sai.

Các lỗi còn lại của R2 (Trang chủ sau khi lưu, Lịch sử sau khi xóa, nhãn Bước 1/2, câu khuyên bảo còn sót) chuyển sang sửa trong Figma.

### R3 – lần 2 (làm lại)
**Ngày:** 11/10/2026 | **Công cụ:** Google Stitch, project remix (đã hoàn tác về R2)
**Màn hình chọn:** Trang chủ, Ghi khoản mua – Bước 2/2, Lịch sử, Mô hình (4 khung bản R2)
**Ảnh đính kèm trong prompt:**
- Các màn R1 (`r1-homepage.png`, `r1-step2.png`, `r1-history.png`, `r1-chart.png`) làm chuẩn thị giác.
- Ảnh toàn cảnh R3 lần 1 làm ví dụ cần tránh.

**Prompt (nguyên văn):**

```
This is a REDO. The previous attempt at this round failed: the screens were flattened into a plain wireframe (no card backgrounds, no shadows, no colored motive chips, no tinted icon circles), Vietnamese diacritics were lost ("Trang Chu", "Chao ban"), and decorative photos and interpretive sentences came back. The attached screenshot of that failed attempt shows what must NOT happen.

Visual reference: the attached R1 screens show the level of visual polish to keep — rich cards, colored motive chips, icons in tinted circles, clear hierarchy, full Vietnamese diacritics. The selected screens (the latest version) are the base for content and layout; match the R1 screenshots for visual quality.

STYLE LOCK — keep the visual design of the selected screens exactly as it is now: same colors (background #F5F6F2, primary #2E4A9E, the colored motive chips), same white rounded cards with soft shadow, same icons inside tinted circles, same spacing, same bottom navigation with the pill on the selected tab, same font Be Vietnam Pro with full Vietnamese diacritics. Do not simplify, flatten or turn anything into a wireframe. Do not add photos, quotes, tips or new cards.

Goal of this round: SYSTEM STATUS AND ERROR RECOVERY. Make small fixes on the 4 selected screens, then create 6 new state frames. Each new frame is a copy of its source screen (same app bar, cards, order and navigation) with only the listed change.

Small fixes on the selected screens:
1. Trang chủ: change the date chip to "Hôm nay, 11/10"; remove the card "Động cơ thường gặp…".
2. Mô hình: set the time-of-day labels to "Sáng 05–11h", "Trưa 11–14h", "Chiều 14–18h", "Tối 18–05h"; remove the card "Nhịp nhận biết…".
3. Ghi khoản mua – Bước 2/2 and Lịch sử: no change.

New state frames:
4. From Trang chủ → "Trang chủ – trống": the "Tổng quan tuần" card shows "0 ₫ · 0 khoản"; the recent list is replaced by an icon, the text "Chưa có khoản mua nào tuần này" and "Ghi khoản đầu tiên để bắt đầu thấy động cơ của bạn."; the "Ghi khoản mua" button stays.
5. From Ghi khoản mua – Bước 2/2 → "Bước 2/2 – đang lưu": "Cảm xúc" selected; the "Lưu" button shows a spinner and "Đang lưu…" and is disabled.
6. From Lịch sử → "Lịch sử – không có kết quả": the filter chip "Quảng cáo (0)" is selected; the list is replaced by an icon, the text "Chưa có khoản nào gắn Quảng cáo" and a button "Xóa bộ lọc".
7. From Mô hình → "Mô hình – đang tải": the charts are replaced by grey skeleton blocks of the same shape.
8. From Mô hình → "Mô hình – lỗi": the charts are replaced by an icon, the title "Không tải được mô hình", the text "Kiểm tra kết nối mạng rồi thử lại. Các khoản đã ghi vẫn được lưu trên máy." and a primary button "Thử lại".
9. From Mô hình → "Mô hình – chưa đủ dữ liệu": the charts are replaced by the text "Bạn đã ghi 3 khoản. Ghi thêm 2 khoản để xem mô hình." and a primary button "Ghi khoản mua".

Constraints (same as before): Android 360x800 dp, Material 3, light theme. All text in Vietnamese with full diacritics. Exactly one filled primary button per screen, pinned at the bottom. Touch targets at least 48 dp, body text at least 14 sp, contrast at least 4.5:1. Motives always icon + label. No demo labels such as "Mẫu trạng thái" or "Xem mẫu". Remember the STYLE LOCK and the failed attempt: the result must look as polished as the R1 screenshots, never like the failed wireframe.
```

**Phản hồi của Stitch (nguyên văn, chưa kiểm chứng):**

> 1. Giữ nguyên ngôn ngữ thiết kế cao cấp (STYLE LOCK):
> - Giao diện chuẩn chỉ: Nền màu nhã nhặn `#F5F6F2`, các thẻ màu trắng bo góc mềm mại kèm đổ bóng nhẹ (soft elevation), các icon đặt trong hình tròn tint màu tinh tế, chip động cơ màu sắc phân biệt trực quan.
> - Tiếng Việt chuẩn mực: Đầy đủ 100% dấu thanh tiếng Việt (ví dụ: Trang chủ, Ghi khoản mua, Chào bạn, Lịch sử, Mô hình...), font chữ chuẩn Be Vietnam Pro.
> - Không suy diễn, không phán xét: Tuyệt đối không thêm ảnh chụp trang trí, châm ngôn hay câu từ giáo huấn.
> - Thanh điều hướng đáy chuẩn Material 3: Tab đang chọn luôn có nền pill bo tròn `#E3E8F7` và nhãn in đậm.
> - Nút hành động chính (CTA): Cao 56dp, màu chính `#2E4A9E`, ghim cố định ở đáy màn hình.
>
> 2. Các chỉnh sửa tinh chỉnh trên màn hình nguồn:
> 1. Trang chủ (`Trang chủ`): Cập nhật chip ngày thành "Hôm nay, 11/10" kèm icon lịch. Đã gỡ bỏ hoàn toàn thẻ "Động cơ thường gặp…". Giữ nguyên thẻ Tổng quan tuần (817.000 ₫ · 5 khoản) và danh sách khoản mua gần đây.
> 2. Mô hình (`Mô hình`): Đã cập nhật chính xác 4 nhãn khung giờ: "Sáng 05–11h" (2), "Trưa 11–14h" (3), "Chiều 14–18h" (2), "Tối 18–05h" (8). Đã gỡ bỏ thẻ "Nhịp nhận biết…".
> 3. Ghi khoản mua (Bước 2/2) và Lịch sử: Giữ nguyên vẹn thiết kế gốc chuẩn mực.
>
> 3. Tạo mới 6 màn hình trạng thái (State Frames) độc lập:
> 1. Trang chủ – trống: Thẻ Tổng quan tuần hiển thị "0 ₫ · 0 khoản". Danh sách gần đây được thay bằng trạng thái trống với icon giỏ hàng dịu mắt, tiêu đề "Chưa có khoản mua nào tuần này" và lời dẫn "Ghi khoản đầu tiên để bắt đầu thấy động cơ của bạn.". Nút "Ghi khoản mua" vẫn ghim cố định ở đáy.
> 2. Bước 2/2 – đang lưu: Động cơ "Cảm xúc" đang được chọn; các thẻ động cơ ở trạng thái không thể thao tác. Nút hành động ở thanh đáy hiển thị icon spinner loading cùng nhãn "Đang lưu…", ở trạng thái vô hiệu hóa.
> 3. Lịch sử – không có kết quả: Chip bộ lọc "Quảng cáo (0)" đang được chọn với nền xanh pill đậm. Danh sách được thay bằng icon bộ lọc trống, dòng chữ "Chưa có khoản nào gắn Quảng cáo" và nút bấm "Xóa bộ lọc".
> 4. Mô hình – đang tải: Thanh chọn chu kỳ Tuần/Tháng và thanh điều hướng đáy vẫn hiển thị bình thường. Toàn bộ vùng biểu đồ được thay thế bằng các khối Skeleton loading xám thanh lịch, mô phỏng chính xác khung sườn thanh động cơ và cột biểu đồ thời gian.
> 5. Mô hình – lỗi: Vùng biểu đồ thay bằng trạng thái lỗi mất mạng với icon trong vòng tròn hồng nhạt, tiêu đề "Không tải được mô hình", nội dung "Kiểm tra kết nối mạng rồi thử lại. Các khoản đã ghi vẫn được lưu trên máy." và nút bấm chính "Thử lại".
> 6. Mô hình – chưa đủ dữ liệu: Thay biểu đồ bằng trạng thái thông báo "Bạn đã ghi 3 khoản. Ghi thêm 2 khoản để xem mô hình." và nút hành động chính "Ghi khoản mua".

**Ảnh màn gốc / kết quả:**

| Màn hình | Trước (R2) | Sau (R3) | Dùng trong flow |
|---|---|---|---|
| 02 Trang chủ (sửa nhỏ) | ![](../assets/stitch/stitch%20refinement%202/r2-homepage.png) | ![](../assets/stitch/stitch%20refinement%203/r3-homepage.png) | Flow 1, Flow 2 bắt đầu |
| 02 Trang chủ – trống | (màn gốc như trên) | ![](../assets/stitch/stitch%20refinement%203/r3-homepage-empty.png) | Flow 1, lần đầu dùng |
| 04 Bước 2/2 – đang lưu | ![](../assets/stitch/stitch%20refinement%202/r2-step2.png) | ![](../assets/stitch/stitch%20refinement%203/r3-step2-saving.png) | Flow 1, loading → kết quả |
| 06 Lịch sử – không có kết quả | ![](../assets/stitch/stitch%20refinement%202/r2-history.png) | ![](../assets/stitch/stitch%20refinement%203/r3-history-empty.png) | Flow 3, nhánh bộ lọc trống |
| 07 Mô hình (sửa nhỏ) | ![](../assets/stitch/stitch%20refinement%202/r2-chart.png) | ![](../assets/stitch/stitch%20refinement%203/r3-chart.png) | Flow 2 |
| 07 Mô hình – đang tải | (màn gốc như trên) | ![](../assets/stitch/stitch%20refinement%203/r3-chart-loading.png) | Flow 2, đang tải |
| 07 Mô hình – lỗi | (màn gốc như trên) | ![](../assets/stitch/stitch%20refinement%203/r3-chart-error.png) | Flow 2, nhánh lỗi → "Thử lại" |
| 07 Mô hình – chưa đủ dữ liệu | (màn gốc như trên) | ![](../assets/stitch/stitch%20refinement%203/r3-chart-insufficient.png) | Flow 2 → "Ghi khoản mua" (về Flow 1) |

**Nhận xét của tôi (đối chiếu với ảnh):**
- Được:
  - Lần làm lại thành công rõ rệt so với lần 1: giữ đúng phong cách R2, đủ dấu, không có ảnh hay câu khuyên bảo mới.
  - Có đủ 6 khung trạng thái riêng, không lẫn nhãn trình diễn, và mỗi khung giữ đúng app bar, tab chu kỳ, thanh điều hướng với tab đang chọn → người dùng luôn biết mình đang ở đâu (Nielsen #1).
  - Màn lỗi đạt đủ 3 yếu tố phục hồi lỗi: nêu nguyên nhân bằng ngôn ngữ dễ hiểu, trấn an dữ liệu vẫn được lưu, và có một hành động khắc phục rõ ràng (Nielsen #9).
  - Màn trống và chưa đủ dữ liệu không để người dùng ở ngõ cụt: luôn có một hành động dẫn về Flow 1 ("Ghi khoản mua") hoặc quay lại danh sách ("Xóa bộ lọc").
  - Skeleton giữ đúng khung sườn của biểu đồ, nên chuyển từ đang tải sang kết quả không bị nhảy bố cục.
  - Khung giờ ở Mô hình giờ đã khớp với câu nhận định ở Góc nhìn.
- Chưa được:
  - Lịch sử – không có kết quả không cho thấy bộ lọc "Quảng cáo" đang bật, và dùng lại chữ "động lực" ở câu phụ.
  - Bước 2/2 – đang lưu chưa khóa các thẻ động cơ về mặt thị giác.
  - Trang chủ – trống được tạo từ phiên bản trước khi sửa chip ngày, nên vẫn hiện "Tuần 41" thay vì "Hôm nay, 11/10" như Trang chủ.
  - Hai khung lỗi và chưa đủ dữ liệu của Mô hình trình bày khác nhau (một có thẻ bao, một không), nút chính không ghim đáy, và khung ngắn hơn 800dp.

**Hướng xử lý:** Chấp nhận 6 khung trạng thái làm cơ sở cho Final UI và Prototype. Phần còn thiếu sửa trong Figma: chip "Quảng cáo (0)" ở trạng thái được chọn và bỏ câu phụ có chữ "động lực"; làm mờ lưới động cơ khi đang lưu; dùng chung component thẻ "Tổng quan tuần" cho Trang chủ và Trang chủ – trống; dùng chung component trạng thái lỗi/trống cho Mô hình, ghim nút ở đáy và đặt mọi khung 360 × 800.

---

## F6 — Flow 6: Danh sách mong muốn (Smart Wishlist)
**Ngày:** 12/10/2026
**Công cụ:** Google Stitch (project https://stitch.withgoogle.com/projects/1668611817022706714), sau đó Claude + Figma connector để dựng trong Figma
**Màn hình Stitch sinh:** Home – Wishlist Entry, Wishlist Overview, Add Wishlist Item, Wishlist Detail, Wishlist Empty, Add Item Error, Wishlist Saved, Wishlist Skipped, Skip Confirmation Dialog, Add Purchase with Prefilled Wishlist Data

**Prompt Stitch (nguyên văn):**

*Lần 1 — Prompt đầu tiên (Trang chủ có lối vào, 11, 12, 13):*

```
Design an extension to an EXISTING mobile app called "Why I Buy?" – a mindful spending and purchase-reflection application inspired by "The Psychology of Money".
Feature name: Smart Wishlist – Flow 6
This is NOT a standalone shopping application. It is a new feature inside an existing Android mobile app.
Existing product context: The app currently allows users to record purchases, select psychological buying motives, view purchase history, analyze spending patterns, and reflect on their behavior.
The new Wishlist must extend that product by helping users understand why they WANT to buy something BEFORE actually buying it.
Target user: Nam, 22, a Vietnamese final-year IT student and intern. He often discovers products through TikTok, Shopee, social media, and flash sales. He wants to make more mindful purchasing decisions without judgment or pressure. He uses his phone one-handed and needs readable text and large touch targets.
Design system – strictly follow:


Platform: Android, Material Design 3.

Mobile frame: 360 × 800 dp.

Light theme.

Font: Be Vietnam Pro.

Background: #F5F6F2.

Primary: #2E4A9E.

Primary container: #E3E8F7.

Surface: #FFFFFF.

Primary text: #1A2320.

Secondary text: #545E59.

Error: #B3261E, only for actual errors.

Spacing: 4, 8, 12, 16, 24, 32 dp.

Horizontal screen padding: 16 dp.

Card radius: 16 dp.

Input radius: 12 dp.

Button height: 56 dp.

Touch targets: at least 48 × 48 dp.

Body text: at least 14 sp.

Text contrast: at least 4.5:1.

All user-facing text must be in natural Vietnamese.
Existing navigation: Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân.
Do NOT add a sixth bottom navigation tab. Wishlist is a nested feature accessible from Trang chủ.
Create four visual designs:


Home Dashboard – Wishlist Entry Variant Preserve the existing weekly summary, recent purchases, bottom navigation, and primary "Ghi khoản mua" button. Introduce a compact, clearly discoverable secondary entry named "Danh sách mong muốn" without replacing the existing primary action.

Screen 11 – Wishlist Overview Title: "Danh sách mong muốn". Show a short, warm, non-judgmental explanation. Display wishlist items with name, estimated price, psychological motive (icon + label), and status. Provide filter choices: "Đang cân nhắc", "Đã mua", "Bỏ qua". Primary button: "+ Thêm món". Example items:


Bàn phím cơ – 650.000 ₫ – Khuyến mãi

Áo khoác – 420.000 ₫ – Mong muốn Also create an empty state.

Screen 12 – Add Wishlist Item Title: "Thêm món mong muốn". Fields:


Tên món đồ (required)

Giá dự kiến (optional, positive VND if supplied)

"Vì sao bạn muốn mua món này?" (required)

Ghi chú thêm (optional) Show exactly eight psychological motives in a 2-column grid: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Use exactly the same icon and motive color system as the existing Purchase Reason screen. Primary button: "Lưu món". Include an inline validation error variant.

Screen 13 – Wishlist Detail Display item name, estimated price, motive, note, creation date, and status. Primary button: "Ghi khoản mua". Secondary action: "Không mua nữa". Provide a small edit action. "Ghi khoản mua" connects conceptually to the EXISTING Add Purchase flow with prefilled information. "Không mua nữa" archives the wishlist item, rather than permanently deleting it. Include a confirmation dialog and success snackbar with an Undo option.
Design behavior and constraints:


No mandatory 72-hour waiting period.

Do not add payment, checkout, shopping cart, product marketplace, or price tracking.

Do not create new psychological motive categories.

Do not use guilt-inducing wording.

Do not describe skipped purchases as guaranteed monetary savings.

Maintain one clear primary action per screen.

Use bottom-positioned actions suitable for one-handed use.

Make all screens visually consistent with the existing "Why I Buy?" Figma screenshots.

Keep reusable components visually identical to existing Button, Text field, Motive card, Dialog and Snackbar.

Avoid oversized illustrations, unnecessary decorative sections, or excessive whitespace.
Generate a cohesive, production-ready mobile UI concept suitable for rebuilding with Figma Auto Layout, Variables, Components, and Variants.
Do not redesign the existing application or change its navigation architecture.
```

*Lần 2 — Tinh chỉnh 4 màn chính:*

```
Refine the four existing Smart Wishlist screens. Do not regenerate the application from scratch.
The overall visual direction is acceptable, but several UX problems must be corrected.
1. Home Dashboard


Preserve the original Why I Buy? Home Dashboard layout.

Keep the original "Tổng quan tuần" card, recent purchases section, five-tab navigation, and main "Ghi khoản mua" button.

Add a compact secondary entry point labeled "Danh sách mong muốn".

Do not redesign existing Home content, rename existing sections, or introduce unrelated quotes.
2. Wishlist Overview


Keep the existing list layout and status filters.

Remove the empty-state illustration and "Chưa có món nào trong danh mục này" message when wishlist items exist.

Create a SEPARATE empty-state variant to be shown only when the selected category contains no items.

Remove mandatory countdown timers or time-based purchase restrictions from all cards.

Each card should clearly display the item name, estimated price, psychological motive, and status.

Keep the "+ Thêm món" button accessible at the bottom.
3. Add Wishlist Item


Keep the existing two-column psychological motive grid with exactly eight motives.

If the item name is valid, do not display a validation error.

Create a separate error-state variant for an empty name or an invalid estimated price.

Estimated price is optional.

Preserve inline form validation and make the primary save action clear.

Reuse the same motive icons, colors, and component styles as the original Add Purchase flow.
4. Wishlist Detail


REMOVE the mandatory 48-hour cooling-off period.

REMOVE the psychological journal timeline and multi-stage psychological tracking.

REMOVE any countdown or locked decision behavior.

Replace them with a straightforward detail layout showing:


Item name

Estimated price

Psychological buying motive

Personal note

Date added

Current wishlist status

Primary action: "Ghi khoản mua".

Secondary action: "Không mua nữa".

Small edit action in the app bar.

Both primary and secondary decisions must be available immediately, with no waiting requirement.

The "Ghi khoản mua" action should lead to the existing Add Purchase flow with prefilled item information.

"Không mua nữa" should move the item to the Skipped status, not permanently delete it.

Add a confirmation dialog for skipping an item, with Cancel and Confirm.

After confirmation, display an Undo snackbar.
5. Maintain strict consistency with the existing Figma design system


Android 360 × 800 dp.

Material Design 3, light theme.

Be Vietnam Pro font.

Primary #2E4A9E.

Background #F5F6F2.

Surface #FFFFFF.

Primary text #1A2320.

Minimum 14sp body text.

Minimum 48 × 48dp touch targets.

Five existing bottom navigation tabs only.

All visible text in Vietnamese.

Avoid excessive text, unnecessary illustrations, overly complex cards, and feature expansion.
The goal is a simple, practical Smart Wishlist that helps users understand WHY they want to buy something, not a shopping marketplace or forced waiting system.
Update the existing designs while preserving their overall visual consistency and reusable components.
```

*Lần 3 — Bổ sung trạng thái và tương tác còn thiếu:*

```
Continue refining Flow 6 – Smart Wishlist of the existing Why I Buy? mobile application.
The main Wishlist Overview, Add Wishlist Item, and Wishlist Detail screens are now approved. Do not redesign them from scratch.
Please complete these missing states and interaction designs:
1. Skip Confirmation Dialog


Based on the existing Wishlist Detail screen.

Open a centered modal overlay.

Title: "Không mua món này nữa?"

Description: "Món đồ sẽ được chuyển vào danh sách Bỏ qua. Bạn có thể xem lại sau."

Actions: "Hủy" and "Bỏ qua".

Use the existing Why I Buy? Dialog component style.
2. Wishlist – Skipped State


After confirmation, navigate to Wishlist Overview.

The item should appear under the "Bỏ qua" filter.

The item must no longer be marked "Đang cân nhắc".

Show a snackbar: "Đã chuyển món vào Bỏ qua" with "Hoàn tác".

Undo restores the item to "Đang cân nhắc".
3. Wishlist – Saved State


Show Wishlist Overview after a new item has been added successfully.

The newly added item must appear in the "Đang cân nhắc" list.

Display a success snackbar: "Đã lưu món vào danh sách mong muốn".
4. Mobile Empty and Error States


Ensure Wishlist Empty and Add Wishlist Error are designed as separate 360 × 800 dp Android mobile screens, not desktop or landscape layouts.

On a filtered empty state, provide a useful action such as "Xem đang cân nhắc" when appropriate.

Preserve existing inline validation patterns.
5. Purchase Integration


When pressing "Ghi khoản mua" in Wishlist Detail, the user should enter the existing Add Purchase flow.

Prefill the item name, estimated price if available, and original motive, but allow the user to edit them.

The wishlist item is marked "Đã mua" only after the purchase is successfully saved.
Strictly reuse the existing Material Design 3 system, Be Vietnam Pro font, primary #2E4A9E, and the same existing components.
Do not introduce mandatory waiting periods, countdown timers, payment features, or additional bottom navigation tabs.
All user-facing text must be Vietnamese.
Generate only the missing states and interaction variants. Do not regenerate the main four screens.

Với "Danh sách mong muốn - Trống" và "Thêm món mong muốn - Báo lỗi" hình như đang bị to quá hay gì á. Làm cho giống các màn khác luôn
```

*Lần 4 — Yêu cầu thêm về kích thước khung:*

```
toàn bộ mấy này làm theo 360x800
```

**Kết quả:**

| Nội dung | Ảnh |
|---|---|
| Home – Wishlist Entry | ![](../assets/stitch/flow6/f6-stitch-home-wishlist-entry.png) |
| Wishlist Overview (bản có 48h, "Đã hạ nhiệt 40%") | ![](../assets/stitch/flow6/f6-stitch-wishlist-overview.png) |
| Add Wishlist Item | ![](../assets/stitch/flow6/f6-stitch-add-item.png) |
| Wishlist Detail (bản có 48h, nhật ký tâm lý) | ![](../assets/stitch/flow6/f6-stitch-wishlist-detail.png) |
| Add Purchase điền sẵn | ![](../assets/stitch/flow6/f6-stitch-add-purchase-prefilled.png) |
| Wishlist Skipped | ![](../assets/stitch/flow6/f6-stitch-wishlist-skipped.png) |
| Wishlist Saved | ![](../assets/stitch/flow6/f6-stitch-wishlist-saved.png) |
| Add Item Error | ![](../assets/stitch/flow6/f6-stitch-add-item-error.png) |
| Skip Confirmation Dialog | ![](../assets/stitch/flow6/f6-stitch-skip-dialog.png) |
| Wishlist Empty (bộ lọc Bỏ qua) | ![](../assets/stitch/flow6/f6-stitch-skipped-empty.png) |

**Phản biện bằng Claude** (đối chiếu ảnh với 10 heuristic của Nielsen, accessibility, persona Nam):

| # | Màn hình | Phát hiện | Heuristic / tiêu chí | Quyết định |
|---|---|---|---|---|
| 1 | Wishlist Detail | Chip "Khoảng lặng 48h", "Đang tĩnh tâm"; ép chờ trước khi mua | #3 User control; persona không phán xét | Từ chối (QĐ 6) |
| 2 | Wishlist Overview | "Còn 48h suy ngẫm", "Đã hạ nhiệt 40%" + đồng hồ cát: số liệu ứng dụng không đo được, gây áp lực | #2 Match real world; #8 | Từ chối (QĐ 6) |
| 3 | Wishlist Detail | Thẻ "Nhật ký tâm lý · Bước 2/3" bắt buộc qua nhiều giai đoạn | #8 Minimalist; phạm vi | Từ chối (QĐ 6) |
| 4 | Home – Wishlist Entry | Trang chủ bị thiết kế lại; nhãn "Danh …" bị cắt; thẻ "Khoảng lặng 24 giờ" mang giọng khuyên bảo | #4 Consistency; DESIGN.md tone | Sửa (QĐ 7) |
| 5 | Add Wishlist Item | Báo lỗi "Vui lòng nhập tên món đồ để lưu" trong khi ô tên đã có "Bàn phím cơ không dây" | #9 Recover from errors; #1 | Sửa: tách khung lỗi riêng (12a), form hợp lệ không báo lỗi |
| 6 | Add Wishlist Item | Thẻ "Không gian trì hoãn lành mạnh" và dòng "Món đồ chỉ thực sự đáng mua khi nó vẫn hữu ích sau 30 ngày." | DESIGN.md: không khuyên bảo | Từ chối |
| 7 | Wishlist Overview | Thẻ món và khung "Chưa có món nào trong danh mục này" hiện cùng lúc | #1 Visibility of status | Sửa: empty state chỉ khi bộ lọc trống |
| 8 | Wishlist Overview / Empty | Chip "Bỏ qua" bị cắt ở mép phải; số lượng giữa các khung không khớp (Đã mua 3 / 0) | Accessibility; #4 | Sửa (QĐ 8), thống nhất dữ liệu mẫu |
| 9 | Saved / Skipped | Snackbar bị cắt chữ ("Đã lưu món vào danh sách mon…"), nhãn hành động viết hoa "ĐÓNG" | #1; tone | Sửa: message 2 dòng, bỏ "Đóng", giữ "Hoàn tác" |
| 10 | Skip Confirmation | Dialog nằm trong canvas ngang, màn nền không phải 360 × 800 | Ràng buộc nền tảng | Chấp nhận nội dung, dựng lại overlay (QĐ 3) |
| 11 | Add Purchase prefilled | Nhãn "Từ Mong muốn" + ghi chú "Động cơ ban đầu: Khuyến mãi (có thể chọn lại ở Bước 2/2)" | #6 Recognition | Chấp nhận, đổi thành banner "Điền sẵn từ Danh sách mong muốn" |

**Chuyển sang Figma (làm tay / bằng Claude, không qua Stitch):** 3 component mới (Wishlist status chip, Wishlist item card có State Default/Pressed, Wishlist entry) và 2 icon (bookmark, archive); 22 khung Final UI (thêm 13c đã bỏ qua, 13d đã mua, và 3 khung chi tiết theo dữ liệu: Áo khoác, Chuột công thái học, Bình giữ nhiệt); 6 wireframe; sơ đồ Flow 6 ở trang 01; prototype 17 khung + overlay + chuyển cảnh đang lưu → đã mua.

**Điều rút ra:** Stitch tự thêm cơ chế "hạ nhiệt" dù không được yêu cầu. Khi đưa vào sản phẩm phải lọc lại theo DESIGN.md, giống bài học ở R2 (Stitch luôn sinh câu khuyên bảo mới).

---

## PB — Phản biện bằng AI trên Final UI (Nielsen, accessibility, persona)
**Ngày:** 12/10/2026
**Công cụ:** Claude (Claude Code), một agent phản biện chạy riêng, chỉ được đọc repo: ảnh Final UI trong `assets/figma/` (chụp từ page `03 Final UI`), `design/DESIGN.md`, `ux/persona.md`, `ux/user-flow.md`. Agent không thấy các quyết định đã có trong `design-decisions.md`.
**Phạm vi:** toàn bộ Final UI (Flow 1–7), khác với bảng phản biện ở F6 chỉ xét ảnh Stitch của Flow 6.

**Prompt (nguyên văn):**

```
Thư mục làm việc: C:\Users\Admin\OneDrive\Documents\FPT_University\prm393_lab02 (chỉ ĐỌC, không sửa file nào). Dùng công cụ Read để mở các file .md và ảnh .png được nhắc tới (đường dẫn tương đối tính từ thư mục trên). Câu trả lời cuối cùng của bạn sẽ được dán NGUYÊN VĂN vào nhật ký AI của bài lab, nên chỉ viết nội dung phản biện, không mô tả quá trình dùng công cụ.

Bạn là chuyên gia UX đánh giá thiết kế ứng dụng di động. Hãy phản biện bộ màn hình Final UI của ứng dụng "Why I Buy?" (Android, 360 × 800 dp, Material 3, light theme).

Bối cảnh:
- Người dùng chính: Nguyễn Hải Nam, 22 tuổi, sinh viên năm cuối CNTT kiêm thực tập sinh, thu nhập 6–9 triệu/tháng. Hay đặt đồ ăn khuya và chốt flash sale sau 22h, dùng điện thoại Android 6.5" bằng một tay (ngón cái chỉ với tới nửa dưới màn hình), cận 2 độ, hay dùng điện thoại trong phòng tối. Đã bỏ các app chi tiêu vì nhập lâu và cảm giác tội lỗi khi thấy cảnh báo đỏ.
- Mục tiêu đo được: ghi một khoản mua kèm động cơ trong ≤ 25 giây; thêm một món vào danh sách mong muốn trong < 20 giây.
- Brief thiết kế đầy đủ (màu, chữ, khoảng cách, từ vựng thống nhất, quy tắc component): design/DESIGN.md. Persona: ux/persona.md. Danh sách màn hình và flow: ux/user-flow.md.
- Ảnh các màn hình nằm trong assets/figma/ (mỗi file là một khung 360 × 800 dp). Hãy mở và xem trực tiếp từng ảnh, đặc biệt: 00a-login, 00b-register, 01-onboarding, 02-home, 02a-home-empty, 02b-home-saved, 02c-home-offline, 03-add-purchase-step1, 03a-add-purchase-error, 03c-add-purchase-from-wishlist, 04-purchase-reason, 04a-purchase-reason-saving, 05-purchase-detail, 05a-delete-dialog, 06-history, 06a-history-no-result, 06b-history-after-delete, 07-patterns, 07a-patterns-loading, 07b-patterns-error, 07c-patterns-insufficient, 08-insights, 09-monthly-reflection, 10-profile, 10a-profile-delete-all-dialog, 11-wishlist-overview, 12-add-item, 12a-add-item-error, 13-wishlist-detail, 13a-skip-dialog.

Yêu cầu đánh giá:
1. Theo 10 heuristic usability của Nielsen (ghi rõ tên và số heuristic: #1 Visibility of system status, #2 Match between system and the real world, #3 User control and freedom, #4 Consistency and standards, #5 Error prevention, #6 Recognition rather than recall, #7 Flexibility and efficiency of use, #8 Aesthetic and minimalist design, #9 Help users recognize, diagnose, and recover from errors, #10 Help and documentation).
2. Theo các quy tắc accessibility cơ bản: contrast chữ ≥ 4.5:1 (chữ lớn và điều khiển UI ≥ 3:1), vùng chạm ≥ 48 × 48 dp, chữ nội dung ≥ 14 sp, không truyền đạt thông tin chỉ bằng màu, chữ không bị cắt / tràn khung ở 360 dp.
3. Theo persona Nam (một tay, cận, dùng đêm, sợ bị phán xét, cần ghi nhanh).
4. Đối chiếu với DESIGN.md: chỗ nào trên màn hình lệch khỏi từ vựng thống nhất, quy tắc component hoặc giọng văn đã đặt ra.

Định dạng câu trả lời:
- Tối thiểu 8 phát hiện. Mỗi phát hiện PHẢI gắn với một hoặc nhiều màn hình cụ thể (ghi tên file ảnh), mô tả cụ thể nhìn thấy gì, thuộc heuristic / tiêu chí nào, mức độ nghiêm trọng (Cao / Trung bình / Thấp) và đề xuất sửa.
- Trình bày một bảng tổng hợp: # | Màn hình | Phát hiện | Heuristic / tiêu chí | Mức độ | Đề xuất.
- Sau bảng, thêm mục "Điểm làm tốt" (ngắn) và "Ưu tiên sửa" (3 việc nên làm trước).
- Chỉ nêu điều nhìn thấy được trong ảnh hoặc đọc được trong tài liệu; không suy đoán điều không có căn cứ. Viết bằng tiếng Việt.
```

**Câu trả lời của AI (nguyên văn):**

> ## Phản biện Final UI: "Why I Buy?" (Android 360 × 800 dp)
>
> Tôi đã xem các khung trong assets/figma/ và đối chiếu với design/DESIGN.md, ux/persona.md, ux/user-flow.md. Số đo contrast lấy từ màu điểm ảnh. Cỡ chữ và kích thước được quy đổi từ ảnh xuất về khung 360 dp, sai số khoảng ±1 sp/dp.
>
> Tổng cộng có 20 phát hiện: 2 Cao, 13 Trung bình, 5 Thấp.
>
> | # | Màn hình | Phát hiện | Heuristic / tiêu chí | Mức độ | Đề xuất |
> |---|---|---|---|---|---|
> | 1 | 02-home, 02a-home-empty, 02b-home-saved, 02c-home-offline, 02d-home-wishlist-entry, 11a-wishlist-empty | Lối vào duy nhất của Danh sách mong muốn là thẻ trên Trang chủ. user-flow.md quy định thẻ này chỉ hiện khi đã có ≥ 1 món đang cân nhắc. Thực tế thẻ chỉ có ở 02d. Các màn 02, 02b, 02c (cùng ngày 11/10, dữ liệu mẫu vẫn có Bàn phím cơ và Áo khoác đang cân nhắc) không có thẻ. Màn 02a của người mới cũng không có. Thanh điều hướng 5 tab không có lối nào khác, nên người mới không thể tới 11a/12 để thêm món đầu tiên. | #6 Recognition rather than recall; #7 Flexibility and efficiency of use; #4 Consistency and standards (khung trạng thái không giống màn gốc); Persona: thêm món < 20 giây | Cao | Luôn hiện hàng "Danh sách mong muốn" trên 02, kể cả khi chưa có món nào ("Chưa có món nào · Thêm món"). Đặt hàng này cùng một vị trí ở 02, 02a, 02b, 02c, 02d. Cân nhắc thêm một lối vào thứ hai, ví dụ trong tab Cá nhân. |
> | 2 | 03c-add-purchase-from-wishlist; 03-add-purchase-step1, 03a-add-purchase-error, 03b-edit-purchase-step1; 06-history, 06a-history-no-result, 06b-history-after-delete | Ở 03c, dòng chú thích dưới nút ("…c tiếp theo: xác nhận động cơ (đã chọn sẵn Khuyến m…") tràn khỏi khung 360 dp và bị cắt ở cả mép trái lẫn mép phải, mất đúng chữ "Khuyến mãi". Nút chính đổi nhãn thành "Bước tiếp theo: xác nhận động cơ" (ở 03 là "Tiếp tục") và lặp lại nội dung chú thích. Ở 03/03a/03b/03c, chip "+100.000 ₫" bị cắt mất đầu bo tròn bên phải, ký hiệu ₫ chạm mép card. Ở 06/06a/06b, hàng chip lọc bị cắt ngay tại lề nội dung ("Mong mu", "Nhu c"), trông giống chữ bị lỗi hơn là gợi ý cuộn ngang. | A11y: chữ không bị cắt/tràn ở 360 dp; #4 Consistency and standards; #8 Aesthetic and minimalist design | Cao | 03c giữ nhãn "Tiếp tục". Rút chú thích thành "Bước tiếp theo: chọn động cơ (đã chọn sẵn Khuyến mãi)" và bật auto-layout cho xuống dòng. Chia đều chiều rộng cho 3 chip số tiền, hoặc bỏ "₫" trong chip. Cho hàng chip lọc tràn tới mép màn hình thay vì clip ở lề 16 dp. |
> | 3 | 03-add-purchase-step1, 03a-add-purchase-error, 03b-edit-purchase-step1 | Bước 1 chỉ có các chip "+20.000 ₫ / +50.000 ₫ / +100.000 ₫". Dấu "+" cho thấy chip cộng dồn, nên không tạo ra được các số Nam hay gặp như 45.000 ₫ hay 40.000 ₫. Màn này cũng không có gợi ý tên món gần đây. Nam luôn phải gõ tên tiếng Việt có dấu bằng một tay lúc nửa đêm, đây là phần tốn thời gian nhất so với mục tiêu ≤ 25 giây. | #7 Flexibility and efficiency of use; Persona: ghi nhanh, một tay | Trung bình | Thêm hàng chip "Gần đây" (ví dụ "Trà sữa nướng · 45.000 ₫", "Cơm tấm · 40.000 ₫"), chạm một lần là điền cả tên lẫn số tiền. Mở sẵn bàn phím số ở ô số tiền. Đo lại thời gian Flow 1 bằng bản thử. |
> | 4 | 06-history, 06a-history-no-result, 07-patterns, 07e-patterns-week, 13-wishlist-detail, 05-purchase-detail | Các điều khiển dùng thường xuyên đều nằm ở phần trên, ngoài tầm ngón cái: bộ chọn tuần/tháng và mũi tên (~105 dp từ đỉnh), công tắc Tuần/Tháng ở 07 (~105 dp), hàng chip lọc động cơ ở 06 (~165 dp). Muốn lọc Tiện lợi hay Khác còn phải vuốt ngang thêm. Ở 13, "Sửa" là icon bút chì ở góc phải trên, còn ở 05 "Sửa" là nút chính ghim đáy: cùng một hành động nhưng ở hai vị trí. | Persona: một tay, ngón cái chỉ với tới nửa dưới; #4 Consistency and standards; #7 Flexibility and efficiency of use | Trung bình | Thêm nút "Lọc" ở nửa dưới màn hình, mở bottom sheet để chọn động cơ và kỳ. Cho vuốt ngang trên danh sách để đổi tuần/tháng. Ở 13, đưa "Sửa" xuống cụm hành động ở đáy, cạnh "Không mua nữa". |
> | 5 | 00a-login, 00b-register, 03-add-purchase-step1, 04-purchase-reason, 12-add-item | Ô nhập là khối nền #E7F0EB không có viền. Độ tương phản chỉ 1.16:1 so với card trắng và 1.07:1 so với nền #F5F6F2 (ở 00a, 00b ô nằm thẳng trên nền). Thẻ động cơ trắng trên nền chỉ ≈ 1.09:1. Token outline #8A918A mà DESIGN.md dành cho "viền ô nhập, chip" không được dùng cho ô nhập. | A11y: contrast điều khiển UI ≥ 3:1; DESIGN.md (bảng màu); Persona: cận 2 độ, hay dùng trong phòng tối | Trung bình | Thêm viền 1 dp màu outline: #8A918A đạt ≈ 3.2:1 trên card trắng, trên nền #F5F6F2 cần đậm hơn một bậc. Có thể dùng chỉ báo gạch dưới của M3 filled field thay cho viền. Khi focus dùng viền 2 dp màu primary. Thẻ động cơ chưa chọn cũng thêm viền outline. |
> | 6 | 02-home, 02b-home-saved, 02c-home-offline, 02d-home-wishlist-entry | Thanh "Động cơ chính" là thanh xếp chồng 4–5 đoạn màu, không có nhãn hay chú giải. Chỉ đoạn lớn nhất được gọi tên ("40% do Khuyến mãi"). Hai đoạn liền nhau là Tiện lợi (#145655) và Nhu cầu (#204D39) chỉ chênh nhau 1.14:1, gần như không phân biệt được. | A11y: không truyền đạt thông tin chỉ bằng màu; DESIGN.md: "Biểu đồ luôn có nhãn chữ và phần trăm"; #2 Match between system and the real world | Trung bình | Thêm chú giải icon + tên + % dưới thanh (dùng lại legend của 09), hoặc thay thanh bằng một dòng chữ kèm lối sang tab Mô hình. Tách các đoạn bằng khe 2 dp màu nền. |
> | 7 | 06-history, 06b-history-after-delete, 00b-register | Giờ của khoản mua ở 06/06b ("23:10", "12:15", "23:40") ước lượng khoảng 12 sp: chữ số cao ≈ 9 dp, trong khi giá 16 sp trong cùng ảnh cao ≈ 11,8 dp. Cùng thông tin này trên 02-home lại ~14 sp. Ở 00b, dòng "Mật khẩu có ít nhất 8 ký tự." cũng ~12 sp và nằm dưới ô "Xác nhận mật khẩu" thay vì dưới ô "Mật khẩu". | A11y: chữ nội dung ≥ 14 sp; DESIGN.md: Label 12 sp chỉ dành cho nhãn phụ; #5 Error prevention; Persona: cận, khung giờ là dữ liệu cốt lõi về thói quen mua đêm | Trung bình | Đưa giờ ở 06 về Body small 14 sp, dùng chung style với 02. Dời gợi ý mật khẩu xuống ngay dưới ô "Mật khẩu", cỡ 14 sp. |
> | 8 | 01-onboarding, 02a-home-empty, 03-add-purchase-step1, 03a-add-purchase-error, 03b-edit-purchase-step1, 03c-add-purchase-from-wishlist, 04-purchase-reason, 04a-purchase-reason-saving, 04d-purchase-reason-from-wishlist, 05-purchase-detail, 09-monthly-reflection, 11-wishlist-overview, 12-add-item, 12a-add-item-error, 13-wishlist-detail | Nhiều chỗ lệch bảng từ vựng thống nhất. Dùng "khoản chi": chip "Bước 1/2: Thông tin khoản chi" ở 03/03a/03b/03c, "KHOẢN CHI VỪA NHẬP" ở 04/04a/04d, "15 khoản chi" ở 09. Dùng "giao dịch": "Chưa có giao dịch" ở 02a. Dùng "lý do" thay cho "động cơ": ở 01, banner của 11, "Chọn một lý do chính" ở 12, lỗi "Vui lòng chọn lý do…" ở 12a, nhãn "Lý do muốn mua" ở 13 (trong khi 05 ở cùng vị trí ghi "Động cơ"). Nhãn thời điểm cũng không thống nhất: 03 ghi "Thời điểm chi tiêu", 05 ghi "Thời gian ghi nhận" (dễ hiểu thành lúc ghi chứ không phải lúc mua). | #4 Consistency and standards; #2 Match between system and the real world; DESIGN.md: Từ vựng thống nhất | Trung bình | Thay đồng loạt thành "Thông tin khoản mua", "Khoản mua vừa nhập", "15 khoản mua", "Chưa có khoản mua", "Động cơ". Ở 12 dùng "Chọn một động cơ chính", ở 12a dùng "Vui lòng chọn một động cơ". Thống nhất "Thời điểm mua" ở 03 và 05. Quản lý các chuỗi này bằng component hoặc text style để không bị lệch lại. |
> | 9 | 02c-home-offline, 11b-wishlist-saved, 11e-wishlist-purchased, 08a-insights-reflection-saved (so với 02b-home-saved, 06b-history-after-delete, 11c-wishlist-skipped) | 02b có snackbar 'Đã lưu "Trà sữa nướng" · Hoàn tác', nhưng các màn khác thì không. 02c chỉ có "Đã lưu trên máy. Sẽ đồng bộ khi có mạng.", không có tên món và không có Hoàn tác, dù Flow 1 vẽ nhánh hoàn tác cho cả trường hợp mất mạng. 11b chỉ có "Đã lưu món vào danh sách mong muốn.", không tên món, không Hoàn tác. 11e có 'Đã ghi khoản mua "Bàn phím cơ" vào Lịch sử' nhưng không có Hoàn tác, dù vừa tạo khoản mua và đổi trạng thái món. 08a ("Đã lưu chiêm nghiệm tháng 10") cũng không có Hoàn tác. | #3 User control and freedom; #4 Consistency and standards; DESIGN.md: snackbar "Đã lưu “…”" kèm "Hoàn tác" 5 giây | Trung bình | Dùng một component snackbar cho mọi lần lưu: tên mục + "Hoàn tác" trong 5 giây. 02c thành 'Đã lưu "Trà sữa nướng" trên máy, sẽ đồng bộ khi có mạng · Hoàn tác'. Ở 11e, Hoàn tác gỡ khoản mua và đưa món về Đang cân nhắc. |
> | 10 | 12-add-item, 12a-add-item-error | Placeholder "Ví dụ: Bàn phím cơ" và "Ví dụ: 650.000 ₫" dùng chữ ~20 sp đậm, cùng style với giá trị đã nhập ở 03 ("Trà sữa nướng"), chỉ khác màu xám, nên trông như đã điền sẵn. Ở 12a, ô vẫn hiện "Ví dụ: Bàn phím cơ" chữ đậm ngay phía trên lỗi "Vui lòng nhập tên món đồ để lưu." | #6 Recognition rather than recall; #9 Help users recognize, diagnose, and recover from errors; #2 Match between system and the real world | Trung bình | Cho placeholder dùng Body 16 sp regular, màu on-surface-variant, giống placeholder ở 00a và 04. Hoặc chuyển ví dụ thành helper text dưới ô. |
> | 11 | 02-home, 07-patterns, 07e-patterns-week, 08-insights, 13-wishlist-detail | Nhiều thông tin bị lặp. Ở 02: 817.000 ₫ hiện hai lần; "Khuyến mãi (2/5)" và "40% do Khuyến mãi" là cùng một số liệu; mỗi hàng khoản mua có icon tròn lặp đúng icon trong chip. Ở 07/07e: card "TỔNG QUAN CHU KỲ – Tháng 10/2026: 15 khoản" lặp lại bộ chọn ngay phía trên, đẩy phần khung giờ (chính là mô hình mua đêm của Nam) ra khỏi màn đầu; cả 07 lẫn 07e đều không thấy phần này. Ở 08: "Góc nhìn" xuất hiện ở cả app bar lẫn tiêu đề, và có cả "THÁNG 10/2026" lẫn "THÁNG 10 · NHÌN LẠI". Ở 13: trạng thái hiện 3 lần (overline "MÓN ĐANG CÂN NHẮC", chip, icon bookmark). | #8 Aesthetic and minimalist design | Trung bình | Ở 02, giữ số lớn + "5 khoản", bỏ một trong hai dòng Khuyến mãi và bỏ icon tròn đầu hàng. Ở 07, bỏ card tổng quan, đặt khung giờ ngay sau phần động cơ và thu gọn các động cơ 0 khoản. Ở 08, bỏ tiêu đề trùng app bar. Ở 13, bỏ overline. |
> | 12 | 13a-skip-dialog (so với 05a-delete-dialog) | Hai nút "Hủy" và "Bỏ qua" đặt cạnh nhau. Trên app tiếng Việt, hai từ này thường cùng mang nghĩa "đóng hộp thoại", nên dễ bấm nhầm. Nội dung "Món đồ sẽ được chuyển vào danh sách Bỏ qua…" không nêu tên món và không nhắc tới hoàn tác. Trong khi đó 05a nêu rõ "Tai nghe Bluetooth" và "Bạn có 5 giây để hoàn tác". | #2 Match between system and the real world; #5 Error prevention; #4 Consistency and standards | Trung bình | Đổi nút xác nhận thành "Chuyển vào Bỏ qua" (vẫn đúng từ vựng DESIGN.md). Đổi nội dung thành '"Bàn phím cơ" sẽ chuyển vào Bỏ qua. Bạn có 5 giây để hoàn tác.' |
> | 13 | 10-profile, 10a-profile-delete-all-dialog | Xóa vĩnh viễn toàn bộ dữ liệu, kể cả trên tài khoản ("Không thể hoàn tác"), chỉ cần một lần chạm "Xóa tất cả". Dialog không gợi ý xuất dữ liệu trước. Dialog chỉ nêu "khoản mua và chiêm nghiệm", không nói món trong Danh sách mong muốn có bị xóa hay không. "Hủy" chỉ là chữ (phần nhìn thấy ≈ 30 × 17 dp) và nằm sát nút xóa. | #5 Error prevention; #1 Visibility of system status; A11y: vùng chạm ≥ 48 × 48 dp | Trung bình | Thêm nút phụ "Xuất dữ liệu trước" trong dialog. Liệt kê đủ phạm vi bị xóa: khoản mua, món mong muốn, chiêm nghiệm, nhắc nhở. Thêm bước xác nhận thứ hai (gõ "XÓA" hoặc giữ nút 2 giây). Cho "Hủy" vùng chạm ≥ 48 dp. |
> | 14 | 10-profile, 10b-profile-exported | "Nhắc ghi khoản mua lúc 21:00 mỗi tối" chỉ có công tắc, không có cách đổi giờ. 21:00 lại sớm hơn khung giờ Nam hay mua (đồ ăn khuya, flash sale sau 22:00), nên lời nhắc đến trước khi có khoản mua. Tài liệu cũng chưa khớp nhau: DESIGN.md ghi "sau 23h", persona.md ghi "sau 22:00". | #7 Flexibility and efficiency of use; Persona: hay mua đêm | Trung bình | Biến hàng nhắc thành ô chọn giờ, chạm để mở time picker. Đặt giờ mặc định muộn hơn (ví dụ 23:30) hoặc cho đặt nhiều mốc. Thống nhất mốc giờ giữa hai tài liệu. |
> | 15 | 00a-login, 00b-register, 01-onboarding, 10-profile, 10a-profile-delete-all-dialog | Thông điệp về lưu trữ mâu thuẫn nhau. 01 ghi "Dữ liệu được lưu trên máy của bạn.", thẻ hồ sơ ở 10 ghi "Dữ liệu cá nhân trên máy này", nhưng chú thích cuối 10 và dialog 10a lại nói đồng bộ và xóa "khỏi máy và tài khoản". Có màn đăng nhập/đăng ký (00a/00b), nhưng 10 không hiện email, trạng thái đồng bộ hay nút "Đăng xuất". 00b có 4 ô nhập, trong đó ô "Họ tên – Tên bạn muốn được gọi" trái với quy tắc chỉ xưng "bạn", không gọi tên (10 cũng chỉ hiện "Bạn"). 00b không có nút hiện/ẩn mật khẩu. 00a/00b không có trong danh sách màn hình của DESIGN.md lẫn user-flow.md. | #1 Visibility of system status; #3 User control and freedom; #4 Consistency and standards; DESIGN.md: Xưng hô, Lưu trữ dữ liệu; Persona: ngại nhập nhiều | Trung bình | Dùng cùng một câu về lưu trữ ở 01 và 10: "Lưu trên máy, đồng bộ với tài khoản khi có mạng". Thêm mục Tài khoản ở 10 (email, lần đồng bộ gần nhất, Đăng xuất). Bỏ "Họ tên" và "Xác nhận mật khẩu" ở 00b, thêm icon hiện/ẩn mật khẩu. Bổ sung 00a/00b vào DESIGN.md và user-flow.md. |
> | 16 | 03-add-purchase-step1, 03a-add-purchase-error, 12-add-item, 12a-add-item-error | 03 tô chữ "Bắt buộc" bằng màu error đỏ ngay ở trạng thái bình thường, còn 12 ghi "(bắt buộc)" màu xám trong nhãn. Tên món ở 03 không được đánh dấu là bắt buộc hay tùy chọn. Cách kiểm lỗi cũng khác nhau: 03a khóa nút "Tiếp tục", còn 12a vẫn cho bấm "Lưu món" rồi mới báo lỗi tại trường. | #4 Consistency and standards; #5 Error prevention; DESIGN.md: màu error chỉ dành cho lỗi nhập liệu và xóa, giọng "không cảnh báo đỏ"; Persona: sợ cảm giác bị cảnh báo | Thấp | Dùng một quy ước: "(bắt buộc)" / "(tùy chọn)" màu on-surface-variant ngay trong nhãn, chỉ dùng đỏ khi thật sự có lỗi. Chọn một cách kiểm lỗi cho cả hai luồng, nên giữ nút bấm được và báo lỗi tại trường như 12a. |
> | 17 | 04-purchase-reason, 04a-purchase-reason-saving, 05-purchase-detail, 12-add-item, 03-add-purchase-step1, 06a-history-no-result, 08-insights | Một số icon lệch nghĩa. Icon biên lai có ký hiệu "$" xuất hiện ở 04 ("KHOẢN CHI VỪA NHẬP"), 05 và ô giá ở 12, trong khi app chỉ dùng ₫. Ô tên món ở 03/12 dùng icon hình xô có quai, dáng gần giống icon thùng rác ở 05/05a. "Xóa bộ lọc" ở 06a dùng icon làm mới (↻). 08 đặt icon mũi tên đi lên cạnh "15 khoản đã ghi" dù không có phép so sánh nào, dễ bị đọc thành "tăng". | #2 Match between system and the real world; #4 Consistency and standards; DESIGN.md: giọng trung lập, không chấm điểm | Thấp | Dùng icon biên lai không có ký hiệu tiền, hoặc có "₫". Dùng icon shopping_bag cho tên món, filter_alt_off cho "Xóa bộ lọc". Thay mũi tên đi lên bằng icon lịch hoặc icon tổng hợp trung tính. |
> | 18 | 12-add-item, 12a-add-item-error (so với 04-purchase-reason, 04b-motive-guide-sheet) | 04 có nút "?" mở 04b giải nghĩa 8 động cơ. 12 dùng đúng lưới 8 động cơ đó nhưng lại không có "?", nên khi thêm món mong muốn không xem được định nghĩa (ví dụ để phân biệt Khuyến mãi với Quảng cáo). Ở 04, nút "?" nằm góc phải trên, ngoài tầm ngón cái. | #10 Help and documentation; #4 Consistency and standards; Persona: thao tác một tay | Thấp | Dùng chung một component đầu lưới động cơ cho 04 và 12. Đặt text button "Các động cơ nghĩa là gì?" ngay dưới câu hỏi "Vì sao bạn…" thay vì chỉ có icon trên app bar. |
> | 19 | 02a-home-empty, 06a-history-no-result, 07b-patterns-error, 07c-patterns-insufficient, 11a-wishlist-empty | Các khung trạng thái không giống màn gốc như DESIGN.md yêu cầu. 02a đổi chip "Hôm nay, 11/10" thành "Tuần 41" và vẫn hiện "Xem tất cả >" khi có 0 khoản. 06a đẩy chip "Quảng cáo (0)" lên vị trí thứ 2 (06 xếp theo thứ tự Nhu cầu, Mong muốn…) và cho chọn một chip vốn có 0 kết quả. 11a mất nút "Thêm món" ghim đáy mà 11 có. 07b, 07c, 11a đặt nút filled ở giữa màn thay vì ghim đáy cao 56 dp. | #4 Consistency and standards; #5 Error prevention; DESIGN.md: quy tắc khung trạng thái, một nút chính ghim đáy, thứ tự 8 động cơ | Thấp | Dựng khung trạng thái từ instance của màn gốc. Giữ nguyên thứ tự chip, chỉ cuộn tới chip đang chọn. Chip 0 khoản hiển thị mờ và không chọn được. Nút chính luôn ghim đáy. |
> | 20 | 00a-login, 02-home, 05a-delete-dialog, 06-history, 07-patterns, 09-monthly-reflection, 13a-skip-dialog | Nhiều điều khiển chỉ là chữ hoặc icon trần, phần nhìn thấy cao 14–17 dp: "Xem tất cả" (≈ 90 × 14 dp), "Quên mật khẩu?", "Đăng ký" (≈ 56 × 14 dp), "Để sau", "Hủy" (≈ 30 × 17 dp), mũi tên đổi tuần/tháng. Ảnh không thể hiện vùng chạm thực, nên không xác nhận được là đạt 48 × 48 dp. | A11y: vùng chạm ≥ 48 × 48 dp; Persona: thao tác một tay khi mệt | Thấp | Trong Figma, đặt khung tối thiểu 48 × 48 dp cho mọi text button và icon button (chiều cao tối thiểu 48, padding ngang 12–16 dp) và ghi chú lại cho dev. Giữ khoảng cách ≥ 8 dp giữa "Hủy" và nút xóa. |
>
> ### Điểm làm tốt
> - **Contrast chữ đạt ở mọi mẫu đã đo:** chữ phụ #545E59 trên nền trắng ≈ 6.7:1, placeholder ≈ 5.8:1, chữ chip động cơ đậm trên nền nhạt. Thông tin không chỉ dựa vào màu: tab đang chọn có pill + chữ đậm, công tắc có dấu tích, trạng thái món là chip icon + chữ.
> - **Nút chính và thẻ động cơ dễ bấm:** nút chính cao ~56 dp, ghim đáy ở phần lớn màn (02, 03, 04, 05, 08, 09, 11, 12, 13). Thẻ động cơ xếp 2 cột, cỡ lớn (~160 × 72 dp), có icon + tên, đúng thứ tự 8 động cơ. Thẻ được chọn có nền, viền và dấu tích.
> - **Trạng thái hệ thống rõ ràng:** 04a hiện "Đang lưu…", 07a có skeleton + "Đang tải…". 07b nêu nguyên nhân, cách sửa, trấn an rằng dữ liệu vẫn lưu trên máy và có "Thử lại". 07c nói rõ còn thiếu 2 khoản.
> - **Phục hồi lỗi tốt:** 03a/12a báo lỗi ngay dưới trường, có icon và cách sửa. 05a nêu tên khoản mua và thời gian hoàn tác. 06b, 11c có "Hoàn tác", 06a có "Xóa bộ lọc".
> - **Giọng văn trung tính, đúng brief:** câu góc nhìn ở 08 đúng mẫu của DESIGN.md. 12 có câu "Không có lựa chọn đúng hay sai", 13 có "Giá dự kiến · chưa tính vào chi tiêu". Dialog 13a dùng nút primary chứ không dùng màu đỏ.
> - **Giảm nhập liệu:** 03 điền sẵn "Hôm nay 23:10". 03c/04d điền sẵn tên, giá và động cơ từ danh sách mong muốn, và nói rõ là có thể đổi. 04b giải nghĩa từng động cơ.
>
> ### Ưu tiên sửa
> 1. **Mở lối vào Danh sách mong muốn cho mọi trạng thái Trang chủ (#1).** Hiện người dùng mới không thể bắt đầu Flow 6, nên mục tiêu thêm món < 20 giây không đạt được.
> 2. **Sửa các lỗi accessibility nhìn thấy được:** chữ bị cắt ở 03c và chip "+100.000 ₫" (#2), viền ô nhập đạt ≥ 3:1 (#5), giờ ở 06 tăng lên 14 sp (#7), thêm chú giải cho thanh "Động cơ chính" (#6). Đây là các điểm ảnh hưởng trực tiếp tới Nam: cận 2 độ, hay dùng trong phòng tối, màn 360 dp.
> 3. **Đồng bộ ngôn ngữ và component với DESIGN.md:** thay "khoản chi / giao dịch / lý do" (#8); snackbar sau khi lưu luôn có tên mục + "Hoàn tác", kể cả khi ngoại tuyến (#9); đổi nhãn nút dialog 13a thành "Chuyển vào Bỏ qua" (#12). Các điểm này giữ cảm giác "không bị phán xét" và cho Nam sửa sai được ngay.

**Đối chiếu với ảnh:** Mô tả của các phát hiện khớp với những gì thấy trên khung. Các con số AI ước lượng từ ảnh, gồm độ chênh giữa hai đoạn màu ở #6 và cỡ chữ ở #7, chưa được đo lại trong Figma. Riêng #20, file Figma đã đo vùng chạm của Button/Text là 48 dp (page `04 Design System › Accessibility check › 4`). Vì vậy #20 là cảnh báo cần kiểm tra lại từng link chữ, không phải lỗi đã chắc chắn. Phát hiện #2 và #5 trái với kết quả "Đạt" của checklist trong Figma: script chỉ đo cỡ chữ và chiều cao vùng chạm, không bắt được chữ tràn khung và contrast của viền ô nhập. Hai mục này được bổ sung vào `design-decisions.md` mục 2.6.

**Quyết định của tôi:**

| # | Phát hiện (tóm tắt) | Quyết định | Lý do | Việc trong Figma |
|---|---|---|---|---|
| PB-1 | Lối vào Danh sách mong muốn chỉ có ở 02d | **Chấp nhận** | Nielsen #6; người mới không thể bắt đầu Flow 6, trái mục tiêu thêm món < 20 giây | Thêm instance `Wishlist entry` vào 02, 02a, 02b, 02c. Khi chưa có món, entry ghi "Chưa có món nào · Thêm món". Không thêm lối vào ở Cá nhân: hai lối vào cùng chức năng làm phân tán, trái Nielsen #8 |
| PB-2 | Chữ tràn ở 03c; chip "+100.000 ₫" bị cắt; chip lọc ở 06 bị cắt tại lề | **Chấp nhận** | Accessibility (chữ không bị cắt ở 360 dp); Nielsen #4 | 03c: nút "Tiếp tục", chú thích "Bước tiếp theo: chọn động cơ (đã chọn sẵn Khuyến mãi)" bật wrap. 3 chip số tiền dùng Fill chia đều. Hàng chip lọc ở 06 cho tràn tới mép màn (bỏ clip ở lề 16 dp) |
| PB-3 | Không có gợi ý "khoản gần đây" ở bước 1 | **Từ chối** | Phạm vi lab: cần thêm nguồn dữ liệu "gần đây" và một hàng chip mới trên màn đã sát 800 dp (Nielsen #8). Thời điểm đã điền sẵn, bàn phím số mở sẵn (handoff), luồng 4 chạm + gõ tên vẫn trong mục tiêu ≤ 25 giây. Ghi lại làm ý tưởng cho bản sau | — |
| PB-4 | Bộ lọc và chọn kỳ nằm ngoài tầm ngón cái; "Sửa" ở 13 khác 05 | **Từ chối** | Hành động chính của mỗi màn đã ở đáy. Lọc và đổi kỳ là thao tác phụ, đặt dưới app bar theo chuẩn Material (Nielsen #4). Ở 05, "Sửa" là hành động chính. Ở 13, hành động chính là "Ghi khoản mua", nên "Sửa" là phụ và nằm trên app bar | — |
| PB-5 | Ô nhập và thẻ động cơ không có viền (1.16 : 1) | **Chấp nhận** | WCAG 1.4.11 (thành phần UI ≥ 3 : 1); Nam cận 2 độ, hay dùng trong phòng tối | Text field/Default và Motive card/Default thêm viền 1 dp. Trên thẻ trắng dùng `color/outline` #8A918A (3.23 : 1). Ô đặt thẳng trên nền #F5F6F2 (Đăng nhập, Đăng ký) dùng #7A817B (3.68 : 1), vì #8A918A trên nền chỉ đạt 2.98 : 1 |
| PB-6 | Thanh "Động cơ chính" không có chú giải; hai đoạn màu gần nhau | **Sửa** | DESIGN.md: biểu đồ luôn có nhãn chữ và phần trăm; WCAG 1.4.1 | Thêm một dòng chú giải dưới thanh: 3 động cơ nhiều nhất, mỗi động cơ có icon + tên + %. Tách các đoạn bằng khe 2 dp |
| PB-7 | Giờ ở 06 khoảng 12 sp; gợi ý mật khẩu đặt sai chỗ | **Chấp nhận** | Giờ là dữ liệu cốt lõi của thói quen mua đêm; đồng bộ với 02 (Nielsen #4); Nielsen #5 | Giờ trong Purchase row dùng Body Small 14 sp. Gợi ý "Mật khẩu có ít nhất 8 ký tự." dời xuống ngay dưới ô Mật khẩu, cỡ 14 sp |
| PB-8 | Lệch từ vựng ("khoản chi", "giao dịch", "lý do", "Thời gian ghi nhận") | **Chấp nhận** | Nielsen #4; bảng từ vựng trong DESIGN.md | "Thông tin khoản mua", "KHOẢN MUA VỪA NHẬP", "15 khoản mua", "Chưa có khoản mua", "Động cơ", "Chọn một động cơ chính", "Vui lòng chọn một động cơ.", "Thời điểm mua" (03 và 05) |
| PB-9 | Snackbar sau khi lưu không đồng nhất | **Chấp nhận một phần** | Nielsen #3, #4 | 02c: "Đã lưu “Trà sữa nướng” trên máy, sẽ đồng bộ khi có mạng · Hoàn tác". 11b: "Đã lưu “Chuột công thái học” · Hoàn tác". 11e: thêm Hoàn tác (gỡ khoản mua, món về Đang cân nhắc). 08a giữ nguyên, vì mở lại 09 là sửa được chiêm nghiệm nên không có rủi ro mất dữ liệu |
| PB-10 | Placeholder ở 12 trông như giá trị đã nhập | **Chấp nhận** | Nielsen #2, #9 | Placeholder dùng Body 16 regular, màu on-surface-variant |
| PB-11 | Thông tin bị lặp ở 02, 07, 08, 13 | **Sửa một phần** | Nielsen #8 | 02: bỏ dòng "Nhiều nhất: …" (trùng "Động cơ chính"), dòng phụ chỉ còn "Tuần này: 5 khoản". 07: bỏ thẻ "Tổng quan chu kỳ" để khung giờ lên màn đầu. 08: bỏ tiêu đề "Góc nhìn" trùng app bar. Giữ icon đầu dòng ở 02 và overline ở 13, vì giúp quét nhanh khi lướt bằng một tay (Nielsen #6) |
| PB-12 | Dialog 13a: hai nút "Hủy" / "Bỏ qua" dễ nhầm | **Chấp nhận** | Nielsen #2, #5 | Nút xác nhận đổi thành "Chuyển vào Bỏ qua". Nội dung: "“Bàn phím cơ” sẽ chuyển vào Bỏ qua. Bạn có 5 giây để hoàn tác." |
| PB-13 | Xóa toàn bộ dữ liệu chỉ cần một chạm | **Sửa một phần** | Nielsen #5 | Nội dung liệt kê đủ phạm vi: khoản mua, món mong muốn, chiêm nghiệm, nhắc nhở. "Hủy" dùng Button/Text cao 48 dp. Từ chối bước gõ "XÓA": dialog đã ghi rõ "Không thể hoàn tác", còn gõ chữ bằng một tay lại thêm ma sát cho persona |
| PB-14 | Giờ nhắc 21:00 cố định, sớm hơn giờ Nam hay mua | **Chấp nhận** | Nielsen #7; persona hay mua sau 22:00 | Hàng nhắc hiển thị giờ, chạm vào mở time picker, mặc định 23:00. Thống nhất "sau 22:00" giữa DESIGN.md và persona |
| PB-15 | Thông điệp lưu trữ mâu thuẫn; thiếu Đăng xuất; ô "Họ tên" trái quy tắc xưng hô | **Chấp nhận một phần** | Nielsen #1, #3, #4; DESIGN.md xưng "bạn"; persona ngại nhập nhiều | 01 và 10 dùng chung câu "Lưu trên máy, đồng bộ với tài khoản khi có mạng". 10 thêm mục Tài khoản (email, Đăng xuất). 00b bỏ "Họ tên" và "Xác nhận mật khẩu", thêm icon hiện/ẩn mật khẩu. Đã bổ sung 00a/00b vào `user-flow.md` và `DESIGN.md` |
| PB-16 | "Bắt buộc" tô đỏ; hai cách kiểm lỗi | **Sửa một phần** | DESIGN.md: đỏ chỉ dành cho lỗi | "Bắt buộc" đổi sang màu on-surface-variant. Giữ hai cách kiểm lỗi: 03 chỉ có một trường số nên kiểm ngay và khóa nút. 12 có 3 quy tắc nên chỉ báo khi bấm Lưu, để không hiện đỏ trong lúc đang gõ (persona sợ bị cảnh báo) |
| PB-17 | Icon lệch nghĩa ("$", xô giống thùng rác, ↻, mũi tên tăng) | **Chấp nhận** | Nielsen #2; giọng trung lập | Icon biên lai bỏ "$", tên món dùng shopping_bag, "Xóa bộ lọc" dùng filter_alt_off, 08 thay mũi tên tăng bằng icon lịch |
| PB-18 | 12 không có giải thích động cơ | **Chấp nhận** | Nielsen #10, #4 | Thêm text button "Các động cơ nghĩa là gì?" dưới câu hỏi ở cả 04 và 12, mở cùng bottom sheet 04b |
| PB-19 | Khung trạng thái lệch so với màn gốc | **Sửa một phần** | Nielsen #4 | 02a giữ chip "Hôm nay, 11/10", ẩn "Xem tất cả" khi 0 khoản. 06a giữ thứ tự chip như 06. Từ chối khóa chip 0 khoản: khi đổi kỳ trong lúc đang lọc vẫn cần trạng thái lọc trống. Từ chối ghim nút ở 07b, 07c, 11a: theo pattern empty / error state, hành động nằm trong thông báo, và màn lỗi không có hành động chính nào khác |
| PB-20 | Link chữ có thể nhỏ hơn 48 dp | **Chấp nhận** | Accessibility | Kiểm tra "Xem tất cả", "Quên mật khẩu?", "Đăng ký", "Để sau", "Hủy" đều là instance Button/Text cao 48 dp |

**Điều rút ra:** Checklist bằng script trong Figma chỉ bắt được những gì đo được bằng số (cỡ chữ, chiều cao). Phản biện trên ảnh bắt thêm chữ tràn khung, viền ô nhập, từ vựng lệch và trạng thái không khớp màn gốc. Hai cách kiểm tra bổ sung cho nhau.

---

## Tổng kết các vòng tinh chỉnh

| Vòng | Mục tiêu | Kết quả chính từ Stitch | Chuyển sang sửa trong Figma |
|---|---|---|---|
| R1 | Nhất quán (Nielsen #4) | 8 động cơ thống nhất, mỗi dòng 1 chip; dữ liệu mẫu liền mạch giữa các màn; chữ đủ dấu; xưng "bạn" | Bố cục 02' và 06' |
| R2 | Phù hợp persona Nam: dùng một tay, dễ đọc, không phán xét | Nút chính ghim đáy; khung lỗi riêng cho Bước 1/2; lưới động cơ icon + tên; bỏ ảnh trang trí; Góc nhìn còn 3 câu quan sát; Chiêm nghiệm và Cá nhân đúng nguyên văn | Câu khuyên bảo Stitch tự thêm; 02' và 06'; sai ngày và số liệu; nhãn Bước 1/2; Onboarding |
| R3 | Trạng thái hệ thống và phục hồi lỗi (Nielsen #1, #9) | Lần 1 thất bại (giao diện bị đơn giản hóa). Lần 2: 6 khung trạng thái trống, đang lưu, đang tải, lỗi, chưa đủ dữ liệu | Chip lọc được chọn; lưới động cơ khi đang lưu; ghim nút trên các khung của Mô hình |
| PB | Phản biện bằng AI trên Final UI (Nielsen, accessibility, persona) | 20 phát hiện gắn với màn hình (2 Cao, 13 Trung bình, 5 Thấp) | 11 chấp nhận, 7 chấp nhận một phần / sửa, 2 từ chối, xem bảng quyết định PB-1 đến PB-20 |

Các quyết định chấp nhận / sửa / từ chối quan trọng nhất được phân tích trong [`design/design-decisions.md`](../design/design-decisions.md).

**Điều rút ra khi làm việc với Stitch:**
- Prompt phải lặp lại đầy đủ ràng buộc mỗi lần; ghi "same constraints" là Stitch bỏ sót.
- Phải cho sẵn từ vựng và dữ liệu mẫu, nếu không Stitch tự đặt tên và tự bịa số liệu.
- Yêu cầu chung ("dùng 'động cơ' ở mọi nơi") dễ bị bỏ sót; liệt kê đích danh từng chỗ thì hiệu quả hơn. Những gì ghi nguyên văn trong prompt (dialog, 3 câu Góc nhìn) ra đúng gần như tuyệt đối.
- Xóa một câu khuyên bảo thì Stitch thường sinh câu khác cùng kiểu; quy tắc giọng văn phải được giữ bằng tay trong Figma.
- Stitch sinh mỗi khung độc lập nên không giữ được bố cục giữa các trạng thái của cùng một màn; phần này làm bằng component trong Figma.
- Prompt dài, sửa nhiều màn cùng lúc làm Stitch sinh lại toàn bộ và đánh mất những gì đã sửa (R3 lần 1). Prompt ngắn, ít màn, có khối khóa phong cách và ảnh ví dụ đúng/sai cho kết quả tốt (R3 lần 2).
- Phần tự báo cáo của Stitch không đáng tin (R1: 4/7 khẳng định sai so với ảnh), mọi kết quả phải đối chiếu với ảnh.

---

## C — Bổ sung theo checklist.design/mobile (13/10/2026)

**Bối cảnh:** nhóm trưởng yêu cầu tìm một checklist để AI review và giải quyết phần lớn vấn đề
trước khi sang bước tiếp theo. Nhóm chọn checklist.design/mobile (25 checklist).

### C0 – Đối chiếu và lập kế hoạch
- Công cụ AI: Claude (Cowork, trình duyệt + Claude Docs)
- Prompt: "Hãy check checklist này và kiểm tra xem hiện tại nhóm tôi đã làm đầy đủ các request về mobile chưa. Tạo 1 file docs liệt kê những gì đã hoàn thành và còn thiếu, gợi ý cho những cái thiếu" → sau đó "không nhất thiết hoàn thành 100%, chỉ cần phần lớn… gợi ý lại" → "tạo kế hoạch phát triển prompt từng giai đoạn".
- Kết quả AI đưa ra: doc đối chiếu (3 đạt, 5 một phần, 5 chưa có, 12 không áp dụng); phạm vi rút gọn còn 57 mục, ước tính 44% → gói 8 khung để lên ~88%; kế hoạch prompt 9 giai đoạn (0–8), mỗi giai đoạn có tiêu chí "Xong khi".
- Nhóm chỉnh sửa lại: loại các mục phụ thuộc backend và mua bán chưa chốt; chốt cách lưu dữ liệu "lưu trên máy, đồng bộ khi đăng nhập"; yêu cầu AI dừng sau mỗi giai đoạn để nhóm xác nhận.
- Đánh giá: checklist giúp phát hiện phần "rìa ứng dụng" (tài khoản, khởi động, quyền) bị bỏ sót; AI ban đầu đếm cả mục không phù hợp, nhóm phải tự quyết phạm vi.

### C1 – Giai đoạn 1: Chuẩn bị icon và component
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: Prompt Giai đoạn 1 trong kế hoạch bổ sung checklist Mobile
- Kết quả AI đưa ra: icon eye/eye-off/logout (342:551, 342:558, 342:567); Dialog thành bộ Type=Danger/Default (343:600); component Password strength 3 mức (344:607); ví dụ ô Mật khẩu trong Text field (342:574)
- Nhóm chỉnh sửa lại: không thêm icon search (Tìm kiếm ngoài phạm vi); Text field Error đã có sẵn nên chỉ bổ sung icon gợi ý; sửa dòng lỗi tự xuống hàng; đổi tên 12 ô icon bị đặt nhầm
- Đánh giá: AI kiểm tra component có sẵn trước khi tạo nên không bị trùng; phải sửa lỗi chữ bị cắt và bố cục trang bị đè sau khi thêm khối mới

### C2 – Giai đoạn 2: Wireframe 8 khung
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: Prompt Giai đoạn 2 trong kế hoạch bổ sung checklist Mobile
- Kết quả AI đưa ra: section "Wireframe – Bổ sung checklist" (351:303) gồm 8 khung low-fi, mỗi khung có ghi chú mục checklist
- Nhóm chỉnh sửa lại: giữ chính tả "Xóa" cho thống nhất với file; sửa tiêu đề App bar của 3 khung còn "Quay lại"; khung Cá nhân để cuộn dọc
- Đánh giá: nhân bản wireframe cũ giữ đúng phong cách WF kit; vẫn phải kiểm tra bằng ảnh chụp vì có chỗ ghi đè chữ không ăn

### C3 – Giai đoạn 3A–3C: Final UI
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: Prompt Giai đoạn 3A, 3B, 3C trong kế hoạch
- Kết quả AI đưa ra: Đăng nhập – lỗi (353:4575), Đăng ký – bản sửa (353:4671); 7 khung Cá nhân & Tài khoản (359:4641, 359:4759, 359:4884, 359:4996, 359:5079, 359:5118, 359:5164); 00 Splash (366:4923), 05a Xin quyền thông báo (366:4930); component App icon (365:599) và khối Icon app ở page 04 (365:1160)
- Nhóm chỉnh sửa lại: màn Flow 7 gốc dùng component từ thư viện đã publish (bản cũ, thiếu trạng thái Error) nên đổi sang component trong file cho khung mới; dùng nút Tonal thay nút viền (bộ Button không có kiểu viền); sửa màu các dòng bị đỏ do nhân bản, cỡ chữ ô mật khẩu, vị trí snackbar, bo góc icon cỡ nhỏ; dời section Flow 8–10 tránh đè
- Đánh giá: dựng nhanh nhờ nhân bản màn có sẵn, nhưng nhân bản kéo theo kiểu chữ/màu của dòng gốc nên cần chụp ảnh kiểm tra từng lần

### C4 – Giai đoạn 4: Cập nhật User Flow
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: Prompt Giai đoạn 4 trong kế hoạch
- Kết quả AI đưa ra: IA thêm Splash và nhánh Tài khoản / Hỗ trợ & thông tin / Dialog đăng xuất; Flow 1 thêm quyết định "Lần đầu lưu & chưa cấp quyền?" và 05a; Flow 7 thêm Splash → "Đã đăng nhập?", vòng lỗi đăng nhập, hàng nhánh tài khoản
- Nhóm chỉnh sửa lại: sửa chữ trong ô quyết định mới bị giữ chữ cũ; dời Flow 8–10 xuống vì Flow 7 cao thêm
- Đánh giá: nhân bản khối có sẵn giữ đúng chú thích của page (liền = chính, đứt đỏ = lỗi, đứt xám = phụ)

### C5 – Giai đoạn 5: Nối Prototype
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: Prompt Giai đoạn 5 trong kế hoạch
- Kết quả AI đưa ra: section mới trên page 06 (377:4390) với 11 khung; luồng ★ bắt đầu ở Splash (After delay 0,8 giây); nối Đăng nhập → lỗi → Trang chủ, Đăng ký mới, 05 → 05a → Trang chủ, nhánh Tài khoản / Đổi mật khẩu / Xóa tài khoản / Đăng xuất; 16 tab Cá nhân dùng điều kiện theo biến thong-bao/da-tu-choi; luồng ★ đi tới 73/79 khung
- Nhóm chỉnh sửa lại: sửa icon nút Đăng xuất (biến thể Tonal không nhận thuộc tính Icon); giữ nguyên 2 khung bản cũ; 3 mục Hỗ trợ & thông tin để ngoài phạm vi
- Đánh giá: biến prototype giúp tab Cá nhân hiển thị đúng trạng thái đã từ chối quyền; AI tự kiểm tra khả năng đi tới của từng khung nên phát hiện khung bị bỏ sót

### C6 – Giai đoạn 6: Sửa nhỏ
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: Prompt Giai đoạn 6 trong kế hoạch
- Kết quả AI đưa ra: "Trước khi mua" chuyển sang nút Tonal (320:8840, 274:4524); khung Hub chưa ghi hôm nay (385:4946); Trang chủ vừa tạo tài khoản (385:5021); Bước 1/2 có bàn phím số (385:5079); quét 90 khung xác nhận không còn màn có 2 nút tô đặc
- Nhóm chỉnh sửa lại: bottom sheet đã có thanh kéo sẵn nên bỏ qua; thêm phím "000" cho số tiền VNĐ
- Đánh giá: kiểm tra trước khi sửa tránh làm trùng thứ đã có; quét tự động bắt cả trường hợp nút ẩn cần loại trừ

### C7 – Giai đoạn 7: AI review theo checklist
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: Prompt Giai đoạn 7 trong kế hoạch
- Kết quả AI đưa ra: bảng chấm 56 mục (10 checklist) kèm node ID; kiểm tra accessibility tự động 14 khung mới; lần 1: 94,6% CHƯA ĐẠT (thiếu ghi chú autofill, haptic); lần 2 sau khi thêm 2 ghi chú: 98,2% ĐẠT
- Nhóm chỉnh sửa lại: thêm ghi chú autofill (354:4762) và haptic (mô tả 15:216); 2 mục Một phần để tuỳ chọn
- Đánh giá: ngưỡng "không còn Chưa có ở Login/Settings/Account" giúp phát hiện mục nhỏ dễ bỏ sót; chấm bằng script đọc node khách quan hơn chấm bằng mắt

### C8 – Giai đoạn 8: Cập nhật tài liệu
- Công cụ AI: Claude (Cowork) soạn nội dung; Claude (Claude Code) dán vào repo và đối chiếu với file hiện có và với tên khung trong Figma
- Prompt: Prompt Giai đoạn 8 trong kế hoạch → "làm đúng như hướng dẫn đi" → "sửa luôn" (sửa các điểm lệch AI báo lại sau khi dán)
- Kết quả AI đưa ra: nội dung cập nhật DESIGN.md, user-flow.md (Flow 1, Flow 7, IA), ghi chú bàn giao Flutter, phần Phạm vi cho báo cáo, mục log này
- Nhóm chỉnh sửa lại:
  - Không thêm trùng 2 token `surface-container`, `error-container` (đã có), chỉ cập nhật cột "Dùng cho".
  - Giữ mã 00a / 00b cho Đăng nhập / Đăng ký; thêm dòng riêng "Quên mật khẩu" và "00 Hub" vào bảng màn hình.
  - Sơ đồ điều hướng mới bỏ sót Danh sách mong muốn (11–13), cạnh 06 → 07 và Đăng xuất, nên nhóm giữ lại các phần này. Sơ đồ Flow 1 mới giữ nhánh "Thêm ghi chú?" và lối vào lần đầu, vì phần mô tả vẫn nhắc tới.
  - "Đổi mật khẩu – đã lưu" ghi màn gốc 10b (bản nháp ghi 10a). Thêm Splash, Hub, Quên mật khẩu, 05a, 10a, 10b vào bảng ánh xạ flow → màn hình.
  - Ghi chú Flutter gộp vào `handoff/flutter-handoff.md` (mục 8) thay vì tạo file mới.
  - Mã cũ 05a / 10a / 10b (dialog xóa, xác nhận xóa toàn bộ, đã xuất dữ liệu) trong handoff trùng với mã màn mới. Nhóm đổi sang tên khung Figma; tên file ảnh trong `assets/figma/` giữ nguyên, có ghi chú.
  - Giờ nhắc: PB-14 từng chốt mặc định 23:00, nhưng Figma (10 Cá nhân, 05a) vẫn ghi 21:00 và cho đổi giờ ở Cá nhân. Theo quy ước "lệch thì lấy Figma", handoff ghi mặc định 21:00.
  - Cập nhật README: công cụ AI, số màn hình (21), mô tả Flow 1 và Flow 7.
- Đánh giá: bản nháp soạn từ tài liệu ngày 11–12/10 nên lệch với repo ở nhiều chỗ (token đã có, Flow 7 đã có, mã màn đã dùng). Dán nguyên văn sẽ gây trùng và mất nội dung. Đối chiếu từng mục với file thật và với tên khung trong Figma là bước bắt buộc. Flow 8–10 (Trước khi mua, AI) có trong Figma nhưng vẫn chưa có trong `user-flow.md`.

---

## RS — Research kiểm chứng (MÔ PHỎNG bằng AI)

**Bối cảnh:** sau buổi góp ý, thầy yêu cầu persona phải đến từ research và mỗi bước có bằng chứng; cho phép dùng người dùng mô phỏng nếu trình bày rõ câu hỏi và quy trình. Nhóm không đủ thời gian khảo sát người thật nên chọn mô phỏng, ghi nhãn rõ.

### RS-1 – Kế hoạch research và desk research
- Công cụ AI: Claude (Cowork, tìm kiếm web)
- Prompt: "Lập kế hoạch research: 5 câu hỏi nghiên cứu, phương pháp, số người; tìm nguồn thật về hành vi mua online và mua bốc đồng của người trẻ Việt Nam và các app quản lý chi tiêu."
- Kết quả AI đưa ra: RQ1–RQ5; nguồn D1 (YouNet ECI 2025), D2 (HUTECH 2026), D3 (blog MoMo); bảng 4 app C1–C4
- Nhóm chỉnh sửa lại: ghi D3 là nguồn quảng bá, diễn đạt "theo mô tả của nhà phát hành"; tự cài app để chụp màn hình
- Đánh giá: nguồn thật cho căn cứ chọn nhóm tuổi (Gen Z 53,4% người mua online hằng tuần) và cơ chế FOMO → mua bốc đồng

### RS-2 – Khảo sát mô phỏng (n = 30)
- Công cụ AI: Claude (Cowork, Python)
- Prompt: "Soạn bộ 15 câu khảo sát theo RQ1–RQ5 rồi viết script sinh 30 người trả lời, mỗi nhóm tuổi một bộ xác suất, ghi rõ giả định nào có nguồn, giả định nào chưa; chốt seed trước khi chạy; vẽ biểu đồ có nhãn MÔ PHỎNG."
- Kết quả AI đưa ra: `survey_sim.py` (seed 2026), `survey-mo-phong.csv`, 5 biểu đồ, bảng so sánh theo nhóm tuổi
- Nhóm chỉnh sửa lại: giữ nguyên kết quả lệch giả định ("Ảnh hưởng MXH" chỉ 4/30), không chạy lại seed; quyết định giữ động cơ này dựa trên nguồn thật D1
- Đánh giá: kết quả trùng với giả định chưa có nguồn chỉ phản ánh lại giả định, không phải bằng chứng; cần khảo sát thật để thay

### RS-3 – Phỏng vấn mô phỏng (5 người)
- Công cụ AI: Claude (Cowork)
- Prompt: prompt đóng vai nguyên văn ở `research.md` mục 5.3, hồ sơ lấy từ dòng khảo sát (S02/S12, S10/S17, S03/S14, S20/S21, S29/S30)
- Kết quả AI đưa ra: 5 transcript (I1–I5)
- Nhóm chỉnh sửa lại: đổi hồ sơ I4 sang nhóm 26–30 cho khớp dòng khảo sát; giữ câu trả lời "không đúng ý" của I5 (thích cảnh báo đỏ) làm căn cứ cho anti-persona
- Đánh giá: phỏng vấn mô phỏng cho câu trích sinh động nhưng không có hành vi bất ngờ như người thật

### RS-4 – Affinity, insight và 5 persona
- Công cụ AI: Claude (Cowork)
- Prompt: "Gom dữ liệu D, C, Q, I thành affinity map; rút insight, mỗi insight ghi mã nguồn và hệ quả thiết kế; viết lại 5 persona (1 chính, 3 phụ, 1 anti-persona) theo cùng một mẫu, có nguồn dữ liệu cho từng persona."
- Kết quả AI đưa ra: 8 nhóm affinity, 7 insight (INS1–INS7), bảng đối chiếu giả định, 5 persona, ma trận persona → flow
- Nhóm chỉnh sửa lại: bỏ ảnh stock; bỏ các chỉ tiêu không đo được trong Lab 2 và số "> 60 giây" không có nguồn; đổi tuổi P4 thành 29 để không mâu thuẫn với dữ liệu nhóm 31+
- Đánh giá: nhờ dữ liệu so sánh theo tuổi, câu "vì sao không làm cho người lớn tuổi" có câu trả lời bằng số liệu

## UT — Kiểm thử khả dụng (MÔ PHỎNG bằng AI)
- Công cụ AI: Claude (Cowork, Figma MCP, Python)
- Prompt: prompt đi qua nhiệm vụ nguyên văn ở `usability-test.md` mục 2; thời gian tính bằng KLM (`usability_sim.py`, seed 393)
- Kết quả AI đưa ra: T1 4/5 đạt ≤ 25 giây (trung vị 21,7 giây); T2 5/5 < 20 giây; T5 5/5 hoàn thành (bản đầu ghi 4/5, đã sửa); SUS 78,0; 5 phát hiện F1–F5
- Nhóm chỉnh sửa lại: đối chiếu F1 và F4 trực tiếp trong Figma (thẻ Cảm xúc ở trạng thái Selected tại 04 Bước 2/2; khối "Mở cài đặt" cao 44 dp); xếp F3, F5 vào "không sửa". Khi rà lại prototype ở vòng R4, phát hiện công tắc nhắc nhở có mở 05a, trái với giả định của bản mô phỏng đầu (1 người bỏ cuộc ở T5) → tính lại T5, hạ F4 từ mức 3 xuống 2
- Đánh giá: F1 là lỗi thật trong file mà tự nhóm review không thấy; AI nhìn ảnh tĩnh không biết chỗ nào có tương tác, nên kết quả mô phỏng phải đối chiếu với prototype; số thời gian chỉ là ước lượng, cần test người thật

## R4 — Sửa sau kiểm thử
- Công cụ AI: Claude (Figma MCP, Plugin API)
- Prompt: "Sửa Figma R4 trước đi" (R4-1, R4-2, R4-3 theo `usability-test.md` mục 8)
- Kết quả AI đưa ra:
  - R4-1: khung "04 Ghi khoản mua – Bước 2/2 (chưa chọn động cơ)" ở 03 Final UI (biến thể Motive grid "Selected=Không", nút Lưu Disabled, dòng "Chọn một động cơ để lưu"); ở 06 Prototype, khung 04 (63:2483) mở ra chưa chọn, 2 biến `dongCo/daChon`, `dongCo/chuaChon` bật nút Lưu khi chạm thẻ bất kỳ; "Tiếp tục" ở bước 1 và nền mờ của sheet giải thích đặt lại trạng thái
  - R4-2: thẻ "Thông báo đang tắt" + nút Tonal "Mở cài đặt" 48 dp → 05a ở "10 Cá nhân – chưa cấp quyền thông báo" (Final UI 359:4759, Prototype 377:4525); bỏ dòng chữ nhỏ 44 dp
  - R4-3: nút chữ "Giải thích động cơ" cạnh câu "Vì sao bạn mua?" ở 16 khung Bước 2/2, mở sheet giải thích; câu phụ rút còn 1 dòng, khoảng cách khối 12 → 8 dp
  - Sửa thêm: biến thể nút Disabled dùng độ mờ của lớp (38%) cho chữ và icon, vì độ mờ của màu bị mất ở instance
- Nhóm chỉnh sửa lại: bỏ R4-4 vì thiết kế đã có mũi tên 48 dp và chip "Tháng 10/2026 ▾"; giữ chọn sẵn ở khung Sửa và khung từ danh sách mong muốn vì động cơ do người dùng chọn trước đó; dời section Flow 8–10 xuống 200 px vì section Flow 7 cao thêm
- Đánh giá: ảnh trước `assets/figma/r4-truoc-04-purchase-reason.png`, ảnh sau `r4-sau-04-chua-chon.png`, `r4-sau-04-da-chon.png`, `r4-sau-10-ca-nhan.png` (cùng thư mục); cần chạy lại T1 và T5 với người thật để xác nhận
