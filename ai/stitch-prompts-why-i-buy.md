# Prompt Google Stitch – Why I Buy? · Smart Wishlist 2.0 (Lab 2)

Bám theo: Final Unified Spec v1.0 (mục 7.3, 7.4, 8.2, 9.4, 11.3, 11.5), Overview & Persona v2.0 (P1–P4), `design/DESIGN.md`.

## 0. Cách dùng

1. **Mở project Stitch cũ (remix)**, chế độ **Mobile**, để Stitch giữ style đã có. Nếu Stitch cho đính kèm ảnh, đính kèm ảnh màn **02 Trang chủ** và **11 Danh sách mong muốn** hiện tại làm tham chiếu.
2. Chạy **lần lượt từ Prompt 1 đến Prompt 10**. Mỗi prompt đã có sẵn **khối chung** ở cuối (bối cảnh, style, từ vựng, dữ liệu mẫu, ràng buộc). **Không xóa khối chung**: lần P2 trước chỉ ghi "same constraints" nên Stitch làm mất dấu, chữ nhỏ.
3. Prompt 9–10 (Chrome extension) chạy ở chế độ **Web**, trong một project riêng.
4. Sau mỗi prompt: chụp ảnh toàn cảnh + từng khung, đối chiếu **checklist mục 3**, ghi prompt nguyên văn và nhận xét vào `ai/ai-design-log.md` (mục R5). Khi lỗi lặp lại, dùng **Prompt 11 (tinh chỉnh)**.
5. Nếu Stitch báo prompt quá dài: chia đôi danh sách màn thành 2 lần chạy, **vẫn giữ nguyên khối chung** ở cả hai.
6. Nhãn **"Dữ liệu mô phỏng"** nên gắn trong Figma sau khi import, không nhờ Stitch (Stitch hay tự đặt sai vị trí hoặc biến nó thành thẻ to).

## 1. Persona → Flow → Prompt

| Prompt | Persona | Flow | Màn sinh ra |
|---|---|---|---|
| 1 | **P1 Nam** (primary) | F11 · Chia sẻ → lưu | Share sheet, 19.1, 19.2, 19.4, 19.5, 11 |
| 2 | **P1 Nam** | F11 · Cân nhắc → Chờ | 13, 20.3, 21.1, 21.2 |
| 3 | **P1 Nam** | F12 · Nhắc → cập nhật giá → Mua / Bỏ qua | Thông báo, 22.2, 20.1, 03 từ danh sách, 11 sau Mua, Bỏ qua + Hoàn tác |
| 4 | **P3 Huy** | F11 · Ngân sách, món cùng nhóm, so sánh | 23.1, 23.2/23.3, "Vì sao con số này?", 20.2, 20.5, So sánh |
| 5 | **P3 Huy** | F12 · Chờ đến đợt sale | Thông báo sale, 26 Lịch sale, 26.2, 26.3, 20.4, 22.3 |
| 6 | **P2 Linh** | Sau mua · Nhìn lại | 27.1, 27.2, 06 lọc "Từ danh sách", 08 hài lòng theo động cơ, 09 |
| 7 | **P4 Mai** | F11 nhánh lỗi · gián đoạn, mất mạng | 19 khôi phục nháp, lưu offline, 11 chưa đồng bộ, 19.3, 03 nháp, "Cần xem lại" (E12) |
| 8 | Chung (P1–P3) | Cá nhân, Hồ sơ mua sắm | 10, 24.1, 24.2, 24.3 |
| 9 | Chung | F13 · phần trên điện thoại | 25.1, 25.2, 25.3, 25.4 |
| 10a | Chung (kênh PC chưa xác minh) | F13 · Extension popup | X1 (7 trạng thái) |
| 10b | Chung | F13 · Extension trang và ghép | X2, X3, X4, X5 |
| 11 | — | Tinh chỉnh | Mẫu prompt sửa lỗi nhất quán |

**Mạch dữ liệu xuyên suốt (để prototype không mâu thuẫn):**

- 03/11: Nam chia sẻ **Tai nghe Bluetooth** (chưa có giá) → Chờ 3 ngày. Mai lưu **Áo Lovito** khi mất mạng.
- 06/11: nhắc xem lại → Nam nhập giá 420.000 ₫ → Mua, giá thực trả 399.000 ₫ (có dùng mã giảm giá).
- 10/11 20:00: nhắc đợt 11.11 → Huy xem **Áo Lovito** và **Áo khoác** → Bỏ qua Áo khoác.
- 13/11: hỏi mức hài lòng Tai nghe → Linh xem Góc nhìn, Chiêm nghiệm tháng 11.
- **Kính cường lực** được lưu từ Chrome extension (F13).

## 2. Cần chốt trước khi chạy

- **Ngày:** màn cũ dùng "Hôm nay 11/10/2026"; flow mới cần đợt 11.11 trong 7 ngày nên đặt trong tháng 11 (03/11–13/11). Nhóm đồng ý hai mốc thời gian này, hoặc đổi sang đợt sale khác.
- **Trùng tên "Tai nghe Bluetooth":** dữ liệu cũ có khoản mua Tai nghe Bluetooth 389.000 ₫ (bị xóa ở Flow 3), spec 11.5 lại dùng Tai nghe Bluetooth 420.000 ₫ cho danh sách. Có thể giữ (đã xóa nên không xung đột) hoặc đổi tên món mới thành "Tai nghe chống ồn".
- **Tiêu đề màn Decision Card trên giao diện:** prompt dùng "Cân nhắc món này" (không để chữ tiếng Anh trên UI).
- **DESIGN.md** vẫn ghi ngân sách là "ngoài phạm vi": prompt đã theo spec mới, cần sửa DESIGN.md cho khớp.

