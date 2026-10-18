# Why I Buy? – Smart Shopping Companion
### PRM323 — Lab 2: Thiết kế UI/UX có hỗ trợ AI (Google Stitch → Figma)

> **Hiểu trước khi thay đổi.**

| | |
|---|---|
| **Nhóm** | Group 7 – Lab 2: The Psychology of Money |
| **Thành viên** | Đào Tâm Hoàng – SE194103 · Nguyễn Đình Ngọc Ân – SE196654 · Huỳnh Đăng Khoa – SE193040 · Ngô Gia Kiệt – SE183268 · Hồ Hữu Hoàng Huân – SE192248 |
| **Lớp** | `[Điền mã lớp]` |
| **Học kỳ** | Fall 2026 |
| **Cập nhật** | 18/10/2026 – đồng bộ theo đặc tả hợp nhất v1.0 (17/10) và Figma "Why I Buy ver2" (18/10). Báo cáo đồng bộ: [`docs/REPO_SYNC_REPORT_2026-10-18.md`](docs/REPO_SYNC_REPORT_2026-10-18.md) |

## 1. Chủ đề và định vị

**Why I Buy?** là trợ lý mua sắm có ý thức trên Android: giúp người trẻ lưu món đang thích, cân nhắc với ngân sách tự đặt, đồ đang có và thời điểm sale, **tự chọn Mua · Chờ · Bỏ qua**, rồi nhìn lại vì sao mình mua — không phán xét, không quyết định thay người dùng, không khuyến khích mua bốc đồng. Lấy cảm hứng từ *The Psychology of Money* (Morgan Housel).

Hướng này mở rộng từ bản đầu (ghi khoản mua kèm động cơ, Flow 1–10) sau góp ý của giảng viên và thảo luận nhóm ngày 15–17/10/2026. Hướng mới là **đề xuất của nhóm, chưa được giảng viên xác nhận**.

### Hành trình trước – trong – sau khi mua

| Giai đoạn | Người dùng làm gì | App hỗ trợ | Màn chính trên Figma |
|---|---|---|---|
| Trước khi mua | Thấy món thích trên Shopee, lưu lại | Android Share, nhập tay, Chrome Extension → Smart Wishlist | 19 Lưu món (bottom sheet), 11 Danh sách mong muốn v3 |
| Cân nhắc | Xem giá đã ghi, ngân sách, động cơ, đồ đang dùng, đợt sale | Decision Card (Rules Engine), Ngân sách theo nhóm, Lịch sử giá, Trước khi mua 3 câu | 28 Decision Card, 31 Ngân sách, 30 Cập nhật giá, 14–16 |
| Quyết định | Tự chọn Mua, Chờ hoặc Bỏ qua | Ba nút bình đẳng; Chờ → nhắc xem lại hoặc đến đợt sale đã công bố | 28, 29 Chờ, 21 Danh sách cho đợt sale |
| Sau khi mua | Ghi giá thực trả, nhìn lại động cơ, mức hài lòng | Ghi khoản mua điền sẵn, Lịch sử, Mô hình, Góc nhìn, Chiêm nghiệm | 03–04, 06–09, 27 |

### App Android và Chrome Extension

| Thành phần | Vai trò | Không phải |
|---|---|---|
| **App Android (Flutter)** – sản phẩm chính | Lưu, cân nhắc, quyết định, nhìn lại; khung 360 × 800 dp | Không phải app theo dõi giá Shopee |
| **Chrome Extension** (TypeScript + React + WXT, MV3) – kênh phụ | Lưu nhanh khi xem Shopee trên máy tính; ghép với app bằng mã 6 số để đồng bộ | Không phải nguồn giá chính xác nhất; không ghi thẳng vào database |
| **Backend đề xuất: Firebase** | Đồng bộ app ↔ extension, ghép thiết bị, thông báo | Không cào Shopee, không dùng API Shopee chưa được cấp quyền |

**Giá và voucher:** giá là dữ liệu người dùng ghi hoặc xác nhận, luôn kèm nguồn, ngày và phân loại — không phải giá thời gian thực. App không đọc tài khoản hay kho voucher Shopee và không tự áp mã; khi mua, người dùng ghi **giá thực trả** và có thể chọn chip "Có dùng mã giảm giá". Chi tiết ở [`design/DESIGN.md`](design/DESIGN.md) mục "Giá, voucher và dữ liệu".

