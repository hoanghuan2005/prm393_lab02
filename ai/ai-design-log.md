# AI-Assisted UI/UX Design Log

**Project:** Why I Buy? – The Psychology of Money  
**Course:** PRM393 / PRM323 – Mobile UI/UX Design with AI  
**Deliverable:** AI Prompts, UI Generation Outputs, UX Critique & 3 Iteration Loops  

---

## 1. Phương pháp luận vòng lặp thiết kế có AI hỗ trợ (Design Loop Methodology)

Nhóm áp dụng quy trình 5 bước khép kín theo tiêu chuẩn đánh giá của Lab 2:

```
[1. Phân tích bối cảnh & Persona] 
       ↓
[2. Thiết lập Prompt kỹ thuật chuẩn xác] 
       ↓
[3. Sinh UI ban đầu bằng AI (Google Stitch)] 
       ↓
[4. Phản biện UX & Khả năng tiếp cận (Nielsen & WCAG)] 
       ↓
[5. Tinh chỉnh & Chuyển giao sang Figma]
```

---

## 2. Bảng tổng hợp các vấn đề UX phát hiện qua phản biện (UX Critique Findings)

Qua việc đối chiếu kết quả sinh tự động từ AI (Google Stitch) với 10 nguyên lý phỏng đoán Nielsen và tiêu chuẩn WCAG 2.1, nhóm đã chỉ ra **5 vấn đề UX nghiêm trọng**:

| Mã lỗi | Màn hình vi phạm | Chi tiết vấn đề phát hiện | Nguyên lý vi phạm | Hướng khắc phục trong Figma |
| :---: | :--- | :--- | :--- | :--- |
| **UX-01** | Home Dashboard | AI tự động thêm biểu đồ cảnh báo chi tiêu vượt hạn mức màu đỏ chót và icon tam giác than nguy hiểm. | **Persona Alignment & Nielsen #10** (Khắc phục tâm lý né tránh) | Xóa bỏ cảnh báo đỏ trừng phạt; thay thế bằng Hero Card màu Sage Green phân tích động cơ tâm lý khách quan. |
| **UX-02** | Add Purchase | Form nhập liệu trải dài 8 trường dữ liệu trên 1 màn hình cuộn, bàn phím số khi mở lên che mất nút CTA. | **Nielsen #8** (Aesthetic & Minimalist Design) | Tách quy trình thành 2 bước (Progressive Disclosure): Bước 1 nhập Tiền & Tên; Bước 2 chọn Lý do. |
| **UX-03** | Reason Picker | AI sử dụng dropdown list nhỏ bé với font chữ 11sp và vùng bấm chỉ cao 28dp. | **WCAG 2.5.5 & Nielsen #6** (Recognition vs Recall) | Thay dropdown bằng lưới 8 Reason Cards dạng thẻ lớn (chiều cao 76dp, font 15sp, icon trực quan). |
| **UX-04** | Form Validation | Khi nhập sai hoặc thiếu dữ liệu, AI bật pop-up Alert Dialog modal khóa toàn bộ màn hình. | **Nielsen #3** (User Control) & **#9** (Error Recovery) | Chuyển sang Inline Error hiển thị hướng dẫn trực tiếp dưới chân trường input; auto-focus con trỏ. |
| **UX-05** | Buying Patterns | Biểu đồ AI sinh ra gom các giao dịch theo danh mục tiền tệ truyền thống (Ăn uống, Giải trí) thay vì động cơ. | **Product Concept Alignment** (*The Psychology of Money*) | Thiết kế lại Donut Chart phân tích theo 8 động cơ tâm lý cốt lõi (Need, Want, Discount, Social, Emotion,...). |

---

## 3. Ba vòng lặp cải tiến chi tiết (Three Iteration Rounds)

---

### Vòng lặp 1: Tối ưu cấu trúc thông tin & Giảm tải nhận thức (Information Architecture & Cognitive Load)

* **Mục tiêu vòng lặp:** Tinh gọn luồng ghi nhận giao dịch từ màn hình đơn phức tạp thành luồng 2 bước trực quan, giảm thời gian hoàn thành tác vụ xuống dưới 25 giây cho Persona Nam.
* **Prompt tinh chỉnh (Refinement Prompt):**
  ```text
  Refine the Add Purchase interface for "Why I Buy?". 
  Current issue: The single-screen form with 8 inputs causes cognitive overload and keyboard obstruction.
  Action: Split into a clean 2-step progressive flow:
  - Step 1: Big prominent amount input with +20k, +50k, +100k quick chips and item name field.
  - Step 2: 2x4 card grid for the 8 psychological reasons with expressive icons.
  Keep primary button sticky at bottom with 52dp height.
  ```