## 3. Checklist soát ảnh Stitch (từ lỗi các vòng trước)

- [ ] Có tự thêm tính năng / thẻ / mẹo / thống kê không có trong prompt? (vòng trước: "Khoảng hạ nhiệt 24h", "48h suy ngẫm", "Đang tĩnh tâm")
- [ ] Từ vựng đúng: "Danh sách mong muốn", "món", 3 trạng thái, **Mua · Chờ · Bỏ qua**, 8 động cơ đúng tên.
- [ ] Ba nút quyết định **cùng kiểu, cùng cỡ**; nút Mua không nổi bật hơn.
- [ ] Giá luôn có nguồn + ngày; không có "0 ₫"; giá trong danh sách không cộng vào tổng chi.
- [ ] Không màu đỏ / cam / xanh lá mang nghĩa tốt–xấu; vượt ngân sách chỉ là chữ + sọc xám.
- [ ] Không vẽ giao diện, logo Shopee.
- [ ] Chữ tiếng Việt đủ dấu, không bị cắt (snackbar, chip), số liệu đúng dữ liệu mẫu.
- [ ] Mỗi màn tối đa 1 nút filled; trạng thái lỗi có lối ra.

---

## Prompt 1 · P1 Nam · F11 – Lưu món từ chia sẻ

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Add the screens below for flow F11 ("Share from a shopping app → save to Danh sách mong muốn"). Persona: Nam, 22, uses Android one-handed late in the evening, hates long forms. Goal: save an item in under 20 seconds without being forced to enter a price. Today is Thứ Ba 03/11/2026.

Name each frame with its code and Vietnamese title.

1. "F11.0 Chia sẻ" – Android system share sheet over a generic blurred shopping app (no real brand). The app row includes the "Why I Buy?" icon.
2. "19.2 Lưu từ chia sẻ – chưa có giá" – bottom sheet over the blurred app, title "Lưu vào danh sách mong muốn". Rows: link "shopee.vn · Tai nghe Bluetooth…" (one line, truncated); name field prefilled "Tai nghe Bluetooth" (editable); price row showing "Chưa có giá" with helper "Không bắt buộc" and a text button "Nhập giá"; optional motive chips in one scrollable row with "Khuyến mãi" selected; dropdown "Nhóm ngân sách: Công nghệ". Filled primary button "Lưu", text button "Hủy".
3. "19.1 Lưu từ chia sẻ – đủ thông tin" – same sheet for "Áo Lovito": price field "250.000 ₫", price type "Giá đơn", variant field "Phân loại: Đen – M", motive "Khuyến mãi", group "Thời trang".
4. "19.4 Lưu từ chia sẻ – món đã lưu" – same sheet layout, message "Món này đã lưu" with the saved price chip "250.000 ₫ · Bạn nhập · 03/11 · Đen – M"; tonal button "Xem", filled button "Cập nhật giá". No duplicate is created.
5. "19.5 Đã lưu" – the blurred shopping app again with snackbar "Đã lưu vào danh sách" and action "Xem".
6. "11 Danh sách mong muốn" – app bar title "Danh sách mong muốn", filter chips "Đang cân nhắc (4)", "Đã mua", "Bỏ qua". One card per item: name, price chip or "Chưa có giá", one motive chip, budget group, source label ("Chia sẻ", "Máy tính" or "Nhập tay") and "Lưu 03/11". Items: Tai nghe Bluetooth (Chưa có giá, Chia sẻ, 03/11); Áo Lovito (250.000 ₫ · Đen – M, Chia sẻ, 03/11); Kính cường lực (180.000 ₫, Máy tính, 03/11); Áo khoác (420.000 ₫ · Giá ghi 10/10 shown with dashed outline, Nhập tay, 10/10). Floating "+" button to add manually.

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 2 · P1 Nam · F11 – Cân nhắc rồi Chờ

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Continue flow F11 for Nam (22, one-handed, dislikes judgmental wording). He opens the item he just saved, looks at the facts, and chooses "Chờ". Today is Thứ Ba 03/11/2026. Name each frame with its code and Vietnamese title.

1. "13 Chi tiết món – Tai nghe Bluetooth" – name, price row "Chưa có giá" with text button "Nhập giá", motive chip "Khuyến mãi", group "Công nghệ", "Lưu từ Chia sẻ · 03/11", text button "Mở link", empty note. A card "Cân nhắc món này" with chevron. Sticky bottom bar with three equal tonal buttons with icons: "Mua", "Chờ", "Bỏ qua".
2. "20.3 Cân nhắc món này – thiếu giá" – title "Cân nhắc món này". Top: neutral summary chip "Cần giá gần đây". Stacked blocks, each with an icon and a small heading:
   - "Giá": "Chưa có giá gần đây" + text buttons "Nhập giá" · "Mở link".
   - "Ngân sách": "Nhóm Công nghệ · khả dụng 630.000 ₫" and "Cần giá để tính tỷ lệ".
   - "Đồ đang có": "Bạn đã ghi có Tai nghe có dây (dùng 2 năm). Bạn muốn thay hay mua thêm?"
   - "Lý do": motive chip "Khuyến mãi", "Bạn chưa trả lời câu hỏi trước khi mua" + text button "Trả lời nhanh".
   - Small line: "Bạn mới lưu hôm nay".
   Sticky bottom bar: "Mua", "Chờ", "Bỏ qua" – equal size, equal style. No "nên mua" or "không nên mua".
