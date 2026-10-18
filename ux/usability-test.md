# Kiểm thử khả dụng – Why I Buy?

> **Cập nhật 18/10/2026:** toàn bộ file này áp dụng cho **Flow 1–10 (hướng cũ)** trên file Figma cũ. **F11–F13 của hướng Smart Shopping Companion chưa được kiểm thử**, kể cả mô phỏng. Kế hoạch kiểm thử thật cho hướng mới (5 người, F11–F13, KPI-01 → KPI-05) ở `ux/persona.md` mục 11–12 và `ux/research.md` mục 11.

> **Đọc trước:** kết quả ở mục 6–7 là **MÔ PHỎNG bằng AI**, không phải 5 người thật.
>
> - Cách làm: AI đóng vai 5 người tham gia, đi qua prototype Figma theo từng nhiệm vụ (cognitive walkthrough, nói to suy nghĩ). Thời gian được **tính** bằng mô hình KLM (Keystroke-Level Model), không bấm giờ.
> - Script, seed và số liệu nằm trong `research-pack/usability_sim.py` và `usability-sim.json`.
> - Kịch bản ở mục 3–4 và phiếu ghi ở mục 10 **dùng nguyên được cho kiểm thử thật**. Nếu nhóm test được người thật, chỉ cần thay số ở mục 6–7.
>
> Phát hiện F1 là lỗi **có thật trong file Figma**, nhìn thấy được trên prototype. F4 có thật một phần: dòng "Mở cài đặt" nhỏ (khối cao 44 dp) là có thật trong file.
>
> **Cập nhật 14/10/2026:** khi sửa R4, nhóm rà lại prototype và thấy công tắc nhắc nhở **có** mở màn 05a. Bản mô phỏng trước giả định công tắc không phản hồi, nên kết quả T5 (1 người bỏ cuộc) bị sai. Mục 6–7 đã được tính lại theo đúng prototype.

## 1. Mục tiêu

1. Kiểm tra tiêu chí của persona: ghi một khoản mua kèm động cơ **≤ 25 giây** (P1, P4); thêm một món mong muốn **< 20 giây** (P1, P3).
2. Tìm các chỗ người dùng phân vân, đi lạc hoặc làm sai, để sửa ở vòng **R4**.
3. Đo mức dễ dùng tổng thể bằng SEQ (từng nhiệm vụ) và SUS (cả app).

## 2. Phương pháp

| Mục | Cách làm |
|---|---|
| Prototype | Figma, page **06 Prototype**, flow "★ Toàn bộ ứng dụng", khung Android 360 × 800 |
| Người tham gia | 5 người mô phỏng (U1–U5), gần với P1–P4 (mục 5) |
| Đi qua nhiệm vụ | AI nhận ảnh chụp từng khung trên đường đi của nhiệm vụ, đóng vai người tham gia, nói to suy nghĩ và chọn chỗ chạm. Chạm sai thì được xem khung kế tiếp đúng như prototype phản hồi |
| Tính thời gian | KLM (mục 4.2) × hệ số làm quen của từng người + thời gian đi lạc + dao động ngẫu nhiên −0,6…+0,9 giây (seed 393) |
| Đo cảm nhận | SEQ 1–7 sau mỗi nhiệm vụ; SUS 10 câu ở cuối buổi |
| Mức nặng | Thang Nielsen 0–4 (0 = không phải lỗi, 4 = thảm họa) |

**Vì sao dùng KLM.** Người mô phỏng không bấm giờ được. KLM là mô hình kinh điển của Card, Moran và Newell (1980), dự đoán thời gian một người **thành thạo** làm một nhiệm vụ bằng cách cộng thời gian các thao tác cơ bản. Hệ số làm quen (1,15–1,45) đại diện cho người dùng lần đầu thấy prototype.

### Prompt mô phỏng đi qua nhiệm vụ (nguyên văn)

