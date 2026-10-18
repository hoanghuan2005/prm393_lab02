# Báo cáo đồng bộ repository – 18/10/2026

**Dự án:** Why I Buy? – Smart Shopping Companion · PRM323 Lab 2 · Nhóm 7
**Người thực hiện:** Claude (Claude Code, VS Code), theo nhiệm vụ "Audit và cập nhật toàn bộ repository theo hướng sản phẩm mới" do nhóm giao.
**Nhánh:** `docs/whyibuy-2026-10-18` (tách từ `main` tại `416f65b`). **Chưa commit, chưa push, chưa merge.** Nhóm xem diff rồi tự commit.

## 1. Nguồn đã đọc

| # | Nguồn | Cách đọc | Trạng thái |
|---|---|---|---|
| 1 | `Why_I_Buy_Final_Unified_Product_Technical_Spec.docx` (v1.0, 17/10) | Trích chữ từ `word/document.xml`; đọc toàn bộ mục 1–16, Change Log, Phụ lục A–B | Đã đọc. Sơ đồ F11–F13 (Hình 3–5) là ảnh nhúng, không đọc chi tiết; F11–F13 được đối chiếu bằng Figma |
| 2 | `Why_I_Buy_Overview_Persona_Guideline.docx` (v2.0) | Trích chữ, đọc toàn bộ 17 mục | Đã đọc |
| 3 | `PRM323 - Lab 2 … (bản tiếng Việt) (1).pdf` (12 trang), `PRM323_Lab2_HuongDan_Slide_Presentation_Demo.docx` | Trích chữ bằng `pdfjs-dist` (cài tạm ở thư mục nháp); trích chữ docx | Đã đọc |
| 4 | `Bạn-mua-sắm-vì-điều-gì_…_Câu-trả-lời.xlsx` (18/10) | Đọc cấu trúc, dấu thời gian, số liệu tổng hợp; **không in và không đưa câu trả lời từng người vào repo** | Đã đọc – **NEEDS VERIFICATION** về nguồn gốc |
| 5 | `So-sanh-gia-va-voucher-Why-I-Buy.docx` (Khoa) | Trích chữ | Đã đọc; là tài liệu đề xuất, có 3 điểm lệch đặc tả (mục 5) |
| 6 | `why_i_buy_repo_patch_2026-10-18/` | Đọc CHANGELOG, `design/current-design-scope.md`, `screen-spec-current.md`, `ux/user-flow-current.md`, `docs/PROJECT_STATUS_2026-10-18.md` | Chỉ dùng để đối chiếu; **không chép đè** (mục 7) |
| 7 | Figma `VaPYFxfpx14tnQmOMSgdjP` (Why I Buy ver2) | `get_metadata` (page 01, 02, 03, 06), `get_screenshot` (3 khung), `use_figma` **chỉ đọc**: thứ tự page, chữ trong frame, component và biến thể, biến màu, starting point và dây nối prototype F11–F13 | Đã đọc; **không sửa, không đổi tên frame** |
| 8 | Google Stitch `1668611817022706714` | `WebFetch` | **NOT VERIFIED** – chỉ nhận được khung ứng dụng, không có nội dung project |

## 2. Kết quả audit

**Git (lúc bắt đầu):** nhánh `main`, không có thay đổi chưa commit ngoài thư mục `WhyIBuy_Update_References/` (chưa theo dõi). Remote `https://github.com/hoanghuan2005/prm393_lab02.git`. Commit mới nhất `416f65b ai design log`.

