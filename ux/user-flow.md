# Information Architecture & User Flows

**Project:** Why I Buy? – lấy cảm hứng từ "The Psychology of Money"
**Course:** PRM323 – Cross-Platform Application Development

---

## 1. Danh sách màn hình

| # | Màn hình | Cấp | Truy cập từ | Mục đích |
|---|---|---|---|---|
| 01 | Onboarding | Điểm vào (lần đầu mở app) | Mở app | Giới thiệu thông điệp "Hiểu trước khi thay đổi" |
| 02 | Home Dashboard | Tab 1 | Thanh điều hướng, sau 01 | Tổng quan tuần, nút "Ghi khoản mua", khoản gần đây |
| 03 | Add Purchase | Lồng – bước 1/2 | 02, trạng thái trống của 07 | Nhập số tiền, tên món, thời điểm |
| 04 | Purchase Reason | Lồng – bước 2/2 | 03 | Chọn 1 trong 8 động cơ, ghi chú tùy chọn, lưu |
| 05 | Purchase Detail | Lồng | 02 (mục Gần đây), 06 | Xem, sửa hoặc xóa một khoản mua |
| 06 | Purchase History | Tab 2 | Thanh điều hướng | Danh sách khoản mua theo ngày, lọc theo động cơ |
| 07 | Buying Patterns | Tab 3 | Thanh điều hướng | Tỷ lệ động cơ, khung giờ hay mua |
| 08 | Personal Insights | Tab 4 | Thanh điều hướng, 07 | Thẻ góc nhìn tổng hợp từ dữ liệu người dùng ghi |
| 09 | Monthly Reflection | Lồng | 08 | Tự đánh giá mức hài lòng và đặt mục tiêu tháng |
| 10 | Profile & Settings | Tab 5 | Thanh điều hướng, 09 | Nhắc nhở, xuất dữ liệu, cài đặt |

Tám động cơ (dùng thống nhất trong toàn bộ dự án): Nhu cầu, Mong muốn, Khuyến mãi,
Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác.

## 2. Cấu trúc điều hướng

```mermaid
flowchart TD
    S01[01 Onboarding] --> NAV{{Thanh điều hướng dưới - 5 tab}}
    NAV --> S02[02 Home Dashboard]
    NAV --> S06[06 Purchase History]
    NAV --> S07[07 Buying Patterns]
    NAV --> S08[08 Personal Insights]
    NAV --> S10[10 Profile & Settings]
    S02 --> S03[03 Add Purchase] --> S04[04 Purchase Reason]
    S02 --> S05[05 Purchase Detail]
    S06 --> S05
    S07 --> S08
    S08 --> S09[09 Monthly Reflection]
```

Độ sâu tối đa: 2 lần chạm từ một tab (02 → 03 → 04).

## 3. User flows

### Flow 1 — Ghi nhanh một khoản mua (có nhánh lỗi và phục hồi)
- **Bắt đầu:** 02 Home Dashboard (lần đầu: 01 Onboarding)
- **Mục tiêu:** ghi một khoản mua kèm động cơ trong ≤ 25 giây
- **Kết thúc:** quay về 02 với snackbar "Đã lưu", khoản mới hiện ở mục Gần đây

```mermaid
flowchart TD
    First([Mở app lần đầu]) --> S01[01 Onboarding] --> Start
    Start([02 Home Dashboard]) --> Add[Nhấn 'Ghi khoản mua']
    Add --> S03[03 Add Purchase: nhập số tiền, tên món]
    S03 --> Valid{Số tiền hợp lệ?}
    Valid -->|Không| Err[Lỗi dưới ô nhập, tự focus ô số tiền] --> S03
    Valid -->|Có| S04[04 Purchase Reason: chọn 1 trong 8 động cơ]
    S04 --> Note{Thêm ghi chú?}
    Note -->|Có| Write[Nhập ghi chú ngay trong 04] --> Save
    Note -->|Không| Save[Nhấn 'Lưu', nút chuyển sang loading]
    Save --> Net{Có mạng?}
    Net -->|Có| Done([02 Home + snackbar 'Đã lưu'])
    Net -->|Không| Offline[Lưu trên máy + banner 'Sẽ đồng bộ khi có mạng'] --> Done
```