```text
Bạn đóng vai người tham gia kiểm thử khả dụng, không phải trợ lý AI.
Hồ sơ: {hồ sơ U.. ở mục 5}. Bạn chưa từng thấy app này.
Tôi sẽ gửi ảnh màn hình hiện tại và một nhiệm vụ. Với mỗi ảnh:
1. Nói to điều bạn nhìn thấy và đang nghĩ (1–3 câu, tiếng Việt nói).
2. Cho biết bạn sẽ chạm vào đâu (gọi đúng chữ hoặc vị trí trên màn hình).
Quy tắc: chỉ dựa vào những gì có trên ảnh; không đoán tính năng không thấy.
Được phép chạm sai, phân vân, hoặc nói "tôi bỏ cuộc" nếu sau khoảng 60 giây vẫn không tìm ra.
Không cố làm đúng ý người hướng dẫn.
Nhiệm vụ: {T..}
```

## 3. Lời dẫn cho người hướng dẫn (đọc nguyên văn)

> "Cảm ơn bạn đã tham gia. Hôm nay chúng mình kiểm tra **ứng dụng**, không kiểm tra bạn, nên không có câu trả lời sai. Bạn cứ nói to điều mình đang nghĩ trong lúc làm. Mình sẽ không gợi ý trong lúc bạn làm; nếu bí quá bạn cứ nói 'mình bỏ qua'. Buổi này khoảng 10 phút, có 5 nhiệm vụ. Bạn đồng ý cho mình quay màn hình (không quay mặt) chứ?"

Sau mỗi nhiệm vụ hỏi SEQ: *"Nhiệm vụ vừa rồi dễ hay khó? Chấm từ 1 (rất khó) đến 7 (rất dễ)."*

## 4. Nhiệm vụ

### 4.1. Danh sách nhiệm vụ

| # | Lời giao nhiệm vụ | Khung bắt đầu | Thành công khi | Mục tiêu |
|---|---|---|---|---|
| T1 | "Bạn vừa mua một ly **trà sữa nướng 45.000 ₫** vì đang buồn. Hãy ghi lại khoản mua này." | 00 Trang chủ (Hub) | Tới màn "Khoản mua đã lưu", động cơ là Cảm xúc | ≤ 25 giây |
| T2 | "Bạn đang thèm một **bàn phím cơ**. Hãy lưu nó lại để suy nghĩ thêm, chưa mua." | 00 Trang chủ (Hub) | Món mới có trong Danh sách mong muốn | < 20 giây |
| T3 | "Tháng 9 bạn mua vì động cơ nào nhiều nhất?" | 07 Mô hình (đang ở tháng 10) | Nói đúng "Khuyến mãi" | ≤ 10 giây |
| T4 | "Bạn vừa nhập sai mật khẩu. Hãy đăng nhập lại." | 07a Đăng nhập – lỗi | Vào được Trang chủ | Tự sửa được, không cần trợ giúp |
| T5 | "Lúc trước bạn chọn 'Để sau' khi app xin gửi thông báo. Giờ bạn muốn được nhắc mỗi tối. Hãy bật lại." | 10 Cá nhân – chưa cấp quyền thông báo | Tới 05a và chạm nút bật thông báo | Tự tìm được |

### 4.2. Thời gian chuẩn theo KLM

Thời gian thao tác:

- **M** (nghĩ hoặc quyết định) = 1,35 giây. Theo Card, Moran & Newell (1980).
- **P** (chạm một nút bằng ngón cái) = 0,6 giây. Đây là giả định của nhóm cho màn hình cảm ứng, vì KLM gốc đo trên chuột.
- **K** (gõ một phím trên bàn phím ảo) = 0,33 giây. Tương đương khoảng 36 từ/phút, gần mức gõ trung bình trên điện thoại trong nghiên cứu của Palin và cộng sự (MobileHCI 2019).
- **R** (chờ hệ thống) lấy đúng độ trễ trong prototype: "Đang lưu" 1,2 giây.