| Phân loại | File / mục | Ghi chú |
|---|---|---|
| KEEP | `ai/ai-design-log-v2.md`, `ai/stitch-prompts-why-i-buy.md` | File mới của thành viên khác; giữ nguyên, chỉ thêm liên kết |
| KEEP | `ux/research-pack/*.py`, `usability-sim.json`, 16 biểu đồ; `ux/userflow/`, `ux/wireframe/`; `assets/stitch/`; ảnh `assets/figma/` | Lịch sử Flow 1–10 và bằng chứng vòng lặp cũ |
| UPDATE | `README.md` | Link Figma cũ (`jCQEcxnXTYJ9b27pdsfFfS`); định vị cũ; chưa có F11–F13, MVP, trạng thái thực tế |
| UPDATE | `ux/persona.md` | 5 persona dùng khảo sát / phỏng vấn MÔ PHỎNG làm bằng chứng; chưa có F11–F13 |
| UPDATE | `ux/research.md` | Tham chiếu `survey-mo-phong.csv` (đã xóa ở `c0c1482`) và bộ 5 biểu đồ cũ; "ngân sách ngoài phạm vi"; chưa có khảo sát 18/10 |
| UPDATE | `ux/user-flow.md`, `design/screen-spec.md`, `handoff/flutter-handoff.md` | Chưa có F11–F13, màn 19–31, EXT, X2–X5 |
| UPDATE | `design/DESIGN.md` | Còn ghi "ngân sách và cảnh báo vượt mức" là ngoài phạm vi (đặc tả 1.5 #6 yêu cầu sửa) |
| UPDATE | `design/design-decisions.md` | Chưa có quyết định của hướng mới |
| ADD | `docs/REPO_SYNC_REPORT_2026-10-18.md`, `archive/before-2026-10-18/` | Báo cáo này; lưu bản persona cũ |
| ARCHIVE | `ux/persona.md` bản 14/10 | Chuyển sang `archive/before-2026-10-18/ux/persona.md` |
| NEEDS VERIFICATION | File khảo sát 18/10 | 30 dòng trong 111,6 giây, cách nhau 3,7–4,1 giây (mục 4) |
| NEEDS VERIFICATION | `ux/research-pack/Bạn mua sắm vì điều gì_ – … (Câu trả lời).xlsx` | Câu trả lời Google Form của bộ mô phỏng 14/10 (30 dòng trong 82 giây). Không có cột định danh, nhưng trái quy tắc "không đưa Excel khảo sát gốc lên GitHub". **Đã bỏ theo dõi** (`git rm --cached`), file vẫn còn trên máy và **vẫn còn trong lịch sử trên `origin/main`** (commit `35b981c`) |
| NEEDS VERIFICATION | `ghi-khoan-mua-360dp.png` ở gốc repo (commit `561ccad`) | Ảnh màn Ghi khoản mua có icon emoji và chữ "Bắt buộc" màu đỏ (trái PB-16); không giống ảnh export Figma. Chưa rõ mục đích; để nguyên |
| NEEDS VERIFICATION | `ux/research-pack/charts.py` | Đọc `survey-summary.json` không có trong repo → không vẽ lại được biểu đồ |

**Khẳng định mô phỏng như thật:** không tìm thấy chỗ nào trong repo ghi khảo sát / phỏng vấn mô phỏng là thật; các file cũ đều có nhãn MÔ PHỎNG. Rủi ro nằm ở **file khảo sát 18/10** (dễ bị hiểu là khảo sát thật) và ở **persona cũ** (dùng số mô phỏng làm "bằng chứng").

## 3. File đã sửa, thêm, lưu trữ

| File | Thay đổi | Lý do |
|---|---|---|
| `README.md` | Viết lại: định vị Smart Shopping Companion, hành trình trước – trong – sau, app vs extension, link Figma ver2 đủ 6 page, link prototype F11/F12/F13 (node ID thật), Stitch (NOT VERIFIED), bảng trạng thái thực tế, MVP và roadmap theo đặc tả, bản đồ tài liệu, cách xem nhanh; giữ mục checklist.design 13/10 dạng lịch sử | Nhiệm vụ V.1 |
| `ux/persona.md` | Viết lại theo 4 proto-persona của Overview (12 trường, ưu tiên P1 → P3 → P2 → P4, P5 anti-persona theo nhu cầu); cấp chứng cứ; kịch bản S1; ma trận persona → Flow 1–10 và F11–F13; Persona → Need → UI → Test; phát biểu vấn đề; KPI-01 → KPI-05 | Nhiệm vụ V.2; Overview mục 6–10 |
| `archive/before-2026-10-18/` | Lưu `ux/persona.md` bản 14/10 + README giải thích | Không xóa lịch sử |
| `ux/research.md` | Tách 3 loại dữ liệu; sửa tham chiếu CSV và danh sách biểu đồ; ghi *[Đã thay thế 18/10]* cho kết luận "không ngân sách"; thêm mục 9 (khảo sát 18/10: cấu trúc, kiểm tra nguồn gốc, số liệu tổng hợp, được / không được kết luận), mục 10 (tách loại kết luận), mục 11 (kế hoạch research thật R1–R8) | Nhiệm vụ V.3 |
| `ux/user-flow.md` | Thêm mục 1.2 (19 màn mới, giai đoạn MVP), 2.2 (IA hướng mới), F11–F13 (Mermaid theo dây nối prototype thật, happy / alternate / error, lỗi prototype đã phát hiện), 4.2 (ánh xạ F11–F13 → màn), 5.2 (khung trạng thái); giữ nguyên Flow 1–10 | Nhiệm vụ V.4 |
| `design/DESIGN.md` | Sửa định vị, người dùng, phạm vi (ngân sách vào phạm vi; thêm ngoài phạm vi: cào Shopee, đọc voucher, tự áp mã, giá realtime, dự đoán giá, tìm shop rẻ nhất); thêm từ vựng; thêm mục "Smart Shopping Companion – quy tắc thiết kế" (nguyên tắc, Smart Wishlist, ngân sách + công thức, Decision Card, giá – voucher – kiến trúc, microcopy, trạng thái bắt buộc, dữ liệu mô phỏng); danh sách màn mới; lịch sử cập nhật. **Không đổi token** | Nhiệm vụ V.5, VI |
| `design/screen-spec.md` | Thêm bảng **ánh xạ mã màn đặc tả ↔ Figma** (23 dòng), danh mục 20 màn mới, đặc tả 12 nhóm màn (nội dung chữ lấy từ Figma) | Nhiệm vụ V.6 |
| `design/design-decisions.md` | Thêm mục 1b: QĐ-N1 → QĐ-N8 kèm căn cứ, quyết định cũ bị thay thế, hiện trạng Figma; QĐ-N3, QĐ-N5 chi tiết; mục 2.7 (tương phản đo được của tag mới, cỡ chữ 12 sp, Text field thiếu biến thể). Không xóa quyết định cũ | Nhiệm vụ V.7 |
| `handoff/flutter-handoff.md` | Sửa phần nguồn chuẩn; thêm mục 9: mô hình dữ liệu Dart, route đề xuất, 12 component → widget, Rules Engine (công thức khả dụng, thứ tự nhãn), mã lỗi E01–E14 → màn, đặc tả **6 mục cho 12 nhóm màn** F11–F13, thông báo, ≥ 600 dp, 12 điểm Figma lệch đặc tả. Giữ nguyên bảng token và component cũ | Nhiệm vụ V.8 |
| `ai/ai-design-log.md` | Thêm dòng khai báo công cụ 18/10; thêm mục R5 (R5-0 bối cảnh, R5-1 phiên đồng bộ, R5-2 phản biện PB2 với 14 phát hiện gắn màn, cột quyết định để nhóm điền). Không sửa mục cũ, không thêm prompt Stitch giả | Nhiệm vụ V.9 |
| `ux/usability-test.md` | Thêm ghi chú đầu file: chỉ áp dụng Flow 1–10; F11–F13 chưa kiểm thử | Tránh hiểu nhầm |
| `assets/figma/README.md` | Thêm checklist ảnh cần xuất từ Figma ver2 | Quy tắc VIII.6 |
| `.gitignore` | Chặn `*.xlsx`, `*.xls`, `*.csv` và `WhyIBuy_Update_References/` | Quy tắc VIII.8; tránh commit nhầm thư mục tham chiếu tạm |
| `ux/research-pack/…(Câu trả lời).xlsx` | `git rm --cached` (file vẫn trên máy) | Quy tắc VIII.8 |

## 4. Khảo sát 18/10 – kiểm tra nguồn gốc

| Kiểm tra | File 18/10 (26 câu) | File 14/10 trong repo (15 câu, đã ghi MÔ PHỎNG) |
|---|---|---|
| Số dòng | 30 | 30 |
| Khoảng thời gian gửi | 12:46–12:47 ngày 18/10, tổng 111,6 giây | 19:38–19:39 ngày 14/10, tổng 82,4 giây |
| Khoảng cách giữa hai lần gửi | 3,7 – 3,8 (trung vị) – 4,1 giây | 2,6 – 2,8 – 3,3 giây |
| Cột định danh (email, tên, số điện thoại) | Không có | Không có |
| Dòng trùng giữa hai file | 0 | — |

Câu trả lời tự do ở cột cuối gần như trùng câu chữ với pain point của persona. **Kết luận: chưa xác minh, nhiều khả năng là dữ liệu mô phỏng nhập tự động vào Google Form.** Đây không phải kết luận gian lận. `ux/research.md` mục 9 chỉ dùng số liệu tổng hợp và ghi rõ không được dùng làm bằng chứng.

## 5. Xung đột giữa các nguồn và cách xử lý

| # | Nguồn A | Nguồn B | Cách xử lý trong repo | Ai quyết |
|---|---|---|---|---|
| 1 | Đặc tả 11.3: Decision Card = 20, Chờ = 21, Cập nhật giá = 22, Ngân sách = 23, Lịch sale = 26 | Figma 18/10: Decision Card = 28, Chờ = 29, Cập nhật giá = 30, Ngân sách = 31; số 20/21/22/23/26 dùng cho OCR / Danh sách cho đợt sale / Gói mua / So sánh / Nhắc nhở & ngưỡng | **Nhóm chốt 18/10: dùng mã Figma**; bảng ánh xạ ở `design/screen-spec.md` | Đã chốt |
| 2 | Đặc tả 11.2: hậu tố số phân cấp (19.1, 02.1) | Figma: vẫn hậu tố chữ (19a, 02a), thêm tiền tố "[MỚI]" | Giữ theo Figma; ghi "chưa áp dụng" | Nhóm + hỏi thầy (đặc tả 15.2) |
| 3 | Đặc tả 7.4: nhãn trung tính, không "Nên…" | Figma: Verdict tag "Hợp lý để mua", "Nên chờ", "Cân nhắc bỏ" | Tài liệu và handoff theo đặc tả; QĐ-N3 đề xuất sửa Figma | Nhóm |
| 4 | Đặc tả 7.8: "giá trị món đã quyết định không mua" | Figma: "Tiền đã giữ lại" (Kept money card, 22b, 23, Trang chủ ở 27) | Theo đặc tả; QĐ-N7 | Nhóm |
| 5 | Đặc tả quyết định 15: thời gian cân nhắc 3 ngày | Figma 26, 11f, thông báo: 7 ngày | Theo đặc tả; QĐ-N2 | Nhóm |
| 6 | Đặc tả 6.5 / 10.2: loại giá đơn · khoảng · Flash Sale; giá sau voucher thuộc khoản mua | Báo cáo Khoa 3.4 + Figma 30a/30b: loại giá "Sau voucher" trong lịch sử giá | **Nhóm chốt 18/10: giữ "Sau voucher"** (theo Khoa), không tính vào "Thấp nhất", không so với giá niêm yết (QĐ-N5) | Đã chốt |
| 7 | Đặc tả 8.3: ngưỡng lệch 30% chỉ để lọc **giá người khác ghi** (GĐ5) | Báo cáo Khoa 3.3: "giá lệch quá 30% so với trung vị bị ẩn" cho mọi lần ghi | Theo đặc tả và yêu cầu nhiệm vụ: không tự coi mọi chênh > 30% là sai (QĐ-N8) | Nhóm |
| 8 | Đặc tả 5.2, quyết định 21: chưa liên kết vẫn lưu được | Figma EXT-1 (theo 8 trạng thái của Kiệt): chặn lưu | Theo đặc tả; QĐ-N6 | Nhóm |
| 9 | Đặc tả X1 popup 400 × 600 | Figma EXT 360 × 560 | Ghi theo Figma | Không cần quyết |
| 10 | Báo cáo Khoa mục 5.4 dẫn "theo khảo sát mô phỏng" làm căn cứ khuyến mãi là lý do hàng đầu | Overview: không dùng dữ liệu mô phỏng làm bằng chứng | Repo dùng D2 (nguồn thật) làm căn cứ cho cơ chế khuyến mãi → FOMO | — |
| 11 | Đặc tả 11.4: 18 đổi thành Mua · Chờ · Bỏ qua; 03/04 có chip "Có dùng mã giảm giá"; 10 Cá nhân có lối vào Ngân sách, Hồ sơ, Thiết bị | Figma 18/10: chưa làm | Ghi là việc còn lại (mục 7) | Nhóm |
| 12 | Đặc tả không có quy đổi giá ra giờ làm | Figma 13 v3 "≈ 9 giờ làm việc", 26 "Thu nhập mỗi giờ" | **Nhóm chốt 18/10: giữ**, không bắt buộc, chỉ hiện khi người dùng tự nhập thu nhập mỗi giờ | Đã chốt |

## 6. Kiểm tra yêu cầu Lab 2

Chỉ ghi **PASS** khi đã kiểm trực tiếp trên Figma hoặc repo trong phiên này.

| Yêu cầu (đề Lab 2) | Bằng chứng kiểm ngày 18/10 | Kết quả |
|---|---|---|
| Đúng 6 page Figma theo thứ tự | `figma.root.children`: 01 User Flow, 02 Wireframe, 03 Final UI, 04 Design System, 05 Components, 06 Prototype | **PASS** |
| ≥ 8 màn khác nhau (không tính dialog, biến thể) | Page 03: Flow 1–10 (≈ 28 màn) + 19 màn mới (`ux/user-flow.md` mục 1.2) | **PASS** |
| ≥ 3 user flow có start, goal, end, nhánh thay thế, bảng ánh xạ | `ux/user-flow.md`: 13 flow; F11–F13 có bảng 4.2 | **PASS** (tài liệu) |
| ≥ 1 nhánh lỗi / phục hồi | Prototype: starting point F11b (19e), F12b (21a), F13b (X4 mã sai); đọc dây nối | **PASS** |
| IA: mọi màn thuộc ≥ 1 flow, mọi màn truy cập được | 23, 24, 26, 27 không thuộc flow nào trên prototype; 24, 25, 26, 31 không có lối vào từ 10 Cá nhân | **PARTIAL** |
| Wireframe low-fi của tất cả màn (page 02) | Có 28–31, X2–X5; **thiếu 19–27, EXT-1…8** | **PARTIAL** |
| Prompt Stitch nguyên văn + ảnh kết quả | Có cho P1, P2, R1–R3, F6 (hướng cũ); hướng mới chỉ có bộ prompt, chưa có ảnh | **PASS (cũ) / chưa có (mới)** |
| ≥ 3 vòng lặp AI khác mục tiêu, có ảnh trước / sau | R1–R3 trong log, ảnh trong `assets/stitch/` (không kiểm lại ảnh hôm nay) | **PASS (hướng cũ)**; hướng mới NOT VERIFIED |
| Phản biện AI ≥ 5 phát hiện gắn màn (Nielsen, accessibility, persona) | PB-1…PB-20 (cũ); PB2-1…PB2-14 (18/10, mục R5-2) | **PASS** |
| Mọi đề xuất quan trọng có chấp nhận / sửa / từ chối, Figma phản ánh | PB cũ có quyết định; PB2 **chưa có quyết định của nhóm** | **PARTIAL** |
| Token bằng Variables / styles, component dùng token | Variables: Color 29, Spacing 6, Radius 5, Size 4; 9 text style; 2 effect style. Chưa kiểm từng component có bind biến | **PASS (định nghĩa)**; bind NOT VERIFIED |
| 9 component với state bắt buộc | Button có Default / Pressed / Disabled / Loading; Navigation 5 biến thể; App bar Tab / Nested; Dialog Danger / Default; Skeleton; Empty / Error state (Empty, Filter empty, Error, Insufficient); Card: Wishlist item card có Pressed. **Text field chỉ Default / Focused / Error – thiếu Filled, Disabled** | **PARTIAL** |
| Accessibility: tương phản, ≥ 48 dp, chữ ≥ 14 sp, không chỉ màu, 360 / 412 dp | Flow 1–10: có checklist (`design-decisions.md` mục 2). Màn mới: tương phản tag đạt (5,14–13,86 : 1), **chữ tag 12 sp**, vùng chạm và 412 dp NOT VERIFIED | **PARTIAL** |
| Prototype: mỗi flow bấm được từ đầu đến cuối, Back đúng, ≥ 1 overlay, loading → kết quả, không ngõ cụt | F11–F13: có starting point; Back ở 28, 29a, 30b, 21, 25, 25b; overlay 25e; 19a → 19 sau 1,2 s; 25 → 25f sau 3 s; không thấy frame cụt. **Lỗi:** Mua ở 28 mở 03 sai món; EXT-1…8, X2a chưa nối; có starting point lạc tên "Flow 11" trỏ vào 09 Chiêm nghiệm tháng | **PASS có lỗi cần sửa** (chưa có người bấm thử) |
| Handoff: 6 mục mỗi màn + 2 bảng ánh xạ | Mục 1, 2 (bảng cũ) + mục 9 (12 nhóm màn F11–F13, mỗi nhóm 6 mục) | **PASS (tài liệu)**; chưa có bạn cùng lớp dựng thử |
| README ánh xạ sản phẩm, link hoạt động | Kiểm link tương đối: 0 link hỏng (mục 9) | **PASS** |
| Tên repo `prm323-lab2-<student-id>` | Repo là `prm393_lab02` | **NEEDS DECISION** (đặc tả 15.1 #22: hỏi thầy) |

## 7. Việc còn phải làm trên Figma / Stitch

1. Sửa câu chữ trái đặc tả: Verdict tag (PB2-1), 19f (PB2-2), "Tiền đã giữ lại" (PB2-11), thông báo "có thể được giảm giá" (PB2-12), 26 thời gian chờ 7 ngày (PB2-9).
2. Sửa EXT-1 để lưu được khi chưa liên kết; nối EXT-1…8 và X2a vào prototype F13; thêm trạng thái X4 nhập mã ban đầu.
3. Sửa prototype: Mua ở 28 → bản 03 điền sẵn đúng món; thêm snackbar Hoàn tác sau Bỏ qua; xóa hoặc đổi tên starting point lạc "Flow 11" (trỏ vào 09).
4. Thêm 4 hàng vào 10 Cá nhân (Ngân sách, Đồ đang dùng, Liên kết extension, Nhắc nhở & ngưỡng) và nối prototype.
5. Thêm chip "Có dùng mã giảm giá" ở 03 từ Wishlist; sửa 18 thành Mua · Chờ · Bỏ qua; sửa 14–16 điền sẵn từ món.
6. Sửa 30b: "Thấp nhất" không lấy giá "Sau voucher" (QĐ-N5 đã chốt giữ loại giá này).
7. Thống nhất dữ liệu mô phỏng (giá tai nghe) và thêm nhãn "Dữ liệu mô phỏng" ở mọi màn có số liệu.
8. Thêm biến thể Text field Filled, Disabled; đổi chữ tag sang 14 sp; Condition tag "Đã hỏng" không dùng màu error.
9. Vẽ wireframe 19–27 và EXT-1…8 trên page 02.
10. Nối hoặc ghi rõ phạm vi cho 22, 23, 24, 26, 27.
11. Nếu dùng Stitch cho hướng mới: chạy prompt trong `ai/stitch-prompts-why-i-buy.md`, lưu ảnh vào `assets/stitch/`, ghi nguyên văn prompt + ảnh trước / sau vào log; ít nhất 3 vòng có mục tiêu khác nhau.
12. Xuất ảnh theo checklist `assets/figma/README.md` và kiểm bố cục 360 / 412 dp.

## 8. Điểm cần nhóm quyết định

1. Chọn lại **10 quyết định quan trọng nhất** (hiện mục 1 + 1b = 18).
2. ~~Cách đánh mã màn~~ → **đã chốt 18/10: theo Figma.**
3. ~~QĐ-N5: giá sau voucher trong lịch sử giá~~ → **đã chốt 18/10: giữ** (không tính vào "Thấp nhất").
4. ~~Quy đổi "giờ làm việc" và "Thu nhập mỗi giờ"~~ → **đã chốt 18/10: giữ**, không bắt buộc.
5. Các màn GĐ4–GĐ5 (20, 22, 23, 24, 26, 27) có tính vào bài Lab 2 không?
6. File khảo sát 18/10: ai tạo câu trả lời, bằng cách nào? Nếu là mô phỏng thì đổi nhãn thành [Mô phỏng].
7. File `.xlsx` 14/10 vẫn nằm trong lịch sử `origin/main`. Có cần xóa khỏi lịch sử không? Việc này cần viết lại lịch sử và force push, **nằm ngoài quyền của phiên này**.
8. `ghi-khoan-mua-360dp.png` ở gốc repo: giữ, chuyển vào `assets/`, hay xóa?
9. Câu hỏi gửi thầy (đặc tả 15.2): phạm vi extension trong Lab 2, dữ liệu mô phỏng có nhãn, thay "vào tài khoản Shopee xem khuyến mãi" bằng lịch sale + giá thực trả, AI đánh giá độ phù hợp bằng quy tắc, cách hiểu "đánh mã phân cấp", quy mô research lại, tên repo.

## 9. Lệnh và kiểm tra đã chạy

| Kiểm tra | Cách chạy | Kết quả |
|---|---|---|
| Trạng thái git | `git status`, `git branch -a`, `git remote -v`, `git log` | `main` sạch; tạo nhánh `docs/whyibuy-2026-10-18` |
| Nguồn gốc khảo sát | Script Node đọc `xl/worksheets/sheet1.xml`, đổi số serial Excel ra giờ, tính khoảng cách | Mục 4 |
| Figma: page, frame, chữ, component, biến | `get_metadata`, `use_figma` chỉ đọc | 6 page đúng thứ tự; danh sách frame ở `design/screen-spec.md` |
| Figma: dây nối prototype F11–F13 | `use_figma`: `page.flowStartingPoints`, `node.reactions` của mọi frame trong 3 section | 18 starting point; dây nối như Mermaid trong `ux/user-flow.md` |
| Tương phản tag mới | `use_figma`: tính WCAG từ màu fill thực tế | 5,14–13,86 : 1; chữ 12 sp |
| Mermaid | `mermaid@11.4.1` + `jsdom` (cài tạm ở thư mục nháp), `mermaid.parse` mọi khối trong `ux/user-flow.md`; thử với một sơ đồ sai để chắc bộ kiểm có bắt lỗi | 15/15 khối hợp lệ |
| Link tương đối trong `.md` | Script Node duyệt mọi link Markdown dạng đường dẫn tương đối trong repo | 0 link hỏng |
| Xuống dòng | `grep -vc $'\r$'` trên các file đã sửa | Mọi file CRLF, UTF-8 |
| Stitch | `WebFetch` | NOT VERIFIED |

## 10. Patch tham khảo `why_i_buy_repo_patch_2026-10-18`

- **Đã tận dụng (sau khi tự kiểm lại trên Figma):** ý "giữ mã Figma tạm thời", danh sách trạng thái tối thiểu cho F11–F13, microcopy nên dùng / nên tránh, nhận xét về 112 giây của file khảo sát.
- **Không dùng:** không chép đè README, persona, handoff, screen-spec; không tạo `user-flow-current.md`, `screen-spec-current.md`, `research-2026-10-18.md` riêng (quy tắc VIII.7: cập nhật file chuẩn của rubric); không đưa `survey-aggregate-2026-10-18.json` vào repo (số liệu tổng hợp đã nằm trong `ux/research.md` mục 9).
- **Điểm patch chưa đúng so với Figma đọc ngày 18/10:** patch ghi F13 bắt đầu ở X4 rồi tới 25 / 25f; trên prototype, phía app (25 → 25f → 25b → 25e) và phía extension (X4 → X4a → X2) là **hai starting point riêng** (F13 và F13b). Patch cũng không nêu các lỗi prototype ở mục 7.

## 11. `git diff --stat`

Chạy `git diff --stat HEAD` sau khi sửa xong (chưa tính chính file báo cáo này):

| File | Thay đổi |
|---|---|
| `.gitignore` | +8 |
| `README.md` | +206 / − (viết lại) |
| `ai/ai-design-log.md` | +49 (mục R5, dòng khai báo công cụ) |
| `assets/figma/README.md` | +14 (checklist export) |
| `design/DESIGN.md` | +138 (quy tắc Smart Shopping Companion) |
| `design/design-decisions.md` | +51 (mục 1b, 2.7) |
| `design/screen-spec.md` | +152 (ánh xạ mã, màn F11–F13) |
| `handoff/flutter-handoff.md` | +272 (mục 9) |
| `ux/persona.md` | +410 dòng thay đổi (viết lại; bản cũ ở `archive/`) |
| `ux/research.md` | +99 (mục 9–11, ghi chú thay thế) |
| `ux/usability-test.md` | +2 |
| `ux/user-flow.md` | +250 (F11–F13) |
| `ux/research-pack/…(Câu trả lời).xlsx` | Bỏ theo dõi (file vẫn trên máy, đã bị `.gitignore` chặn) |
| **Tổng (file đã theo dõi)** | **13 file, +1307 / −344 dòng** |
| File mới (chưa theo dõi) | `docs/REPO_SYNC_REPORT_2026-10-18.md`, `archive/before-2026-10-18/README.md`, `archive/before-2026-10-18/ux/persona.md` |

**Không commit, không push.** Gợi ý commit sau khi nhóm duyệt: `git add -A` rồi `git commit -m "docs: sync repo to Smart Shopping Companion spec v1.0 and Figma ver2 (18/10)"`. Thư mục `WhyIBuy_Update_References/` đã được `.gitignore` chặn nên `git add -A` không đưa nó vào commit.
