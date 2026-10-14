# Flutter Handoff — Why I Buy?

**Project:** Why I Buy? – lấy cảm hứng từ "The Psychology of Money"
**Course:** PRM323 – Lab 2
**Nguồn chuẩn:** token trong [`design/DESIGN.md`](../design/DESIGN.md) và page `04 Design System` của Figma; component ở page `05 Components`; màn hình ở page `03 Final UI`. Ảnh từng khung nằm trong [`assets/figma/`](../assets/figma/). Nếu tài liệu này và Figma khác nhau, lấy Figma.

Cách đọc: phần 1–2 là hai bảng chung (token → Flutter, component → widget). Phần 3 là cấu trúc app và điều hướng. Phần 4 đặc tả từng màn theo 6 mục: Layout · Components · States · Interactions · Navigation · Constraints. Phần 5 là nhãn TalkBack, phần 6 là hành vi màn rộng. **Phần 7 liệt kê các thay đổi đã quyết sau phản biện bằng AI (PB-x); khi dựng, phần 7 ghi đè phần 4.** Phần 8 là ghi chú cho các màn bổ sung theo checklist.design/mobile (Splash, xin quyền thông báo, tài khoản).

---

## 1. Token → Flutter

Font: **Be Vietnam Pro** qua `google_fonts` (`GoogleFonts.beVietnamProTextTheme()`). Theme: Material 3, chỉ light theme.

```dart
// lib/core/theme/app_theme.dart
final theme = ThemeData(
  useMaterial3: true,
  colorScheme: appColorScheme,
  scaffoldBackgroundColor: AppColors.background,
  textTheme: appTextTheme,
  extensions: const [MotiveColors.light],
);
```

### 1.1. Màu → `ColorScheme` / hằng số

| Token (Figma variable) | Hex | Flutter | Dùng cho |
|---|---|---|---|
| `color/primary` | `#2E4A9E` | `colorScheme.primary` | Nút chính, tab được chọn, số tiền ở Chi tiết, link "Xem tất cả" |
| `color/on-primary` | `#FFFFFF` | `colorScheme.onPrimary` | Chữ / icon trên nút chính |
| `color/primary-container` | `#E3E8F7` | `colorScheme.primaryContainer` | Nền thẻ động cơ đang chọn, chip ngày, nền pill tab, banner "Điền sẵn…" |
| (chữ trên primary-container) | `#2E4A9E` | `colorScheme.onPrimaryContainer` | Chữ chip ngày, chữ thẻ được chọn |
| `color/background` | `#F5F6F2` | `AppColors.background` → `scaffoldBackgroundColor` | Nền mọi màn |
| `color/surface` | `#FFFFFF` | `colorScheme.surface` | Card, dialog, bottom sheet, thanh điều hướng |
| `color/surface-container` | `#E8F0EB` | `colorScheme.surfaceContainer` | Nền ô nhập (tonal), chip mặc định, khối "Động cơ chính", thẻ tổng quan chu kỳ, skeleton |
| `color/on-surface` | `#1A2320` | `colorScheme.onSurface` | Chữ chính |
| `color/on-surface-variant` | `#545E59` | `colorScheme.onSurfaceVariant` | Chữ phụ, placeholder, nhãn tab chưa chọn |
| `color/outline` | `#8A918A` | `colorScheme.outline` | Viền chip "Bỏ qua", viền switch tắt, vạch chia (chỉ viền, không dùng cho chữ) |
| `color/error` | `#B3261E` | `colorScheme.error` | Chữ / viền lỗi, "Bắt buộc", nút Xóa, mục "Xóa toàn bộ dữ liệu" |
| `color/error-container` | `#F9DEDC` | `colorScheme.errorContainer` | Nền ô nhập khi lỗi, nền tròn icon trong dialog xóa và màn lỗi |
| (snackbar) | `#1A2320` / `#FFFFFF` | `colorScheme.inverseSurface` / `onInverseSurface` | Nền và chữ snackbar |
| (scrim) | đen 32 % | `ModalBarrier` mặc định M3 | Nền mờ sau dialog và bottom sheet |

**Màu động cơ** — `ThemeExtension<MotiveColors>`, mỗi động cơ một cặp nền / chữ (chữ cũng là màu của thanh % ở Mô hình và đoạn màu trong thanh xếp chồng ở Trang chủ, Chiêm nghiệm):

| Động cơ (`Motive`) | Nền | Chữ / thanh | Icon (Figma `motive/*`) | Material tương đương |
|---|---|---|---|---|
| `need` – Nhu cầu | `#E3EEE8` | `#1F4D3A` | `motive/nhu-cau` (khiên) | `Icons.shield_outlined` |
| `want` – Mong muốn | `#F3E6F3` | `#5E2A5E` | `motive/mong-muon` (lấp lánh) | `Icons.auto_awesome_outlined` |
| `promo` – Khuyến mãi | `#FFF3C4` | `#6B5200` | `motive/khuyen-mai` (nhãn giá) | `Icons.sell_outlined` |
| `social` – Ảnh hưởng MXH | `#E1EEF8` | `#154466` | `motive/anh-huong-mxh` (nhóm người) | `Icons.group_outlined` |
| `ads` – Quảng cáo | `#EDE7F8` | `#3F2C78` | `motive/quang-cao` (loa) | `Icons.campaign_outlined` |
| `emotion` – Cảm xúc | `#FBEBDC` | `#7A3A05` | `motive/cam-xuc` (tim) | `Icons.favorite_border` |
| `convenience` – Tiện lợi | `#E2F1F1` | `#135656` | `motive/tien-loi` (tia sét) | `Icons.bolt` |
| `other` – Khác | `#ECEEE8` | `#3E4743` | `motive/khac` (ba chấm) | `Icons.more_horiz` |

Thứ tự `Motive.values` phải đúng như bảng (lưới 2 × 4 và danh sách ở Mô hình dùng thứ tự này khi số lượng bằng nhau). Ưu tiên export SVG từ page `05 Components › Icons` và dùng `flutter_svg`; bảng Material chỉ là phương án dự phòng.

### 1.2. Typography → `TextTheme`

| Style Figma | Cỡ / dòng (sp) | Độ đậm | Flutter | Dùng cho |
|---|---|---|---|---|
| Display | 28 / 36 | w700 | `textTheme.headlineMedium` | Số tiền lớn, "Why I Buy?", tiêu đề Đăng nhập / Đăng ký |
| Title | 20 / 28 | w600 | `textTheme.titleLarge` (ghi đè cỡ 20) | Tiêu đề app bar, tên khoản ở Chi tiết |
| Subtitle | 16 / 24 | w600 | `textTheme.titleMedium` | Tiêu đề nhóm, tên khoản trong danh sách, số tiền trong dòng |
| Body | 16 / 24 | w400 | `textTheme.bodyLarge` | Nội dung chính, câu quan sát ở Góc nhìn |
| Body Small | 14 / 20 | w400 | `textTheme.bodyMedium` | Mô tả phụ, dòng lỗi |
| Label | 14 / 20 | w500 | `textTheme.labelLarge` | Chip, nút chữ, nhãn ô nhập |
| Overline | 14 / 20 | w500, viết hoa | `AppTextStyles.overline` | "TỔNG QUAN TUẦN", "BƯỚC 2/2", "MỤC ĐÃ CHI TIÊU" |
| Caption | 12 / 16 | w500 | `textTheme.labelMedium` | Nhãn tab chưa chọn, mốc giờ |
| Caption Strong | 12 / 16 | w700 | `AppTextStyles.captionStrong` | Nhãn tab đang chọn |

Quy tắc: chữ nội dung ≥ 14 sp; 12 sp chỉ cho nhãn tab và mốc giờ. Không khóa `textScaler`; bố cục phải chịu được cỡ chữ hệ thống 1.3×.

### 1.3. Khoảng cách, bo góc, elevation, kích thước

```dart
abstract class AppSpacing { // dp
  static const xs = 4.0, sm = 8.0, md = 12.0, lg = 16.0, xl = 24.0, xxl = 32.0;
  static const screen = 16.0;   // lề trái/phải mọi màn
  static const blockGap = 12.0; // khoảng cách giữa các card
}
abstract class AppRadius {
  static const sm = 8.0, field = 12.0, card = 16.0, dialog = 24.0, full = 999.0;
}
abstract class AppSize {
  static const buttonLarge = 56.0, buttonMedium = 48.0, minTouch = 48.0;
  static const appBar = 64.0, navBar = 80.0, motiveCard = Size(156, 72);
  static const icon = 24.0, avatar = 40.0, rowLeading = 48.0;
}
```

| Token | Giá trị | Flutter |
|---|---|---|
| `elevation/1` | bóng nhẹ cho card | `Card(elevation: 1, shadowColor: Colors.black26)` |
| `elevation/2` | dialog, snackbar, bottom sheet | `elevation: 2` (dialog, sheet), `SnackBar(elevation: 2)` |
| `radius/card` 16 | card, thẻ món | `RoundedRectangleBorder(borderRadius: BorderRadius.circular(16))` |
| `radius/field` 12 | ô nhập, thẻ động cơ | `OutlineInputBorder(borderRadius: …12)` |
| `radius/dialog` 24 | dialog, góc trên bottom sheet | `AlertDialog(shape: …24)` |
| `radius/full` | nút, chip, pill tab, segmented | `StadiumBorder()` |

---

## 2. Component → Widget