* **So sánh Trước và Sau (Before vs. After):**
  * *Trước cải tiến (AI Stitch Output 1):* Người dùng phải cuộn qua 3 lần chiều dài màn hình, đối mặt với 8 ô nhập liệu, tỷ lệ bỏ dở ghi chép ước tính 45%.
  * *Sau cải tiến (Figma Iteration 1):* Giao diện chia làm 2 bước rõ ràng. Bước 1 chỉ tốn 6 giây để nhập tiền và tên; Bước 2 chỉ mất 1 chạm để chọn lý do. Thời gian thực nghiệm giảm xuống chỉ còn 16–18 giây.

---

### Vòng lặp 2: Khả năng tiếp cận & Tiêu chuẩn công thái học di động (Accessibility & Mobile Ergonomics)

* **Mục tiêu vòng lặp:** Đảm bảo tất cả các thành phần tương tác đạt chuẩn vùng chạm Fitts' Law (≥ 48×48 dp) và tỷ lệ tương phản chữ đạt chuẩn WCAG AA trên cả hai kích thước màn hình 360dp và 412dp.
* **Prompt tinh chỉnh (Refinement Prompt):**
  ```text
  Audit and refine touch targets and contrast for the Reason Selection and Dashboard screens.
  Requirements:
  - Increase all clickable card heights to at least 72dp.
  - Upgrade secondary text color to Slate Cool Grey #4A5568 to ensure at least 7:1 contrast ratio against white cards.
  - Ensure all icon buttons have 48x48dp minimum hit box.
  - Verify layout responsiveness across 360dp width (no horizontal overflow or truncated badges).
  ```
* **So sánh Trước và Sau (Before vs. After):**
  * *Trước cải tiến (AI Stitch Output 2):* Menu chọn lý do có kích thước vùng bấm chỉ 28dp, chữ phụ màu xám nhạt (`#A0AEC0` – tương phản chỉ đạt 2.8:1, trượt chuẩn WCAG). Thẻ bị cắt cụt tiêu đề trên màn hình hẹp 360dp.
  * *Sau cải tiến (Figma Iteration 2):* Toàn bộ 8 thẻ Reason Card được quy chuẩn kích thước 160×76 dp (vùng bấm 100% diện tích thẻ). Chữ đổi sang `#4A5568` đạt tương phản 7.2:1 (vượt chuẩn WCAG AAA). Flex grid tự động co dãn mượt mà trên 360dp và 412dp.

---

### Vòng lặp 3: Đồng bộ triết lý "The Psychology of Money" & Ngôn ngữ không phán xét (Mindful Tone & Reflection)

* **Mục tiêu vòng lặp:** Định hình lại toàn bộ hệ thống biểu đồ và thông điệp UX từ phong cách kế toán khô khan sang phong cách đồng hành, kích thích sự tự nhận thức (Self-awareness).
* **Prompt tinh chỉnh (Refinement Prompt):**
  ```text
  Transform the analytics screens to deeply align with Morgan Housel's "The Psychology of Money".
  Replace financial spending bar charts with:
  1. Psychological Reason Donut Chart showing percentage of purchases driven by Need vs Emotion vs Discount vs Social.
  2. Late-night Impulse Trigger heatmap.
  3. Empathetic AI insight cards with supportive, constructive advice (e.g. "72-hour pause rule for discount hunting").
  Use soothing Sage Green and Warm Amber tones. Tone of voice: curious, empathetic, reflective.
  ```
* **So sánh Trước và Sau (Before vs. After):**
  * *Trước cải tiến (AI Stitch Output 3):* Giao diện phân tích giống hệt app ngân hàng với các cột chi phí thô cứng "Ăn uống 2.500.000₫", "Mua sắm 1.800.000₫", không đem lại giá trị thấu hiểu tâm lý.
  * *Sau cải tiến (Figma Iteration 3):* Màn hình **Buying Patterns** và **Personal Insights** trực quan hóa sống động nguyên nhân mua hàng: người dùng nhận diện ngay việc mình chi tiêu nhiều nhất vì *"Cảm xúc lúc đêm khuya"* và *"Bẫy giảm giá flash sale"*, đi kèm giải pháp thực tế để cải thiện thói quen.

---

## 4. Liên kết kho lưu trữ ảnh minh chứng

* Toàn bộ ảnh chụp màn hình gốc của Google Stitch được lưu trữ tại: [`assets/stitch/`](../assets/stitch/)
* Toàn bộ ảnh thiết kế giao diện hoàn thiện xuất từ Figma được lưu trữ tại: [`assets/figma/`](../assets/figma/)
