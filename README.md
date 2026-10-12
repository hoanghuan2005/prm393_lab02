# Why I Buy? – The Psychology of Money
### PRM323 — Lab 2: Thiết kế UI/UX có hỗ trợ AI (Google Stitch → Figma)

| | |
|---|---|
| **Sinh viên / nhóm** | `[Điền họ tên – MSSV]` |
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
| Chạy prototype (danh sách flow ở cột trái) | https://www.figma.com/proto/jCQEcxnXTYJ9b27pdsfFfS/Untitled?node-id=63-2429&show-proto-sidebar=1&scaling=scale-down |

Dự án Google Stitch (Flow 6): https://stitch.withgoogle.com/projects/1668611817022706714

## 3. Công cụ AI đã dùng

| Công cụ | Dùng để làm gì |
|---|---|
| Google Stitch | Sinh UI ban đầu (P1, P2), 3 vòng tinh chỉnh R1–R3 và Flow 6 (F6). Prompt nguyên văn và ảnh trong `ai/ai-design-log.md`, `assets/stitch/` |
| Claude (claude.ai) | Soạn nháp persona, user flow, DESIGN.md và prompt Stitch; hỗ trợ đối chiếu ảnh khi nhận xét output Stitch |
| Claude (claude.ai + Figma connector) | Phản biện ảnh Stitch của Flow 6; dựng Flow 6 trong Figma theo prompt của nhóm |
| Claude (Claude Code) | Phản biện Final UI theo 10 heuristic Nielsen, accessibility và persona (mục PB trong log); rà tài liệu theo đề bài, soạn lại handoff, screen-spec, design-decisions cho khớp Figma |

Mọi đề xuất của AI đều được ghi Chấp nhận / Sửa / Từ chối kèm lý do trong `ai/ai-design-log.md` và `design/design-decisions.md`.

## 4. Bản đồ sản phẩm

| Sản phẩm (theo đề) | File | Nội dung chính |
|---|---|---|
| Vấn đề và persona | [`ux/persona.md`](ux/persona.md) | Persona Nam, bối cảnh hằng ngày, pain point, thói quen thiết bị, nhu cầu accessibility, câu phát biểu vấn đề, tiêu chí thành công |
| IA và user flow | [`ux/user-flow.md`](ux/user-flow.md) | 15 màn hình, sơ đồ điều hướng, 7 flow (Mermaid, có nhánh lỗi / phục hồi), bảng ánh xạ flow → màn hình, bảng khung trạng thái |
| Bản mô tả thiết kế | [`design/DESIGN.md`](design/DESIGN.md) | Brief cho Stitch: màu, chữ, khoảng cách, giọng văn, từ vựng thống nhất, quy tắc component, dữ liệu mẫu |
| Đặc tả màn hình | [`design/screen-spec.md`](design/screen-spec.md) | Mỗi màn dùng để làm gì, hiển thị gì, thuộc flow nào, các trạng thái |
| Quyết định thiết kế | [`design/design-decisions.md`](design/design-decisions.md) | 10 quyết định quan trọng nhất + kết quả checklist accessibility (contrast, vùng chạm, cỡ chữ, không chỉ dùng màu, 360 / 412 dp) |
| Nhật ký AI | [`ai/ai-design-log.md`](ai/ai-design-log.md) | Prompt nguyên văn, kết quả, nhận xét, R1–R3, F6, phản biện bằng AI (PB) và quyết định |
| Ảnh Stitch | [`assets/stitch/`](assets/stitch/) | Mọi phiên bản Stitch: P1, P2, R1, R2, R3, Flow 6 |
| Ảnh Figma | [`assets/figma/`](assets/figma/) | Ảnh tất cả khung Final UI (màn chính và trạng thái) |
| Flutter handoff | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) | Token → Flutter, component → widget, đặc tả 6 mục cho từng màn, nhãn TalkBack, hành vi ≥ 600 dp |

## 5. Màn hình và flow

**15 màn hình:** 00a Đăng nhập · 00b Đăng ký · 01 Onboarding · 02 Trang chủ · 03 Ghi khoản mua – Bước 1/2 · 04 Ghi khoản mua – Bước 2/2 · 05 Chi tiết khoản mua · 06 Lịch sử · 07 Mô hình · 08 Góc nhìn · 09 Chiêm nghiệm tháng · 10 Cá nhân · 11 Danh sách mong muốn · 12 Thêm món mong muốn · 13 Chi tiết món mong muốn. Thanh điều hướng 5 tab: Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân.

| Flow | Bắt đầu → kết thúc | Nhánh lỗi / phục hồi |
|---|---|---|
| 1 – Ghi nhanh một khoản mua | 02 → 03 → 04 → 02 (snackbar "Đã lưu … · Hoàn tác") | Số tiền 0 ₫ → báo lỗi, khóa "Tiếp tục"; mất mạng → lưu trên máy; Hoàn tác 5 giây |
| 2 – Mô hình → Góc nhìn → Chiêm nghiệm | 02 → 07 → 08 → 09 | Đang tải → lỗi → "Thử lại"; chưa đủ dữ liệu → "Ghi khoản mua" |
| 3 – Xem lại, sửa, xóa và hoàn tác | 06 → 05 → (sửa 03/04) hoặc (dialog xóa) → 06 | Dialog xác nhận; Hoàn tác 5 giây; bộ lọc trống → "Xóa bộ lọc" |
| 4 – Xem theo tháng / năm | 06 → chọn tháng → 06 tháng 9 → 07 tháng 9 | Tháng chưa có dữ liệu bị khóa |
| 5 – Cá nhân & dữ liệu | 10 → nhắc nhở / xuất CSV / xóa toàn bộ | Xóa toàn bộ qua dialog có "Hủy" |
| 6 – Danh sách mong muốn | 02 → 11 → 12 → 11 → 13 → mua / bỏ qua / cân nhắc tiếp | 12a lỗi tại trường; bỏ qua có dialog + Hoàn tác |
| 7 – Đăng nhập & đăng ký | 01 → 00a (↔ 00b) → 02 | Email sai định dạng, sai mật khẩu → lỗi dưới ô |

## 6. Cấu trúc repository

```text
├── README.md
├── ux/
│   ├── persona.md
│   └── user-flow.md
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