| Component Figma (variant) | Widget Flutter | Cấu hình chính |
|---|---|---|
| **Button** — Style: Primary / Tonal / Danger / Text · Size: Large 56 / Medium 48 · State: Default / Pressed / Disabled / Loading | `FilledButton` (Primary), `FilledButton.tonal` (Tonal), `FilledButton` với `backgroundColor: error` (Danger), `TextButton` (Text) | `minimumSize: Size.fromHeight(56)` hoặc 48; `StadiumBorder`; icon 20 trước chữ. **Loading:** giữ nền primary đầy đủ, `CircularProgressIndicator(strokeWidth: 2)` 20 dp + "Đang lưu…", bọc `AbsorbPointer`. **Disabled:** `onPressed: null` (M3 mặc định) |
| **Filter chip** — Default / Selected | `FilterChip(showCheckmark: true)` | Cao 48; nhãn kèm số "Khuyến mãi (2)"; Selected nền primary, chữ on-primary; Default nền surface-container |
| **Motive chip** (8 động cơ) | `MotiveChip` = `Container(StadiumBorder)` + `Row(Icon 16, Text Label)` | Màu theo `MotiveColors`; bọc `Semantics(label: 'Động cơ: Khuyến mãi')` |
| **Text field** — Default / Focused / Error (+ Filled, Disabled: dùng M3 mặc định) | `TextFormField` | `filled: true, fillColor: surfaceContainer`, không viền ở Default; Focused viền primary 2; Error viền error 2 + `fillColor: errorContainer` + `errorText` có icon `error_outline`; prefix icon 24 |
| **Amount input** — Default / Error | `AmountField` (TextFormField số) | Display 28/36 w700, hậu tố "₫", `IconButton(Icons.close, tooltip: 'Xóa số tiền đã nhập')`; nhãn "Số tiền thực chi" + "Bắt buộc" (error); 3 `ActionChip` "+20.000 ₫ / +50.000 ₫ / +100.000 ₫" cao 48 |
| **Switch** — On / Off | `Switch` | `thumbIcon` dấu tích khi bật; vùng chạm 52 × 48 |
| **Segmented control** — Tuần / Tháng | `SegmentedButton<PeriodType>` | Pill nền surface-container, segment chọn nền surface + chữ primary đậm |
| **Period switcher** | `PeriodSwitcher` = `Row(IconButton chevron_left, InkWell pill, IconButton chevron_right)` | Pill 224 × 52: icon lịch + dòng 1 (Label đậm: "Tuần này · 05/10 – 11/10") + dòng 2 (Body Small: "6 khoản · 862.000 ₫") + `expand_more`; mũi tên phải disabled khi đang ở kỳ hiện tại |
| **Motive card / Motive grid** — Default / Selected / Disabled | `GridView.count(crossAxisCount: 2, childAspectRatio: 156/72, mainAxisSpacing: 12, crossAxisSpacing: 12)` + `Card` + `InkWell` | Icon tròn 48 + tên (Label). Selected: nền primary-container, viền primary 2, icon tròn nền primary, dấu tích góc phải trên |
| **Purchase row** | `PurchaseRow` = `InkWell` + `Row` | Leading tròn 48 nền màu động cơ + icon; giữa: tên (Subtitle, tối đa 2 dòng) + `MotiveChip` + giờ (Caption); phải: số tiền (Subtitle, không xuống dòng). Pressed: `overlayColor` surface-container |
| **Weekly summary card** — Normal / Saved / Empty | `WeeklySummaryCard` (Card) | Overline "TỔNG QUAN TUẦN" + chip ngày; tổng (Display); 2 dòng phụ; khối "Động cơ chính" với thanh xếp chồng `Row(Expanded(flex: count))` cao 8 |
| **Skeleton** — Line / Block / Circle | `SkeletonBox` (Container surface-container, bo góc) + `AnimatedOpacity` 0.4 ↔ 1, 1 s | Giữ đúng bố cục màn có dữ liệu để không nhảy layout |
| **Empty / Error state** — Empty / Filter empty / Error / Insufficient | `StateMessage(icon, title, body, action)` | Icon trong tròn 96 (Error: nền error-container, icon error); tiêu đề Subtitle; mô tả Body Small căn giữa; một nút (Tonal hoặc Primary Medium) |
| **Rating scale** — 1–5 | `Row` 5 `ChoiceChip` tròn 48 | Chọn: nền primary, chữ on-primary; nhãn hai đầu "Không hài lòng" / "Rất hài lòng" |
| **App bar** — Tab (logo + avatar) / Nested (Back + action) | `AppBar` | Cao 64, nền background, `scrolledUnderElevation: 0`; tab gốc: leading logo tròn 40 (primary-container), action avatar tròn 40 nền primary; màn lồng: `BackButton` + action (help / delete / edit) 48 × 48 |
| **Navigation bar** — 5 variant, mỗi tab một trạng thái chọn | `NavigationBar` | Cao 80, 5 `NavigationDestination` (Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân); `indicatorShape: StadiumBorder`, `indicatorColor: primaryContainer`; nhãn chọn Caption Strong |
| **Snackbar** — Saved / Deleted / Offline / Exported | `SnackBar(behavior: floating)` | Icon trái (check_circle / delete / cloud_off / archive), chữ Body Small tối đa 2 dòng, `SnackBarAction('Hoàn tác')` khi có thể hoàn tác, `duration: 5s`; nổi trên nút đáy |
| **Dialog** — Destructive (Xóa) | `AlertDialog` qua `showDialog` | Icon tròn 48 nền error-container; tiêu đề Title; nội dung Body Small; `TextButton('Hủy')` + `FilledButton.icon` màu error |
| Dialog xác nhận không phá hủy (Bỏ qua món) | `AlertDialog` | Như trên nhưng icon và nút xác nhận màu primary |
| **Insight card** | `InsightCard` (Card) | Ô icon 48 bo 12 nền màu động cơ; câu quan sát (Body); chip loại ("Động cơ", "Khung giờ", "Cảm xúc") nền surface-container |
| **Bottom sheets** — Month picker / Motive guide | `showModalBottomSheet(isScrollControlled: true, showDragHandle: true)` | Góc trên 24; Month picker: lưới 4 × 3 ô tháng 48 dp, chọn năm `<` `>`, nút "Xem tháng 9/2026"; Motive guide: danh sách 8 động cơ + mô tả 1 dòng |
| **Wishlist item card** — Status × Pressed | `WishlistItemCard` (Card + InkWell) | Tên (Subtitle, 2 dòng) + giá; `Wrap(spacing: 8)` chip động cơ + chip trạng thái; ghi chú 2 dòng; ngày (Caption) |
| **Wishlist status chip** | `Container` + `Row(Icon, Text)` | Cao 24, `StadiumBorder`; Đang cân nhắc: bookmark, nền primary-container; Đã mua: check_circle, nền surface-container; Bỏ qua: archive, viền outline |
| **Wishlist entry** (Trang chủ) | `Card` + `ListTile` | Cao 64; leading tròn 40 primary-container + bookmark; trailing `chevron_right` |
| **Before You Buy entry** (Trang chủ) | `Card` + `FilledButton.tonal` | Tiêu đề "Trước khi mua", mô tả, dòng "Hiểu trước khi thay đổi.", nút Tonal Medium cao 48 "Trước khi mua"; không cạnh tranh với nút chính "Ghi khoản mua" |
| **AI analysis state** | `AiAnalysisState` = `Column` (tiêu đề, mô tả, dòng ngữ cảnh, khối `SkeletonBox`, dòng trạng thái) | Bọc `Semantics(liveRegion: true)`; dùng cho 08a (2 khung) và 17; tự chuyển sang màn kết quả khi có dữ liệu (prototype: 1,5 giây) |
| **AI pattern card** | `Card` + danh sách `ListTile` động cơ + `TextButton` | Mỗi dòng: icon động cơ + tên + số đếm ("5/15"); `TextButton` "Xem mô hình của tôi" → 08b. Dùng ở 08 Góc nhìn (có AI) |
| **Step header** | `Column(Text overline, Text Title)` | Overline "BƯỚC n/3" (`AppTextStyles.overline`) + tiêu đề Title; dùng ở 14, 15, 16 |

---

## 3. Cấu trúc app và điều hướng

### 3.1. Mô hình dữ liệu

```dart
enum Motive { need, want, promo, social, ads, emotion, convenience, other }

class Purchase {
  final String id;
  final int amount;              // VND, > 0, tối đa 999.999.999
  final String name;             // trim() khác rỗng, tối đa 60 ký tự
  final Motive motive;           // đúng 1 động cơ
  final String? note;            // tối đa 200 ký tự
  final DateTime occurredAt;     // thời điểm mua, không ở tương lai
  final SyncStatus syncStatus;   // synced | pendingUpload (lưu khi mất mạng)
}

class MonthlyReflection { final String month; final int rating; final String? goal; } // rating 1–5, goal ≤ 200
```

Khung giờ dùng chung cho Mô hình và Góc nhìn: Sáng 05–11h · Trưa 11–14h · Chiều 14–18h · Tối 18–05h. Mô hình cần ≥ 5 khoản trong kỳ, nếu ít hơn thì hiện trạng thái "Chưa đủ dữ liệu".

### 3.2. Route

| Route | Màn | Kiểu |
|---|---|---|
| `/onboarding` | 01 Onboarding | gốc, chỉ lần đầu |
| `/login`, `/register` | Đăng nhập, Đăng ký | gốc, thay thế (`pushReplacement`) |
| `/home`, `/history`, `/patterns`, `/insights`, `/profile` | 02, 06, 07, 08, 10 | 5 tab trong `StatefulShellRoute` (go_router) hoặc `IndexedStack`, giữ trạng thái từng tab |
| `/purchase/new` → `/purchase/new/reason` | 03 → 04 | push trên root navigator (ẩn thanh điều hướng) |
| `/purchase/:id` | 05 Chi tiết | push trên root navigator |
| `/purchase/:id/edit` → `/purchase/:id/edit/reason` | 03 / 04 Sửa | push |
| `/reflection/:yyyy-MM` | 09 Chiêm nghiệm tháng | push |
| `/wishlist`, `/wishlist/add`, `/wishlist/:id`, `/wishlist/:id/edit` | 11, 12, 13, 12c | push |
| `/splash` | 00 Splash | gốc, thay thế bằng màn đích *(đề xuất)* |
| `/forgot-password` | Quên mật khẩu | push từ Đăng nhập *(đề xuất)* |
| `/home` | 00 Trang chủ tổng hợp (Hub) | tab 1; Hub là phiên bản hiện tại của 02, dùng chung route `/home` *(đề xuất)* |
| `/notifications/permission` | 05a Xin quyền thông báo | push trên root navigator *(đề xuất)* |
| `/profile/account` → `/profile/account/password` | 10a Tài khoản → 10b Đổi mật khẩu | push trên root navigator *(đề xuất)* |
| `/purchase/:id/saved` | 05 Khoản mua đã lưu | `pushReplacement` từ 04 *(đề xuất)* |
| `/purchase/:id/ai` | 08c Nhận định AI về khoản vừa lưu (Flow 8) | push *(đề xuất)* |
| `/insights/ai/:purchaseId` | 08c Nhận định AI về khoản mua (Flow 10) | push *(đề xuất)* |
| `/patterns/ai` | 08b Chi tiết mô hình mua sắm | push *(đề xuất)* |
| `/before-buy/item` → `/before-buy/questions` → `/before-buy/discount` → `/before-buy/result` | 14 → 15 → 16 → 18 | push; bỏ qua `/before-buy/discount` khi câu 2 ở 15 không chọn Khuyến mãi *(đề xuất)* |

- **Màn lồng** (03, 04, 05, 05 Khoản mua đã lưu, 08b, 08c, 09, 10a, 10b, 11, 12, 13, 14, 15, 16, 18) không có thanh điều hướng, có nút Back ở app bar. 05a cũng ẩn thanh điều hướng (mục 8.3).
- **Back hệ thống** ở màn lồng = nút Back trên app bar. Ở tab khác Trang chủ, Back → về tab Trang chủ; ở Trang chủ, Back → thoát app.
- Avatar trên app bar của 4 tab Trang chủ, Lịch sử, Mô hình, Góc nhìn → chuyển sang tab Cá nhân (không push).
- Snackbar sau khi lưu / xóa hiện ở **màn đích** (dùng `ScaffoldMessenger` gốc), nổi phía trên nút đáy.

---

## 4. Đặc tả từng màn (6 mục)

### 00 Splash (`/splash`, đề xuất) — Flow 7
1. **Layout:** splash gốc của Android (mục 8.4), tiếp nối bằng `Scaffold(backgroundColor: colorScheme.primary)` → `Center` → `Column(mainAxisSize: min)`: App icon + wordmark "Why I Buy?". Không app bar, không thanh điều hướng, không cuộn.
2. **Components:** App icon.
3. **States:** chỉ một trạng thái (khung `00 Splash`, node 366:4923).
4. **Interactions:** không có phần tử bấm được. Trong lúc hiện splash: đọc phiên đăng nhập và cờ `onboardingDone`.
5. **Navigation:** đã đăng nhập → `go('/home')` (00 Hub); chưa đăng nhập, lần đầu → `/onboarding`; chưa đăng nhập, đã xem onboarding → `/login`. Prototype: sau 0,8 giây chuyển Dissolve 300 ms sang 01 Onboarding.
6. **Constraints:** chỉ giữ trong lúc kiểm tra phiên (mục tiêu ≤ 0,8 giây, mục 8.4); không xin quyền ở màn này (quyền thông báo hỏi ở 05a); nền #2E4A9E trùng màu nền của splash gốc để không bị nháy.

### Đăng nhập (`/login`) — Flow 7
1. **Layout:** `Scaffold` → `SafeArea` → `SingleChildScrollView` padding 16: hàng "← Quay lại" (TextButton.icon) → logo 40 + "Why I Buy?" (Subtitle) → gap 24 → "Chào bạn trở lại" (Display) → mô tả (Body Small, on-surface-variant) → gap 24 → `Form`: nhãn "Email" + TextFormField → gap 16 → "Mật khẩu" + TextFormField → "Quên mật khẩu?" căn phải (TextButton) → gap 16 → nút Primary Large "Đăng nhập" → "Chưa có tài khoản? Đăng ký" căn giữa → `Spacer` → thẻ primary-container (icon bóng đèn, "Hiểu mình, không phán xét", "Mỗi khoản mua là một dịp để lắng nghe chính bạn."). Cả màn cuộn khi bàn phím mở.
2. **Components:** Button/Text (Quay lại, Quên mật khẩu, Đăng ký), Text field/Default–Focused–Error, Button/Primary/Large (Default, Loading).
3. **States:** mặc định (khung `Đăng nhập`); đang đăng nhập: nút Loading; lỗi nhập liệu và lỗi sai thông tin: Text field/Error — *chưa có khung riêng trong Figma, dùng component Text field/Error*.
4. **Interactions:** Email: `keyboardType: emailAddress`, `textInputAction: next`; Mật khẩu: `obscureText: true`, `textInputAction: done` → gửi form. Validation khi bấm "Đăng nhập": email trống → "Vui lòng nhập email."; sai định dạng → "Email chưa đúng định dạng."; mật khẩu trống → "Vui lòng nhập mật khẩu."; máy chủ từ chối → lỗi dưới ô mật khẩu "Email hoặc mật khẩu chưa đúng." Lỗi hiện dưới ô, mất khi sửa.
5. **Navigation:** đến từ 01 Onboarding ("Bắt đầu") hoặc từ Đăng ký ("Đăng nhập"). Đăng nhập thành công → `go('/home')` (xóa stack). "Đăng ký" → `/register`. "Quay lại" / Back → 01 Onboarding.
6. **Constraints:** nút và link ≥ 48 dp; email tối đa 254 ký tự; không lưu mật khẩu dạng chữ thường; bàn phím không che nút (cuộn). ≥ 600 dp: form tối đa 400 dp, căn giữa.

