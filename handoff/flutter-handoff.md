# Developer Handoff Guide for Flutter

**Project:** Why I Buy? – The Psychology of Money  
**Course:** PRM393 / PRM323 – Mobile UI/UX Design with AI  
**Deliverable:** Token-to-Flutter Mapping, Component Mapping & 6-Part Screen Specs  

---

## 1. Bảng ánh xạ Design Tokens sang Flutter (Token Mapping Table)

Lập trình viên Flutter triển khai hệ thống token thông qua các class tiện ích hằng số (`const`) và Theme Extension trong Flutter:

```dart
// lib/core/theme/app_colors.dart
// lib/core/theme/app_typography.dart
// lib/core/theme/app_spacing.dart
// lib/core/theme/app_radius.dart
```

### 1.1. Color Tokens Mapping

| Design Token | Figma Hex | Flutter Code Snippet | Mục đích sử dụng |
| :--- | :--- | :--- | :--- |
| `color-primary-500` | `#2D6A4F` | `const Color(0xFF2D6A4F)` | Màu thương hiệu chính, nút CTA, active tint |
| `color-primary-100` | `#D8F3DC` | `const Color(0xFFD8F3DC)` | Nền thẻ/chip được chọn, highlight nhẹ |
| `color-secondary-500`| `#DDA15E` | `const Color(0xFFDDA15E)` | Màu hổ phách ấm, thẻ Insight, icon bóng đèn |
| `color-background` | `#F8F9FA` | `const Color(0xFFF8F9FA)` | `ThemeData.scaffoldBackgroundColor` |
| `color-surface` | `#FFFFFF` | `const Color(0xFFFFFFFF)` | `ThemeData.cardColor`, Modal background |
| `color-surface-variant`| `#EDF2F4` | `const Color(0xFFEDF2F4)` | Nền ô Input, Shimmer loading base color |
| `color-text-primary` | `#1A202C` | `const Color(0xFF1A202C)` | Văn bản tiêu đề chính, giá tiền hiển thị |
| `color-text-secondary`| `#4A5568` | `const Color(0xFF4A5568)` | Văn bản mô tả, phụ đề, nhãn trạng thái |
| `color-text-tertiary` | `#718096` | `const Color(0xFF718096)` | Placeholder input, metadata phụ |
| `color-semantic-success`| `#38B000` | `const Color(0xFF38B000)` | Thông báo thành công, badge tích cực |
| `color-semantic-warning`| `#E07A5F` | `const Color(0xFFE07A5F)` | Màu đất nung cảnh báo chi tiêu cảm xúc |
| `color-semantic-error`| `#C53030` | `const Color(0xFFC53030)` | Thông báo lỗi xác thực form, mất mạng |

---

### 1.2. Typography Tokens Mapping

Sử dụng Google Fonts `PlusJakartaSans` qua package `google_fonts`:

| Design Token | Kích thước | Trọng số (Weight) | Chiều cao dòng | Flutter TextStyle |
| :--- | :---: | :---: | :---: | :--- |
| `font-display-lg` | 32 sp | Bold (w700) | 40 dp | `GoogleFonts.plusJakartaSans(fontSize: 32, fontWeight: FontWeight.w700, height: 1.25)` |
| `font-heading-md` | 24 sp | Bold (w700) | 32 dp | `GoogleFonts.plusJakartaSans(fontSize: 24, fontWeight: FontWeight.w700, height: 1.33)` |
| `font-heading-sm` | 20 sp | SemiBold (w600) | 28 dp | `GoogleFonts.plusJakartaSans(fontSize: 20, fontWeight: FontWeight.w600, height: 1.40)` |
| `font-title` | 16 sp | SemiBold (w600) | 24 dp | `GoogleFonts.plusJakartaSans(fontSize: 16, fontWeight: FontWeight.w600, height: 1.50)` |
| `font-body-md` | 15 sp | Regular (w400) | 22 dp | `GoogleFonts.plusJakartaSans(fontSize: 15, fontWeight: FontWeight.w400, height: 1.46)` |
| `font-body-sm` | 14 sp | Regular (w400) | 20 dp | `GoogleFonts.plusJakartaSans(fontSize: 14, fontWeight: FontWeight.w400, height: 1.42)` |
| `font-caption` | 12 sp | Medium (w500) | 16 dp | `GoogleFonts.plusJakartaSans(fontSize: 12, fontWeight: FontWeight.w500, height: 1.33)` |