Tiếng Việt gõ theo kiểu Telex:

- "Trà sữa nướng" = `traf suwxa nuowngs`: 18 phím (tính cả dấu cách).
- "Bàn phím cơ" = `bafn phism cow`: 14 phím.
- Số tiền "45" + phím "000" = 3 phím.

| # | Chuỗi thao tác | M | P | K | R | **Thời gian chuẩn** |
|---|---|:-:|:-:|:-:|:-:|:-:|
| T1 | M chạm "Ghi khoản mua" → gõ 45 + 000 → M chạm ô tên → gõ tên (18) → chạm "Tiếp tục" → M chọn "Cảm xúc" → chạm "Lưu" → chờ lưu | 4 | 5 | 21 | 1,2 | **16,5 giây** |
| T2 | M chạm thẻ Danh sách mong muốn → M chạm "Thêm món" → chạm ô tên → gõ tên (14) → M chọn lý do → chạm "Lưu món" | 3 | 5 | 14 | 0 | **11,7 giây** |
| T3 | M tìm cách đổi tháng → chạm "‹" → M đọc động cơ đầu bảng | 2 | 1 | 0 | 0 | **3,3 giây** |
| T4 | M đọc lỗi → chạm ô mật khẩu → gõ 8 ký tự → chạm "Đăng nhập" | 1 | 2 | 8 | 0 | **5,2 giây** |
| T5 | M tìm chỗ bật → chạm "Mở cài đặt" → M đọc 05a → chạm nút bật thông báo | 2 | 2 | 0 | 0 | **3,9 giây** |

Ghi chú: trên prototype, số tiền và tên món ở bước 1 đã điền sẵn. KLM tính như app thật, tức là người dùng phải gõ.

## 5. Người tham gia (MÔ PHỎNG)

| Mã | Hồ sơ | Gần persona | Hệ số làm quen | Ghi chú |
|---|---|---|:-:|---|
| U1 | Nam, 22, SV năm cuối, dùng Shopee hằng ngày | P1 | 1,15 | Quen app di động |
| U2 | Nữ, 26, nhân viên văn phòng | P2 | 1,25 | |
| U3 | Nam, 19, SV năm 2 | P3 | 1,20 | |
| U4 | Nữ, 30, kế toán, có con nhỏ | P4 | 1,35 | Làm toàn bộ bằng **một tay** |
| U5 | Nam, 28, làm tự do, ít dùng app tài chính | P1 / P2 | 1,45 | Ít quen Material Design |

## 6. Kết quả (MÔ PHỎNG)

### 6.1. Thời gian từng người (giây)

| | T1 | T2 | T3 | T4 | T5 |
|---|:-:|:-:|:-:|:-:|:-:|
| U1 | 19,0 | 13,1 | 3,2 | 6,5 | 4,6 |
| U2 | 20,3 | 14,3 | 4,8 | 6,0 | 5,7 ⚠ |
| U3 | 24,9 ⚠ | 17,2 | 3,7 | 6,5 | 4,8 |
| U4 | 21,7 | 15,4 | 8,8 ⚠ | 7,5 | 7,0 ⚠ |
| U5 | **31,1** ⚠ | 17,2 | 12,4 ⚠ | 7,7 | 8,8 ⚠ |

⚠ = có đi lạc hoặc phân vân (xem mục 7). U1 làm T3 nhanh hơn thời gian chuẩn 0,1 giây do dao động ngẫu nhiên: KLM là ước lượng trung bình, không phải giới hạn dưới.

### 6.2. Tổng hợp