### Đăng ký (`/register`) — Flow 7
1. **Layout:** như Đăng nhập; tiêu đề "Tạo tài khoản", mô tả "Bắt đầu hành trình hiểu thói quen mua sắm của bạn, theo cách nhẹ nhàng."; 4 ô: Họ tên ("Tên bạn muốn được gọi"), Email, Mật khẩu ("Tạo mật khẩu"), Xác nhận mật khẩu ("Nhập lại mật khẩu") + helper "Mật khẩu có ít nhất 8 ký tự." → nút Primary Large "Tạo tài khoản" → "Đã có tài khoản? Đăng nhập".
2. **Components:** Text field, Button/Primary/Large, Button/Text.
3. **States:** mặc định; đang tạo (nút Loading); lỗi từng ô (Text field/Error — chưa có khung riêng).
4. **Interactions:** validation khi bấm "Tạo tài khoản": họ tên trống → "Vui lòng nhập tên bạn muốn được gọi." (tối đa 40 ký tự); email như Đăng nhập; mật khẩu < 8 ký tự → "Mật khẩu cần ít nhất 8 ký tự."; xác nhận khác mật khẩu → "Mật khẩu nhập lại chưa khớp."; email đã tồn tại → "Email này đã có tài khoản. Hãy đăng nhập."
5. **Navigation:** đến từ Đăng nhập. Tạo thành công → quay về Đăng nhập (đúng như prototype Flow 7). "Đăng nhập" / Back → Đăng nhập.
6. **Constraints:** như Đăng nhập; `autofillHints` cho email / mật khẩu mới. ≥ 600 dp: form tối đa 400 dp.

### Quên mật khẩu (`/forgot-password`, đề xuất) — Flow 7
1. **Layout:** như Đăng nhập: `Scaffold` → `SafeArea` → `SingleChildScrollView` padding 16: TextButton.icon "Quay lại" → wordmark "Why I Buy?" → "Quên mật khẩu" (Display) → mô tả "Nhập email bạn dùng để đăng ký. Chúng mình sẽ gửi liên kết để bạn đặt lại mật khẩu." (Body Small, on-surface-variant) → nhãn "Email" + TextFormField (hint "Nhập email của bạn") → nút Primary Large "Gửi liên kết đặt lại" → TextButton "Quay lại Đăng nhập" → `Spacer` → thẻ "Hiểu mình, không phán xét" / "Mỗi khoản mua là một dịp để lắng nghe chính bạn." (giống Đăng nhập).
2. **Components:** Button/Text (Quay lại, Quay lại Đăng nhập), Text field/Default–Focused, Button/Primary/Large.
3. **States:** mặc định (khung `Quên mật khẩu`, node 320:8025); Focused khi chạm ô Email. *(Đề xuất, chưa có khung trong Figma)*: lỗi email dùng cùng mẫu với `Đăng nhập – lỗi`; đang gửi: nút Loading; đã gửi: snackbar "Đã gửi liên kết tới email của bạn".
4. **Interactions:** ô Email theo mục 8.1 (`AutofillHints.email`, `keyboardType: emailAddress`), `textInputAction: done` → gửi form. Validation *(đề xuất)*: email trống → "Vui lòng nhập email."; sai định dạng → "Email chưa đúng định dạng." (giống Đăng nhập).
5. **Navigation:** đến từ "Quên mật khẩu?" ở Đăng nhập. "Quay lại", "Quay lại Đăng nhập", Back → Đăng nhập. "Gửi liên kết đặt lại" → Đăng nhập (đúng như prototype).
6. **Constraints:** nút và link ≥ 48 dp; email tối đa 254 ký tự; bàn phím không che nút (cuộn). ≥ 600 dp: form tối đa 400 dp, căn giữa.

### 01 Onboarding (`/onboarding`) — Flow 1, Flow 7
1. **Layout:** `Scaffold` → `SafeArea` → `Column` padding 16: `Spacer` → icon app trong tròn 112 (primary-container) → gap 24 → overline "NHẬT KÝ ĐỘNG CƠ MUA SẮM" (primary) → "Why I Buy?" (Display) → mô tả 3 dòng (Body, on-surface-variant) → gap 24 → Card trắng gồm 3 dòng (icon tròn 40 + Body): ghi số tiền / xem theo tuần, tháng / đọc quan sát → `Spacer` → nút Primary Large "→ Bắt đầu" → caption "Dữ liệu được lưu trên máy của bạn." Không app bar, không thanh điều hướng, không cuộn ở 360 × 800.
2. **Components:** Button/Primary/Large, Card.
3. **States:** chỉ một trạng thái.
4. **Interactions:** chạm "Bắt đầu" → đánh dấu `onboardingDone = true`.
5. **Navigation:** chỉ hiện lần đầu mở app. "Bắt đầu" → Đăng nhập. Back hệ thống → thoát app.
6. **Constraints:** nếu chiều cao < 700 dp thì cho `SingleChildScrollView`; mô tả không cắt chữ. ≥ 600 dp: nội dung tối đa 480 dp, căn giữa.

### 00 Trang chủ tổng hợp – Hub (`/home`) — Flow 1, 6, 7, 8, 9
1. **Layout:** như 02 Trang chủ (mục dưới): `Scaffold` → `AppBar` (tab: logo, "Trang chủ", avatar) → `CustomScrollView` padding 16, gap 12: "Chào bạn," → `WeeklySummaryCard` ("TỔNG QUAN TUẦN", chip "Hôm nay, 11/10", "817.000 ₫", "Tuần này: 5 khoản · 817.000 ₫", "Nhiều nhất: Khuyến mãi (2/5)", "Động cơ chính · 40% do Khuyến mãi") → `WishlistEntry` ("Danh sách mong muốn" / "2 món đang cân nhắc") → `BeforeYouBuyEntry` ("Trước khi mua", "Dừng lại một chút. Vài câu hỏi nhanh giúp bạn hiểu điều gì đứng sau một lần mua.", "Hiểu trước khi thay đổi.", `FilledButton.tonal` "Trước khi mua") → hàng "Khoản mua gần đây" + badge 3 + "Xem tất cả ›" → Card 3 `PurchaseRow` (Cơm tấm · Tiện lợi · Hôm nay 12:15 · 40.000 ₫ / Tai nghe Bluetooth · Khuyến mãi · Hôm qua 23:40 · 389.000 ₫ / Sách “Tâm lý học về tiền” · Mong muốn · 08/10 20:05 · 159.000 ₫). `bottomNavigationBar`: nút Primary Large "Ghi khoản mua" + `NavigationBar` (Trang chủ).
2. **Components:** App bar/Tab, Weekly summary card, Wishlist entry, Before You Buy entry, Button/Tonal/Medium, Button/Primary/Large, Purchase row, Motive chip, Navigation bar/Trang chủ.
3. **States:** có dữ liệu (khung `00 Trang chủ tổng hợp (Hub)`, node 320:8064); chưa ghi hôm nay (`00 Trang chủ (Hub) – chưa ghi hôm nay`, node 385:4946: "Hôm nay bạn chưa ghi khoản nào"). Trống, sau khi lưu, ngoại tuyến, loading lần đầu: dùng các trạng thái của 02 (`02a`–`02c`).
4. **Interactions:** `WishlistEntry` → 11; "Trước khi mua" → 14 Trước khi mua – Bước 1/3; "Xem tất cả" → tab Lịch sử; chạm `PurchaseRow` → 05 Chi tiết khoản mua của đúng khoản đó; "Ghi khoản mua" → 03; avatar → tab Cá nhân; "Hoàn tác" và kéo để làm mới như 02.
5. **Navigation:** tab gốc. Đến từ Splash (đã đăng nhập), Đăng nhập, "Đã hiểu" ở 08c (Flow 8), "Để mình nghĩ thêm" ở 18 (Flow 9). Back → thoát app.
6. **Constraints:** như 02. "Ghi khoản mua" là nút chính duy nhất; "Trước khi mua" dùng Tonal Medium 48 để không cạnh tranh; nội dung cuộn phía sau thanh đáy, nút luôn hiện.

### 02 Trang chủ (`/home`) — Flow 1, 2, 6
1. **Layout:** `Scaffold` → `AppBar` (tab: logo, "Trang chủ", avatar) → `CustomScrollView` padding 16, gap 12: "Chào bạn," (Subtitle) → `WeeklySummaryCard` → (`WishlistEntry` nếu có ≥ 1 món đang cân nhắc) → hàng tiêu đề "Khoản mua gần đây" + badge số + "Xem tất cả ›" → Card chứa tối đa 3 `PurchaseRow` (ngăn bằng `Divider`). `bottomNavigationBar`: `Column(Padding(16,8) FilledButton.icon "Ghi khoản mua" cao 56, NavigationBar)`. Nội dung cuộn phía sau, nút luôn hiện.
2. **Components:** App bar/Tab, Weekly summary card/Normal–Saved–Empty, Wishlist entry, Purchase row, Empty / Error state/Empty, Button/Primary/Large, Snackbar/Saved–Offline, Navigation bar/Trang chủ.
3. **States:** có dữ liệu (`02`, 817.000 ₫ · 5 khoản); trống (`02a`: thẻ tổng quan 0 ₫, chip "Tuần 41", "Chưa có dữ liệu", empty state "Chưa có khoản mua nào tuần này"); sau khi lưu (`02b`: 862.000 ₫ · 6 khoản, khoản mới ở đầu, snackbar "Đã lưu “Trà sữa nướng” · Hoàn tác"); ngoại tuyến (`02c`: snackbar "Đã lưu trên máy. Sẽ đồng bộ khi có mạng."); có lối vào danh sách mong muốn (`02d`). Loading lần đầu: Skeleton cho thẻ tổng quan và 3 dòng.
4. **Interactions:** chạm `PurchaseRow` → 05; "Xem tất cả" → tab Lịch sử; "Ghi khoản mua" → 03; `WishlistEntry` → 11; "Hoàn tác" trong 5 giây → xóa khoản vừa lưu, thẻ tổng quan về số cũ; kéo xuống để làm mới (`RefreshIndicator`).
5. **Navigation:** tab gốc. Đến từ Đăng nhập, từ 04 sau khi lưu (pop về đây + snackbar), từ tab bar. Back → thoát app.
6. **Constraints:** phần trăm "Động cơ chính" làm tròn số nguyên; tên món 2 dòng, không "…" trước 2 dòng; số tiền không xuống dòng; snackbar nằm trên nút đáy (offset 56 + 16). Nhãn đọc: avatar "Mở Cá nhân", tab "Trang chủ, tab 1 trên 5, đang chọn". ≥ 600 dp: `NavigationRail` thay `NavigationBar`, nút "Ghi khoản mua" thành `FloatingActionButton.extended`, thẻ tổng quan và danh sách gần đây nằm 2 cột khi ≥ 840 dp.

### 03 Ghi khoản mua – Bước 1/2 (`/purchase/new`) — Flow 1, 6
1. **Layout:** `Scaffold(resizeToAvoidBottomInset: true)` → `AppBar` (Back, "Ghi khoản mua") → `SingleChildScrollView` padding 16, gap 12: hàng tiến trình (2 chấm, chấm 1 dài) + chip "Bước 1/2: Thông tin khoản chi" → (banner "Điền sẵn từ Danh sách mong muốn…" khi đến từ 13) → Card 1: `AmountField` + 3 chip cộng nhanh → Card 2: "Tên món đồ hoặc dịch vụ" (TextFormField icon túi) + "Thời điểm chi tiêu" (ô chọn ngày giờ, 2 dòng + icon lịch). `bottomNavigationBar`: nút Primary Large "→ Tiếp tục" + caption "Bước tiếp theo: chọn động cơ của khoản mua".
2. **Components:** App bar/Nested, Amount input/Default–Error, Text field, Button/Primary/Large/Default–Disabled.
3. **States:** mặc định (`03`, 45.000 ₫, "Trà sữa nướng", Hôm nay 23:10); lỗi (`03a`: 0 ₫, ô nền error-container viền error, dòng "Vui lòng nhập số tiền lớn hơn 0 ₫", nút "Tiếp tục" Disabled); sửa (`03b`: tiêu đề "Sửa khoản mua", điền sẵn); điền sẵn từ danh sách mong muốn (`03c`).
4. **Interactions:** mở màn → `autofocus` ô số tiền, bàn phím số; nhập "45000" hiển thị "45.000"; chip "+20.000 ₫" cộng dồn; nút X xóa số về trống; số tiền ≤ 0 hoặc trống → hiện lỗi và khóa "Tiếp tục" (kiểm tra ngay khi rời ô hoặc khi bấm); tên món bắt buộc, tối đa 60 ký tự, lỗi "Vui lòng nhập tên món." (Figma chưa vẽ khung lỗi tên — dùng Text field/Error); chạm ô thời điểm → `showDatePicker` rồi `showTimePicker`, không cho chọn tương lai; "Tiếp tục" → 04 mang theo `PurchaseDraft`.
5. **Navigation:** từ 02 ("Ghi khoản mua"), 07 trạng thái chưa đủ dữ liệu, 13 ("Ghi khoản mua", điền sẵn), 05 ("Sửa"). Back → màn trước, **không** lưu nháp; nếu đã nhập dữ liệu thì hỏi "Bỏ khoản đang ghi?" (Hủy / Bỏ) — *đề xuất, chưa vẽ trong Figma*.
6. **Constraints:** nút đáy luôn trên bàn phím; số tiền tối đa 999.999.999 ₫; 3 chip cộng nhanh dùng `Wrap` để không tràn mép phải ở 360 dp; nhãn đọc nút X "Xóa số tiền đã nhập", icon lịch "Chọn ngày giờ khác". ≥ 600 dp: form tối đa 600 dp, căn giữa.