---

### 1.3. Spacing & Radius Tokens Mapping

```dart
class AppSpacing {
  static const double space4 = 4.0;
  static const double space8 = 8.0;
  static const double space12 = 12.0;
  static const double space16 = 16.0;
  static const double space24 = 24.0;
  static const double space32 = 32.0;
  static const double space48 = 48.0;
}

class AppRadius {
  static const BorderRadius sm = BorderRadius.all(Radius.circular(8.0));
  static const BorderRadius md = BorderRadius.all(Radius.circular(12.0));
  static const BorderRadius lg = BorderRadius.all(Radius.circular(16.0));
  static const BorderRadius xl = BorderRadius.all(Radius.circular(24.0));
  static const BorderRadius full = BorderRadius.all(Radius.circular(999.0));
}
```

---

## 2. Bảng ánh xạ Components sang Flutter Widgets (Component Mapping Table)

| Figma Component | Flutter Widget Đề Xuất | Gói hỗ trợ (Package) | Thuộc tính & Cấu hình then chốt |
| :--- | :--- | :--- | :--- |
| **Primary Button** | `ElevatedButton` | Flutter Material 3 | `minimumSize: Size.fromHeight(52)`, `backgroundColor: AppColors.primary500`, `shape: RoundedRectangleBorder(borderRadius: AppRadius.xl)` |
| **Secondary Button** | `OutlinedButton` | Flutter Material 3 | `side: BorderSide(color: AppColors.primary500, width: 1.5)`, `shape: RoundedRectangleBorder(borderRadius: AppRadius.xl)` |
| **Input Text Field** | `TextFormField` | Flutter Material 3 | `decoration: InputDecoration(filled: true, fillColor: AppColors.surfaceVariant, border: OutlineInputBorder(borderRadius: AppRadius.md))` |
| **Purchase Card** | `Card` / `InkWell` | Flutter Material 3 | `elevation: 1`, `shape: RoundedRectangleBorder(borderRadius: AppRadius.lg)`, `padding: EdgeInsets.all(16)` |
| **Reason Chip Card** | Custom `StatefulWidget` / `FilterChip` | Flutter Material 3 | Dùng `InkWell` bọc `Container` có `BoxDecoration(color: isSelected ? AppColors.primary100 : AppColors.surface, border: Border.all(...))` |
| **Bottom Navigation** | `NavigationBar` | Flutter Material 3 | 5 `NavigationDestination(icon, selectedIcon, label)`, `indicatorColor: AppColors.primary100` |
| **Top App Bar** | `AppBar` / `SliverAppBar` | Flutter Material 3 | `elevation: 0`, `scrolledUnderElevation: 2`, `backgroundColor: AppColors.background` |
| **Confirmation Dialog** | `AlertDialog` | Flutter Material 3 | `showDialog()` bọc trong modal barrier mờ `Colors.black54` |
| **Bottom Modal Sheet** | `showModalBottomSheet()` | Flutter Material 3 | `shape: RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(24)))`, `isScrollControlled: true` |
| **Loading State** | `Shimmer.fromColors` | `shimmer: ^3.0.0` | `baseColor: AppColors.surfaceVariant`, `highlightColor: Colors.white` |
| **Analytics Charts** | `PieChart` / `BarChart` | `fl_chart: ^0.68.0` | Donut chart có `sectionsSpace: 2`, `centerSpaceRadius: 48` |

---

## 3. Đặc tả kỹ thuật chi tiết theo 6 phần cho mỗi màn hình (Screen Implementation Specs)

