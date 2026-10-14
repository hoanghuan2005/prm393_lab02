# Why I Buy? – The Psychology of Money
### PRM323 — Lab 2: Thiết kế UI/UX có hỗ trợ AI (Google Stitch → Figma)

| | |
|---|---|
| **Nhóm** | Group 7 – Lab 2: The Psychology of Money |
| **Thành viên** | Đào Tâm Hoàng – SE194103 · Nguyễn Đình Ngọc Ân – SE196654 · Huỳnh Đăng Khoa – SE193040 · Ngô Gia Kiệt – SE183268 · Hồ Hữu Hoàng Huân – SE192248 |
| **Lớp** | `[Điền mã lớp]` |
| **Học kỳ** | Fall 2026 |

## 1. Chủ đề

**Why I Buy?** là ứng dụng Android giúp người trẻ mới đi làm ghi nhanh một khoản mua kèm **động cơ** (Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác). App tổng hợp lại thành mô hình theo động cơ và khung giờ mà không chấm điểm, không cảnh báo đỏ. Lấy cảm hứng từ *The Psychology of Money* (Morgan Housel), với thông điệp "Hiểu trước khi thay đổi".

**Persona một dòng:** Nguyễn Hải Nam, 22 tuổi, sinh viên năm cuối CNTT kiêm thực tập sinh (6–9 triệu/tháng), hay chốt flash sale và đặt đồ ăn sau 22h, dùng điện thoại một tay, cận 2 độ, đã bỏ các app chi tiêu vì nhập lâu và cảm giác tội lỗi.

**Tiêu chí thành công:** ghi một khoản mua kèm động cơ trong ≤ 25 giây; thêm một món vào danh sách mong muốn trong < 20 giây.

## 2. Link Figma (ai có link đều xem được)

| Page | Link |
|---|---|
| File Figma | https://www.figma.com/design/jCQEcxnXTYJ9b27pdsfFfS/Untitled |
| 01 User Flow | https://www.figma.com/design/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=0-1 |
| 02 Wireframe | https://www.figma.com/design/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=2-2 |
| 03 Final UI | https://www.figma.com/design/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=2-3 |
| 04 Design System | https://www.figma.com/design/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=2-4 |
| 05 Components | https://www.figma.com/design/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=2-5 |
| 06 Prototype | https://www.figma.com/design/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=2-6 |
| Chạy prototype (bắt đầu từ Splash, danh sách flow ở cột trái) | https://www.figma.com/proto/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=377-4391&show-proto-sidebar=1&scaling=scale-down |

Dự án Google Stitch (Flow 6): https://stitch.withgoogle.com/projects/1668611817022706714

## 3. Công cụ AI đã dùng

| Công cụ | Dùng để làm gì |
|---|---|
| Google Stitch | Sinh UI ban đầu (P1, P2), 3 vòng tinh chỉnh R1–R3 và Flow 6 (F6). Prompt nguyên văn và ảnh trong `ai/ai-design-log.md`, `assets/stitch/` |
| Claude (claude.ai) | Soạn nháp persona, user flow, DESIGN.md và prompt Stitch; hỗ trợ đối chiếu ảnh khi nhận xét output Stitch |
| Claude (claude.ai + Figma connector) | Phản biện ảnh Stitch của Flow 6; dựng Flow 6 trong Figma theo prompt của nhóm |
| Claude (Claude Code) | Phản biện Final UI theo 10 heuristic Nielsen, accessibility và persona (mục PB trong log); rà tài liệu theo đề bài, soạn lại handoff, screen-spec, design-decisions cho khớp Figma |
| Claude (Cowork, Figma MCP) | Đối chiếu với checklist.design/mobile, lập kế hoạch prompt theo giai đoạn, dựng thêm component / wireframe / Final UI / user flow / prototype trong Figma, AI review theo checklist (mục C trong log) |
| Claude (Cowork) | Mô phỏng khảo sát (n = 30, script Python, seed 2026) và 5 phỏng vấn để kiểm chứng persona; mô phỏng kiểm thử khả dụng 5 người (cognitive walkthrough + KLM); tổng hợp affinity và insight. Mọi dữ liệu mô phỏng đều có nhãn "MÔ PHỎNG" (mục RS, UT trong log) |

Mọi đề xuất của AI đều được ghi Chấp nhận / Sửa / Từ chối kèm lý do trong `ai/ai-design-log.md` và `design/design-decisions.md`.

## 4. Bản đồ sản phẩm