### 04 Ghi khoản mua – Bước 2/2 (`/purchase/new/reason`) — Flow 1, 6
1. **Layout:** `Scaffold` → `AppBar` (Back, "Ghi khoản mua", action `help_outline`) → `SingleChildScrollView` padding 16, gap 12: overline "BƯỚC 2/2" + "Nhận diện động cơ" (Title) + chấm tiến trình → khối tóm tắt surface-container ("KHOẢN CHI VỪA NHẬP — Trà sữa nướng · 45.000 ₫") → "Vì sao bạn mua?" (Subtitle) + "Chọn động cơ gần nhất với lúc bạn quyết định mua." → Motive grid 2 × 4 → "Ghi chú thêm (tùy chọn)" + TextFormField (`maxLines: 3`). `bottomNavigationBar`: nút Primary Large "✓ Lưu".
2. **Components:** App bar/Nested + action, Motive grid / Motive card/Default–Selected, Text field, Button/Primary/Large/Default–Loading, Bottom sheet/Motive guide.
3. **States:** chưa chọn (nút Lưu Disabled); đã chọn (`04`, Cảm xúc); đang lưu (`04a`: nút Loading "Đang lưu…", lưới không nhận chạm); giải thích động cơ (`04b`, bottom sheet); sửa (`04c`: "Sửa khoản mua", "KHOẢN CHI ĐANG SỬA", nút "Lưu thay đổi"); từ danh sách mong muốn (`04d`: động cơ chọn sẵn, câu phụ "Lúc thêm vào danh sách, bạn chọn Khuyến mãi. Đổi nếu lý do bây giờ đã khác.").
4. **Interactions:** chạm thẻ → chọn đúng 1 động cơ (chạm thẻ khác thì đổi); `help` → `showModalBottomSheet` 8 định nghĩa; ghi chú tối đa 200 ký tự; "Lưu" → ghi `Purchase`: thành công → pop về 02 + snackbar "Đã lưu “<tên>” · Hoàn tác" (5 s); mất mạng → vẫn lưu với `syncStatus: pendingUpload` + snackbar ngoại tuyến; lỗi ghi máy (hiếm) → snackbar "Chưa lưu được. Thử lại." và giữ nguyên dữ liệu.
5. **Navigation:** từ 03. Back → 03 giữ nguyên dữ liệu đã nhập. Sau khi lưu: về 02 (Flow 1), về 05 (sửa), về 11 bộ lọc Đã mua (Flow 6).
6. **Constraints:** cả lưới, ô ghi chú và nút Lưu nằm gọn trong 800 dp khi bàn phím đóng; tên động cơ dài ("Ảnh hưởng MXH") xuống 2 dòng trong thẻ; thẻ 156 × 72; nhãn đọc thẻ "Cảm xúc, đã chọn, 6 trên 8", nút help "Giải thích các động cơ". ≥ 600 dp: lưới 4 cột, nội dung tối đa 600 dp.

### 05 Chi tiết khoản mua (`/purchase/:id`) — Flow 3
1. **Layout:** `Scaffold` → `AppBar` (Back, "Chi tiết khoản mua", action thùng rác màu error) → `SingleChildScrollView` padding 16, gap 12: Card 1 (overline "MỤC ĐÃ CHI TIÊU" + icon hóa đơn, tên (Title), số tiền (Display, primary), khối surface-container "Động cơ" + `MotiveChip`) → Card 2 (dòng icon đồng hồ: "Thời gian ghi nhận", "Hôm qua 23:40", "Thứ Bảy, 10/10/2026"; dòng icon ghi chú: "Ghi chú của bạn" + khối trích dẫn). `bottomNavigationBar`: nút Primary Large "✎ Sửa".
2. **Components:** App bar/Nested (action delete), Motive chip, Card, Button/Primary/Large, Dialog/Destructive.
3. **States:** mặc định (`05`); dialog xóa (khung "05 Chi tiết khoản mua – dialog xóa"; không nhầm với màn 05a Xin quyền thông báo); không có ghi chú → ẩn dòng ghi chú; đang tải chi tiết → Skeleton 2 card.
4. **Interactions:** thùng rác → `showDialog` "Xóa khoản mua này?" / "“Tai nghe Bluetooth” sẽ bị xóa khỏi lịch sử. Bạn có 5 giây để hoàn tác." — "Hủy" đóng dialog; "Xóa" → xóa mềm, pop về màn trước + snackbar "Đã xóa “…” · Hoàn tác"; hết 5 giây mới xóa hẳn. "Sửa" → 03b.
5. **Navigation:** từ 02 (Gần đây) hoặc 06 (Lịch sử). Back → màn trước. Sau khi sửa → quay lại 05 + snackbar "Đã cập nhật “…”" (dùng Snackbar/Saved).
6. **Constraints:** thùng rác 48 × 48, nhãn đọc "Xóa khoản mua Tai nghe Bluetooth"; ghi chú dài xuống dòng không giới hạn; số tiền không xuống dòng. ≥ 840 dp: hiển thị ở khung phải của Lịch sử (list-detail).

### 05a Xin quyền thông báo (`/notifications/permission`, đề xuất) — Flow 1, 5
1. **Layout:** `Scaffold` → `SafeArea` → `Column` padding 16: icon trong vòng tròn → tiêu đề "Để Why I Buy? nhắc bạn mỗi tối?" (Display) → mô tả "Một lời nhắc lúc 21:00 giúp bạn ghi lại khoản mua trong ngày khi còn nhớ rõ lý do." → Card xem trước thông báo (App icon, "Why I Buy? · 21:00", "Hôm nay bạn có mua gì không? Ghi lại trong 10 giây.") → `Spacer` → khối hành động: nút Primary Large "Bật nhắc nhở" → TextButton "Để sau" → caption "Bạn có thể đổi giờ nhắc trong Cá nhân." Không có thanh điều hướng (mục 8.3).
2. **Components:** App icon, Card, Button/Primary/Large, Button/Text/Medium.
3. **States:** một khung (`05a Xin quyền thông báo`, node 366:4930). Sau khi bấm "Bật nhắc nhở", hộp thoại xin quyền là của hệ thống Android, không vẽ trong Figma.
4. **Interactions:** theo mục 8.5: "Bật nhắc nhở" → `Permission.notification.request()`; được cấp → hẹn nhắc 21:00 bằng `flutter_local_notifications`; "Để sau" hoặc bị từ chối → lưu `notificationDenied = true` (prototype dùng biến `thong-bao/da-tu-choi`). Nếu quyền đã bị từ chối vĩnh viễn thì `request()` không hiện hộp thoại nữa; khi đó "Bật nhắc nhở" gọi `openAppSettings()` như mục 8.5 *(đề xuất)*.
5. **Navigation:** đến sau lần lưu khoản mua đầu tiên (từ 05 Khoản mua đã lưu, Flow 1) hoặc từ nút Tonal "Mở cài đặt" trong thẻ "Thông báo đang tắt" ở `10 Cá nhân – chưa cấp quyền thông báo` (R4-2). Sau khi chọn: Flow 1 → 02 sau khi lưu; khi đến từ 10 → `pop` về 10 *(đề xuất)*.
6. **Constraints:** một màn chỉ xin một quyền; không hỏi lúc mở app; "Để sau" ≥ 48 dp và không chặn người dùng. Android 13+ cần `POST_NOTIFICATIONS` (mục 8.5); dưới Android 13 không cần hỏi quyền nên bỏ qua 05a *(đề xuất)*.

### 06 Lịch sử (`/history`) — Flow 3, 4
1. **Layout:** `Scaffold` → `AppBar` (tab: logo, "Lịch sử", avatar) → `CustomScrollView` padding 16, gap 12: `PeriodSwitcher` (mặc định "Tuần này") → hàng `FilterChip` cuộn ngang ("Tất cả (6)" + 8 động cơ có số lượng) → (banner primary-container "Xem mô hình động cơ tháng 9 ›" khi đang xem một tháng) → mỗi ngày một Card: tiêu đề ngày ("Hôm nay, 11/10/2026") + tổng ngày (primary) + các `PurchaseRow`. `NavigationBar` (Lịch sử).
2. **Components:** App bar/Tab, Period switcher, Filter chip, Purchase row, Empty / Error state/Filter empty, Snackbar/Deleted, Bottom sheet/Month picker, Navigation bar/Lịch sử.
3. **States:** có dữ liệu (`06`); bộ lọc trống (`06a`: "Chưa có khoản nào gắn Quảng cáo" + "Xóa bộ lọc"); sau khi xóa (`06b`: 5 khoản · 473.000 ₫ + snackbar Hoàn tác); chọn tháng (`06c`, bottom sheet); xem tháng 9/2026 (`06d`: 11 khoản · 1.254.000 ₫); đang tải: Skeleton 2 card.
4. **Interactions:** `<` `>` đổi kỳ trước / sau (`>` khóa ở kỳ hiện tại); chạm pill kỳ → bottom sheet chọn năm + tháng (tháng chưa có dữ liệu bị làm mờ, không chọn được) → "Xem tháng 9/2026"; chạm chip → lọc (chỉ 1 chip chọn); "Xóa bộ lọc" → về "Tất cả"; chạm dòng → 05; banner "Xem mô hình…" → tab Mô hình với cùng kỳ.
5. **Navigation:** tab gốc; từ "Xem tất cả" ở 02. Back → tab Trang chủ.
6. **Constraints:** hàng chip cuộn ngang cần mép mờ hoặc chip cuối hiện một phần để báo còn nội dung; chip cao 48; tổng ngày tính lại sau xóa / hoàn tác; nhãn đọc pill kỳ "Đang xem Tuần này, 05/10 đến 11/10, 6 khoản. Chạm hai lần để chọn tháng", mũi tên "Kỳ trước" / "Kỳ sau" (khi khóa: "Kỳ sau, không khả dụng"). ≥ 840 dp: list-detail (danh sách trái, 05 bên phải).

### 07 Mô hình (`/patterns`) — Flow 2, 4
1. **Layout:** `Scaffold` → `AppBar` (tab, "Mô hình") → `CustomScrollView` padding 16, gap 12: `SegmentedButton` Tuần / Tháng → `PeriodSwitcher` → thẻ surface-container "TỔNG QUAN CHU KỲ — Tháng 10/2026: 15 khoản — Động cơ của các khoản mua trong tháng" → hàng "Động cơ chi tiêu · 8 động cơ" → Card danh sách 8 dòng (icon + tên + "5 (33%)" + `LinearProgressIndicator` cao 8 màu động cơ) → "Khung giờ chi tiêu" + Card 4 cột (Sáng / Trưa / Chiều / Tối, mỗi cột có số khoản). `NavigationBar` (Mô hình).
2. **Components:** Segmented control, Period switcher, Skeleton, Empty / Error state/Error–Insufficient, Navigation bar/Mô hình.
3. **States:** đang tải (`07a`: pill ghi "Đang tải…", skeleton giữ khung); kết quả tháng (`07`); kết quả tuần (`07e`: "Tuần 41: 6 khoản"); tháng khác (`07d`); lỗi (`07b`: "Không tải được mô hình" + "Kiểm tra kết nối mạng rồi thử lại. Các khoản đã ghi vẫn được lưu trên máy." + "Thử lại"); chưa đủ dữ liệu (`07c`: "Bạn đã ghi 3 khoản. Ghi thêm 2 khoản để xem mô hình." + "Ghi khoản mua").
4. **Interactions:** đổi Tuần / Tháng hoặc kỳ → tải lại (hiện 07a rồi kết quả, chuyển cảnh `AnimatedSwitcher` 200 ms); "Thử lại" → tải lại; "Ghi khoản mua" → 03; sắp xếp động cơ theo số lượng giảm dần, bằng nhau thì theo thứ tự `Motive`.
5. **Navigation:** tab gốc; từ banner ở 06 (mang theo kỳ). Back → tab Trang chủ.
6. **Constraints:** phần trăm làm tròn để tổng = 100; động cơ 0 khoản vẫn hiện (chữ on-surface-variant); thanh % dùng tỉ lệ (không đặt độ rộng cố định); nhãn đọc thanh "Khuyến mãi: 5 khoản, 33 phần trăm", cột giờ "Tối, 18 giờ đến 5 giờ: 8 khoản, cao nhất". ≥ 840 dp: danh sách động cơ và khung giờ thành 2 cột.