Dưới đây là đặc tả chuẩn xác 6 phần cho các màn hình chủ chốt của dự án:

---

### Màn hình 1: 02. Home Dashboard Screen

1. **Layout Structure:**
   * Sử dụng `Scaffold` với `CustomScrollView` hoặc `SingleChildScrollView`.
   * Thứ tự các khối từ trên xuống:
     * Khối Lời chào & Trích dẫn tâm lý (`Padding: 16dp`).
     * Khối Hero Card "Mindset Breakdown" (`Margin: 16dp`, tỷ lệ chiều ngang 100%).
     * Khối Nút Primary CTA "Ghi khoản mua" (`Padding: 16dp`).
     * Khối Tiêu đề Section "Góc nhìn gần đây" kèm danh sách `ListView.builder` (shrinkWrap: true, physics: NeverScrollableScrollPhysics).
   * Đáy màn hình: Ghim `NavigationBar` 5 tabs.
2. **Components Used:**
   * `AppBar`, `HeroMindsetCard`, `PrimaryCTAButton`, `PurchaseItemCard`, `NavigationBar`.
3. **States Matrix:**
   * `Loading State:` Hiển thị skeleton shimmer cho thẻ Hero và 3 item card.
   * `Empty State:` Khi user chưa có dữ liệu tuần này → Hiển thị `EmptyDashboardWidget` với illustration ấm áp và nút "Ghi khoản mua đầu tiên".
   * `Populated State:` Đầy đủ thông số tỷ lệ % lý do và danh sách 3 giao dịch mới nhất.
   * `Error State:` Banner nhỏ thông báo lỗi tải dữ liệu kèm nút "Thử lại".
4. **Interactions & Micro-animations:**
   * Kéo xuống để tải lại (`RefreshIndicator`).
   * Chạm vào nút CTA: Hiển thị hiệu ứng nhấn nhẹ (`ScaleTransition` 0.98 trong 100ms) rồi mở modal Add Purchase.
   * Chạm vào một Purchase Card: Chuyển hướng sang màn hình chi tiết `05. Purchase Detail`.
5. **Navigation Paths:**
   * Chạm FAB / CTA Button → `Navigator.pushNamed(context, '/add-purchase')`.
   * Chạm Tab Bottom Bar → Thay đổi `currentIndex` chuyển tab tương ứng (`/history`, `/patterns`, `/insights`, `/profile`).
   * Chạm "Xem tất cả" → Chuyển sang Tab History.
6. **UI Constraints & Responsiveness:**
   * Thiết bị 360dp: Padding ngang 16dp, tên món hàng dùng `TextOverflow.ellipsis` nếu dài quá 18 ký tự.
   * Thiết bị 412dp: Tăng padding ngang lên 20dp, bố cục Hero Card giữ khoảng cách lề thoáng.

---

### Màn hình 2: 03. Add Purchase Screen (Step 1) & 04. Reason Screen (Step 2)

1. **Layout Structure:**
   * Màn hình mở dưới dạng Full-screen Modal (`PageRouteBuilder` trượt từ dưới lên).
   * Bọc trong `Scaffold` với `SafeArea` và `SingleChildScrollView`.
   * Phần trên: Top bar có nút đóng 'X' và thanh tiến trình `LinearProgressIndicator` (giá trị 0.5 cho bước 1, 1.0 cho bước 2).
   * Phần thân (Bước 1): Trường số tiền cỡ lớn (32sp), hàng chip gợi ý số tiền nhanh, ô nhập tên món hàng và danh mục.
   * Phần thân (Bước 2): Header câu hỏi tâm lý và `GridView.count(crossAxisCount: 2)` chứa 8 thẻ lý do.
   * Phần đáy: Cố định `Container` chứa nút CTA bằng `bottomNavigationBar`.
2. **Components Used:**
   * `CloseIconButton`, `CurrencyInputField`, `QuickAmountChip`, `ItemNameTextField`, `ReasonCardGridItem`, `StickyActionButton`.
