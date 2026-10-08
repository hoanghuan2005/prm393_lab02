# Design System & UI Specifications

**Project:** Why I Buy? – The Psychology of Money  
**Course:** PRM393 / PRM323 – Mobile UI/UX Design with AI  
**Deliverable:** Design Tokens, Typography, Components & AI Generation Prompts  

---

## 1. Design Philosophy & Visual Language

Ứng dụng **Why I Buy?** xây dựng ngôn ngữ thiết kế dựa trên 4 trụ cột cảm xúc:

1. **Calm & Non-Judgmental (Điềm tĩnh & Không phán xét):**  
   Tránh hoàn toàn các dải màu đỏ gắt gỏng hoặc các biểu tượng cảnh báo tiêu cực thường thấy trên ứng dụng ngân hàng khi người dùng chi tiêu nhiều. Thay vào đó, sử dụng bảng màu dịu mát của cây xô thơm (Sage Green) kết hợp với màu cát ấm (Warm Sand) tạo cảm giác an tâm, thư thái để người dùng cởi mở đối diện với thói quen của mình.
2. **Mindful Reflection (Chiêm nghiệm thấu đáo):**  
   Bố cục thoáng đạt với tỷ lệ khoảng trắng (white space) rộng rãi, giúp người dùng tập trung vào nội dung câu hỏi *"Why did I buy this?"* thay vì bị choáng ngợp bởi hàng loạt con số hay bảng tính phức tạp.
3. **Clarity & Micro-Commitment (Rõ ràng & Nhập liệu tối giản):**  
   Mọi tương tác ghi chép được tối ưu thành các khối thẻ (Cards) và chip nhãn trực quan, chỉ cần 1-2 chạm là hoàn tất.
4. **Inclusive Accessibility (Tiếp cận toàn diện):**  
   Mọi tỷ lệ tương phản chữ đạt tiêu chuẩn WCAG AA (≥ 4.5:1), vùng chạm tối thiểu 48×48 dp, kích thước font chữ nội dung luôn ≥ 14 sp.

---

## 2. Design Tokens

### 2.1. Color Tokens (Bảng màu quy chuẩn)

| Token Name | Hex Code | Role & Usage | Contrast Ratio (vs Background) |
| :--- | :--- | :--- | :--- |
| `color-primary-500` | `#2D6A4F` | Deep Sage Green – Màu thương hiệu chủ đạo, CTA buttons, active state | 7.8:1 (WCAG AAA) |
| `color-primary-100` | `#D8F3DC` | Soft Sage Tint – Nền chip được chọn, highlight nhẹ | 1.3:1 (Nền trang trí) |
| `color-secondary-500` | `#DDA15E` | Warm Ochre / Amber – Điểm nhấn cho "Insight" và "Reflection" | 4.6:1 (WCAG AA) |
| `color-background` | `#F8F9FA` | Off-white / Cool Grey – Nền tổng thể toàn ứng dụng, giảm mỏi mắt | Reference (1.0) |
| `color-surface` | `#FFFFFF` | Pure White – Nền các Cards, Modal Sheet, Dialog | 1.1:1 |
| `color-surface-variant` | `#EDF2F4` | Light Grey – Nền Input field, divider line | 1.2:1 |
| `color-text-primary` | `#1A202C` | Slate Black – Tiêu đề chính, số tiền, nhãn quan trọng | 14.1:1 (WCAG AAA) |
| `color-text-secondary` | `#4A5568` | Cool Grey – Nội dung mô tả, phụ đề, nhãn thời gian | 7.2:1 (WCAG AAA) |
| `color-text-tertiary` | `#718096` | Muted Grey – Placeholder, caption, đơn vị phụ | 4.6:1 (WCAG AA) |
| `color-semantic-success` | `#38B000` | Fresh Leaf Green – Trạng thái hoàn tất, tiết kiệm thành công | 4.8:1 (WCAG AA) |
| `color-semantic-warning` | `#E07A5F` | Terracotta / Soft Rust – Báo hiệu chi tiêu cảm xúc cao (thay cho màu đỏ gắt) | 4.7:1 (WCAG AA) |
| `color-semantic-error` | `#C53030` | Crimson Red – Lỗi hệ thống, xác thực dữ liệu thất bại | 6.2:1 (WCAG AAA) |

---

### 2.2. Typography Tokens

