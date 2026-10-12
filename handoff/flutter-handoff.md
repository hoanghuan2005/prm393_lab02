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

> Flow 6 không thêm token. Các token Flow 6 dùng: `color/primary` #2E4A9E, `color/primary-container` #E3E8F7, `color/surface` #FFFFFF, `color/surface-container` #E8F0EB, `color/on-surface` #1A2320, `color/on-surface-variant` #545E59, `color/outline` #8A918A, `color/error` #B3261E, 8 cặp `motive/*`, spacing 4/8/12/16, radius 16 (card) và full (chip), text style Subtitle 16/600, Body Small 14/400, Label 14/500, Caption 12/500, Elevation/1.

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
| **Wishlist item card** (Status: Đang cân nhắc / Đã mua / Bỏ qua × State: Default / Pressed) | `Card` + `InkWell` → `WishlistItemCard` | Flutter Material 3 | `padding: 16`, `borderRadius: 16`, `elevation: 1`; Pressed = `overlayColor` surface-container #E8F0EB; tên `maxLines: 2, overflow: TextOverflow.ellipsis`; ghi chú `maxLines: 2`; `Wrap(spacing: 8)` cho chip |
| **Wishlist status chip** | `Container` + `Row(Icon, Text)` bọc `Semantics(label: 'Trạng thái: …')` | Flutter Material 3 | cao 24, `StadiumBorder`; Bỏ qua có `Border.all(outline)` |
| **Wishlist entry** (Trang chủ) | `Card` + `ListTile` | Flutter Material 3 | `minVerticalPadding` đủ 64 dp; `leading` CircleAvatar 40 (primaryContainer); `trailing: Icon(Icons.chevron_right)` |
| **Bộ lọc trạng thái** | `Wrap(spacing: 8, runSpacing: 8)` chứa 3 `FilterChip` | Flutter Material 3 | `showCheckmark: true`; nhãn kèm số lượng |
| **Dialog bỏ qua** | `AlertDialog` qua `showDialog` | Flutter Material 3 | Nút "Hủy" `TextButton`, "Bỏ qua" `FilledButton` (màu primary, không phải error) |
| **Snackbar hoàn tác** | `SnackBar` + `SnackBarAction('Hoàn tác')` | Flutter Material 3 | `duration: Duration(seconds: 5)`, `behavior: SnackBarBehavior.floating` |
| **Giá dự kiến** | `TextFormField` | `intl` | `keyboardType: TextInputType.number`, `FilteringTextInputFormatter.digitsOnly` + formatter `NumberFormat('#,###', 'vi_VN')` → "650.000", hậu tố " ₫" |

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

---

### Flow 6 — Mô hình dữ liệu và điều hướng

```dart
enum WishlistStatus { pending, purchased, skipped } // Đang cân nhắc / Đã mua / Bỏ qua

class WishlistItem {
  final String id;
  final String name;            // bắt buộc, trim() khác rỗng, tối đa 60 ký tự
  final int? estimatedPrice;    // VND, null = chưa biết; nếu có thì > 0
  final Motive motive;          // 1 trong 8 động cơ hiện có (dùng lại enum Motive)
  final String? note;           // tối đa 200 ký tự
  final DateTime createdAt;
  final WishlistStatus status;
  final String? linkedPurchaseId; // gán khi khoản mua lưu thành công
}
```

Routes: `/wishlist` (11), `/wishlist/add` (12), `/wishlist/:id` (13), `/wishlist/:id/edit` (12c).
Mua từ món: `Navigator.pushNamed('/add-purchase', arguments: PurchaseDraft(name, amount: estimatedPrice, motive, fromWishlistId: id))`. Chỉ khi route trả về `Purchase` đã lưu mới gọi `markPurchased(id, purchase.id)`. Pop trả về `null` thì không đổi gì.

Lưu `WishlistItem` không được ghi vào bảng `purchases`, không đổi tổng tuần và biểu đồ Mô hình.

---

### Màn hình: 11. Wishlist Overview

1. **Layout:** `Scaffold` → `AppBar` (Back, "Danh sách mong muốn") → `body: CustomScrollView` padding ngang 16, khoảng cách khối 12: thẻ Intro → `Wrap` 3 `FilterChip` → `SliverList` các `WishlistItemCard` (gap 12). `bottomNavigationBar`: `Padding(8, 16)` chứa `FilledButton.icon(+ "Thêm món")` cao 56. Không có `NavigationBar` (màn lồng).
2. **Components:** App bar/Nested, Filter chip (Default/Selected), Wishlist item card (3 status), Motive chip, Wishlist status chip, Empty / Error state (Filter empty), Snackbar, Button/Primary/Large.
3. **States:** populated (11) · empty toàn bộ (11a: icon bookmark, "Bạn chưa có món nào đang cân nhắc.", nút "Thêm món" trong empty state, ẩn nút đáy) · bộ lọc trống (11a: icon archive, "Chưa có món nào trong danh mục này.", nút tonal "Xem đang cân nhắc") · đã lưu (11b) · đã bỏ qua (11c) · sau hoàn tác (11d) · đã mua (11e). Loading: dùng `Skeleton` 2 thẻ như màn 06 (chưa vẽ khung riêng trong Figma).
4. **Interactions:** chạm chip → đổi bộ lọc, giữ vị trí cuộn về đầu; chạm thẻ → 13 (món Bỏ qua → 13c, món Đã mua → 13d); "Thêm món" → 12; "Hoàn tác" (11c) → status về pending, cùng `id`, không tạo bản mới.
5. **Navigation:** đến từ 02 (Wishlist entry); Back → 02; sau khi lưu ở 12 quay về 11 với bộ lọc "Đang cân nhắc"; sau khi mua ở 04 quay về 11 với bộ lọc "Đã mua".
6. **Constraints:** thẻ có trạng thái Pressed khi chạm giữ; chip ≥ 48 dp, wrap khi thiếu chỗ; số trên chip luôn bằng số thẻ; tên món tối đa 2 dòng rồi "…"; snackbar nằm trên nút đáy (bottom offset 72 + 8). ≥ 600 dp: danh sách thành lưới 2 cột, nội dung tối đa 840 dp, căn giữa.

