# Design Decisions & Accessibility

**Project:** Why I Buy? – lấy cảm hứng từ "The Psychology of Money"
**Course:** PRM323 – Lab 2
**Nguồn:** các quyết định dưới đây lấy từ quá trình làm việc với Google Stitch (P1, P2, R1–R3) trong [`ai/ai-design-log.md`](../ai/ai-design-log.md). Token màu, chữ, khoảng cách theo [`DESIGN.md`](DESIGN.md).

---

## 1. Các quyết định thiết kế

| # | Đề xuất của AI | Quyết định | Căn cứ chính |
|---|---|---|---|
| 1 | Thẻ nhắc nhở, khuyên bảo, khen ngợi trên màn ghi khoản mua và chi tiết | **Từ chối** | Persona (cảm giác tội lỗi), thông điệp "Hiểu trước khi thay đổi" |
| 2 | Thẻ động cơ có icon + tên + một dòng mô tả | **Sửa** | Ràng buộc 800dp và ≥ 14sp; mục tiêu ghi ≤ 25 giây; Nielsen #6 |
| 3 | Dialog xác nhận xóa dạng overlay | **Chấp nhận** (bổ sung hoàn tác) | Nielsen #3, #5; Nam thao tác một tay dễ chạm nhầm |
| 4 | Thẻ Góc nhìn chứa số liệu và diễn giải tâm lý | **Sửa** | Brief: insight là quan sát trung lập; Nielsen #2; persona |
| 5 | Màn lỗi và skeleton loading của Mô hình | **Chấp nhận** (chỉnh vị trí nút) | Nielsen #1, #9 |

---

### Quyết định 1 — TỪ CHỐI: thẻ nhắc nhở và khuyên bảo

**AI đề xuất:** Ở P1, Stitch tự thêm thẻ "Bạn có đang thật sự cần? Các khoản chi sau 23:00 thường xuất phát từ áp lực học tập hoặc sự mệt mỏi…" vào bước 1 của Ghi khoản mua. Khi các thẻ này bị xóa, Stitch lại sinh câu mới cùng kiểu ở R2: "Ghi nhận đơn thuần, không tự phán xét…" (Bước 1/2), "Bạn nhận diện được cơn sốt ưu đãi kịp thời. Sự tỉnh thức là bước đầu tiên…" (Chi tiết).

| Trước | Sau (đã bỏ thẻ) |
|---|---|
| ![](../assets/stitch/stitch1/v1-03-add-purchase-error.png) | ![](../assets/stitch/stitch%20refinement%202/r2-step1-error.png) |

**Phân tích:**
- **Persona:** Nam đã bỏ các app chi tiêu vì cảm giác tội lỗi khi bị cảnh báo. Câu "Bạn có đang thật sự cần?" đặt đúng lúc Nam vừa mua xong chính là trải nghiệm đó.
- **Thứ tự hiển thị:** thẻ xuất hiện *trước* bước chọn động cơ, nên có thể khiến Nam chọn động cơ "đúng đắn" hơn là động cơ thật → dữ liệu mất giá trị.
- **Thông điệp sản phẩm:** "Hiểu trước khi thay đổi" nghĩa là app quan sát, không dạy bảo. Cả câu khen ("Bạn nhận diện được… kịp thời") cũng là đánh giá hành vi.

**Quyết định:** Từ chối mọi thẻ, câu nhắc nhở, khen ngợi hoặc suy diễn tâm lý. Vì Stitch tự thêm lại sau mỗi vòng, các câu còn sót được xóa tay trong Figma, và quy tắc giọng văn được ghi vào DESIGN.md.
**Vị trí trong Figma:** `03 Final UI` – màn 03, 05.

---

### Quyết định 2 — SỬA: thẻ động cơ chỉ còn icon + tên

**AI đề xuất:** Ở P1, Stitch làm lưới 8 thẻ động cơ, mỗi thẻ có icon, tên và một dòng mô tả nhỏ ("Thiết yếu thường ngày", "Ưu đãi, combo…").

| Trước | Sau |
|---|---|
| ![](../assets/stitch/stitch1/v1-04-purchase-reason.png) | ![](../assets/stitch/stitch%20refinement%202/r2-step2.png) |