| | Hoàn thành | Trung bình | Trung vị | Nhanh nhất – chậm nhất | Đạt mục tiêu | SEQ TB (1–7) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| T1 Ghi khoản mua | 5/5 | 23,4 giây | **21,7 giây** | 19,0 – 31,1 | **4/5** (≤ 25 giây) | 5,8 |
| T2 Thêm món mong muốn | 5/5 | 15,4 giây | **15,4 giây** | 13,1 – 17,2 | **5/5** (< 20 giây) | 6,2 |
| T3 Động cơ tháng 9 | 5/5 | 6,6 giây | 4,8 giây | 3,2 – 12,4 | 4/5 (≤ 10 giây) | 5,4 |
| T4 Sửa lỗi đăng nhập | 5/5 | 6,8 giây | 6,5 giây | 6,0 – 7,7 | 5/5 | 6,6 |
| T5 Bật lại nhắc nhở | 5/5 | 6,2 giây | 5,7 giây | 4,6 – 8,8 | 5/5 | 5,2 |

**Đọc nhanh:**

- Tiêu chí 25 giây **đạt ở 4/5 người**. Người không đạt (U5) chậm vì phân vân giữa các động cơ (F2), không phải vì số bước.
- T5: cả 5 người hoàn thành, nhưng 3/5 chạm công tắc trước rồi mới hiểu app đang xin quyền thông báo (F4).
- T4 tốt: cả 5 người tự sửa được. Thông báo lỗi kèm cách sửa phát huy tác dụng.

### 6.3. SUS (MÔ PHỎNG)

Mười câu SUS bản tiếng Việt, mỗi câu chấm 1 (rất không đồng ý) đến 5 (rất đồng ý):

1. Tôi nghĩ tôi sẽ muốn dùng app này thường xuyên.
2. Tôi thấy app phức tạp không cần thiết.
3. Tôi thấy app dễ dùng.
4. Tôi nghĩ tôi cần người kỹ thuật hỗ trợ mới dùng được app.
5. Các chức năng trong app gắn kết tốt với nhau.
6. Tôi thấy app có nhiều chỗ không nhất quán.
7. Tôi nghĩ phần lớn mọi người sẽ học dùng app rất nhanh.
8. Tôi thấy app rất rườm rà khi dùng.
9. Tôi thấy tự tin khi dùng app.
10. Tôi cần học nhiều thứ trước khi dùng được app.

| | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | **Điểm SUS** |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| U1 | 5 | 1 | 5 | 1 | 4 | 2 | 5 | 1 | 4 | 1 | **92,5** |
| U2 | 4 | 2 | 4 | 1 | 4 | 2 | 5 | 2 | 4 | 2 | **80,0** |
| U3 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 1 | **77,5** |
| U4 | 4 | 2 | 4 | 1 | 3 | 2 | 4 | 2 | 4 | 2 | **75,0** |
| U5 | 3 | 2 | 4 | 2 | 3 | 3 | 4 | 2 | 3 | 2 | **65,0** |
| **TB** | | | | | | | | | | | **78,0** |

Cách tính: câu lẻ lấy (điểm − 1), câu chẵn lấy (5 − điểm), cộng lại rồi nhân 2,5. Mốc tham khảo: 68 là mức trung bình.

## 7. Phát hiện