### 08 Góc nhìn (`/insights`) — Flow 2
1. **Layout:** `Scaffold` → `AppBar` (tab, "Góc nhìn") → `CustomScrollView` padding 16, gap 12: overline "THÁNG 10/2026" + "Góc nhìn" (Title) + mô tả "Những quan sát trung tính, tổng hợp từ các khoản bạn đã ghi trong tháng." → thẻ surface-container "THÁNG 10 · NHÌN LẠI — 15 khoản đã ghi" → 3 `InsightCard`. `bottomNavigationBar`: nút Primary Large "Mở chiêm nghiệm tháng" + `NavigationBar` (Góc nhìn).
2. **Components:** Insight card, Button/Primary/Large, Snackbar, Navigation bar/Góc nhìn.
3. **States:** có dữ liệu (`08`); sau khi lưu chiêm nghiệm (`08a`: snackbar "Đã lưu chiêm nghiệm tháng 10"); chưa đủ dữ liệu (< 5 khoản): dùng Empty / Error state/Insufficient như 07c; đang tải: Skeleton 3 thẻ.
4. **Interactions:** thẻ chỉ để đọc (không bấm); "Mở chiêm nghiệm tháng" → 09 của tháng đang xem.
5. **Navigation:** tab gốc. Back → tab Trang chủ.
6. **Constraints:** câu quan sát chỉ dùng số đếm từ dữ liệu người dùng (vd "5 trong 15 khoản tháng này gắn với Khuyến mãi."), không khuyên bảo, không suy diễn tâm lý; tối đa 3 thẻ; chữ xuống dòng tự do. ≥ 840 dp: 3 thẻ thành lưới 2 cột.

### 09 Chiêm nghiệm tháng (`/reflection/:yyyy-MM`) — Flow 2
1. **Layout:** `Scaffold` → `AppBar` (Back, "Chiêm nghiệm tháng") → `SingleChildScrollView` padding 16, gap 12: Card tổng quan ("Tháng 10/2026: 15 khoản chi" + chip "Tổng quan", thanh xếp chồng, lưới chip 2 cột chấm màu + tên + số) → Card "Mức độ hài lòng của bạn" (câu hỏi + Rating scale 1–5 + nhãn hai đầu) → Card "⚑ Mục tiêu cho tháng 11" (TextFormField nhiều dòng, placeholder "Một điều bạn muốn để ý trong tháng 11"). `bottomNavigationBar`: nút Primary Large "✓ Lưu chiêm nghiệm" + TextButton "Để sau".
2. **Components:** App bar/Nested, Weekly summary bar (thanh xếp chồng), Rating scale, Text field, Button/Primary/Large, Button/Text.
3. **States:** chưa chấm điểm (nút Lưu Disabled); đã chọn mức; đang lưu (nút Loading); đã lưu → về 08a.
4. **Interactions:** chọn đúng 1 mức 1–5; mục tiêu tùy chọn, tối đa 200 ký tự; "Lưu chiêm nghiệm" → lưu `MonthlyReflection` → pop về 08 + snackbar; "Để sau" → pop về 08, không lưu.
5. **Navigation:** từ 08. Back = "Để sau".
6. **Constraints:** ô tròn 48 × 48, nhãn đọc "Mức 3 trên 5, chưa chọn"; nút đáy trên bàn phím; chỉ hiện động cơ có ≥ 1 khoản trong lưới chip. ≥ 600 dp: nội dung tối đa 600 dp.

### 10 Cá nhân (`/profile`) — Flow 5
1. **Layout:** `Scaffold` → `AppBar` (tab, "Cá nhân") → `ListView` padding 16, gap 12: Card "Bạn — Dữ liệu cá nhân trên máy này" → overline "CÀI ĐẶT NHẮC NHỞ" → Card 2 `SwitchListTile` ("Nhắc ghi khoản mua — … lúc 21:00 mỗi tối"; "Nhắc chiêm nghiệm hằng tháng — Ngày cuối tháng…") → overline "CÀI ĐẶT DỮ LIỆU" → Card 2 `ListTile` có chevron ("Xuất dữ liệu — … dưới dạng CSV"; "Xóa toàn bộ dữ liệu" chữ error) → ghi chú surface-container (icon khiên, "Dữ liệu được lưu trên máy và đồng bộ với tài khoản của bạn khi có mạng."). `NavigationBar` (Cá nhân).
2. **Components:** Switch, Card, Dialog/Destructive, Snackbar/Exported, Navigation bar/Cá nhân.
3. **States:** mặc định (`10`); xác nhận xóa toàn bộ (khung "10 Cá nhân – xác nhận xóa toàn bộ": "Xóa toàn bộ dữ liệu?" / "Mọi khoản mua và chiêm nghiệm đã lưu sẽ bị xóa vĩnh viễn khỏi máy và tài khoản. Không thể hoàn tác." / "Hủy" · "Xóa tất cả"); đã xuất (khung "10 Cá nhân – đã xuất dữ liệu": snackbar "Đã lưu “whyibuy-10-2026.csv” vào Tải xuống"). Mã 10a / 10b nay là màn Tài khoản / Đổi mật khẩu (xem mục 8).
4. **Interactions:** gạt switch → lưu ngay + đặt / hủy lịch thông báo (`flutter_local_notifications`); nếu chưa cấp quyền thông báo → mở 05a (xem mục 8.5); "Xuất dữ liệu" → tạo CSV (cột: ngày giờ, tên, số tiền, động cơ, ghi chú) vào Tải xuống; "Xóa toàn bộ dữ liệu" → dialog → "Xóa tất cả" xóa dữ liệu cục bộ và trên tài khoản, ở lại 10, các tab khác về trạng thái trống.
5. **Navigation:** tab gốc; từ avatar ở các tab khác. Back → tab Trang chủ.
6. **Constraints:** mỗi dòng cài đặt ≥ 56 dp; switch 52 × 48, nhãn đọc "Nhắc ghi khoản mua lúc 21 giờ, đang bật"; "Xóa toàn bộ" không có hoàn tác nên bắt buộc dialog. ≥ 600 dp: nội dung tối đa 600 dp.

### 10a Tài khoản (`/profile/account`, đề xuất) — Flow 7
1. **Layout:** `Scaffold` → `AppBar` (Back, "Tài khoản") → `ListView` padding 16, gap 12: Card 2 `ListTile` ("Email" · "minhanh@gmail.com", chỉ hiển thị; "Đổi mật khẩu" · "Cập nhật mật khẩu đăng nhập" + `chevron_right`) → khoảng trống → Card riêng ở cuối màn (nhóm nguy hiểm): `ListTile` icon thùng rác + "Xóa tài khoản" · "Xóa vĩnh viễn tài khoản và mọi khoản mua đã đồng bộ", chữ và icon màu error.
2. **Components:** App bar/Nested, Card, Dialog/Danger, Button/Text/Medium, Button/Danger/Medium, Snackbar/Saved.
3. **States:** mặc định (`10a Tài khoản`, node 359:4884); xác nhận xóa (`10a Tài khoản – xác nhận xóa`, node 359:5118: scrim 40% + dialog "Xóa tài khoản?" / "Tài khoản và toàn bộ khoản mua của bạn sẽ bị xóa vĩnh viễn, không thể khôi phục." / TextButton "Hủy" · nút Danger "Xóa tài khoản" bên phải); sau khi đổi mật khẩu (khung tên `10b Đổi mật khẩu – đã lưu`, node 359:5079: nội dung 10a + snackbar "Đã đổi mật khẩu").
4. **Interactions:** "Đổi mật khẩu" → 10b; "Xóa tài khoản" → `showDialog` (Danger): "Hủy" đóng dialog; "Xóa tài khoản" → xóa tài khoản và dữ liệu đã đồng bộ (mục 8.6). Dòng Email không bấm được.
5. **Navigation:** đến từ thẻ tài khoản ở 10 Cá nhân. Back → 10. Xóa tài khoản xong → `pushNamedAndRemoveUntil('/login')` (mục 8.6).
6. **Constraints:** mỗi dòng ≥ 56 dp; nhóm nguy hiểm tách riêng ở cuối màn; không có hoàn tác nên bắt buộc dialog; "Xóa tài khoản" khác "Xóa toàn bộ dữ liệu" ở 10 (chỉ xóa khoản mua, giữ tài khoản). ≥ 600 dp: nội dung tối đa 600 dp.

### 10b Đổi mật khẩu (`/profile/account/password`, đề xuất) — Flow 7
1. **Layout:** `Scaffold(resizeToAvoidBottomInset: true)` → `AppBar` (Back, "Đổi mật khẩu") → `Form` trong `SingleChildScrollView` padding 16: TextFormField "Mật khẩu hiện tại" (hint "Nhập mật khẩu đang dùng") → "Mật khẩu mới" → `PasswordStrength` → "Nhập lại mật khẩu mới". `bottomNavigationBar`: nút Primary Large "Lưu".
2. **Components:** App bar/Nested, Text field (ô mật khẩu có icon eye / eye-off), Password strength (Yếu / Trung bình / Mạnh), Button/Primary/Large (Default, Disabled).
3. **States:** đang nhập (`10b Đổi mật khẩu`, node 359:4996: độ mạnh "Độ mạnh: Trung bình · Thêm ký tự để mạnh hơn", nút "Lưu" Disabled); đã lưu (về 10a + snackbar "Đã đổi mật khẩu"). *(Đề xuất, chưa có khung trong Figma)*: đang lưu (nút Loading); lỗi "Mật khẩu hiện tại chưa đúng." dưới ô thứ nhất, "Mật khẩu nhập lại chưa khớp." dưới ô thứ ba.
4. **Interactions:** theo mục 8.1: bọc `AutofillGroup`; ô mới dùng `AutofillHints.newPassword`; `obscureText` bật / tắt bằng eye / eye-off; độ mạnh tính lại sau mỗi lần gõ; nút "Lưu" `onPressed: null` cho tới khi đủ 3 ô và ô mới trùng ô nhập lại. Mật khẩu mới tối thiểu 8 ký tự như Đăng ký *(đề xuất)*.
5. **Navigation:** đến từ 10a. Back → 10a. Lưu thành công → `Navigator.pop` về 10a + SnackBar "Đã đổi mật khẩu" (mục 8.1).
6. **Constraints:** nút đáy luôn trên bàn phím; nhãn độ mạnh luôn có chữ, không chỉ dựa vào màu; không hiện mật khẩu dạng chữ thường khi chưa bấm eye. ≥ 600 dp: form tối đa 400 dp, căn giữa.

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
Mua từ món: `Navigator.pushNamed('/purchase/new', arguments: PurchaseDraft(name, amount: estimatedPrice, motive, fromWishlistId: id))`. Chỉ khi route trả về `Purchase` đã lưu mới gọi `markPurchased(id, purchase.id)`. Pop trả về `null` thì không đổi gì.

Lưu `WishlistItem` không được ghi vào bảng `purchases`, không đổi tổng tuần và biểu đồ Mô hình.