| Sản phẩm (theo đề) | File | Nội dung chính |
|---|---|---|
| Research | [`ux/research.md`](ux/research.md) | 5 câu hỏi nghiên cứu, desk research (thật), rà 4 app tương tự (thật), khảo sát n = 30 và 5 phỏng vấn (MÔ PHỎNG bằng AI), affinity → 7 insight, hạn chế. Dữ liệu và biểu đồ trong `ux/research-pack/` |
| Vấn đề và persona | [`ux/persona.md`](ux/persona.md) | 5 persona (1 chính, 3 phụ, 1 anti-persona) rút từ research, lý do chọn persona chính, ma trận persona → flow, phát biểu vấn đề, tiêu chí đo được |
| IA và user flow | [`ux/user-flow.md`](ux/user-flow.md) | 28 màn hình, sơ đồ điều hướng, 10 flow, Flow 1–10 bằng Mermaid trong file (có nhánh lỗi / phục hồi), bảng ánh xạ flow → màn hình, bảng khung trạng thái |
| Kiểm thử khả dụng | [`ux/usability-test.md`](ux/usability-test.md) | Kịch bản 5 nhiệm vụ, thời gian chuẩn KLM, kết quả 5 người (MÔ PHỎNG), SEQ, SUS, 5 phát hiện, vòng sửa R4, phiếu ghi cho test thật |
| Bản mô tả thiết kế | [`design/DESIGN.md`](design/DESIGN.md) | Brief cho Stitch: màu, chữ, khoảng cách, giọng văn, từ vựng thống nhất, quy tắc component, dữ liệu mẫu |
| Đặc tả màn hình | [`design/screen-spec.md`](design/screen-spec.md) | Mỗi màn dùng để làm gì, hiển thị gì, thuộc flow nào, các trạng thái |
| Quyết định thiết kế | [`design/design-decisions.md`](design/design-decisions.md) | 10 quyết định quan trọng nhất + kết quả checklist accessibility (contrast, vùng chạm, cỡ chữ, không chỉ dùng màu, 360 / 412 dp) |
| Nhật ký AI | [`ai/ai-design-log.md`](ai/ai-design-log.md) | Prompt nguyên văn, kết quả, nhận xét, R1–R3, F6, phản biện bằng AI (PB), bổ sung theo checklist.design/mobile (C0–C8), research mô phỏng (RS), kiểm thử khả dụng (UT), vòng sửa R4 và quyết định |
| Ảnh Stitch | [`assets/stitch/`](assets/stitch/) | Mọi phiên bản Stitch: P1, P2, R1, R2, R3, Flow 6 |
| Ảnh Figma | [`assets/figma/`](assets/figma/) | Ảnh tất cả khung Final UI (màn chính và trạng thái) |
| Flutter handoff | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) | Token → Flutter, component → widget, đặc tả 6 mục cho từng màn, nhãn TalkBack, hành vi ≥ 600 dp |

## 5. Màn hình và flow

**28 màn hình:** 00 Splash · 00a Đăng nhập · 00b Đăng ký · Quên mật khẩu · 01 Onboarding · 00 Trang chủ tổng hợp (Hub) · 02 Trang chủ · 03 Ghi khoản mua – Bước 1/2 · 04 Ghi khoản mua – Bước 2/2 · 05 Chi tiết khoản mua · 05 Khoản mua đã lưu · 05a Xin quyền thông báo · 06 Lịch sử · 07 Mô hình · 08 Góc nhìn · 08b Chi tiết mô hình mua sắm · 08c Nhận định AI về khoản mua · 09 Chiêm nghiệm tháng · 10 Cá nhân · 10a Tài khoản · 10b Đổi mật khẩu · 11 Danh sách mong muốn · 12 Thêm món mong muốn · 13 Chi tiết món mong muốn · 14 Trước khi mua – Bước 1/3 · 15 Trước khi mua – Bước 2/3 · 16 Trước khi mua – Bước 3/3 · 18 Nhận định trước khi mua. 07 và 08 hiện dùng phiên bản có AI; 08a và 17 là trạng thái đang tải. Thanh điều hướng 5 tab: Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân.