3. "21.1 Chờ – chọn thời điểm xem lại" – bottom sheet over 20.3, title "Khi nào bạn muốn xem lại?". Radio list: "Sau 3 ngày · Thứ Sáu 06/11" (selected), "Đến đợt sale 11.11 · Thứ Tư 11/11", "Tự chọn ngày". Helper "Bạn vẫn có thể mua bất cứ lúc nào." Filled button "Đặt nhắc".
4. "21.2 Đã đặt nhắc" – Danh sách mong muốn (same layout as frame 11) with snackbar "Sẽ nhắc bạn xem lại vào 06/11". The Tai nghe Bluetooth card shows status "Đang cân nhắc" and a line with a bell icon "Xem lại 06/11".

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 3 · P1 Nam · F12 – Được nhắc, cập nhật giá, Mua hoặc Bỏ qua

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Add flow F12 for Nam: the reminder arrives, he enters the price he sees, reviews the facts, then buys (or skips, with undo). Today is Thứ Sáu 06/11/2026. Name each frame with its code and Vietnamese title.

1. "F12.0 Thông báo xem lại" – Android notification shade, 09:00: "Why I Buy? · Đến hẹn xem lại Tai nghe Bluetooth. Bạn đã lưu 3 ngày trước."
2. "22.2 Cập nhật giá – gõ giá" – bottom sheet titled "Giá bạn đang thấy là bao nhiêu?": large VND amount field "420.000 ₫" with a numeric keypad that has a "000" key; segmented control "Giá đơn" (selected) · "Khoảng giá" · "Flash Sale"; field "Phân loại: Đen"; text button "Mở link để xem giá"; filled button "Lưu giá".
3. "20.1 Cân nhắc món này – đủ dữ liệu" – same layout as 20.3. Summary chip "Có thể chờ". Blocks:
   - "Giá": price chip "420.000 ₫ · Bạn nhập · 06/11 · Đen".
   - "Ngân sách": "Chiếm khoảng 67% phần khả dụng của nhóm Công nghệ tháng này (630.000 ₫)", a neutral indigo budget meter, text button "Vì sao con số này?".
   - "Đồ đang có": "Bạn đã ghi có Tai nghe có dây (dùng 2 năm)."
   - "Lý do": chip "Khuyến mãi".
   - "Thời điểm": calendar icon, "Đợt 11.11 còn 5 ngày, có thể có giá tốt hơn".
   Bottom bar "Mua", "Chờ", "Bỏ qua" – equal.
4. "03 Ghi khoản mua – từ danh sách" – existing "Ghi khoản mua · Bước 1/2" screen, prefilled from the item: small label "Từ danh sách mong muốn", field label "Giá thực trả" with value "399.000 ₫" (editable), helper "Bạn trả thấp hơn giá đã ghi 5%", a toggle chip "Có dùng mã giảm giá" (selected, no code input), item name "Tai nghe Bluetooth", filled button "Tiếp tục". There is NO voucher code field.
5. "11.4 Danh sách – đã mua" – Danh sách mong muốn with filter "Đã mua" selected; card "Tai nghe Bluetooth · Đã mua · 399.000 ₫ · 06/11"; snackbar "Đã ghi khoản mua".
6. "11.3 Danh sách – bỏ qua" – Danh sách mong muốn (Đang cân nhắc) right after choosing "Bỏ qua" on Tai nghe Bluetooth: the card is gone and a snackbar reads "Đã chuyển sang Bỏ qua" with action "Hoàn tác".

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 4 · P3 Huy · F11 – Ngân sách theo nhóm, món cùng nhóm, so sánh

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Persona: Huy, 19, student, keeps many items in the list, several compete for the same monthly limit he sets himself. He must understand that budget percentages only use purchases he logged, and compare two items without help. Today is Thứ Ba 03/11/2026. Name each frame with its code and Vietnamese title.