### 11 Danh sách mong muốn (`/wishlist`) — Flow 6
1. **Layout:** `Scaffold` → `AppBar` (Back, "Danh sách mong muốn") → `body: CustomScrollView` padding ngang 16, khoảng cách khối 12: thẻ Intro → `Wrap` 3 `FilterChip` → `SliverList` các `WishlistItemCard` (gap 12). `bottomNavigationBar`: `Padding(8, 16)` chứa `FilledButton.icon(+ "Thêm món")` cao 56. Không có `NavigationBar` (màn lồng).
2. **Components:** App bar/Nested, Filter chip (Default/Selected), Wishlist item card (3 status), Motive chip, Wishlist status chip, Empty / Error state (Filter empty), Snackbar, Button/Primary/Large.
3. **States:** populated (11) · empty toàn bộ (11a: icon bookmark, "Bạn chưa có món nào đang cân nhắc.", nút "Thêm món" trong empty state, ẩn nút đáy) · bộ lọc trống (11a: icon archive, "Chưa có món nào trong danh mục này.", nút tonal "Xem đang cân nhắc") · đã lưu (11b) · đã bỏ qua (11c) · sau hoàn tác (11d) · đã mua (11e). Loading: dùng `Skeleton` 2 thẻ như màn 06 (chưa vẽ khung riêng trong Figma).
4. **Interactions:** chạm chip → đổi bộ lọc, giữ vị trí cuộn về đầu; chạm thẻ → 13 (món Bỏ qua → 13c, món Đã mua → 13d); "Thêm món" → 12; "Hoàn tác" (11c) → status về pending, cùng `id`, không tạo bản mới.
5. **Navigation:** đến từ 02 (Wishlist entry); Back → 02; sau khi lưu ở 12 quay về 11 với bộ lọc "Đang cân nhắc"; sau khi mua ở 04 quay về 11 với bộ lọc "Đã mua".
6. **Constraints:** thẻ có trạng thái Pressed khi chạm giữ; snackbar giãn theo chiều ngang (lề 16 dp hai bên) và bám đáy; chip ≥ 48 dp, wrap khi thiếu chỗ; số trên chip luôn bằng số thẻ; tên món tối đa 2 dòng rồi "…"; snackbar nằm trên nút đáy (bottom offset 72 + 8). ≥ 600 dp: danh sách thành lưới 2 cột, nội dung tối đa 840 dp, căn giữa.

### 12 Thêm món mong muốn (`/wishlist/add`, 12c `/wishlist/:id/edit`) — Flow 6
1. **Layout:** `Scaffold(resizeToAvoidBottomInset: true)` → `AppBar` (Back, "Thêm món mong muốn" / "Sửa món mong muốn") → `Form` trong `SingleChildScrollView` padding 16, gap 12: `Card` (Tên món, Giá dự kiến) → câu hỏi (Subtitle + Body Small) → `GridView.count(crossAxisCount: 2, shrinkWrap: true)` 8 thẻ động cơ (giống 04) → TextFormField ghi chú (maxLines 3) → `bottomNavigationBar` nút "Lưu món" / "Lưu thay đổi".
2. **Components:** App bar/Nested, Text field (Default/Focused/Error), Motive grid / Motive card (Default/Selected), Button/Primary/Large (Default/Loading).
3. **States:** trống (12) · lỗi (12a) · đã điền (12b) · sửa (12c, điền sẵn dữ liệu món) · đang lưu: nút ở trạng thái Loading.
4. **Interactions & validation (chạy khi bấm Lưu):** tên `trim().isEmpty` → "Vui lòng nhập tên món đồ để lưu."; giá có nhập và ≤ 0 → "Vui lòng nhập số tiền lớn hơn 0."; chưa chọn động cơ → "Vui lòng chọn lý do bạn muốn mua món này." (hiện dưới câu hỏi, màu error, icon cảnh báo). Cuộn tới và focus trường lỗi đầu tiên. Lỗi tự mất khi trường được sửa. Nhập giá `650000` → hiển thị `650.000 ₫`. Chỉ chọn được 1 động cơ.
5. **Navigation:** từ 11 ("Thêm món") hoặc 13 (icon Sửa); lưu hợp lệ → `pop` về 11 + SnackBar "Đã lưu món vào danh sách mong muốn." (12c → về 13 + "Đã cập nhật “<tên>”"); Back khi đã nhập dữ liệu → dialog "Bỏ thay đổi?" (đề xuất, chưa vẽ trong Figma).
6. **Constraints:** nút đáy luôn trên bàn phím; tên tối đa 60 ký tự, ghi chú 200; thẻ động cơ ≥ 72 dp cao; không có trường ảnh, URL hay người bán; placeholder ("Ví dụ: Bàn phím cơ") dùng màu on-surface-variant, cỡ Body, không đậm, để không bị nhầm với giá trị đã nhập. ≥ 600 dp: form tối đa 600 dp, căn giữa; lưới động cơ 4 cột.

### 13 Chi tiết món mong muốn (`/wishlist/:id`) — Flow 6
1. **Layout:** `Scaffold` → `AppBar` (Back, "Chi tiết món mong muốn", `IconButton(Icons.edit)` có `tooltip: 'Sửa món'`) → `SingleChildScrollView` padding 16, gap 12: `Card` tóm tắt (overline, tên Title, giá Display màu primary, caption "Giá dự kiến · chưa tính vào chi tiêu", chip trạng thái, khối "Lý do muốn mua" + chip động cơ) → `Card` chi tiết (ngày thêm, ghi chú dạng trích dẫn) → `bottomNavigationBar`: `Column(FilledButton "Ghi khoản mua", TextButton.icon "Không mua nữa")`.
2. **Components:** App bar/Nested (icon Sửa), Motive chip, Wishlist status chip, Button/Primary/Large, Button/Text/Medium, Dialog (xác nhận, màu primary), Snackbar.
3. **States:** đang cân nhắc (13) · dialog xác nhận (13a) · sau khi sửa (13b) · đã bỏ qua (13c: chỉ một nút "Đưa về Đang cân nhắc" → status pending, về 11 + snackbar "Đã đưa “<tên>” về Đang cân nhắc") · đã mua (13d: chỉ xem, ẩn `bottomNavigationBar` và icon Sửa).
4. **Interactions:** "Ghi khoản mua" → 03 điền sẵn; "Không mua nữa" → `showDialog`: "Hủy" đóng dialog, "Bỏ qua" → status skipped, về 11 (bộ lọc Bỏ qua) + SnackBar 5 giây có "Hoàn tác"; icon Sửa → 12c.
5. **Navigation:** từ 11; Back → 11 (món vẫn pending = "tiếp tục cân nhắc"); từ 03/04 Back khi chưa lưu → quay lại 13, không đổi status.
6. **Constraints:** không khóa nút theo thời gian, không đếm ngược; icon Sửa 48 × 48; tên dài xuống dòng, giá không xuống dòng. ≥ 600 dp: nội dung tối đa 600 dp; 2 nút đáy nằm ngang.

### Thay đổi ở màn có sẵn do Flow 6
- **02 Trang chủ:** chèn `WishlistEntry` ngay dưới Tổng quan tuần, chỉ hiện khi có ≥ 1 món; subtitle "n món đang cân nhắc". Không thêm tab.
- **03/04 Ghi khoản mua:** nhận `PurchaseDraft`. Có `fromWishlistId` thì: 03 hiện banner primary-container "Điền sẵn từ Danh sách mong muốn: “<tên>”…", số tiền và tên điền sẵn (sửa được); 04 chọn sẵn động cơ cũ, câu phụ "Lúc thêm vào danh sách, bạn chọn <động cơ>. Đổi nếu lý do bây giờ đã khác."

### Flow 8–10 — Mô hình dữ liệu và điều hướng

Các màn nằm ở section "Flow 8–10 – AI (Góc nhìn AI, Trước khi mua)" của page `03 Final UI`. Route xem mục 3.2 (đều là đề xuất).

```dart
// (đề xuất) Phiên "Trước khi mua": chỉ giữ trong bộ nhớ, không ghi vào purchases hay wishlist
enum Influence { promo, social, ads, none }   // câu 2 ở 15: Khuyến mãi / Ảnh hưởng MXH / Quảng cáo / Không có
enum WithoutPromo { yes, unsure, no }         // 16: Có, vẫn muốn / Chưa chắc / Không

class BeforeBuySession {
  final String name;                // bắt buộc
  final int? estimatedPrice;        // VND, null = không nhập
  final Motive reason;              // câu 1 ở 15: need | want | emotion | other
  final Influence influence;
  final WithoutPromo? withoutPromo; // chỉ có khi influence == promo
}
```

**Ràng buộc chung cho nội dung AI** (áp dụng cho 08b, 08c, 18; nhắc lại ở mục Constraints của từng màn):
- Chỉ nêu quan sát từ dữ liệu người dùng đã ghi hoặc vừa trả lời, kèm số liệu khi có (ví dụ "5/15").
- Luôn có một câu "Gợi mở".
- Không khuyên, không phán xét, không dự đoán. Có câu chốt kiểu "Đây là gợi ý để nhìn lại, không phải chẩn đoán hay phán xét."
- Trạng thái đang tải tối đa khoảng 1,5 giây trong prototype.
- Lỗi hoặc mất mạng: Error state có "Thử lại" *(đề xuất, chưa có khung trong Figma)*.

### 05 Khoản mua đã lưu (`/purchase/:id/saved`, đề xuất) — Flow 1, 8
1. **Layout:** `Scaffold` → `AppBar` (Back, "Đã lưu khoản mua") → `SingleChildScrollView` padding 16, gap 12: "Khoản mua đã được lưu" → "Một khoảnh khắc để nhận biết." → Card `PurchaseRow` (Trà sữa nướng · Cảm xúc · Hôm nay · 45.000 ₫) → "Động cơ đã chọn: Cảm xúc" → Card "Nhận định của bạn ở Góc nhìn" / "Nhận định AI và chiêm nghiệm nằm ở Góc nhìn. Xem điều gì đúng với bạn." → "Hiểu trước khi thay đổi." `bottomNavigationBar`: `Column(FilledButton "Mở Góc nhìn" cao 56, FilledButton.tonal "Về Trang chủ" cao 48)`.
2. **Components:** App bar/Nested, Purchase row, Motive chip, Button/Primary/Large, Button/Tonal/Medium.
3. **States:** một khung (node 320:8703).
4. **Interactions:** "Mở Góc nhìn" → 08a AI đang phân tích – khoản vừa lưu → 08c; "Về Trang chủ" → 02 sau khi lưu + snackbar "Đã lưu". Lần lưu đầu tiên và chưa cấp quyền thông báo → 05a trước khi về Trang chủ (Flow 1).
5. **Navigation:** đến từ 04 sau khi lưu (thay cho việc pop thẳng về 02, xem "Thay đổi ở màn có sẵn do Flow 8–10"). Back hệ thống = "Về Trang chủ" *(đề xuất)*.
6. **Constraints:** không khen, không đánh giá khoản vừa lưu, chỉ nhắc lại động cơ người dùng đã chọn; "Mở Góc nhìn" là nút chính duy nhất, "Về Trang chủ" là Tonal. ≥ 600 dp: nội dung tối đa 600 dp.

### 08b Chi tiết mô hình mua sắm (`/patterns/ai`, đề xuất) — Flow 8, 9, 10
1. **Layout:** `Scaffold` → `AppBar` (Back, "Chi tiết mô hình") → `CustomScrollView` padding 16, gap 12: "Mô hình mua sắm của bạn" + "Tháng 10/2026 · 15 khoản" → Card overline "ĐỘNG CƠ PHỔ BIẾN NHẤT" + "Khuyến mãi · 5/15" + "Khuyến mãi là động cơ bạn chọn nhiều nhất, chiếm khoảng một phần ba số khoản trong tháng." → 3 `InsightCard` (Khuyến mãi 5/15; Cảm xúc 4/15; Nhu cầu 2 · Tiện lợi 2) → dòng "Mong muốn: 1 · Ảnh hưởng MXH: 1 · Quảng cáo: 0. Đây là động cơ bạn đã ghi, không phải dự đoán về bạn." → khối "Gợi mở": "Điều gì khiến một ưu đãi có giá trị với bạn?". `bottomNavigationBar`: nút Primary Large "Xem mô hình của tôi".
2. **Components:** App bar/Nested, AI analysis state, Skeleton, Insight card, Button/Primary/Large.
3. **States:** đang tải (`08a AI đang phân tích – mô hình`, node 320:8385: "AI đang phân tích", "Đang xem kỹ hơn", "Đang tổng hợp các động cơ bạn đã ghi trong tháng này.", "Tháng 10/2026 · 15 khoản", skeleton, "Đang so sánh các động cơ bạn đã chọn…", tự chuyển); có kết quả (`08b`, node 320:8503). Lỗi hoặc mất mạng *(đề xuất, chưa có khung trong Figma)*: `StateMessage` loại Error có "Thử lại", giống `07 Mô hình – lỗi`.
4. **Interactions:** các thẻ chỉ để đọc; "Xem mô hình của tôi" → 07 Mô hình (có AI).
5. **Navigation:** từ "Để AI phân tích" ở 07 Mô hình (có AI), qua 08a; từ "Xem mô hình của tôi" ở thẻ "Mô hình mua sắm (AI)" của 08 (vào thẳng, không qua 08a); chạm thẻ nhận định ở 08c hoặc 18. Back → màn trước.
6. **Constraints:** theo "Ràng buộc chung cho nội dung AI": chỉ số đếm từ dữ liệu đã ghi ("5/15"); luôn có "Gợi mở"; không khuyên, không phán xét, không dự đoán ("không phải dự đoán về bạn"); đang tải ≤ 1,5 giây trong prototype; lỗi có "Thử lại" *(đề xuất)*. Đang tải bọc `Semantics(liveRegion: true)`. ≥ 840 dp: 3 thẻ thành lưới 2 cột.