**Persona chính (một dòng, proto-persona – giả định chưa kiểm chứng):** Nguyễn Hải Nam, 22 tuổi, sinh viên năm cuối CNTT kiêm thực tập, xem Shopee trên Android một tay, hay gặp flash sale buổi tối, ngại nhập nhiều và không muốn bị phán xét.

**Tiêu chí thành công (mục tiêu kiểm thử, chưa phải kết quả):** lưu một món vào Wishlist dưới 20 giây; ghi một khoản mua kèm động cơ trong 25 giây; không người thử nào nhầm giá đã ghi của món chưa mua với tiền đã chi.

## 2. Link thiết kế (ai có link đều xem được)

**Figma hiện hành – Why I Buy ver2:** https://www.figma.com/design/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2

| Page | Link |
|---|---|
| 01 User Flow | https://www.figma.com/design/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=0-1 |
| 02 Wireframe | https://www.figma.com/design/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2-2 |
| 03 Final UI | https://www.figma.com/design/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2-3 |
| 04 Design System | https://www.figma.com/design/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2-4 |
| 05 Components | https://www.figma.com/design/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2-5 |
| 06 Prototype | https://www.figma.com/design/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2-6 |

**Chạy prototype** (mở cột trái "Flows" để chọn flow):

| Flow | Link |
|---|---|
| ★ Toàn bộ ứng dụng (Flow 1–10, bắt đầu từ Splash) | https://www.figma.com/proto/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=377-4391&starting-point-node-id=377%3A4391&show-proto-sidebar=1&scaling=scale-down |
| F11 – Lưu món qua nút Chia sẻ | https://www.figma.com/proto/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2063-5157&starting-point-node-id=2063%3A5157&show-proto-sidebar=1&scaling=scale-down |
| F12 – Ngày sale: cập nhật giá và quyết định | https://www.figma.com/proto/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2063-5541&starting-point-node-id=2063%3A5541&show-proto-sidebar=1&scaling=scale-down |
| F13 – Liên kết extension | https://www.figma.com/proto/VaPYFxfpx14tnQmOMSgdjP/Why-I-Buy-ver2?node-id=2063-5873&starting-point-node-id=2063%3A5873&show-proto-sidebar=1&scaling=scale-down |

Nhánh lỗi có điểm bắt đầu riêng trên page 06: F11b (19e link không phải Shopee), F12b (21a chưa có món), F13b (X4 mã sai). Dây nối của F11–F13 đã được đọc trực tiếp bằng Figma Plugin API ngày 18/10 (xem báo cáo đồng bộ); chưa có người thật bấm thử.

**Google Stitch:** https://stitch.withgoogle.com/projects/1668611817022706714 — nội dung project **NOT VERIFIED** khi đồng bộ ngày 18/10 (trang chỉ trả về khung ứng dụng, cần đăng nhập để xem). Ảnh Stitch đã lưu nằm trong [`assets/stitch/`](assets/stitch/).

**File Figma cũ** (`jCQEcxnXTYJ9b27pdsfFfS`, Flow 1–10, đến 14/10): giữ làm lịch sử; các ảnh trong `assets/figma/` được xuất từ file này.

## 3. Trạng thái thực tế (18/10/2026)

| Hạng mục | Trạng thái | Bằng chứng |
|---|---|---|
| UI Flow 1–10 (ghi khoản mua, mô hình, wishlist v1, tài khoản, AI) | Đã thiết kế, có prototype | Figma page 03, 06; ảnh hiện hành `assets/figma/ver2/` (bản cũ 14/10 ở `assets/figma/`); log C5 |
| UI F11–F13 (19–31, X2–X5, EXT-1…8) | Đã thiết kế trên Figma; F11–F13 đã nối prototype | Figma section "Flow 11–12…", "[MỚI · 18/10]…"; ảnh 1× ở `assets/figma/ver2/` |
| Wireframe cho 19–27 và EXT-1…8 | **Chưa có** | Page 02 chỉ có wireframe 28–31, X2–X5 |
| Vòng Stitch cho hướng mới | **Chưa có bằng chứng** | Có bộ prompt `ai/stitch-prompts-why-i-buy.md`, chưa có ảnh kết quả |
| Nghiên cứu người dùng | Chỉ có dữ liệu **mô phỏng** | `ux/research.md`; khảo sát 18/10 chưa xác minh nguồn gốc |
| Kiểm thử khả dụng | Chỉ có **mô phỏng** (Flow cũ) | `ux/usability-test.md` |
| App Flutter, extension, backend | **Chưa có code** (đề Lab 2 không yêu cầu code) | — |