| Mã | Vấn đề | Nhiệm vụ | Bằng chứng | Nguyên tắc | Mức nặng |
|---|---|---|---|---|:-:|
| **F1** | Ở bước 2, thẻ "Cảm xúc" **đã được chọn sẵn** và nút "Lưu" bấm được ngay. Người dùng có thể lưu mà không tự chọn động cơ | T1 | 3/5 (U1, U2, U4) chạm "Lưu" mà không chạm thẻ nào. Hỏi lại sau nhiệm vụ, U2: "Ủa, nó chọn sẵn à? Mình tưởng mình chọn rồi." **Lỗi có thật trong Figma**: khung 04 Bước 2/2 dùng thẻ Cảm xúc ở trạng thái Selected | Nielsen #5 Phòng ngừa lỗi; mục tiêu cốt lõi của app là ghi **đúng** động cơ | **3** |
| **F4** | Khi chưa cấp quyền thông báo, lý do chỉ nằm trong một dòng chữ nhỏ "Chưa cấp quyền thông báo · Mở cài đặt" (khối cao 44 dp, thấp hơn mức 48 dp). Công tắc trông như đang tắt bình thường | T5 | 3/5 (U2, U4, U5) chạm công tắc trước. Công tắc mở màn 05a nên vẫn hoàn thành, nhưng cả ba dừng lại vì tưởng công tắc sẽ bật ngay. U4: "Ủa, sao lại sang màn khác?" | Nielsen #1 Hiển thị trạng thái; #6 Nhận ra hơn nhớ lại; vùng chạm ≥ 48 dp | **2** |
| **F2** | Khó phân biệt "Mong muốn" và "Cảm xúc". Nút "?" (giải thích 8 động cơ) nằm trên thanh tiêu đề, không ai để ý | T1 | U3, U5 phân vân, mất thêm 5–6,5 giây; cả hai đều không chạm "?". U5: "Mua vì buồn thì là mong muốn hay cảm xúc nhỉ?" | Nielsen #10 Trợ giúp; #6 | **2** |
| F3 | Có hai cách đổi tháng: mũi tên "‹ ›" (48 × 48 dp) và chip "Tháng 10/2026 ▾" mở sheet chọn tháng. Hai người không dùng cách ngắn nhất | T3 | U4 dùng chip (+4 giây, vẫn đúng); U5 vào tab Lịch sử trước (+7 giây) | Nielsen #7 Linh hoạt và hiệu quả | 1 |
| F5 | Ở 12 Thêm món, một người hỏi "Giá dự kiến" có bắt buộc không | T2 | U3 cuộn tìm và hỏi (+3 giây). Nhãn đã ghi "(tùy chọn)" | — | 1 |

**Điểm tốt nên giữ:**

- T4: 5/5 tự sửa lỗi đăng nhập, SEQ 6,6.
- T2: 5/5 dưới 20 giây.
- Không ai thắc mắc về giọng văn hay thấy bị phán xét. U1: "App không la mình, thích."

## 8. Vòng R4: đã sửa trong Figma (14/10/2026)

Ảnh trước: `assets/figma/04-purchase-reason.png`. Ảnh sau: `r4-sau-04-chua-chon.png`, `r4-sau-04-da-chon.png`, `r4-sau-10-ca-nhan.png`.

| Mã | Đã sửa | Khung Figma | Kết quả |
|---|---|---|---|
| **R4-1** (F1) | Bước 2 mở ra **không có thẻ nào được chọn**. Nút "Lưu" bị khóa, phía trên có dòng "Chọn một động cơ để lưu". Chạm một thẻ bất kỳ thì thẻ được chọn và nút "Lưu" bật | 03 Final UI: thêm khung "04 Ghi khoản mua – Bước 2/2 (chưa chọn động cơ)" trong Khung trạng thái; khung 04 cũ là trạng thái sau khi chọn. 06 Prototype: khung 04 mở ra ở trạng thái chưa chọn; 2 biến prototype `dongCo/daChon`, `dongCo/chuaChon` điều khiển nút; "Tiếp tục" ở bước 1 và nền mờ của sheet giải thích đặt lại trạng thái | Không còn lưu theo lựa chọn có sẵn. Thời gian chuẩn KLM không đổi (16,5 giây), vì KLM đã tính 1 chạm chọn động cơ |
| **R4-2** (F4) | Bỏ dòng chữ nhỏ. Thêm thẻ "Thông báo đang tắt": icon chuông, câu "Bạn chưa cho phép thông báo nên app chưa thể nhắc bạn ghi khoản mua.", nút Tonal "Mở cài đặt" cao 48 dp → 05a. Công tắc vẫn mở 05a | 10 Cá nhân – chưa cấp quyền thông báo (Final UI và Prototype) | Lý do và cách sửa hiện rõ trước khi người dùng chạm công tắc; vùng chạm ≥ 48 dp |
| **R4-3** (F2) | Thêm nút chữ "Giải thích động cơ" (cao 48 dp) ngay cạnh câu "Vì sao bạn mua?", mở sheet giải thích như nút "?". Câu phụ rút còn một dòng ("Chọn động cơ gần nhất lúc bạn quyết định mua."), khoảng cách giữa các khối 12 → 8 dp để ô ghi chú vẫn nằm trong màn 800 dp | Cả 16 khung Bước 2/2 (6 ở Final UI, 10 ở Prototype, gồm khung sửa và khung từ danh sách mong muốn) | Trợ giúp nằm ngay chỗ người dùng phân vân |
| — (F3) | **Không sửa.** Thiết kế đã có mũi tên 48 × 48 dp và chip "Tháng 10/2026 ▾"; cả hai cách đều đúng. Đề xuất R4-4 cũ được bỏ | — | — |
| — (F5) | **Không sửa.** Nhãn đã ghi "(tùy chọn)"; chỉ 1/5 người hỏi | — | — |