### 08c Nhận định AI về khoản mua (`/purchase/:id/ai`, `/insights/ai/:purchaseId`, đề xuất) — Flow 8, 10
1. **Layout:** `Scaffold` → `AppBar` (Back, "Nhận định AI về khoản mua") → `SingleChildScrollView` padding 16, gap 12: "AI nhận thấy" → Card `PurchaseRow` (Trà sữa nướng · Cảm xúc · 45.000 ₫) → "Bạn đã chọn Cảm xúc." → "Một món quen thuộc đôi khi giúp tâm trạng khá hơn một chút. Điều đó có thể đúng với khoản này — hoặc không. Chỉ bạn biết lúc đó thế nào." → 2 `InsightCard` ("Bạn gắn ly trà này với cảm xúc lúc đó, hơn là một nhu cầu thiết thực." – tag "Động cơ bạn chọn"; "Sự quen thuộc có thể là một phần khiến món này hấp dẫn." – tag "Một tín hiệu dễ chịu có thể có") → khối "Gợi mở": "Bạn mong ly trà giúp mình cảm thấy thế nào?" → "Đây là gợi ý để nhìn lại, không phải chẩn đoán hay phán xét." `bottomNavigationBar`: `Column(FilledButton "Đã hiểu" cao 56, FilledButton.tonal "Xem mô hình của tôi" cao 48)`.
2. **Components:** App bar/Nested, AI analysis state, Skeleton, Purchase row, Motive chip, Insight card, Button/Primary/Large, Button/Tonal/Medium.
3. **States:** đang tải, chỉ ở Flow 8 (`08a AI đang phân tích – khoản vừa lưu`, node 320:8747: "AI đang phân tích", "Đang xem kỹ hơn", "Đang nhìn lại động cơ bạn chọn: Cảm xúc.", "Trà sữa nướng · 45.000 ₫", skeleton, "Đang xem động cơ bạn đã chọn…", "Hiểu trước khi thay đổi.", tự chuyển sau 1,5 giây); có kết quả: 2 khung cùng nội dung, khác điểm vào (`08c Nhận định AI về khoản vừa lưu` node 320:8775; `08c Nhận định AI về khoản mua` node 320:8552). Lỗi hoặc mất mạng *(đề xuất, chưa có khung trong Figma)*: Error state có "Thử lại".
4. **Interactions:** "Đã hiểu" → đóng màn; "Xem mô hình của tôi" → 07 Mô hình (có AI); chạm thẻ nhận định → 08b.
5. **Navigation:** Flow 8: từ "Mở Góc nhìn" ở 05 Khoản mua đã lưu, qua 08a; "Đã hiểu" → 00 Hub. Flow 10: từ "Xem chi tiết" ở thẻ "AI nhận thấy" của 08; "Đã hiểu" → 08 Góc nhìn. Back → màn trước.
6. **Constraints:** theo "Ràng buộc chung cho nội dung AI": chỉ dựa trên động cơ người dùng đã chọn; luôn có "Gợi mở"; không khuyên, không phán xét, không dự đoán, giữ câu chốt "không phải chẩn đoán hay phán xét"; đang tải ≤ 1,5 giây trong prototype; lỗi có "Thử lại" *(đề xuất)*. ≥ 600 dp: nội dung tối đa 600 dp.

### 14 Trước khi mua – Bước 1/3 (`/before-buy/item`, đề xuất) — Flow 9
1. **Layout:** `Scaffold(resizeToAvoidBottomInset: true)` → `AppBar` (Back, "Trước khi mua") → `Form` trong `SingleChildScrollView` padding 16, gap 12: `StepHeader` ("BƯỚC 1/3", "Bạn đang cân nhắc món gì?") + "Bắt đầu với món bạn đang cân nhắc. Bước này không ghi khoản mua." → TextFormField "Tên món" (Tai nghe Bluetooth) → TextFormField "Giá dự kiến (không bắt buộc)" (389.000 ₫) → Card "Một chút để hiểu mình" / "Tiếp theo, bạn sẽ xem vì sao mình muốn món này và điều gì thu hút bạn. Không có câu trả lời đúng hay sai." → "AI chỉ gợi ý để nhìn lại. Quyết định vẫn là của bạn." `bottomNavigationBar`: nút Primary Large "Tiếp tục".
2. **Components:** App bar/Nested, Step header, Text field, Button/Primary/Large.
3. **States:** đã điền (node 320:8963). *(Đề xuất, chưa có khung trong Figma)*: tên trống → nút "Tiếp tục" Disabled, lỗi dưới ô theo Text field/Error.
4. **Interactions:** tên bắt buộc, `trim()` khác rỗng, tối đa 60 ký tự *(đề xuất, giống `WishlistItem`)*; giá dùng bàn phím số và định dạng như mục 8.2, nếu có thì > 0; "Tiếp tục" → 15 mang theo `BeforeBuySession`.
5. **Navigation:** đến từ nút "Trước khi mua" ở 00 Hub hoặc `02 Trang chủ – lối vào Trước khi mua`. Back → Trang chủ, không lưu gì.
6. **Constraints:** không tạo `Purchase` hay `WishlistItem`; giá dự kiến không cộng vào chi tiêu; nút đáy luôn trên bàn phím. ≥ 600 dp: form tối đa 600 dp.

### 15 Trước khi mua – Bước 2/3 (`/before-buy/questions`, đề xuất) — Flow 9
1. **Layout:** `Scaffold` → `AppBar` (Back, "Câu hỏi nhanh") → `SingleChildScrollView` padding 16, gap 12: `StepHeader` ("BƯỚC 2/3", "Điều gì đứng sau lựa chọn?") + "Tai nghe Bluetooth · 389.000 ₫" → câu 1 "Vì sao bạn muốn món này?" + "Chọn động cơ gần nhất với cảm nhận của bạn." + 4 Motive card (Nhu cầu, Mong muốn, Cảm xúc, Khác) → câu 2 "Điều gì tác động đến lần mua này?" + "Chọn tác động rõ nhất." + 4 Motive card (Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Không có) → "Không có câu trả lời đúng hay sai." `bottomNavigationBar`: nút Primary Large "Tiếp tục".
2. **Components:** App bar/Nested, Step header, Motive card (Default / Selected), Button/Primary/Large.
3. **States:** khung mẫu đang chọn Mong muốn + Khuyến mãi (node 320:9009). Chưa chọn đủ 2 câu → nút "Tiếp tục" Disabled *(đề xuất, chưa có khung trong Figma)*.
4. **Interactions:** mỗi câu chọn đúng 1 thẻ (chạm thẻ khác thì đổi).
5. **Navigation:** từ 14. "Tiếp tục" → 16 nếu câu 2 chọn Khuyến mãi; nếu không → 17 AI đang phân tích – trước khi mua → 18. Back → 14, giữ dữ liệu đã nhập.
6. **Constraints:** thẻ có icon + tên, thẻ được chọn có nền, viền và dấu tích (không chỉ đổi màu); thẻ ≥ 72 dp cao như Motive card; nhãn đọc "Mong muốn, đã chọn". ≥ 600 dp: nội dung tối đa 600 dp.

### 16 Trước khi mua – Bước 3/3 (`/before-buy/discount`, đề xuất) — Flow 9
1. **Layout:** `Scaffold` → `AppBar` (Back, "Câu hỏi về khuyến mãi") → `SingleChildScrollView` padding 16, gap 12: `StepHeader` ("BƯỚC 3/3", "Thử bỏ qua ưu đãi") → "Tai nghe Bluetooth" + "389.000 ₫ · Mong muốn + Khuyến mãi" → câu hỏi "Không có khuyến mãi, bạn vẫn muốn món này chứ?" + "Hãy nghĩ về món đồ, tách khỏi ưu đãi." → 3 lựa chọn dạng Motive card ("Có, vẫn muốn", "Chưa chắc", "Không") → "Chưa chắc cũng không sao. Câu trả lời giúp gợi ý sát hơn." `bottomNavigationBar`: nút Primary Large "Xem nhận định".
2. **Components:** App bar/Nested, Step header, Motive card, Button/Primary/Large.
3. **States:** một khung (node 320:9091). Chỉ hiện khi câu 2 ở 15 chọn Khuyến mãi.
4. **Interactions:** chọn đúng 1 trong 3 lựa chọn; "Xem nhận định" → 17 → 18.
5. **Navigation:** từ 15. Back → 15.
6. **Constraints:** "Chưa chắc" là lựa chọn hợp lệ, không bị coi là sai; lựa chọn được chọn không chỉ đổi màu. ≥ 600 dp: nội dung tối đa 600 dp.

### 18 Nhận định trước khi mua (`/before-buy/result`, đề xuất) — Flow 9
1. **Layout:** `Scaffold` → `AppBar` (Back, "Nhận định trước khi mua") → `SingleChildScrollView` padding 16, gap 12: "Rõ hơn một chút trước khi mua" → "Tai nghe Bluetooth" + "389.000 ₫ · Dựa trên câu trả lời của bạn" → 2 `InsightCard` ("Bạn chọn Mong muốn: món này hấp dẫn bạn, hơn là một nhu cầu bạn đã xác định." – tag Mong muốn; "Bạn chọn Khuyến mãi và chưa chắc sẽ muốn nó khi đủ giá. Ưu đãi là một phần sức hút." – tag Khuyến mãi) → "Câu trả lời cho thấy cả món đồ lẫn ưu đãi đều quan trọng với bạn. Đây là gợi ý từ điều bạn chia sẻ, không phải dự đoán việc bạn sẽ làm." → khối "Gợi mở": "Không có khuyến mãi, điều gì khiến tai nghe này đáng mua với bạn?" → "Không có lựa chọn đúng hay sai. Quyết định là của bạn." `bottomNavigationBar`: `Column(FilledButton "Để mình nghĩ thêm" cao 56, FilledButton.tonal "Vẫn mua" cao 48)`.
2. **Components:** App bar/Nested, AI analysis state, Skeleton, Insight card, Button/Primary/Large, Button/Tonal/Medium.
3. **States:** đang tải (`17 AI đang phân tích – trước khi mua`, node 320:9139: "AI đang phân tích", "Đang xem kỹ hơn", "Đang nhìn lại Mong muốn, Khuyến mãi và câu trả lời “Chưa chắc”.", "Tai nghe Bluetooth · 389.000 ₫", skeleton, "Đang kết nối các câu trả lời của bạn…", tự chuyển sau 1,5 giây); có kết quả (node 320:9167). Lỗi hoặc mất mạng *(đề xuất, chưa có khung trong Figma)*: Error state có "Thử lại".
4. **Interactions:** "Để mình nghĩ thêm" → `go('/home')`, không ghi gì; "Vẫn mua" → `/purchase/new` (03 Ghi khoản mua – Bước 1/2, sang Flow 1), điền sẵn tên và giá dự kiến như khi mua từ Danh sách mong muốn *(đề xuất)*; chạm thẻ nhận định → 08b.
5. **Navigation:** từ 15 (không chọn Khuyến mãi) hoặc 16, qua 17. Back → bước trước.
6. **Constraints:** theo "Ràng buộc chung cho nội dung AI": chỉ dựa trên câu trả lời người dùng vừa chọn; luôn có "Gợi mở"; không khuyên nên mua hay không, không dự đoán ("không phải dự đoán việc bạn sẽ làm"); đang tải ≤ 1,5 giây trong prototype; lỗi có "Thử lại" *(đề xuất)*. Flow 9 không tạo `Purchase` nếu người dùng không chọn "Vẫn mua". ≥ 600 dp: 2 nút đáy nằm ngang.

### Thay đổi ở màn có sẵn do Flow 8–10
- **00 Hub / 02 Trang chủ:** thêm `BeforeYouBuyEntry` (nút Tonal "Trước khi mua" → 14). Khung `02 Trang chủ – lối vào Trước khi mua` là biến thể của 02: giống Hub nhưng không có `WishlistEntry`.
- **04 Ghi khoản mua – Bước 2/2:** "Lưu" thành công → 05 Khoản mua đã lưu (Flow 1, Flow 8 trên Figma), thay vì pop thẳng về 02.
- **07 Mô hình (có AI):** phiên bản hiện tại của 07, thêm nút Primary "Để AI phân tích" → 08a → 08b.
- **08 Góc nhìn (có AI):** phiên bản hiện tại của 08, gồm dòng mạch "Dữ liệu mua sắm → Nhận định AI → Chiêm nghiệm", thẻ "AI nhận thấy" (nút chữ "Xem chi tiết" → 08c), `AiPatternCard` "Mô hình mua sắm (AI)" ("Xem mô hình của tôi" → 08b) và thẻ "Chiêm nghiệm tháng" ("Mở chiêm nghiệm tháng" → 09). Sau khi lưu chiêm nghiệm: khung `08 Góc nhìn – đã lưu chiêm nghiệm (có AI)` với snackbar "Đã lưu chiêm nghiệm tháng 10".

