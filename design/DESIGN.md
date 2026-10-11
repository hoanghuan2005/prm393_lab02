# DESIGN.md — Design brief cho Google Stitch

## Sản phẩm
Why I Buy? — ứng dụng di động giúp người trẻ ghi nhanh khoản mua và gắn động cơ
tâm lý, lấy cảm hứng từ "The Psychology of Money" (Morgan Housel).
Thông điệp: "Hiểu trước khi thay đổi".

## Người dùng
Nguyễn Hải Nam, 22 tuổi, sinh viên năm cuối ngành CNTT kiêm thực tập sinh,
thu nhập 6–9 triệu/tháng. Hay đặt đồ ăn khuya và chốt flash sale sau 23h,
dùng điện thoại một tay, cận 2 độ. Đã bỏ các app chi tiêu vì nhập lâu và
cảm giác tội lỗi khi thấy cảnh báo đỏ.

## Nền tảng
Android, khung 360 × 800 dp, Material Design 3, light theme.

## Tone & giọng văn
- Bình tĩnh, ấm áp, trung lập, không phán xét.
- Không cảnh báo đỏ, không "vượt ngân sách", không chấm điểm người dùng.
- Insight viết dạng quan sát: "42% khoản mua tháng này gắn với Khuyến mãi".
- Toàn bộ chữ trên giao diện bằng tiếng Việt, tiền tệ VND (45.000 ₫).

## Màu
| Token | Giá trị | Dùng cho |
|---|---|---|
| primary | #2E4A9E | Nút chính, tab được chọn |
| on-primary | #FFFFFF | Chữ trên nút chính |
| primary-container | #E3E8F7 | Nền phần tử được chọn |
| background | #F5F6F2 | Nền màn hình |
| surface | #FFFFFF | Card, ô nhập |
| on-surface | #1A2320 | Chữ chính |
| on-surface-variant | #545E59 | Chữ phụ |
| outline | #8A918A | Viền ô nhập, chip |
| error | #B3261E | Lỗi nhập liệu, hành động xóa |

Màu động cơ (nền / chữ):
| Động cơ | Nền | Chữ |
|---|---|---|
| Nhu cầu | #E3EEE8 | #1F4D3A |
| Mong muốn | #F3E6F3 | #5E2A5E |
| Khuyến mãi | #FFF3C4 | #6B5200 |
| Ảnh hưởng MXH | #E1EEF8 | #154466 |
| Quảng cáo | #EDE7F8 | #3F2C78 |
| Cảm xúc | #FBEBDC | #7A3A05 |
| Tiện lợi | #E2F1F1 | #135656 |
| Khác | #ECEEE8 | #3E4743 |

## Typography (Be Vietnam Pro)
| Style | Cỡ / dòng (sp) | Độ đậm |
|---|---|---|
| Display | 28 / 36 | 700 |
| Title | 20 / 28 | 600 |
| Subtitle | 16 / 24 | 600 |
| Body | 16 / 24 | 400 |
| Body small | 14 / 20 | 400 |
| Label | 12 / 16 | 500 (chỉ cho nhãn phụ, không dùng cho nội dung) |

## Khoảng cách, bo góc, elevation
- Spacing: 4 · 8 · 12 · 16 · 24 · 32 dp; lề màn hình 16 dp.
- Bo góc: 8 (nhỏ) · 12 (ô nhập, thẻ động cơ) · 16 (card) · 24 (dialog) · full (nút, chip).
- Elevation: 1 = bóng nhẹ cho card · 2 = dialog, snackbar.

## Quy tắc component
- Mỗi màn hình chỉ có **một** nút chính (filled, primary), đặt ở nửa dưới màn hình
  vì Nam thao tác một tay.
- Vùng chạm tối thiểu 48 × 48 dp; chữ nội dung tối thiểu 14 sp.
- Độ tương phản chữ tối thiểu 4.5:1 (Nam cận và hay dùng trong phòng tối).
- Động cơ luôn hiển thị **icon + tên**, không chỉ dùng màu.
- Biểu đồ luôn có nhãn chữ và phần trăm.
- Thanh điều hướng dưới 5 tab: Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân.
  Tab được chọn có nền pill + chữ đậm, không chỉ đổi màu.
- Lỗi nhập liệu hiển thị ngay dưới ô nhập, kèm icon và cách sửa.
- Hành động xóa luôn có dialog xác nhận và snackbar hoàn tác 5 giây.
- Mỗi màn hình có dữ liệu cần thiết kế đủ trạng thái: loading, trống, lỗi.

## Danh sách màn hình
01 Onboarding · 02 Home Dashboard · 03 Add Purchase · 04 Purchase Reason ·
05 Purchase Detail · 06 Purchase History · 07 Buying Patterns ·
08 Personal Insights · 09 Monthly Reflection · 10 Profile & Settings