**Giữ nguyên có chủ đích:** khung "Sửa khoản mua – Bước 2/2" và các khung "từ danh sách mong muốn" vẫn chọn sẵn động cơ, vì động cơ đó do chính người dùng chọn trước đó (khi ghi hoặc khi thêm món).

**Sửa thêm khi làm R4:** biến thể nút Disabled hiển thị chữ và icon đậm như nút thường (độ mờ 38% bị mất ở instance). Đã chuyển sang độ mờ của lớp, nên mọi nút bị khóa trong file (ví dụ "Tiếp tục" ở 03a) giờ hiển thị đúng.

## 9. Hạn chế

1. Người tham gia là mô phỏng. AI "nhìn" ảnh tĩnh và không có thói quen tay thật, nên không phát hiện được lỗi về cảm giác chạm, tốc độ hoạt ảnh hay độ chói.
2. Thời gian là **ước lượng KLM**, không phải bấm giờ. Giá trị P = 0,6 giây là giả định của nhóm.
3. Hệ số làm quen và thời gian đi lạc do nhóm đặt. Thời gian đi lạc được ước bằng KLM của các bước thừa rồi làm tròn.
4. F1 là lỗi có thật, kiểm lại được trực tiếp trong Figma; F4 có thật một phần (dòng chữ nhỏ 44 dp). F2, F3 là dự đoán, cần người thật để xác nhận.
5. Bản mô phỏng đầu tiên giả định sai hành vi của công tắc ở T5. Bài học: AI "nhìn ảnh tĩnh" không biết chỗ nào có tương tác; phải đối chiếu với prototype trước khi kết luận.

## 10. Phiếu ghi cho kiểm thử thật (👥 in ra, mỗi người một tờ)

```text
Mã người tham gia: U__   Tuổi: ___   Nghề: ________   Cầm máy: một tay / hai tay
Thiết bị: __________   Ngày: __/__/2026   Người hướng dẫn: ________

| Nhiệm vụ | Bắt đầu (s) | Kết thúc (s) | Thời gian | Hoàn thành (Có / Có trợ giúp / Không) | Lỗi hoặc đi lạc (ghi chạm sai ở đâu) | SEQ 1–7 | Câu nói đáng chú ý |
| T1 | | | | | | | |
| T2 | | | | | | | |
| T3 | | | | | | | |
| T4 | | | | | | | |
| T5 | | | | | | | |

SUS (1–5):  C1 __ C2 __ C3 __ C4 __ C5 __ C6 __ C7 __ C8 __ C9 __ C10 __   → Điểm: ____
Câu hỏi cuối: "Điều gì làm bạn khó chịu nhất?" ____________________
```

Cách bấm giờ: mở Figma prototype trên điện thoại (app Figma, chế độ Mirror hoặc link prototype) và quay màn hình. Thời gian tính từ lúc đọc xong nhiệm vụ tới lúc thấy khung thành công.