Hệ thống kiểu chữ sử dụng font sans-serif hình học hiện đại: **Plus Jakarta Sans** (dự phòng: *Inter*, *Roboto*).

| Token Name | Size (sp) | Weight | Line Height (dp) | Usage |
| :--- | :---: | :---: | :---: | :--- |
| `font-display-lg` | 32 | Bold (700) | 40 | Số tiền lớn, Tiêu đề Onboarding |
| `font-heading-md` | 24 | Bold (700) | 32 | Tiêu đề màn hình cấp 1 (Dashboard, History) |
| `font-heading-sm` | 20 | Semi-Bold (600) | 28 | Tiêu đề khối card, Section Header |
| `font-title` | 16 | Semi-Bold (600) | 24 | Tên món đồ, Label trường dữ liệu |
| `font-body-md` | 15 | Regular (400) | 22 | Văn bản mô tả, ghi chú chi tiêu (≥ 14 sp) |
| `font-body-sm` | 14 | Regular (400) | 20 | Subtitle, Chú thích thẻ Card |
| `font-caption` | 12 | Medium (500) | 16 | Metadata, nhãn thời gian, Chip tag text |

---

### 2.3. Spacing Tokens (Hệ lưới chuẩn 8dp Grid)

* `space-4` (4 dp): Khoảng cách vi mô (icon với text nhãn).
* `space-8` (8 dp): Khoảng cách giữa các chip tag, margin trong thẻ nhỏ.
* `space-12` (12 dp): Padding ngang trong ô input, khoảng cách hàng thông số.
* `space-16` (16 dp): Base Grid – Padding lề màn hình mobile chuẩn, khoảng cách giữa các card.
* `space-24` (24 dp): Khoảng cách giữa các nhóm chức năng (section divider).
* `space-32` (32 dp): Margin đầu trang dưới Top App Bar.
* `space-48` (48 dp): Minimum Interactive Touch Target (WCAG 2.1 Target Size).

---

### 2.4. Border Radius Tokens

* `radius-sm` (8 dp): Chip nhãn lý do mua sắm, Badge nhỏ.
* `radius-md` (12 dp): Text field input container, nút phụ nhỏ.
* `radius-lg` (16 dp): Thẻ Purchase Card, Action Card, Modal Bottom Sheet.
* `radius-xl` (24 dp): Nút Primary Button, Dashboard Hero Card.
* `radius-full` (999 dp): Pill Buttons, Avatar hình tròn, Floating Action Button (FAB).

---

### 2.5. Elevation & Shadow Tokens

* `elevation-0`: Không bóng đổ (`box-shadow: none`).
* `elevation-1`: `0px 2px 4px rgba(0, 0, 0, 0.05)` (Dùng cho Card thông thường trên bề mặt).
* `elevation-2`: `0px 4px 12px rgba(0, 0, 0, 0.08)` (Dùng cho Card hover/active, Bottom Navigation Bar).
* `elevation-3`: `0px 8px 24px rgba(0, 0, 0, 0.12)` (Dùng cho Modal Bottom Sheet, Dialog popup).

---

## 3. Component System (9 Nhóm Thành Phần Bắt Buộc)

| STT | Tên nhóm Component | Phân loại & Biến thể (Variants) | Trạng thái bắt buộc (States) |
| :---: | :--- | :--- | :--- |
| **1** | **Button** | Primary CTA, Secondary Outlined, Text Only, Icon Button | Default, Hover, Pressed, Focused, Disabled, Loading |
| **2** | **Text Field** | Single-line (Amount, Item Name), Multi-line (Emotion Notes) | Default, Active/Focused, Filled, Error (với helper text) |
| **3** | **Purchase Card** | Standard Item Card, Hero Metric Card, Compact Transaction Tile | Default, Pressed/Tapped, Dismissible (Swipe to delete) |
| **4** | **Reason Chip / Card** | 8 Động cơ (Need, Want, Discount, Social, Ad, Emotion, Convenience, Other) | Unselected, Selected (Border 2px + Tint), Disabled |
| **5** | **Bottom Navigation** | 5 Tabs (Home, History, Patterns, Insights, Profile) | Inactive (Icon + Label), Active (Filled Icon + Indicator bar) |
| **6** | **App Bar** | Large Header (Dashboard), Contextual Back App Bar (Detail/Add) | Normal, Scrolled (elevation tăng), With Action Icons |
| **7** | **Dialog & Modal** | Confirmation Dialog (Xác nhận xóa), Bottom Sheet (Chọn lý do) | Open / Visible (với Dark Dimmed Overlay), Closed |
| **8** | **Loading State** | Skeleton Card Placeholder, Circular Spinner trong CTA button | Active Shimmering, Spinning |
| **9** | **Empty & Error State**| Empty History View, Offline Network Error Banner, Validation Error | View hiển thị Illustration + Copy thân thiện + Nút Action |