**Phân tích:**
- **Giữ lại:** dạng lưới thẻ có icon thay vì danh sách thả xuống là đề xuất tốt. Nam nhận ra động cơ qua icon mà không phải nhớ (Nielsen #6), và mỗi thẻ là một vùng chạm lớn.
- **Vấn đề:** dòng mô tả nhỏ hơn 14sp (Nam cận 2 độ) và làm lưới dài quá khung 800dp. Nút "Lưu" bị đẩy xuống dưới, Nam phải cuộn bằng một tay, đi ngược mục tiêu ghi ≤ 25 giây.
- **Đánh đổi:** tên 8 động cơ đã đủ rõ; phần giải thích có thể đặt ở Onboarding.

**Quyết định:** Sửa: giữ lưới 2 × 4 với icon + tên, bỏ dòng mô tả. Thẻ được chọn thể hiện bằng nền, viền và dấu tích (không chỉ đổi màu). Lưới, ô ghi chú và nút "Lưu" nằm gọn trong một màn.
**Vị trí trong Figma:** `05 Components` – Motive card (default / selected / disabled); `03 Final UI` – màn 04.

---

### Quyết định 3 — CHẤP NHẬN: dialog xác nhận xóa, bổ sung hoàn tác 5 giây

**AI đề xuất:** Ở P2, Stitch làm dialog xóa dạng overlay trên nền tối, nút "Hủy" dạng chữ và nút "Xóa" màu đỏ có icon.

| P2 | Sau R2 |
|---|---|
| ![](../assets/stitch/stitch2/v2-05b-delete-dialog.png) | ![](../assets/stitch/stitch%20refinement%202/r2-delete-dialog.png) |

**Phân tích:**
- **Nielsen #5 (phòng ngừa lỗi):** xóa là hành động khó đảo ngược, cần một bước xác nhận. Hai nút tách biệt, nút nguy hiểm có màu đỏ và icon, nên không chỉ dựa vào màu.
- **Nielsen #3 (kiểm soát và tự do):** bản P2 hứa "có thể hoàn tác" nhưng màn sau khi xóa không có hoàn tác. Lời hứa này phải được thực hiện.
- **Persona:** Nam dùng một tay, dễ chạm nhầm. Hoàn tác ngay sau khi xóa tốn ít công hơn nhập lại cả khoản mua.

**Quyết định:** Chấp nhận dạng dialog. Sửa nội dung thành "“Tai nghe Bluetooth” sẽ bị xóa khỏi lịch sử. Bạn có 5 giây để hoàn tác." và thêm snackbar "Đã xóa … · Hoàn tác" ở màn Lịch sử. Cùng kiểu snackbar dùng cho "Đã lưu … · Hoàn tác" sau khi ghi khoản mua.
**Vị trí trong Figma:** `05 Components` – Dialog, Snackbar; `06 Prototype` – Flow 3.

---

### Quyết định 4 — SỬA: thẻ Góc nhìn chỉ còn câu quan sát từ dữ liệu

**AI đề xuất:** Ở P2 và R1, Stitch viết thẻ Góc nhìn có số liệu không có nguồn ("Khoảng dừng 15 phút giúp giảm 40% mua bốc đồng", "75% đơn sau 23h…") và diễn giải tâm lý ("Bạn thường lướt điện thoại trước khi ngủ", "…những ngày có lịch học dày đặc").

| Trước | Sau |
|---|---|
| ![](../assets/stitch/stitch2/v2-08-insights.png) | ![](../assets/stitch/stitch%20refinement%202/r2-quote.png) |

**Phân tích:**
- **Ràng buộc trong brief:** insight phải là quan sát trung lập, lấy từ chính dữ liệu Nam đã ghi.
- **Nielsen #2:** con số không lấy từ dữ liệu của người dùng thì không đúng với thực tế của họ, và làm giảm niềm tin vào toàn bộ màn hình.
- **Nhất quán dữ liệu:** các số liệu bịa còn mâu thuẫn với màn Mô hình (P2: "8/15 khoản từ 22h" vs "75% đơn sau 23h").

**Quyết định:** Sửa: giữ dạng thẻ có icon, thay nội dung bằng 3 câu kiểm chứng được từ dữ liệu mẫu: "5 trong 15 khoản tháng này gắn với Khuyến mãi.", "8 trong 15 khoản được ghi sau 18:00.", "Cả 4 khoản Cảm xúc đều được ghi sau 22:00." Khung "Tối" ở màn Mô hình được định nghĩa là 18–05h để hai màn dùng cùng một cách tính.
**Vị trí trong Figma:** `03 Final UI` – màn 07, 08.

---

### Quyết định 5 — CHẤP NHẬN: trạng thái lỗi và đang tải của Mô hình

**AI đề xuất:** Ở R3 (lần 2), Stitch tạo màn lỗi gồm icon wifi gạch trong vòng tròn, tiêu đề, câu nêu nguyên nhân và trấn an dữ liệu, nút "Thử lại". Màn đang tải là skeleton giữ đúng khung sườn biểu đồ.

| Đang tải | Lỗi | Chưa đủ dữ liệu |
|---|---|---|
| ![](../assets/stitch/stitch%20refinement%203/r3-chart-loading.png) | ![](../assets/stitch/stitch%20refinement%203/r3-chart-error.png) | ![](../assets/stitch/stitch%20refinement%203/r3-chart-insufficient.png) |

**Phân tích:**
- **Nielsen #1:** skeleton cho Nam biết app đang xử lý, và vì giữ đúng hình dạng biểu đồ nên khi có kết quả bố cục không bị nhảy.
- **Nielsen #9:** màn lỗi có đủ 3 yếu tố: nguyên nhân bằng ngôn ngữ dễ hiểu ("Kiểm tra kết nối mạng…"), trấn an ("Các khoản đã ghi vẫn được lưu trên máy") và một hành động khắc phục.
- **Không ngõ cụt:** màn chưa đủ dữ liệu dẫn thẳng về Flow 1 bằng nút "Ghi khoản mua".

**Quyết định:** Chấp nhận, với 2 chỉnh sửa trong Figma: nút "Thử lại" và "Ghi khoản mua" ghim ở thanh đáy như mọi màn khác; khung lỗi và khung chưa đủ dữ liệu dùng chung một component Empty/Error state.
**Vị trí trong Figma:** `05 Components` – Skeleton, Empty/Error state; `06 Prototype` – Flow 2 (đang tải → kết quả, lỗi → Thử lại).

---

## 2. Accessibility

### 2.1. Độ tương phản (WCAG 2.1, tính từ token trong DESIGN.md)

| Cặp màu | Giá trị | Tỷ lệ | Yêu cầu | Kết quả |
|---|---|:-:|:-:|:-:|
| Chữ trắng trên nút chính | `#FFFFFF` / `#2E4A9E` | 8.11 : 1 | 4.5 : 1 | Đạt |
| Chữ chính trên nền màn hình | `#1A2320` / `#F5F6F2` | 14.82 : 1 | 4.5 : 1 | Đạt |
| Chữ phụ trên nền màn hình | `#545E59` / `#F5F6F2` | 6.20 : 1 | 4.5 : 1 | Đạt |
| Chữ phụ trên thẻ trắng | `#545E59` / `#FFFFFF` | 6.73 : 1 | 4.5 : 1 | Đạt |
| Chữ lỗi trên thẻ trắng | `#B3261E` / `#FFFFFF` | 6.54 : 1 | 4.5 : 1 | Đạt |
| Chữ primary trên nền được chọn | `#2E4A9E` / `#E3E8F7` | 6.62 : 1 | 4.5 : 1 | Đạt |
| Viền ô nhập, chip | `#8A918A` / `#FFFFFF` | 3.23 : 1 | 3 : 1 (thành phần giao diện) | Đạt — chỉ dùng cho viền, không dùng cho chữ |
| 8 chip động cơ (chữ / nền) | ví dụ `#6B5200` / `#FFF3C4` | 6.66 – 9.43 : 1 | 4.5 : 1 | Đạt cả 8 |

Cách tính: công thức độ sáng tương đối của WCAG 2.1. Có thể kiểm lại bằng WebAIM Contrast Checker.

### 2.2. Vùng chạm (tối thiểu 48 × 48 dp)

| Thành phần | Kích thước | Đạt? |
|---|---|:-:|
| Nút chính (ghim đáy) | cao 56 dp, full width | [đo trong Figma] |
| Thẻ động cơ | [đo trong Figma] | |
| Chip số tiền nhanh "+20.000…" | [đo trong Figma] | |
| Chip lọc ở Lịch sử | [đo trong Figma] | |
| Icon button (Back, Xóa) | icon 24 dp trong vùng chạm 48 dp | [đo trong Figma] |
| Tab thanh điều hướng | [đo trong Figma] | |

### 2.3. Cỡ chữ
- Chữ nội dung tối thiểu 14 sp (Body small 14/20); chỉ nhãn thanh điều hướng và mốc giờ dùng 12 sp, medium.
- Kiểm tra trong Figma: không text layer nào dưới 14 sp ngoài hai loại trên. [ghi kết quả sau khi kiểm tra]

### 2.4. Không chỉ dùng màu
- Động cơ luôn có icon + tên.
- Thẻ động cơ được chọn: nền + viền + dấu tích.
- Tab đang chọn: nền pill + chữ đậm.
- Lỗi nhập liệu: viền + icon + câu hướng dẫn.
- Biểu đồ Mô hình: mỗi thanh và cột đều có số và phần trăm. Biểu đồ chấm không có số đã bị bỏ ở R2.

### 2.5. Màn hình 360 dp và 412 dp

| Màn hình | 360 × 800 | 412 × 915 | Ghi chú |
|---|---|---|---|
| 02 Trang chủ | [ảnh] | [ảnh] | |
| 04 Ghi khoản mua – Bước 2/2 | [ảnh] | [ảnh] | Lưới 2 × 4 co giãn theo chiều ngang |
| 06 Lịch sử | [ảnh] | [ảnh] | Tên món xuống 2 dòng, không cắt |
| 07 Mô hình | [ảnh] | [ảnh] | |

Cách kiểm tra: các khung dùng Auto Layout với ràng buộc Left & Right. Nhân bản khung 360 rồi đổi chiều rộng thành 412, kiểm tra không có chữ bị cắt hay phần tử tràn khung.