3. **States Matrix:**
   * `Default/Initial State:` Số tiền 0 ₫, nút CTA disabled (`onPressed: null`).
   * `Validating/Error State:` Bấm tiếp tục khi số tiền = 0 → Kích hoạt `FormState.validate()`, hiển thị inline error đỏ dưới chân input, rung nhẹ thiết bị (`HapticFeedback.lightImpact()`).
   * `Selected State (Bước 2):` Thẻ lý do được chọn cập nhật biến `selectedReasonId`, viền chuyển sang xanh Sage.
4. **Interactions & Micro-animations:**
   * Bàn phím số tự động hiển thị khi mở Bước 1 (`autofocus: true` trên Amount Field).
   * Chạm vào chip nhanh (+20k): Số tiền tăng tương ứng kèm hiệu ứng đổi số mượt mà.
   * Chuyển từ Bước 1 sang Bước 2: Hiệu ứng slide ngang `PageController.animateToPage(1, duration: 250ms)`.
5. **Navigation Paths:**
   * Bấm nút 'X' → Hiện Dialog xác nhận hủy bản nháp nếu đã nhập dữ liệu, hoặc đóng modal (`Navigator.pop()`).
   * Bước 2 bấm "Lưu giao dịch" → Gửi event lưu dữ liệu, đóng modal và bắn `SnackBar` thành công ở màn hình Home.
6. **UI Constraints & Responsiveness:**
   * Tự động né bàn phím ảo bằng `resizeToAvoidBottomInset: true`.
   * Chiều cao lưới Reason Cards dùng `childAspectRatio: 1.1` để tránh tràn viền chiều dọc trên màn hình ngắn 360×640 dp.

---

### Màn hình 3: 07. Buying Patterns & 08. Personal Insights Screen

1. **Layout Structure:**
   * Sử dụng `Scaffold` với `AppBar` hiển thị tháng hiện tại và nút lọc thời gian.
   * Phần thân cuộn `SingleChildScrollView`:
     * Khối Biểu đồ Donut thể hiện 8 lý do mua sắm (`AspectRatio: 1.3`).
     * Khối Chú giải màu sắc và tỷ lệ phần trăm tương ứng (`Wrap` spacing 8dp).
     * Khối Biểu đồ thời gian (Khung giờ mua sắm bốc đồng).
     * Danh sách các Thẻ Insight thông minh (`InsightCard`).
2. **Components Used:**
   * `fl_chart: PieChart`, `LegendChip`, `BarChart`, `InsightCard`, `ExpansionTile`.
3. **States Matrix:**
   * `Loading State:` Shimmer tròn giả lập Donut Chart và các thẻ xám chữ nhật.
   * `Insufficient Data State:` Hiển thị widget hướng dẫn ghi chép tối thiểu 5 giao dịch để thuật toán kích hoạt.
   * `Populated State:` Đồ họa vector mượt mà kèm chú giải số liệu chi tiết.
4. **Interactions & Micro-animations:**
   * Chạm vào từng phần của biểu đồ Donut: Phần được chạm bung to ra 6dp (`radius: touchedIndex == i ? 56 : 48`), đồng thời cập nhật dòng text chú thích trung tâm.
   * Chạm vào thẻ Insight: Mở rộng để xem hướng dẫn thực hành chi tiết.
5. **Navigation Paths:**
   * Chạm nút "Mở báo cáo Monthly Reflection" → Điều hướng sang màn hình `09. Monthly Reflection`.
   * Chuyển tab qua lại giữa Patterns và Insights trên Bottom Navigation.
6. **UI Constraints & Responsiveness:**
   * Kích thước bán kính biểu đồ Donut tính toán động theo bề rộng: `MediaQuery.of(context).size.width * 0.28`.
   * Đảm bảo không bị lỗi chữ chồng chéo khi người dùng bật chế độ chữ to trên hệ thống (Accessibility Font Scale 1.3x).