| Flow | Bắt đầu → kết thúc | Nhánh lỗi / phục hồi |
|---|---|---|
| 1 – Ghi nhanh một khoản mua | 02 → 03 → 04 → 05 (lần lưu đầu: 05a xin quyền thông báo) → 02 (snackbar "Đã lưu … · Hoàn tác") | Số tiền 0 ₫ → báo lỗi, khóa "Tiếp tục"; mất mạng → lưu trên máy; Hoàn tác 5 giây; "Để sau" ở 05a không chặn người dùng |
| 2 – Mô hình → Góc nhìn → Chiêm nghiệm | 02 → 07 → 08 → 09 | Đang tải → lỗi → "Thử lại"; chưa đủ dữ liệu → "Ghi khoản mua" |
| 3 – Xem lại, sửa, xóa và hoàn tác | 06 → 05 → (sửa 03/04) hoặc (dialog xóa) → 06 | Dialog xác nhận; Hoàn tác 5 giây; bộ lọc trống → "Xóa bộ lọc" |
| 4 – Xem theo tháng / năm | 06 → chọn tháng → 06 tháng 9 → 07 tháng 9 | Tháng chưa có dữ liệu bị khóa |
| 5 – Cá nhân & dữ liệu | 10 → nhắc nhở / xuất CSV / xóa toàn bộ | Xóa toàn bộ qua dialog có "Hủy" |
| 6 – Danh sách mong muốn | 02 → 11 → 12 → 11 → 13 → mua / bỏ qua / cân nhắc tiếp | 12a lỗi tại trường; bỏ qua có dialog + Hoàn tác |
| 7 – Khởi động, đăng nhập & tài khoản | Mở app → 00 Splash → (01 → 00a ↔ 00b) → 00 Hub; 10 → 10a → 10b | Sai email / mật khẩu → lỗi dưới ô kèm "Quên mật khẩu?"; xóa tài khoản và đăng xuất qua dialog có "Hủy" |
| 8 – Nhận định AI sau khi lưu | 04 → 05 Khoản mua đã lưu → 08a → 08c → 00 Hub (hoặc 07, 08b) | Lỗi AI: Error state có "Thử lại" (đề xuất, chưa có khung) |
| 9 – Trước khi mua | 00 Hub → 14 → 15 → (16 nếu chọn Khuyến mãi) → 17 → 18 → về Trang chủ hoặc 03 | Không tạo khoản mua nếu không chọn "Vẫn mua"; lỗi AI: "Thử lại" (đề xuất) |
| 10 – AI phân tích mô hình | 07 (có AI) → 08a → 08b → 07; 08 (có AI) → 08c / 08b / 09 | Lỗi AI: "Thử lại" như 07 Mô hình – lỗi (đề xuất) |

## 6. Phạm vi so với checklist.design/mobile

Nhóm đối chiếu thiết kế với 25 checklist ở checklist.design/mobile. Mục tiêu là đạt phần lớn các
mục áp dụng được, không cần 100%.

**Trong phạm vi (10 checklist, 56 mục):** Tab Bar Navigation, Dashboard, Action Sheet, Login,
Sign up, Onboarding, Settings, Account, Splash Screen, Push Notification Opt-in.
**Kết quả AI review:** 98,2%. Đạt 54 mục, Một phần 2 mục (lỗi email mới có trong ghi chú;
"Xóa toàn bộ dữ liệu" chưa gom xuống nhóm cuối), không còn mục Chưa có.

**Ngoài phạm vi (có lý do):**
| Checklist / mục | Lý do |
|---|---|
| Search | Lịch sử đã lọc được theo động cơ và chọn tháng/năm; mỗi tháng khoảng 10–20 khoản |
| Onboarding Checklist | Onboarding chỉ 1 màn; Trang chủ trống và dòng nhắc "chưa ghi hôm nay" đã hướng dẫn bước đầu |
| Gesture navigation | Back hệ thống, cử chỉ và haptic do Android/Flutter xử lý; đã ghi trong tài liệu bàn giao |
| Đăng nhập Google, sinh trắc học, magic link, xác minh email | Backend chưa chốt |
| Checkout, Cart, Billing, Paywall | Chưa chốt chức năng mua bán / thanh toán |
| Chat, Referral, Invite | Không có tính năng xã hội; dữ liệu mua sắm là riêng tư |
| Camera, Map View, In-App Browser | Không chụp hoá đơn, không dùng vị trí, không mở web ngoài |
| Profile | Không có hồ sơ công khai; thông tin cá nhân nằm trong Tài khoản |
| In-App Notifications | Không có hộp thông báo; nhắc nhở đi qua thông báo hệ thống |
| Màn Gửi góp ý, Điều khoản, Chính sách quyền riêng tư | Đã có lối vào trong Cá nhân; nội dung văn bản chưa thuộc phạm vi Lab 2 |

## 7. Cấu trúc repository

```text
├── README.md
├── ux/
│   ├── research.md
│   ├── persona.md
│   ├── user-flow.md
│   ├── usability-test.md
│   └── research-pack/  (script mô phỏng, CSV khảo sát, biểu đồ)
├── design/
│   ├── DESIGN.md
│   ├── screen-spec.md
│   └── design-decisions.md
├── ai/
│   └── ai-design-log.md
├── assets/
│   ├── stitch/        (ảnh chụp mọi phiên bản do Stitch tạo)
│   └── figma/         (ảnh các màn hình cuối cùng)
└── handoff/
    └── flutter-handoff.md
```