- **Happy path:** 02 → 03 (nhập "Trà sữa", 45.000 ₫) → 04 (chọn Cảm xúc) → Lưu → 02.
- **Nhánh thay thế:** thêm ghi chú "Mệt sau giờ làm đồ án" trong 04 trước khi lưu.
- **Nhánh lỗi:** nhập 0 ₫ → báo lỗi, sửa lại; hoặc mất mạng → lưu trên máy, không mất dữ liệu.

### Flow 2 — Khám phá mô hình và chiêm nghiệm tháng
- **Bắt đầu:** 02 Home Dashboard
- **Mục tiêu:** hiểu động cơ mua phổ biến nhất trong tháng và tự đánh giá
- **Kết thúc:** hoàn tất Monthly Reflection (tùy chọn bật nhắc hằng tháng)

```mermaid
flowchart TD
    Start([02 Home Dashboard]) --> S07[07 Buying Patterns]
    S07 --> Load[Skeleton loading]
    Load --> Res{Kết quả tải}
    Res -->|Lỗi| Error[Trạng thái lỗi: nguyên nhân + 'Thử lại'] --> Load
    Res -->|Chưa đủ 5 khoản| Empty[Trạng thái trống: 'Ghi thêm vài khoản'] --> Go03([03 Add Purchase])
    Res -->|Đủ dữ liệu| View[Xem tỷ lệ động cơ và khung giờ]
    View --> Period[Đổi Tuần / Tháng] --> View
    View --> S08[08 Personal Insights: đọc thẻ góc nhìn]
    S08 --> S09[09 Monthly Reflection]
    S09 --> Act{Người dùng}
    Act -->|Để sau| Back08([Quay lại 08])
    Act -->|Tự đánh giá + đặt mục tiêu| Remind{Bật nhắc hằng tháng?}
    Remind -->|Có| S10[10 Profile & Settings: bật nhắc] --> End
    Remind -->|Không| End([Hoàn tất chiêm nghiệm tháng])
```

### Flow 3 — Xem lại, xóa và hoàn tác (nhánh phục hồi)
- **Bắt đầu:** 06 Purchase History
- **Mục tiêu:** sửa hoặc xóa một khoản ghi nhầm
- **Kết thúc:** lịch sử được cập nhật, hoặc khôi phục nếu hoàn tác

```mermaid
flowchart TD
    Start([06 Purchase History]) --> Filter{Lọc theo động cơ}
    Filter -->|Không có kết quả| Empty[Trạng thái trống: 'Xóa bộ lọc'] --> Start
    Filter -->|Có kết quả| S05[05 Purchase Detail]
    S05 --> Choice{Người dùng}
    Choice -->|Sửa| Edit[Sửa động cơ hoặc ghi chú, lưu] --> S05
    Choice -->|Xóa| Dialog[Dialog: 'Xóa khoản mua này?']
    Dialog -->|Hủy| S05
    Dialog -->|Xóa| Snack[06 + snackbar 'Đã xóa · Hoàn tác']
    Snack -->|Hoàn tác trong 5 giây| Restored([Khoản mua được khôi phục])
    Snack -->|Hết 5 giây| Gone([Đã xóa khỏi lịch sử])
```

## 4. Bảng ánh xạ flow → màn hình

| Màn hình | Flow 1 | Flow 2 | Flow 3 |
|---|:-:|:-:|:-:|
| 01 Onboarding | ✓ (lần đầu) | | |
| 02 Home Dashboard | ✓ bắt đầu, kết thúc | ✓ bắt đầu | |
| 03 Add Purchase | ✓ bước 1, nhánh lỗi | ✓ từ trạng thái trống | |
| 04 Purchase Reason | ✓ bước 2 | | |
| 05 Purchase Detail | | | ✓ sửa, xóa |
| 06 Purchase History | | | ✓ bắt đầu, kết thúc |
| 07 Buying Patterns | | ✓ loading, lỗi, trống | |
| 08 Personal Insights | | ✓ | |
| 09 Monthly Reflection | | ✓ | |
| 10 Profile & Settings | | ✓ bật nhắc | |