## 4. Tính năng MVP và roadmap

Theo đặc tả hợp nhất v1.0 (17/10). Mã tính năng A- (app) và EX- (extension).

| Giai đoạn | Nội dung | Ghi chú |
|---|---|---|
| **Lab 2** | Figma 6 page, prototype F11–F13 có nhánh lỗi, tài liệu, dữ liệu mô phỏng có nhãn | Phạm vi môn học |
| GĐ1 · Flutter MVP (local-first) | A-01 ghi khoản mua · A-02 Smart Wishlist · A-03 thêm thủ công · A-04 Android Share · A-05 Trước khi mua · A-06 Decision Card v1 (Rules Engine) · A-07 Mua/Chờ/Bỏ qua · A-08 ngân sách theo nhóm · A-09 nhắc xem lại · A-10 Lịch sử/Mô hình/Góc nhìn | Sau Lab |
| GĐ2 · Extension MVP | EX-01 Quick Save · EX-02 Wishlist cục bộ · EX-03 chống trùng · EX-04 giá tùy chọn · EX-05 offline | Sau Lab |
| GĐ3 · Đồng bộ | A-11 thiết bị đã liên kết, EX-06 ghép mã 6 số, EX-07 đồng bộ hai chiều | Sau Lab |
| GĐ4 · Thông minh | Hồ sơ mua sắm, lịch sale, Price Insights, so sánh món, hỏi hài lòng 7 ngày, OCR ảnh chụp | Sau Lab, không cam kết |
| GĐ5 · Nâng cao | AI diễn giải, gói mua vừa ngân sách, giá người khác ghi (ẩn danh), Affiliate API khi có quyền | Không cam kết |

Một số màn trên Figma thuộc GĐ4–GĐ5 (20 OCR, 22 Gói mua, 23 So sánh, 24 Đồ đang dùng, 27 Hỏi hài lòng). Chúng được thiết kế để minh họa lộ trình, không phải MVP.

## 5. Công cụ AI đã dùng

| Công cụ | Dùng để làm gì |
|---|---|
| Google Stitch | Sinh UI ban đầu (P1, P2), 3 vòng tinh chỉnh R1–R3 và Flow 6 (F6). Prompt nguyên văn và ảnh trong `ai/ai-design-log.md`, `assets/stitch/` |
| Claude (claude.ai) | Soạn nháp persona, user flow, DESIGN.md và prompt Stitch; hỗ trợ đối chiếu ảnh khi nhận xét output Stitch |
| Claude (claude.ai + Figma connector) | Phản biện ảnh Stitch của Flow 6; dựng Flow 6 trong Figma theo prompt của nhóm |
| Claude (Claude Code) | Phản biện Final UI theo 10 heuristic Nielsen, accessibility và persona (mục PB trong log); rà tài liệu theo đề bài; đồng bộ repo với Figma ver2 ngày 18/10 (mục R5 trong log) |
| Claude (Cowork, Figma MCP) | Đối chiếu checklist.design/mobile, dựng thêm component / wireframe / Final UI / prototype trong Figma (mục C trong log) |
| Claude (Cowork) | Mô phỏng khảo sát và phỏng vấn, mô phỏng kiểm thử khả dụng. Mọi dữ liệu mô phỏng có nhãn "MÔ PHỎNG" (mục RS, UT trong log) |
| Nhiều trợ lý AI (theo `ai/ai-design-log-v2.md`) | Nghiên cứu khả thi nguồn giá Shopee, extension, góp ý giảng viên, sách nguồn cảm hứng (session S1–S4) |