---

### Màn hình: 12. Add Wishlist Item (và 12c Sửa)

1. **Layout:** `Scaffold(resizeToAvoidBottomInset: true)` → `AppBar` (Back, "Thêm món mong muốn" / "Sửa món mong muốn") → `Form` trong `SingleChildScrollView` padding 16, gap 12: `Card` (Tên món, Giá dự kiến) → câu hỏi (Subtitle + Body Small) → `GridView.count(crossAxisCount: 2, shrinkWrap: true)` 8 thẻ động cơ (giống 04) → TextFormField ghi chú (maxLines 3) → `bottomNavigationBar` nút "Lưu món" / "Lưu thay đổi".
2. **Components:** App bar/Nested, Text field (Default/Focused/Error), Motive grid / Motive card (Default/Selected), Button/Primary/Large (Default/Loading).
3. **States:** trống (12) · lỗi (12a) · đã điền (12b) · sửa (12c, điền sẵn dữ liệu món) · đang lưu: nút ở trạng thái Loading.
4. **Interactions & validation (chạy khi bấm Lưu):** tên `trim().isEmpty` → "Vui lòng nhập tên món đồ để lưu."; giá có nhập và ≤ 0 → "Vui lòng nhập số tiền lớn hơn 0."; chưa chọn động cơ → "Vui lòng chọn lý do bạn muốn mua món này." (hiện dưới câu hỏi, màu error, icon cảnh báo). Cuộn tới và focus trường lỗi đầu tiên. Lỗi tự mất khi trường được sửa. Nhập giá `650000` → hiển thị `650.000 ₫`. Chỉ chọn được 1 động cơ.
5. **Navigation:** từ 11 ("Thêm món") hoặc 13 (icon Sửa); lưu hợp lệ → `pop` về 11 + SnackBar "Đã lưu món vào danh sách mong muốn." (12c → về 13 + "Đã cập nhật “<tên>”"); Back khi đã nhập dữ liệu → dialog "Bỏ thay đổi?" (đề xuất, chưa vẽ trong Figma).
6. **Constraints:** nút đáy luôn trên bàn phím; tên tối đa 60 ký tự, ghi chú 200; thẻ động cơ ≥ 72 dp cao; không có trường ảnh, URL hay người bán. ≥ 600 dp: form tối đa 600 dp, căn giữa; lưới động cơ 4 cột.

---

### Màn hình: 13. Wishlist Detail

1. **Layout:** `Scaffold` → `AppBar` (Back, "Chi tiết món mong muốn", `IconButton(Icons.edit)` có `tooltip: 'Sửa món'`) → `SingleChildScrollView` padding 16, gap 12: `Card` tóm tắt (overline, tên Title, giá Display màu primary, caption "Giá dự kiến · chưa tính vào chi tiêu", chip trạng thái, khối "Lý do muốn mua" + chip động cơ) → `Card` chi tiết (ngày thêm, ghi chú dạng trích dẫn) → `bottomNavigationBar`: `Column(FilledButton "Ghi khoản mua", TextButton.icon "Không mua nữa")`.
2. **Components:** App bar/Nested (icon Sửa), Motive chip, Wishlist status chip, Button/Primary/Large, Button/Text/Medium, Dialog, Snackbar.
3. **States:** đang cân nhắc (13) · dialog xác nhận (13a) · sau khi sửa (13b) · đã bỏ qua (13c: chỉ một nút "Đưa về Đang cân nhắc" → status pending, về 11 + snackbar "Đã đưa “<tên>” về Đang cân nhắc") · đã mua (13d: chỉ xem, ẩn `bottomNavigationBar` và icon Sửa).
4. **Interactions:** "Ghi khoản mua" → 03 điền sẵn; "Không mua nữa" → `showDialog`: "Hủy" đóng dialog, "Bỏ qua" → status skipped, về 11 (bộ lọc Bỏ qua) + SnackBar 5 giây có "Hoàn tác"; icon Sửa → 12c.
5. **Navigation:** từ 11; Back → 11 (món vẫn pending = "tiếp tục cân nhắc"); từ 03/04 Back khi chưa lưu → quay lại 13, không đổi status.
6. **Constraints:** không khóa nút theo thời gian, không đếm ngược; icon Sửa 48 × 48; tên dài xuống dòng, giá không xuống dòng. ≥ 600 dp: nội dung tối đa 600 dp; 2 nút đáy nằm ngang.

---

### Thay đổi ở màn có sẵn
- **02 Trang chủ:** chèn `WishlistEntry` ngay dưới Tổng quan tuần, chỉ hiện khi có ≥ 1 món; subtitle "n món đang cân nhắc". Không thêm tab.
- **03/04 Ghi khoản mua:** nhận `PurchaseDraft`. Có `fromWishlistId` thì: 03 hiện banner primary-container "Điền sẵn từ Danh sách mong muốn: “<tên>”…", số tiền và tên điền sẵn (sửa được); 04 chọn sẵn động cơ cũ, câu phụ "Lúc thêm vào danh sách, bạn chọn <động cơ>. Đổi nếu lý do bây giờ đã khác."