1. "23.1 Ngân sách – chưa đặt" – title "Ngân sách tháng 11". Short text "Ngân sách là mốc tham chiếu do bạn tự đặt. App không chặn việc mua." List of 6 groups (Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác), each with text button "Đặt mức". Filled button "Đặt ngân sách", text button "Để sau".
2. "23.2 Ngân sách – đã đặt" – one card per group with: name, "Hạn mức", "Đã chi", "Còn lại", a neutral indigo meter. Thời trang: hạn mức 1.500.000 ₫, đã chi 400.000 ₫, line "Khả dụng cho danh sách: 864.000 ₫". Công nghệ: 1.000.000 ₫, đã chi 200.000 ₫, "Khả dụng cho danh sách: 630.000 ₫". Làm đẹp (state 23.3): hạn mức 300.000 ₫, đã chi 350.000 ₫, meter full with diagonal grey (#545E59) stripes and the text "Đã vượt 50.000 ₫" – no red, no warning icon. Footnote: "Đã chi chỉ tính khoản mua bạn đã ghi. Món trong danh sách mong muốn không được cộng." Text button "Vì sao con số này?" on Thời trang.
3. "23.4 Vì sao con số này?" – bottom sheet for Thời trang showing the calculation as rows: "Hạn mức 1.500.000 ₫" − "Đã chi 400.000 ₫" = "Còn lại 1.100.000 ₫"; "Dự phòng chi thường ngày: 5.000 ₫ × 28 ngày = 140.000 ₫"; "Biên độ an toàn 10%"; result "Khả dụng cho danh sách: 864.000 ₫". Button "Đã hiểu".
4. "20.2 Cân nhắc món này – chưa có ngân sách" – for Áo Lovito: "Giá" chip "250.000 ₫ · Bạn nhập · 03/11 · Đen – M"; "Ngân sách" block: "Chưa thiết lập ngân sách" + text button "Thiết lập" (no percentage at all); "Lý do" chip "Khuyến mãi"; line "Bạn mới lưu hôm nay". Summary chip "Có thể chờ". Bottom bar Mua · Chờ · Bỏ qua.
5. "20.5 Cân nhắc món này – có món cùng nhóm" – Áo Lovito with budget set: "Ngân sách": "Chiếm khoảng 29% phần khả dụng của nhóm Thời trang (864.000 ₫)" + meter; block "Món cùng nhóm": "Bạn đang cân nhắc thêm 1 món cùng nhóm: Áo khoác" + text button "So sánh"; "Lý do": "Khuyến mãi"; "Bạn mới lưu hôm nay". Summary chip "Có thể chờ". Bottom bar Mua · Chờ · Bỏ qua.
6. "20.6 So sánh" – two columns "Áo Lovito" and "Áo khoác". Rows: Giá ("250.000 ₫ · 03/11" vs "420.000 ₫ · Giá ghi 10/10" with dashed outline and text "Giá cũ, chưa so được"), Động cơ (Khuyến mãi vs Mong muốn), Ngày lưu (03/11 vs 10/10), Mức ưu tiên (3 vs 2 stars, set by the user), Phần khả dụng (29% vs 49%). Bottom line: "Cả hai: 670.000 ₫ · khoảng 78% phần khả dụng của nhóm Thời trang". No winner, no recommendation.

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 5 · P3 Huy · F12 – Chờ đến đợt sale

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Persona: Huy, 19. He waits for a sale day Shopee has announced. He must be able to tell a SALE DATE apart from a promise that the price will drop. Today is Thứ Ba 10/11/2026 unless stated. Name each frame with its code and Vietnamese title.

1. "26.1 Thông báo đợt sale" – Android notification shade at 20:00: "Why I Buy? · Mai là 11.11. Bạn có 2 món trong danh sách. Mở xem nhé?" (one grouped notification, no countdown).
2. "26 Lịch sale" – list of sale days with a status tag: "11.11 · Thứ Tư 11/11 · Đã xác nhận", "Sale giữa tháng · 15/11 · Dự kiến", "Sale ngày lương · 25/11 · Dự kiến", "12.12 · Dự kiến". Note: "Chỉ đợt đã xác nhận mới gửi thông báo." Setting row "Nhắc tôi" with segmented "Chỉ đợt lớn" · "Mọi đợt" · "Tắt".
3. "26.2 Danh sách cho 11.11" – header "Đợt 11.11 · Thứ Tư 11/11 · Đã xác nhận" and the note "Đây là ngày sale Shopee đã công bố, không có nghĩa món nào cũng giảm giá." Item cards: Áo Lovito (price chip "250.000 ₫ · 03/11 · Đen – M", text button "Cập nhật giá"); Áo khoác (dashed price chip "420.000 ₫ · Giá ghi 10/10", text button "Xác nhận lại").
4. "26.3 Danh sách cho đợt sale – trống" – same header, empty state: icon, "Chưa có món nào cho đợt này", text button "Mở danh sách mong muốn".
5. "20.4 Cân nhắc món này – giá cũ" – Áo khoác on 11/11: summary chip "Cần giá gần đây"; "Giá": dashed chip "420.000 ₫ · Giá ghi 10/10 · 32 ngày trước" + text button "Xác nhận lại"; "Ngân sách": "Cần giá gần đây để tính tỷ lệ"; "Lý do": "Mong muốn"; "Bạn đã lưu 32 ngày". Bottom bar Mua · Chờ · Bỏ qua.
6. "22.3 Lịch sử giá – Áo Lovito" – list of price records, each with source and date: "250.000 ₫ · Giá đơn · Bạn nhập · 03/11 · Đen – M"; "229.000 ₫ · Giá đơn · Bạn nhập · 08/11 · Đen – M" with text "Thấp hơn lúc lưu 8%" (indigo text with down arrow, not green); "199.000 ₫ · Flash Sale · Bạn nhập · 11/11" with text "Flash Sale chỉ so với giá Flash Sale". Filled button "Thêm giá".

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 6 · P2 Linh · Nhìn lại sau khi mua

```text
Edit the existing "Why I Buy?" project. Keep the current visual style and the existing screens Lịch sử, Góc nhìn, Chiêm nghiệm tháng. Persona: Linh, 26, office worker, reviews her purchases at the end of the week or month. She wants patterns grounded in what she logged, never judgement. Today is Thứ Sáu 13/11/2026. Name each frame with its code and Vietnamese title.

1. "27.1 Hỏi mức hài lòng" – dialog over Trang chủ: "Tai nghe Bluetooth · bạn mua 06/11 · Khuyến mãi". Question "Sau một tuần, bạn thấy hài lòng với món này thế nào?" Five large star buttons with end labels "Không hài lòng" and "Rất hài lòng". Text button "Bỏ qua", filled button "Lưu".
2. "27.2 Đã ghi mức hài lòng" – Trang chủ with snackbar "Đã ghi. Mức hài lòng sẽ hiện trong Góc nhìn."
3. "06.5 Lịch sử – từ danh sách mong muốn" – existing Lịch sử with one extra filter chip "Từ danh sách mong muốn" (selected). Row: Tai nghe Bluetooth, chip Khuyến mãi, 06/11, 399.000 ₫, with secondary text "Từ danh sách mong muốn". Keep one motive chip per row.
4. "08.4 Góc nhìn – mức hài lòng theo động cơ" – existing Góc nhìn, add ONE card "Mức hài lòng theo động cơ": rows "Nhu cầu · 4,5/5 · 2 khoản" and "Khuyến mãi · 3,0/5 · 2 khoản", each with icon + label + a small neutral bar; caption "Chỉ tính các khoản bạn đã chấm." Observation sentence: "Các khoản Khuyến mãi bạn đã chấm có mức hài lòng trung bình 3,0/5." No advice.
5. "09.3 Chiêm nghiệm tháng 11" – existing Chiêm nghiệm tháng, add ONE block "Món bạn đã cân nhắc": "Bạn đã mua 1 món từ danh sách, giá thực trả thấp hơn giá đã ghi 5%." and "Bạn đã cân nhắc và không mua 1 món, tổng giá đã ghi 420.000 ₫." Never call it "tiết kiệm".

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 7 · P4 Mai · Bị gián đoạn, mất mạng, lỗi

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Persona: Mai, 29, office worker with family duties, often interrupted, switches apps, weak network, one hand. Nothing she typed may be lost and no state may be a dead end. Today is Thứ Ba 03/11/2026. Name each frame with its code and Vietnamese title.

1. "19.6 Lưu từ chia sẻ – tiếp tục bản nháp" – the save bottom sheet reopened after an interruption, with an info banner "Bạn đang lưu dở món này lúc 21:14. Thông tin đã được giữ lại." Fields still filled: name "Áo Lovito", "Phân loại: Đen – M", price "250.000 ₫". Filled button "Lưu", text button "Bỏ bản nháp".
2. "19.7 Đã lưu trên máy" – blurred shopping app with snackbar "Đã lưu trên máy. Sẽ đồng bộ khi có mạng." (full text visible, two lines allowed).
3. "11.6 Danh sách – chưa đồng bộ" – Danh sách mong muốn with a thin top banner (cloud-off icon) "Đang ngoại tuyến · 1 món chưa đồng bộ"; the Áo Lovito card has a small status chip with icon "Chưa đồng bộ". Other cards unchanged.
4. "19.3 Lưu từ chia sẻ – link không phải Shopee" – save sheet with link "lazada.vn/…" and an info message (not an error): "Hiện chỉ hỗ trợ Shopee. Bạn vẫn lưu được thủ công, nhưng app sẽ không nhắc sale và không so giá cho món này." Empty name field "Tên món", filled button "Lưu thủ công", text button "Hủy".
5. "03.3 Ghi khoản mua – tiếp tục bản nháp" – "Ghi khoản mua · Bước 1/2" with banner "Tiếp tục khoản mua đang ghi dở" and the amount and name still filled; filled button "Tiếp tục", text button "Bỏ bản nháp".
6. "11.7 Danh sách – cần xem lại" – Danh sách mong muốn when notifications are off: a section "Cần xem lại (1)" at the top with the Tai nghe Bluetooth card ("Đến hẹn 06/11"), and an inline card "Bật thông báo để được nhắc đúng hẹn" with text buttons "Bật" and "Để sau".

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 8 · Chung · Cá nhân và Hồ sơ mua sắm

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Update the profile area so all new settings are reachable, and add the optional shopping profile used by "Cân nhắc món này". Name each frame with its code and Vietnamese title.

1. "10 Cá nhân" – keep the existing profile card, toggles "Nhắc ghi khoản mua", "Nhắc chiêm nghiệm hằng tháng", rows "Xuất dữ liệu" and the red "Xóa toàn bộ dữ liệu". Add a group "Mua sắm" with rows (icon + label + chevron): "Ngân sách tháng", "Hồ sơ mua sắm", "Lịch sale và nhắc", "Thiết bị đã liên kết".
2. "24.1 Hồ sơ mua sắm – trống" – text "Ghi những món bạn đang dùng để phần Cân nhắc nhắc bạn món tương tự. Không bắt buộc." Filled button "Thêm đồ đang dùng".
3. "24.2 Hồ sơ mua sắm" – section "Đồ đang dùng": card "Tai nghe có dây · Công nghệ · dùng 2 năm · thẻ: tai nghe". Section "Phong cách": chip "Tối giản". Section "Thương hiệu hay dùng": empty with text button "Thêm". Floating "+" button.
4. "24.3 Thêm đồ đang dùng" – bottom sheet: fields "Tên món", dropdown "Nhóm ngân sách", tag input "Thẻ", field "Ghi chú" (placeholder "Ví dụ: dùng 2 năm"). Filled button "Lưu", text button "Hủy".

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 9 · Chung · F13 – Liên kết máy tính (trên điện thoại)

```text
Edit the existing "Why I Buy?" project. Keep the current visual style. Add the phone side of flow F13: link the Chrome extension with a one-time 6-digit code, confirm the device, and manage linked devices. Today is Thứ Ba 03/11/2026. Name each frame with its code and Vietnamese title.

1. "25.1 Liên kết máy tính – mã còn hạn" – three numbered steps: "1. Mở tiện ích Why I Buy? trên Chrome", "2. Chọn Liên kết với app", "3. Nhập mã bên dưới". Large code "482 913" in a surface card, text "Mã dùng một lần, hết hạn sau 5 phút." Tonal button "Lấy mã mới". No ticking countdown.
2. "25.2 Liên kết máy tính – mã hết hạn" – same screen, the code is greyed out with text "Mã đã hết hạn". Filled button "Lấy mã mới".
3. "25.3 Xác nhận thiết bị" – dialog: "Cho phép Chrome trên Windows liên kết?" body "Thiết bị này sẽ thêm và xem món trong danh sách mong muốn của bạn." Buttons "Từ chối" (text) and "Cho phép" (filled).
4. "25.4 Thiết bị đã liên kết" – list row: computer icon, "Chrome trên Windows", "Liên kết 03/11 · Đồng bộ 2 phút trước", text button "Thu hồi". Below: tonal button "Liên kết thiết bị mới". Footnote: "Thu hồi sẽ ngắt đồng bộ. Món chưa đồng bộ vẫn còn trên máy tính."

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 10a · Chung · F13 – Chrome extension popup (chế độ Web)

```text
Design the popup of a Chrome extension called "Why I Buy?" – the desktop companion of an existing Android app. Each frame is a 400 x 600 px popup. The extension only reads the current tab URL and title when the user clicks its icon. Saving works WITHOUT signing in or linking; linking is optional and only needed to sync to the phone. Name each frame with its code and Vietnamese title.

1. "X1.1 Đang đọc trang" – grey skeleton blocks (loading under 1 second).
2. "X1.2 Không phải trang sản phẩm" – icon + "Mở một sản phẩm trên shopee.vn để lưu." Buttons "Dán link" (tonal) and "Nhập tay" (text).
3. "X1.3 Sẵn sàng lưu" – header "Lưu vào danh sách mong muốn"; link "shopee.vn · Kính cường lực…" (one line); name field prefilled "Kính cường lực" (editable); price field "180.000 ₫" with helper "Không bắt buộc"; segmented "Giá đơn" · "Khoảng giá" · "Flash Sale"; dropdown "Động cơ: Chưa chọn"; dropdown "Nhóm ngân sách: Chưa chọn". Filled button "Lưu". A small dismissible strip at the bottom: "Chưa liên kết với app · Liên kết" – it does not block saving.
4. "X1.4 Đã có trong danh sách" – "Món này đã lưu" + price chip "180.000 ₫ · Máy tính · 03/11". Buttons "Xem" (tonal), "Cập nhật giá" (filled).
5. "X1.5 Đã lưu trên máy" – check icon, "Đã lưu trên máy", secondary text "Liên kết với app để thấy món này trên điện thoại." Buttons "Mở danh sách" (tonal), "Liên kết" (text).
6. "X1.6 Đã đồng bộ" – check icon, "Đã đồng bộ lên điện thoại" (shown only after the server confirms). Button "Mở danh sách".
7. "X1.7 Liên kết đã bị hủy" – info message "Liên kết đã bị hủy. Dữ liệu chưa đồng bộ vẫn ở trên máy." Filled button "Nhập mã mới".

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion. The Android app is the main product; this Chrome extension (Manifest V3) is a secondary channel to save items quickly while browsing shopee.vn on a computer and to glance at the facts. Message: "Hiểu trước khi thay đổi". The extension never reads prices automatically in this version: the user may type a price, and it is optional. It never blocks buying, never scores the user, never decides for them.

=== STYLE (same design system as the app) ===
Font Be Vietnam Pro, body text at least 14 px. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and destructive actions. 16 px padding, 8 px grid, 12 px corner radius, soft low elevation. Small app logo + "Why I Buy?" in the popup header. Never use orange (Shopee-like) or green/red to mean good/bad.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist"); one entry = "món". Item states: "Đang cân nhắc", "Đã mua", "Bỏ qua".
- Decision buttons "Mua", "Chờ", "Bỏ qua": same size, same tonal style.
- 8 motives: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Sync status chips (icon + text): "Chỉ trên máy", "Đang đồng bộ", "Đã đồng bộ", "Chưa gửi được, sẽ thử lại".
- Address the user as "bạn".

=== PRICE RULES ===
Every price shows its source and date ("180.000 ₫ · Máy tính · 03/11"). No price = "Chưa có giá", never "0 ₫". A saved price is not money spent.

=== SAMPLE DATA (use only this) ===
Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 trên máy tính. Áo Lovito · Thời trang · Khuyến mãi · Đen – M · 250.000 ₫ · 03/11. Khả dụng nhóm Công nghệ: 630.000 ₫. Linked device name: "Chrome trên Windows". Pairing code: 482 913. Today: Thứ Ba 03/11/2026.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "180.000 ₫".
- At most one filled primary button per frame. Click targets at least 40 x 40 px, visible keyboard focus ring, works at 200% zoom. Every state uses icon + text, never color alone. No truncated text in chips.
- Do not draw Shopee's website, logo or orange color.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", countdown timers, scores, badges, red warnings, decorative illustrations, sign-in walls.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 10b · Chung · F13 – Extension: danh sách, ghép thiết bị, cài đặt

```text
Using the same style as the "Why I Buy?" extension popup, add these extension pages. X2 and X5 are full browser pages (1280 px wide, content max 720 px centered); X3 is a Chrome side panel (360 px wide); X4 is shown as three 400 x 600 px popup frames. Name each frame with its code and Vietnamese title.

1. "X2 Danh sách mong muốn (máy tính)" – title, search field, filter chips "Đang cân nhắc", "Đã mua", "Bỏ qua". Rows: Kính cường lực (180.000 ₫ · 03/11, sync chip "Đã đồng bộ"), Áo Lovito (250.000 ₫ · 03/11 · Đen – M, sync chip "Chỉ trên máy"). Each row: "Mở link", "Sửa", overflow menu. Empty variant: "Chưa có món nào. Mở một sản phẩm trên shopee.vn rồi bấm biểu tượng Why I Buy?".
2. "X3 Cân nhắc món này (bảng cạnh)" – side panel for Kính cường lực: blocks "Giá" (180.000 ₫ · Máy tính · 03/11), "Ngân sách" ("Chiếm khoảng 29% phần khả dụng của nhóm Công nghệ"), "Lý do" (Nhu cầu). Three equal buttons "Mua", "Chờ", "Bỏ qua". Variant when not linked: the "Ngân sách" block shows "Thiết lập ngân sách trên app" instead of numbers.
3. "X4.1 Ghép thiết bị – nhập mã" – title "Liên kết với app", text "Mở app Why I Buy? → Cá nhân → Thiết bị đã liên kết → Liên kết máy tính để lấy mã.", six separate digit boxes (filled "482 913"), filled button "Liên kết". "X4.2 Ghép thiết bị – mã sai hoặc hết hạn": same layout, message "Mã không đúng hoặc đã hết hạn. Lấy mã mới trên điện thoại." (does not reveal which). "X4.3 Ghép thiết bị – đang chờ xác nhận": "Hãy xác nhận trên điện thoại" with a small spinner, then success text "Đã liên kết. Món lưu trên máy sẽ được đồng bộ."
4. "X5 Cài đặt và quyền riêng tư" – section "Dữ liệu tiện ích đọc": "Chỉ đọc địa chỉ và tiêu đề tab khi bạn bấm biểu tượng. Không đọc cookie, lịch sử duyệt web hay tài khoản Shopee." Section "Liên kết": "Đã liên kết với điện thoại" + text button "Hủy liên kết". Section "Dữ liệu trên máy": red text button "Xóa dữ liệu trên máy" (only destructive action).

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion. The Android app is the main product; this Chrome extension (Manifest V3) is a secondary channel to save items quickly while browsing shopee.vn on a computer and to glance at the facts. Message: "Hiểu trước khi thay đổi". The extension never reads prices automatically in this version: the user may type a price, and it is optional. It never blocks buying, never scores the user, never decides for them.

=== STYLE (same design system as the app) ===
Font Be Vietnam Pro, body text at least 14 px. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and destructive actions. 16 px padding, 8 px grid, 12 px corner radius, soft low elevation. Small app logo + "Why I Buy?" in the popup header. Never use orange (Shopee-like) or green/red to mean good/bad.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist"); one entry = "món". Item states: "Đang cân nhắc", "Đã mua", "Bỏ qua".
- Decision buttons "Mua", "Chờ", "Bỏ qua": same size, same tonal style.
- 8 motives: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Sync status chips (icon + text): "Chỉ trên máy", "Đang đồng bộ", "Đã đồng bộ", "Chưa gửi được, sẽ thử lại".
- Address the user as "bạn".

=== PRICE RULES ===
Every price shows its source and date ("180.000 ₫ · Máy tính · 03/11"). No price = "Chưa có giá", never "0 ₫". A saved price is not money spent.

=== SAMPLE DATA (use only this) ===
Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 trên máy tính. Áo Lovito · Thời trang · Khuyến mãi · Đen – M · 250.000 ₫ · 03/11. Khả dụng nhóm Công nghệ: 630.000 ₫. Linked device name: "Chrome trên Windows". Pairing code: 482 913. Today: Thứ Ba 03/11/2026.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "180.000 ₫".
- At most one filled primary button per frame. Click targets at least 40 x 40 px, visible keyboard focus ring, works at 200% zoom. Every state uses icon + text, never color alone. No truncated text in chips.
- Do not draw Shopee's website, logo or orange color.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", countdown timers, scores, badges, red warnings, decorative illustrations, sign-in walls.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

## Prompt 11 · Mẫu tinh chỉnh (dùng khi Stitch sai)

Thay phần trong ngoặc vuông bằng lỗi thực tế quan sát được, giữ khối chung ở cuối.

```text
Edit the existing screens. Goal of this round: CONSISTENCY ONLY. Do not change the visual style and do not add anything.

Fix exactly these problems:
1. [Frame "20.1 Cân nhắc món này": the "Mua" button is filled indigo while "Chờ" and "Bỏ qua" are outlined → make the three buttons the same tonal style and the same width.]
2. [Frame "11 Danh sách mong muốn": the chip "Đang cân nhắc (4)" is truncated → allow the chip row to scroll horizontally, never cut text.]
3. [Frame "21.1": remove the added card "Khoảng lặng 48 giờ" – it was not requested.]
4. [All frames: replace "Wishlist" with "Danh sách mong muốn".]

The same item must keep the same name, price, date and variant on every frame. Use only the sample data below.

=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

---

## Phụ lục · Khối chung

Hai khối dưới đây đã được chèn sẵn vào cuối từng prompt; để ở đây cho dễ sửa một chỗ.

### Khối chung – app Android

```text
=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion for Android, inspired by "The Psychology of Money". Message: "Hiểu trước khi thay đổi". Users save items they are considering (shared from the Shopee app, saved from a Chrome extension, or added by hand) into "Danh sách mong muốn", weigh them against facts they entered themselves (price they saw, a monthly budget they set, things they already own, announced sale days), choose "Mua", "Chờ" or "Bỏ qua", and later reflect on why they bought. The app never blocks buying, never scores the user and never decides for them. Code computes the numbers; the app only states facts and says clearly when data is missing.

=== STYLE (keep exactly) ===
Android 360 x 800 dp, Material 3, light theme, font Be Vietnam Pro. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and delete actions. 16 dp side margins, 8 dp grid, 12–16 dp corner radius, soft low elevation. Bottom navigation (5 tabs): Trang chủ, Lịch sử, Mô hình, Góc nhìn, Cá nhân; selected tab = pill background + bold label. Never use orange (Shopee-like), and never use green/red to mean good/bad. Budget meters are indigo on #E8F0EB; over the limit = grey #545E59 diagonal stripes + text, never red.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist" or "giỏ hàng"); one entry = "món".
- Item states, only these three: "Đang cân nhắc", "Đã mua", "Bỏ qua". "Chờ" is a button, NOT a state: a waiting item stays "Đang cân nhắc" with a bell line "Xem lại 06/11".
- Decision buttons always appear together as "Mua", "Chờ", "Bỏ qua": same size, same tonal style, icon + label. None of them is the filled primary button.
- One purchase = "khoản mua"; the action = "Ghi khoản mua"; the amount actually paid = "Giá thực trả". "Mua" opens "Ghi khoản mua" prefilled; the item becomes "Đã mua" only after it is saved.
- 8 motives, exact names and order: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Always icon + label, one chip per item.
- Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Screen for weighing an item: "Cân nhắc món này". Summary chips allowed: "Cần giá gần đây", "Có thể chờ", "Vượt phần khả dụng", "Trong ngân sách", "Chưa đủ dữ liệu".
- Address the user as "bạn". Prefer "có thể", "bạn đã ghi", "chưa đủ dữ liệu".

=== PRICE RULES ===
Every price shows its source and date, e.g. "420.000 ₫ · Bạn nhập · 06/11 · Đen". Sources: "Bạn nhập", "Chia sẻ", "Máy tính". No price = "Chưa có giá" (never "0 ₫"). A price older than 7 days has a dashed outline, the text "Giá ghi 10/10" and a text button "Xác nhận lại". A saved price is NOT money spent: it is never added to any total. Price changes are indigo text with an arrow ("↓ Thấp hơn lúc lưu 8%"), not green or red.

=== SAMPLE DATA (use only this) ===
Danh sách mong muốn:
- Tai nghe Bluetooth · Công nghệ · Khuyến mãi · lưu 03/11 từ Chia sẻ · no price at first; later 420.000 ₫ (Bạn nhập, 06/11, phân loại Đen); bought 06/11, giá thực trả 399.000 ₫, có dùng mã giảm giá.
- Áo Lovito · Thời trang · Khuyến mãi · phân loại Đen – M · 250.000 ₫ (Bạn nhập, 03/11) · lưu 03/11 từ Chia sẻ.
- Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 từ Máy tính.
- Áo khoác · Thời trang · Mong muốn · 420.000 ₫ (Giá ghi 10/10) · lưu 10/10 Nhập tay · mức ưu tiên 2 sao.
Ngân sách tháng 11: Thời trang 1.500.000 ₫ (đã chi 400.000 ₫, khả dụng cho danh sách 864.000 ₫); Công nghệ 1.000.000 ₫ (đã chi 200.000 ₫, khả dụng 630.000 ₫); Làm đẹp 300.000 ₫ (đã chi 350.000 ₫, đã vượt 50.000 ₫).
Hồ sơ mua sắm: Tai nghe có dây (Công nghệ, dùng 2 năm). Đợt sale đã xác nhận: 11.11 (Thứ Tư 11/11/2026). Mã liên kết: 482 913.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "420.000 ₫".
- At most one filled primary button per screen. Touch targets at least 48 dp. Body text at least 14 sp. Text contrast at least 4.5:1. Every state uses icon + text, never color alone. Text in chips and snackbars must never be truncated.
- Do not draw the Shopee app, its logo or its orange color; a shopping app in the background is a generic blurred placeholder.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", "giá thời gian thực", countdown timers, "hạ nhiệt", "suy ngẫm", "tĩnh tâm", "khoảng lặng", "48h", scores, streaks, badges, red warnings, decorative illustrations, or guesses about the user's psychology.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```

### Khối chung – Chrome extension

```text
=== PRODUCT ===
"Why I Buy?" is a calm, non-judgmental shopping companion. The Android app is the main product; this Chrome extension (Manifest V3) is a secondary channel to save items quickly while browsing shopee.vn on a computer and to glance at the facts. Message: "Hiểu trước khi thay đổi". The extension never reads prices automatically in this version: the user may type a price, and it is optional. It never blocks buying, never scores the user, never decides for them.

=== STYLE (same design system as the app) ===
Font Be Vietnam Pro, body text at least 14 px. Background #F5F6F2, surface #FFFFFF, surface-container #E8F0EB, primary indigo #2E4A9E, primary-container #E3E8F7, text #1A2320, secondary text #545E59, outline #8A918A, error #B3261E ONLY for input errors and destructive actions. 16 px padding, 8 px grid, 12 px corner radius, soft low elevation. Small app logo + "Why I Buy?" in the popup header. Never use orange (Shopee-like) or green/red to mean good/bad.

=== VOCABULARY (use exactly) ===
- "Danh sách mong muốn" (never "Wishlist"); one entry = "món". Item states: "Đang cân nhắc", "Đã mua", "Bỏ qua".
- Decision buttons "Mua", "Chờ", "Bỏ qua": same size, same tonal style.
- 8 motives: Nhu cầu, Mong muốn, Khuyến mãi, Ảnh hưởng MXH, Quảng cáo, Cảm xúc, Tiện lợi, Khác. Budget groups: Ăn uống, Thời trang, Công nghệ, Làm đẹp, Học tập, Khác.
- Sync status chips (icon + text): "Chỉ trên máy", "Đang đồng bộ", "Đã đồng bộ", "Chưa gửi được, sẽ thử lại".
- Address the user as "bạn".

=== PRICE RULES ===
Every price shows its source and date ("180.000 ₫ · Máy tính · 03/11"). No price = "Chưa có giá", never "0 ₫". A saved price is not money spent.

=== SAMPLE DATA (use only this) ===
Kính cường lực · Công nghệ · Nhu cầu · 180.000 ₫ · lưu 03/11 trên máy tính. Áo Lovito · Thời trang · Khuyến mãi · Đen – M · 250.000 ₫ · 03/11. Khả dụng nhóm Công nghệ: 630.000 ₫. Linked device name: "Chrome trên Windows". Pairing code: 482 913. Today: Thứ Ba 03/11/2026.

=== CONSTRAINTS ===
- All UI text in Vietnamese WITH full diacritics; money as "180.000 ₫".
- At most one filled primary button per frame. Click targets at least 40 x 40 px, visible keyboard focus ring, works at 200% zoom. Every state uses icon + text, never color alone. No truncated text in chips.
- Do not draw Shopee's website, logo or orange color.
- Never show: "tiết kiệm được", "nên mua", "không nên mua", "chắc chắn giảm", countdown timers, scores, badges, red warnings, decorative illustrations, sign-in walls.
- Do not add any feature, card, tip, statistic, label or screen that is not described in this prompt.
```