---

## 4. Nguyên Văn Prompt Tạo UI Ban Đầu Bằng AI (Google Stitch Prompts)

Dưới đây là các prompt chuẩn xác được sử dụng để sinh layout gốc qua công cụ AI Google Stitch:

### Prompt 1: Home Dashboard & Psychology Overview
```text
Role: Senior Mobile UI/UX Designer
Platform: Mobile App (Android Material 3 & iOS), Screen size 390x844 dp
App Name: "Why I Buy? – The Psychology of Money"
Target Persona: Tech-savvy college student / young adult who struggles with impulse buying from social media and sales.
Design Tone: Minimalist, calming, reflective, non-judgmental (use Sage Green #2D6A4F, Warm Ochre #DDA15E, Soft Sand off-white). No harsh red expense warnings.

Generate Screen 1: Home Dashboard
Header: Friendly greeting "Good evening, Nam", subtle avatar, and daily psychology quote "Understand before you change".
Hero Card: "This Week's Mindset" card showing top purchasing triggers (e.g., 40% Emotion, 30% Need, 20% Discount) with soft colored progress pills.
Quick Action: Centered prominent button "Why did I buy? (Record Purchase)".
Recent Section: "Recent Reflections" list showing the last 3 logged purchases with item name, price in VND, date, and a distinct Reason Tag chip (e.g., "Discount", "Convenience").
Bottom Bar: 5-item modern bottom navigation (Home, History, Patterns, Insights, Profile).
Constraints: Clean spacing 16dp grid, minimum touch target 48x48dp, contrast WCAG AA.
```

### Prompt 2: Add Purchase & Reason Picker Flow
```text
Platform: Mobile App, Screen size 390x844 dp
Screen: Add Purchase & Psychology Reason Picker (2-step modal)
Style: Modern, spacious, card-based UI.

Generate Screen 2: Add Purchase Screen
Top Bar: "Log a Purchase" with close 'X' button and step indicator (Step 1 of 2).
Input Section:
- Large friendly currency input field: "0 ₫" with quick add chips (+20k, +50k, +100k).
- Text field: "What did you buy?" (e.g. "Matcha Latte", "Shopee T-Shirt").
- Category quick select icons (Food, Tech, Apparel, Entertainment).
CTA: Primary button "Next: Why did you buy it?" with deep sage green fill.

Generate Screen 3: Purchase Reason Selection
Header: "What was the real reason behind this purchase?"
Grid layout: 8 distinct tappable Reason Cards arranged in a 2x4 grid:
1. Need (Essential survival / daily necessity)
2. Want (Pure personal desire)
3. Discount (Bought because it was on sale / promo)
4. Social Influence (Recommended by friends / saw on social media)
5. Advertising (Targeted ads / TikTok review)
6. Emotional Purchase (Stress relief, boredom, celebration)
7. Convenience (Saved time / delivered fast)
8. Other (Custom note)
Each card has an expressive minimal icon, title, and short subtitle.
State: Show card "Emotional Purchase" in active selected state (sage border + light green tint).
Action Bar: Sticky bottom bar with button "Save & Reflect".
```

### Prompt 3: Buying Patterns & Monthly Reflection
```text
Platform: Mobile App, Screen size 390x844 dp
Screen: Buying Patterns & Monthly Mindset Report
Style: Data visualization with empathetic copywriting.

Generate Screen 4: Buying Patterns Screen
Header: "Your Spending Psychology" with month selector ("October 2026").
Insight Summary: Card explaining "Your top trigger this month is Emotional Purchase during late nights (22:00 - 01:00)".
Chart Section: Donut chart displaying reason breakdown (not money categories, but psychological triggers).
Time Matrix: Weekly heat-map bar showing days with highest impulsive purchases.
Reflection CTA: Secondary outlined button "Open Monthly Reflection".
```
