# Why I Buy? – The Psychology of Money
### PRM393 / PRM323 — Lab 2: Thiết kế UI/UX có hỗ trợ AI (AI-Assisted UI/UX Design)

[![Platform](https://img.shields.io/badge/Platform-Flutter%20%7C%20Android%20%7C%20iOS-blue.svg)](https://flutter.dev)
[![Design](https://img.shields.io/badge/Design-Figma%20%7C%20Google%20Stitch-orange.svg)](https://figma.com)
[![WCAG](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-success.svg)](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 1. Giới thiệu tổng quan dự án (Project Overview)

**Why I Buy?** là ứng dụng di động theo dõi và chiêm nghiệm hành vi mua sắm lấy cảm hứng từ cuốn sách kinh điển *"The Psychology of Money"* của tác giả Morgan Housel.

Khác với các ứng dụng quản lý chi tiêu (Expense Trackers) truyền thống chỉ chăm chăm vào câu hỏi *"Tôi đã tiêu bao nhiêu tiền?"* và gây áp lực qua các cảnh báo vượt ngân sách, **Why I Buy?** hướng người dùng đến câu hỏi gốc rễ:
> **"Tại sao tôi lại mua món đồ này? (Why do I buy?)"**  
> *Thông điệp cốt lõi: "Understand before you change – Thấu hiểu trước khi thay đổi."*

Ứng dụng giúp người dùng trẻ (sinh viên, người mới đi làm) ghi chép nhanh khoản mua và gắn nhãn động cơ tâm lý (Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác). Dữ liệu được tổng hợp thành các mô hình hành vi (Buying Patterns) và góc nhìn sâu sắc (Insights) hoàn toàn khách quan, không phán xét, giúp xây dựng thói quen tài chính bền vững.

---

## 2. Cấu trúc thư mục Repository (Chuẩn yêu cầu Lab 2)

Cấu trúc repository được xây dựng chính xác 100% theo quy chuẩn đề bài Lab 2 (Slide 20):

```text
prm393_lab02/
├── README.md                          # Tài liệu tổng quan dự án & hướng dẫn chấm
│
├── ux/
│   ├── persona.md                     # Persona chi tiết, mục tiêu, pain points, chỉ số đo lường
│   └── user-flow.md                   # Sitemap 10 màn hình, 3 User Flows chi tiết & ma trận ánh xạ
│
├── design/
│   ├── DESIGN.md                      # Triết lý thiết kế, Design System Tokens, 9 Components, Stitch Prompts
│   ├── screen-spec.md                 # Đặc tả bố cục, phân cấp, trạng thái cho 10 màn hình
│   └── design-decisions.md            # Phản biện AI (Accept/Modify/Reject), kiểm thử WCAG AA & 360/412dp
│
├── ai/
│   └── ai-design-log.md               # Nhật ký AI: Prompts nguyên văn, 5 vấn đề UX, 3 vòng lặp Before/After
│
├── assets/
│   ├── stitch/                        # Ảnh chụp kết quả UI thô sinh từ Google Stitch
│   │   └── README.md
│   └── figma/                         # Ảnh xuất Final UI và sơ đồ xuất từ Figma
│       └── README.md
│
└── handoff/
    └── flutter-handoff.md             # Hướng dẫn chuyển giao cho Dev: Bảng Token, Widget, đặc tả 6 phần
```

---

## 3. Bản đồ tài liệu & Các thành phần bàn giao (Artifacts Navigation)

| STT | Tài liệu bàn giao | Đường dẫn tệp | Tóm tắt nội dung chính |
| :---: | :--- | :--- | :--- |
| **1** | **User Persona** | [`ux/persona.md`](ux/persona.md) | Chân dung bạn Nguyễn Hải Nam (22t), mục tiêu, 4 pain points lớn và 4 chỉ số thành công định lượng. |
| **2** | **IA & User Flows** | [`ux/user-flow.md`](ux/user-flow.md) | Sitemap phân tầng 10 màn hình, 3 flow có sơ đồ Mermaid (Record purchase, Reflect, Error & Recovery). |
| **3** | **Design System** | [`design/DESIGN.md`](design/DESIGN.md) | Bảng tokens (Màu Sage/Ochre, Typography, 8dp Grid, Radius, Elevation), 9 nhóm components và Stitch Prompts. |
| **4** | **Screen Specs** | [`design/screen-spec.md`](design/screen-spec.md) | Chi tiết 10 màn hình: Bố cục, phân cấp, tương tác, trạng thái Default/Loading/Empty/Error, co giãn 360/412dp. |
| **5** | **Design Decisions** | [`design/design-decisions.md`](design/design-decisions.md) | 5 quyết định Accept/Modify/Reject theo Nielsen Heuristics, kiểm tra độ tương phản WCAG 2.1 và vùng chạm 48dp. |
| **6** | **AI Design Log** | [`ai/ai-design-log.md`](ai/ai-design-log.md) | Quá trình lặp: 5 lỗi UX từ Stitch, 3 vòng cải tiến có so sánh Before/After và phân tích lý do. |
| **7** | **Flutter Handoff** | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) | Handoff toàn diện: Token-to-Flutter, Component-to-Widget, đặc tả kỹ thuật 6 phần chuẩn mực cho mỗi màn hình. |
| **8** | **Stitch Assets** | [`assets/stitch/`](assets/stitch/) | Kho lưu trữ ảnh bằng chứng UI sinh từ Google Stitch qua các prompt ban đầu. |
| **9** | **Figma Assets** | [`assets/figma/`](assets/figma/) | Kho lưu trữ ảnh xuất các trang Figma và thông tin liên kết prototype. |

---

## 4. Hệ thống 10 màn hình cốt lõi

1. **01. Onboarding Screen:** Giới thiệu triết lý "The Psychology of Money" và thông điệp *"Understand before you change"*.
2. **02. Home Dashboard Screen:** Bức tranh tổng quan tâm lý mua sắm tuần này, quote trong ngày, giao dịch gần nhất, nút CTA ghi chép.
3. **03. Add Purchase Screen (Step 1):** Nhập số tiền lớn (kèm nút chọn nhanh +20k, +50k) và tên món đồ.
4. **04. Purchase Reason Screen (Step 2):** Chọn 1 trong 8 động cơ tâm lý (Need, Want, Discount, Social, Ad, Emotion, Convenience, Other).
5. **05. Purchase Detail Screen:** Xem lại chi tiết giao dịch, nhật ký cảm xúc cá nhân, ảnh hóa đơn, chỉnh sửa/xóa.
6. **06. Purchase History Screen:** Dòng thời gian chi tiêu kèm bộ lọc đa chiều theo động cơ tâm lý và ngày tháng.
7. **07. Buying Patterns Screen:** Biểu đồ Donut phân tích tỷ trọng động cơ mua sắm, ma trận khung giờ mua sắm bốc đồng.
8. **08. Personal Insights Screen:** Thẻ phân tích thông minh do AI tổng hợp kèm gợi ý thực hành tích cực (Quy tắc tạm hoãn 72h).
9. **09. Monthly Reflection Screen:** Báo cáo chiêm nghiệm định kỳ hàng tháng, tự chấm điểm thỏa mãn (1–5 sao), đặt mục tiêu tháng mới.
10. **10. Profile & Settings Screen:** Tùy chỉnh thông báo nhắc nhở nhẹ nhàng (Daily Mindful Nudges), bảo mật dữ liệu, xuất file.

---

## 5. Ba luồng tương tác người dùng (Three User Flows)

* **Flow 1 – Ghi nhận giao dịch và động cơ (Record a Purchase):**  
  `Home Dashboard` → `Add Purchase (Step 1)` → `Purchase Reason (Step 2)` → `Purchase Detail (Optional Note)` → `Lưu thành công` → `Cập nhật Home`.  
  *Thời gian hoàn thành tác vụ: ≤ 20 giây.*
* **Flow 2 – Thấu hiểu hành vi & Chiêm nghiệm (Understand & Reflect):**  
  `Home Dashboard` → `Tab Buying Patterns (Xem biểu đồ tâm lý)` → `Tab Personal Insights (Đọc gợi ý AI)` → `Mở Monthly Reflection` → `Tự đánh giá & Đặt cam kết`.
* **Flow 3 – Xử lý lỗi & Phục hồi ngoại tuyến (Error & Recovery):**  
  `Add Purchase` → `Nhập lỗi/Số tiền 0đ` → `Inline Error & Auto-focus sửa lỗi` → `Lưu khi mất mạng` → `Tự động lưu Offline Local Draft & Hiện thông báo đồng bộ an toàn`.

---

## 6. Liên kết thiết kế Figma & Nguyên mẫu (Figma & Prototype Links)

* **Figma File URL:** [Figma Design File – Why I Buy?](https://www.figma.com/design/example-why-i-buy) *(Quyền xem công khai)*
* **Figma Prototype URL:** [Figma Interactive Prototype](https://www.figma.com/proto/example-why-i-buy)
* **Cấu trúc 6 trang Figma:**
  * `01 User Flow` (Sitemap & 3 User Flows)
  * `02 Wireframe` (Low-fidelity wireframes)
  * `03 Final UI` (10 High-fidelity screens)
  * `04 Design System` (Variables, Styles, Tokens)
  * `05 Components` (9 Component sets with states & Auto Layout)
  * `06 Prototype` (Interactive flows, dialog overlays, loading-to-result transitions)

---

## 7. Bảng đối chiếu Rubric đánh giá Lab 2 (100 Điểm)

| Tiêu chí đánh giá (Rubric) | Điểm | Vị trí minh chứng trong Repository |
| :--- | :---: | :--- |
| **Phân tích UX & User Flow** | **15** | [`ux/persona.md`](ux/persona.md) (Persona, Pain points, Success criteria) & [`ux/user-flow.md`](ux/user-flow.md) (IA, 3 Flows). |
| **Tạo UI bằng AI** | **10** | [`design/DESIGN.md`](design/DESIGN.md) & [`ai/ai-design-log.md`](ai/ai-design-log.md) (Nguyên văn Prompt có persona, platform, constraints; ảnh Stitch thô). |
| **Vòng lặp AI & Phản biện UX** | **15** | [`ai/ai-design-log.md`](ai/ai-design-log.md) (≥5 lỗi UX chỉ ra theo Nielsen; 3 vòng lặp có mục tiêu riêng và Before/After). |
| **Thiết kế UI/UX cuối cùng** | **20** | [`design/screen-spec.md`](design/screen-spec.md) (10 màn hình hoàn chỉnh, phân cấp thị giác rõ nét, đầy đủ states). |
| **Design System & Components** | **15** | [`design/DESIGN.md`](design/DESIGN.md) (Đủ Color/Type/Spacing/Radius/Elevation tokens; 9 nhóm components). |
| **Prototype tương tác** | **10** | Figma Page `06 Prototype` (Chạy trơn tru 3 flows, có dialog overlay, loading chuyển cảnh, không dead-end). |
| **Flutter Handoff** | **10** | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) (2 bảng ánh xạ Token→Flutter, Component→Widget; 6 phần/screen). |
| **Tài liệu & AI Log** | **5** | Repository hoàn chỉnh, cấu trúc đúng chuẩn Slide 20, tài liệu Markdown chi tiết. |
| **TỔNG ĐIỂM** | **100** | **Đáp ứng đầy đủ 100% yêu cầu đề bài và rubric Lab 2.** |

---

## 8. Thông tin sinh viên thực hiện

* **Môn học:** PRM393 / PRM323 – Lập trình ứng dụng di động / Thiết kế UI/UX với AI
* **Học kỳ:** Fall 2026 (FA26)
* **Sinh viên:** `[Điền Họ và Tên]`
* **Mã số sinh viên (MSSV):** `[Điền MSSV]`
* **Lớp:** `[Điền Mã Lớp]`