Mọi đề xuất của AI đều được ghi Chấp nhận / Sửa / Từ chối kèm lý do trong `ai/ai-design-log.md`, `ai/ai-design-log-v2.md` và `design/design-decisions.md`.

## 6. Bản đồ sản phẩm

| Sản phẩm (theo đề) | File | Nội dung chính |
|---|---|---|
| Research | [`ux/research.md`](ux/research.md) | Desk research (thật); khảo sát và phỏng vấn **mô phỏng** (14/10); khảo sát 18/10 (chưa xác minh nguồn gốc, chỉ số liệu tổng hợp); giả định và kết luận được hỗ trợ |
| Vấn đề và persona | [`ux/persona.md`](ux/persona.md) | 4 proto-persona (P1 Nam chính · P3 Huy · P2 Linh · P4 Mai) + anti-persona P5, 12 trường mỗi persona, ma trận persona → flow F1–F13, phát biểu vấn đề, tiêu chí đo được |
| IA và user flow | [`ux/user-flow.md`](ux/user-flow.md) | Danh sách màn, sơ đồ điều hướng, 13 flow bằng Mermaid (F11–F13 theo dây nối prototype thật), bảng ánh xạ flow → màn, bảng khung trạng thái |
| Kiểm thử khả dụng | [`ux/usability-test.md`](ux/usability-test.md) | Kịch bản, KLM, kết quả **mô phỏng** cho Flow cũ, phiếu ghi cho test thật |
| Bản mô tả thiết kế | [`design/DESIGN.md`](design/DESIGN.md) | Token, giọng văn, quy tắc component; Smart Wishlist, ngân sách, Decision Card, giá có nguồn và ngày, voucher |
| Đặc tả màn hình | [`design/screen-spec.md`](design/screen-spec.md) | Mục đích, nội dung, flow, trạng thái từng màn; bảng ánh xạ mã đặc tả ↔ mã Figma cho 19–31, X1–X5 |
| Quyết định thiết kế | [`design/design-decisions.md`](design/design-decisions.md) | Quyết định quan trọng kèm lý do + checklist accessibility; bổ sung quyết định hướng mới (chờ nhóm chọn top 10) |
| Nhật ký AI | [`ai/ai-design-log.md`](ai/ai-design-log.md) · [`ai/ai-design-log-v2.md`](ai/ai-design-log-v2.md) | Prompt nguyên văn, R1–R3, F6, PB, C0–C8, RS, UT, R4, R5 (đổi hướng 18/10); v2: session S1–S4 nghiên cứu hướng mới |
| Prompt Stitch hướng mới | [`ai/stitch-prompts-why-i-buy.md`](ai/stitch-prompts-why-i-buy.md) | Bộ prompt F11–F13 (chưa có bằng chứng đã chạy) |
| Ảnh Stitch | [`assets/stitch/`](assets/stitch/) | Mọi phiên bản Stitch: P1, P2, R1, R2, R3, Flow 6 |
| Ảnh Figma | [`assets/figma/ver2/`](assets/figma/ver2/) · [`assets/figma/`](assets/figma/) | **ver2/**: 157 ảnh của mọi khung Final UI trên Figma ver2 (18/10, có bảng tra cứu). Thư mục cha: ảnh Flow 1–10 từ file cũ (14/10) và ảnh trước / sau R4 |
| Flutter handoff | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) | Token → Flutter, component → widget, đặc tả 6 mục cho từng màn (kể cả F11–F13), mô hình dữ liệu, mã lỗi E01–E14 |
| Báo cáo đồng bộ | [`docs/REPO_SYNC_REPORT_2026-10-18.md`](docs/REPO_SYNC_REPORT_2026-10-18.md) | Audit, bảng ánh xạ mã màn, xung đột nguồn, việc còn lại ở Figma/Stitch, kiểm tra Lab 2 |

## 7. Cách xem nhanh

1. **Prototype:** mở link F11, F12, F13 ở mục 2; mỗi flow có nhánh lỗi riêng (F11b, F12b, F13b).
2. **User flow:** đọc [`ux/user-flow.md`](ux/user-flow.md) mục 3 (Mermaid hiển thị trực tiếp trên GitHub), đối chiếu page 01 của Figma.
3. **AI design log:** [`ai/ai-design-log.md`](ai/ai-design-log.md) từ P1 đến R5; phần nghiên cứu hướng mới ở [`ai/ai-design-log-v2.md`](ai/ai-design-log-v2.md).
4. **Handoff:** [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) mục 1–2 (hai bảng ánh xạ), mục 4 và mục 9 (đặc tả từng màn).

## 8. Màn hình và flow

**Flow 1–10** (thiết kế đến 14/10): ghi khoản mua, mô hình – góc nhìn – chiêm nghiệm, xóa và hoàn tác, xem theo tháng, cá nhân và dữ liệu, danh sách mong muốn v1, tài khoản, AI sau khi lưu, trước khi mua, AI phân tích mô hình. Danh sách 28 màn và mọi khung trạng thái ở [`ux/user-flow.md`](ux/user-flow.md) mục 1.

**Flow 11–13** (thiết kế 18/10):

| Flow | Bắt đầu → kết thúc | Nhánh lỗi / phục hồi |
|---|---|---|
| F11 – Android Share → Smart Wishlist → Decision Card | 19a → 19 → 19g → 11 v3 → 28 → Mua / Chờ (29 → 29a) / Bỏ qua | 19e link không phải Shopee → lưu thủ công; 20 → 20a lấy giá từ ảnh; thiếu giá vẫn lưu được |
| F12 – Wishlist → Chờ → nhắc đợt sale → Quyết định | Thông báo 20:00 → 21 Danh sách cho 11/11 → 30 / 30a cập nhật giá → 28 → Mua / Chờ / Bỏ qua | 21a chưa có món → về Wishlist; 30b lịch sử giá chỉ so khi "so được" |
| F13 – Extension → Lưu món → Ghép thiết bị → Đồng bộ | App: 25 mã 6 số → 25f xác nhận → 25b → 25e hủy liên kết (overlay). Extension: X4 → X4a → X2 → X3 / X5 | X4 mã sai → nhập lại; X2a lỗi đồng bộ (chưa nối prototype) |

## 9. Lịch sử: đối chiếu checklist.design/mobile (13/10/2026)

Áp dụng cho Flow 1–10. Trong phạm vi 10 checklist, 56 mục (Tab Bar Navigation, Dashboard, Action Sheet, Login, Sign up, Onboarding, Settings, Account, Splash Screen, Push Notification Opt-in); kết quả AI review 98,2% (54 Đạt, 2 Một phần). Ngoài phạm vi có lý do: Search, Onboarding Checklist, Gesture navigation (Android/Flutter xử lý), đăng nhập Google/sinh trắc, Checkout/Cart/Billing/Paywall, Chat/Referral/Invite, Camera/Map/In-App Browser, Profile công khai, In-App Notifications, nội dung Điều khoản/Chính sách. Chi tiết ở mục C trong `ai/ai-design-log.md`. Chưa đối chiếu lại cho F11–F13.

## 10. Cấu trúc repository

```text
├── README.md
├── ux/
│   ├── research.md
│   ├── persona.md
│   ├── user-flow.md
│   ├── usability-test.md
│   ├── research-pack/   (script mô phỏng, biểu đồ; không chứa dữ liệu khảo sát thô)
│   ├── userflow/        (ảnh sơ đồ IA, Flow 1–13 xuất từ Figma)
│   └── wireframe/       (ảnh wireframe; 5_F11-F13-bo-sung-18-10/ = 28–31, X2–X5)
├── design/
│   ├── DESIGN.md
│   ├── screen-spec.md
│   └── design-decisions.md
├── ai/
│   ├── ai-design-log.md
│   ├── ai-design-log-v2.md
│   └── stitch-prompts-why-i-buy.md
├── assets/
│   ├── stitch/          (ảnh chụp mọi phiên bản do Stitch tạo)
│   └── figma/           (ảnh các màn hình cuối cùng; ver2/ = Figma hiện hành 18/10)
├── handoff/
│   └── flutter-handoff.md
├── archive/             (bản cũ giữ làm lịch sử, không dùng làm tài liệu hiện hành)
└── docs/
    └── REPO_SYNC_REPORT_2026-10-18.md
```