---

## 5. Nhãn cho trình đọc màn hình (TalkBack)

Lấy từ page `04 Design System › Accessibility check › 7`. Dùng `Semantics(label: …)` hoặc `tooltip` của `IconButton`.

| Thành phần | Màn | Nhãn đọc |
|---|---|---|
| Nút ← | mọi màn lồng | "Quay lại" |
| Nút ? | 04 | "Giải thích các động cơ" |
| Nút thùng rác | 05 | "Xóa khoản mua <tên>" |
| Avatar | các tab | "Mở Cá nhân" |
| Nút × trong ô số tiền | 03 | "Xóa số tiền đã nhập" |
| Icon lịch ở ô thời điểm | 03 | "Chọn ngày giờ khác" |
| `<` / `>` chọn kỳ | 06, 07 | "Kỳ trước" / "Kỳ sau" (khi khóa: "Kỳ sau, không khả dụng") |
| Nhãn kỳ ở giữa | 06, 07 | "Đang xem Tuần này, 05/10 đến 11/10, 6 khoản. Chạm hai lần để chọn tháng" |
| Thẻ động cơ | 04, 12 | "Cảm xúc, đã chọn, 6 trên 8" / "Khuyến mãi, chưa chọn" |
| Thang hài lòng | 09 | "Mức 3 trên 5, chưa chọn" |
| Switch nhắc nhở | 10 | "Nhắc ghi khoản mua lúc 21 giờ, đang bật" |
| Tab điều hướng | các tab | "Trang chủ, tab 1 trên 5, đang chọn" |
| Thanh % động cơ | 07 | "Khuyến mãi: 5 khoản, 33 phần trăm" |
| Cột khung giờ | 07 | "Tối, 18 giờ đến 5 giờ: 8 khoản, cao nhất" |
| Snackbar | sau khi lưu / xóa | thông báo `liveRegion`: "Đã xóa Tai nghe Bluetooth. Hoàn tác trong 5 giây" |

## 6. Màn hình rộng hơn (≥ 600 dp) — tóm tắt

| Chiều rộng | Thay đổi |
|---|---|
| < 600 dp (360–412) | Như Figma: `NavigationBar` đáy, nút chính ghim đáy, 1 cột |
| 600–839 dp | `NavigationRail` bên trái thay `NavigationBar`; nội dung tối đa 600 dp căn giữa; nút chính thành `FloatingActionButton.extended` ở tab gốc, ở màn lồng vẫn ghim đáy nhưng rộng tối đa 400 dp; lưới động cơ 4 cột |
| ≥ 840 dp | Lịch sử + Chi tiết thành list-detail 2 khung; Mô hình chia 2 cột (động cơ / khung giờ); Góc nhìn và Danh sách mong muốn thành lưới 2 cột; dialog giữ rộng 312 dp |

Dùng `LayoutBuilder` / `MediaQuery.sizeOf(context).width` với các mốc trên. Không thiết kế riêng cho màn rộng trong Figma (đề bài không yêu cầu).

## 7. Thay đổi đã quyết sau phản biện bằng AI (PB)

Các mục dưới đây được chấp nhận ở vòng phản biện (bảng PB-1 → PB-20 trong [`ai/ai-design-log.md`](../ai/ai-design-log.md)). Chúng **ghi đè** mô tả ở mục 4. Khung Figma tương ứng được cập nhật theo cùng mã.

| Mã | Màn / component | Thay đổi khi dựng |
|---|---|---|
| PB-1 | 02 (mọi trạng thái) | `WishlistEntry` luôn hiện dưới thẻ tổng quan. Khi 0 món: subtitle "Chưa có món nào · Thêm món", chạm vào → 12 |
| PB-2 | 03, 03c; 06 | 3 chip số tiền `Expanded` chia đều. 03c giữ nhãn "Tiếp tục", chú thích "Bước tiếp theo: chọn động cơ (đã chọn sẵn <động cơ>)" xuống dòng được. Hàng `FilterChip` ở 06 cuộn tràn tới mép màn (`padding` nằm trong `ListView`, không clip ở lề 16) |
| PB-5 | Text field, Motive card | Default có viền 1 dp: `colorScheme.outline` #8A918A trên thẻ trắng; ô đặt thẳng trên nền #F5F6F2 (Đăng nhập, Đăng ký) dùng `AppColors.outlineStrong` #7A817B. Focused: viền primary 2 dp |
| PB-6 | Weekly summary card | Dưới thanh xếp chồng thêm `Wrap` chú giải 3 động cơ nhiều nhất (icon 16 + tên + %); các đoạn cách nhau 2 dp |
| PB-7 | Purchase row; Đăng ký | Giờ dùng Body Small 14 sp. Gợi ý "Mật khẩu có ít nhất 8 ký tự." là `helperText` của ô Mật khẩu |
| PB-8 | Chuỗi hiển thị | "Thông tin khoản mua", "KHOẢN MUA VỪA NHẬP", "KHOẢN MUA ĐANG SỬA", "15 khoản mua", "Chưa có khoản mua", "Động cơ" (13), "Chọn một động cơ chính" (12), "Vui lòng chọn một động cơ." (12a), "Thời điểm mua" (03, 05). Gom chuỗi vào `lib/l10n/app_vi.arb` |
| PB-9 | Snackbar | 02c: "Đã lưu “<tên>” trên máy, sẽ đồng bộ khi có mạng" + Hoàn tác. 11b: "Đã lưu “<tên>”" + Hoàn tác (xóa món vừa thêm). 11e: thêm Hoàn tác (xóa `Purchase` vừa tạo, món về `pending`) |
| PB-10 | 12 | `hintStyle`: Body 16 w400, màu on-surface-variant |
| PB-11 | 02, 07, 08 | 02: bỏ dòng "Nhiều nhất: …", dòng phụ chỉ "Tuần này: 5 khoản". 07: bỏ thẻ "Tổng quan chu kỳ", khung giờ đặt ngay sau danh sách động cơ. 08: bỏ tiêu đề "Góc nhìn" trong thân (giữ overline tháng) |
| PB-12 | 13a | Nút xác nhận "Chuyển vào Bỏ qua"; nội dung "“<tên>” sẽ chuyển vào Bỏ qua. Bạn có 5 giây để hoàn tác." |
| PB-13 | 10 – xác nhận xóa toàn bộ | Nội dung: "Mọi khoản mua, món mong muốn, chiêm nghiệm và nhắc nhở sẽ bị xóa vĩnh viễn khỏi máy và tài khoản. Không thể hoàn tác." Nút "Hủy" là `TextButton` cao 48 |
| PB-14 | 10 | Hàng "Nhắc ghi khoản mua" hiển thị giờ (mặc định 21:00, khớp Figma ở 10 và 05a; người dùng đổi được); chạm vào chữ → `showTimePicker`; switch vẫn bật / tắt |
| PB-15 | 01, 10, 00b | Câu lưu trữ chung: "Lưu trên máy, đồng bộ với tài khoản khi có mạng." 10 thêm Card "Tài khoản" (email, "Đăng xuất" → `/login`, xóa phiên). 00b chỉ còn Email + Mật khẩu (có `IconButton` hiện / ẩn, tooltip "Hiện mật khẩu") |
| PB-16 | 03 | Nhãn "Bắt buộc" màu on-surface-variant (chỉ đổi sang error khi có lỗi) |
| PB-17 | Icon | Biên lai không ký hiệu tiền (`Icons.receipt_long_outlined`), tên món `Icons.shopping_bag_outlined`, "Xóa bộ lọc" `Icons.filter_alt_off_outlined`, 08 dùng `Icons.calendar_month_outlined` |
| PB-18 | 04, 12 | `TextButton` "Các động cơ nghĩa là gì?" dưới câu hỏi, mở bottom sheet giải thích động cơ |
| PB-19 | 02a, 06a | 02a giữ chip "Hôm nay, 11/10" và ẩn "Xem tất cả" khi 0 khoản; 06a giữ thứ tự chip theo `Motive.values` |
| PB-20 | Text button | Mọi link chữ ("Xem tất cả", "Quên mật khẩu?", "Đăng ký", "Để sau", "Hủy") dùng `TextButton` với `minimumSize: Size(48, 48)` |

## 8. Ghi chú bàn giao Flutter – phần bổ sung checklist (13/10/2026)

### 8.1. Đăng nhập / Đăng ký / Đổi mật khẩu
- Bọc form trong `AutofillGroup`; ô Email: `autofillHints: [AutofillHints.email]`,
  `keyboardType: TextInputType.emailAddress`, `textInputAction: TextInputAction.next`.
- Ô Mật khẩu: `autofillHints: [AutofillHints.password]` (Đăng ký / Đổi mật khẩu dùng
  `AutofillHints.newPassword`), `obscureText` bật/tắt bằng `suffixIcon` eye / eye-off,
  `Semantics(label: 'Hiện mật khẩu' / 'Ẩn mật khẩu')`.
- Lỗi đăng nhập: hiện ở `errorText` của ô sai (email: "Email này chưa được đăng ký";
  mật khẩu: "Mật khẩu chưa đúng. Thử lại hoặc chọn Quên mật khẩu?"), kèm icon cảnh báo.
- Password strength: tính lại sau mỗi lần gõ (onChanged), 3 mức; nhãn chữ luôn hiện.
- Đổi mật khẩu: nút Lưu `onPressed: null` cho tới khi đủ 3 ô và ô mới trùng ô nhập lại;
  lưu xong `Navigator.pop` về Tài khoản + SnackBar "Đã đổi mật khẩu".

### 8.2. Ô số tiền
- `keyboardType: TextInputType.number`, `inputFormatters: [FilteringTextInputFormatter.digitsOnly]`,
  định dạng hiển thị 45.000 ₫. Nút "Tiếp tục" nằm trong `bottomNavigationBar`/`persistentFooterButtons`
  để luôn nằm trên bàn phím (Scaffold `resizeToAvoidBottomInset: true`).

### 8.3. Thanh tab và cử chỉ
- Khi đổi tab: `HapticFeedback.selectionClick()`.
- Back hệ thống (`PopScope`): ở màn cấp sâu thì quay về màn trước; ở tab gốc khác Trang chủ thì
  về Trang chủ; ở Trang chủ thì thoát app.
- Thanh tab ẩn ở: Ghi khoản mua, Chi tiết khoản mua, Tài khoản, Đổi mật khẩu, Xin quyền thông báo.

### 8.4. Splash
- Android 12+ dùng SplashScreen API (gói `flutter_native_splash`): nền #2E4A9E, icon app
  ở giữa. Giữ splash chỉ trong lúc kiểm tra phiên đăng nhập (mục tiêu ≤ 0,8 giây), sau đó điều
  hướng: đã đăng nhập → Trang chủ tổng hợp, chưa → Onboarding (lần đầu) hoặc Đăng nhập.
- Icon app: adaptive icon (foreground ký hiệu chart-search trắng trong vùng 66 dp, background
  #2E4A9E), tạo bằng `flutter_launcher_icons`.

### 8.5. Quyền thông báo (nhắc nhở 21:00)
- Android 13+ cần `POST_NOTIFICATIONS` trong AndroidManifest.
- Chỉ hiện màn 05a sau lần lưu khoản mua đầu tiên. "Bật nhắc nhở" → gọi
  `Permission.notification.request()` (`permission_handler`) → hệ thống hiện hộp thoại của Android.
- "Để sau" hoặc bị từ chối → lưu cờ `notificationDenied = true`. Màn Cá nhân đọc cờ này để hiện
  "Chưa cấp quyền thông báo · Mở cài đặt". Link gọi `openAppSettings()`.
- Hẹn giờ nhắc bằng `flutter_local_notifications` (mặc định 21:00 mỗi ngày, đổi giờ ở Cá nhân theo PB-14); chạm thông báo mở thẳng
  03 Ghi khoản mua.

### 8.6. Tài khoản, đăng xuất, xóa
- Đăng xuất: dialog loại Default. Dữ liệu đã đồng bộ vẫn giữ trên tài khoản; xóa phiên đăng nhập
  rồi `pushNamedAndRemoveUntil` về Đăng nhập.
- Xóa tài khoản: dialog loại Danger, xóa tài khoản và dữ liệu đã đồng bộ, rồi về Đăng nhập.
  Khác với "Xóa toàn bộ dữ liệu" (chỉ xóa khoản mua, giữ tài khoản).
