# Persona – Why I Buy?

> Thay toàn bộ `ux/persona.md` hiện tại.
>
> Mọi persona được rút ra từ [`research.md`](../../../ux/research.md). Mã nguồn dữ liệu: D = desk research (thật), C = rà app (thật), Q = câu khảo sát, S = người trả lời khảo sát, I = phỏng vấn. **Q, S, I là dữ liệu MÔ PHỎNG bằng AI.** Câu nói của mỗi persona trích từ phỏng vấn mô phỏng, có ghi mã người nói.
>
> Không dùng ảnh người thật hay ảnh stock. Mỗi persona dùng chữ cái đầu tên trong vòng tròn màu, giống avatar trong app.

## 1. Tổng quan

| # | Persona | Vai trò | Vì sao có persona này | Flow phục vụ chính |
|---|---|---|---|---|
| P1 | **Nguyễn Hải Nam, 22**: SV năm cuối CNTT kiêm thực tập | **Persona chính** | Đại diện nhóm 18–25 tuổi, chiếm 19/30 mẫu và dồn vào đúng vấn đề app giải quyết | Flow 1, 3, 6, 7, 8 |
| P2 | **Trần Thu Linh, 26**: nhân viên hành chính văn phòng | Phụ | Mua theo cảm xúc sau giờ làm, muốn hiểu vì sao cứ lặp lại | Flow 2, 4, 8, 10 |
| P3 | **Lê Gia Huy, 19**: SV năm 2 | Phụ | Bị bạn bè và KOL kéo theo, ngân sách nhỏ, hay hối tiếc | Flow 6, 9 |
| P4 | **Phạm Ngọc Mai, 29**: kế toán, có con 2 tuổi | Phụ | Rất ít thời gian, luôn dùng một tay, muốn xem cả tháng | Flow 1, 4, 5 |
| P5 | **Đỗ Văn Hùng, 58**: nhân viên sắp nghỉ hưu | **Anti-persona** | Nhóm app **không** nhắm tới, có số liệu giải thích | Không (dùng để giới hạn phạm vi) |

**Vì sao 5 persona.** Một persona chính để mọi quyết định thiết kế có một người cụ thể làm chuẩn. Ba persona phụ phủ ba nhóm hành vi khác nhau mà research tìm ra: cảm xúc (INS3, INS4), ảnh hưởng xã hội (INS5, INS6), thiếu thời gian (INS1, INS7). Một anti-persona trả lời câu hỏi "vì sao không làm cho người lớn tuổi" bằng dữ liệu.

## 2. Vì sao P1 là persona chính

| Tiêu chí | 18–25 (n = 19) | 26–30 (n = 6) | 31+ (n = 5) | Nguồn |
|---|:-:|:-:|:-:|---|
| Chốt đơn sau 22h | **11/19** | 2/6 | 0/5 | Q6 |
| Đã dùng app chi tiêu rồi bỏ | **12/19** | 4/6 | 0/5 | Q8 |
| Hối tiếc từ 3 lần/tháng trở lên | **13/19** | 2/6 | 0/5 | Q14 |
| Cảm giác với cảnh báo đỏ (TB, 1 = rất khó chịu) | **1,79** | 2,33 | 4,60 | Q12 |
| Muốn biết vì sao mua (TB, 1–5) | **4,21** | 3,83 | 3,00 | Q11 |
| Tỉ trọng người mua online hằng tuần | Gen Z chiếm 53,4% | — | — | D1 (thật) |

Nhóm 18–25 có vấn đề nặng nhất ở cả 5 chỉ số, và cũng là nhóm mua online nhiều nhất theo nguồn thật D1. Thiết kế đúng cho nhóm này trước thì giải quyết được phần lớn nhu cầu của P2–P4. Ngược lại thì không đúng: thiết kế cho P4 trước sẽ bỏ sót việc ghi khoản mua lúc khuya, việc né cảnh báo đỏ và danh sách mong muốn.

## 3. P1 – Nguyễn Hải Nam, 22 (persona chính)

**Thông tin cơ bản**

- Sinh viên năm cuối ngành CNTT, thực tập ở một công ty công nghệ.
- Thu nhập 6–9 triệu/tháng (lương thực tập và trợ cấp).
- Sống ở nhà trọ tại TP.HCM.

**Một ngày của Nam**

- 8:30–17:30: thực tập, ăn trưa đặt ShopeeFood cùng đồng nghiệp.
- 19:00–22:00: làm đồ án tốt nghiệp ở nhà trọ hoặc quán cà phê.
- Sau 22:00: nằm lướt TikTok, Shopee cho đỡ mệt. Đây là lúc hay đặt đồ ăn khuya và chốt flash sale.

**Hành vi mua**

- Mua online 2–3 lần/tuần, chủ yếu Shopee và ShopeeFood.
- Món thường mua: đồ ăn khuya, phụ kiện công nghệ khi có flash sale.
- Đã cài Money Lover năm nhất, ghi được 2 tuần rồi bỏ.

**Thiết bị và accessibility**

- Android 6,5 inch, cầm **một tay** khi nằm hoặc đi bộ; ngón cái chỉ với tới nửa dưới màn hình.
- Cận 2 độ, nên cần chữ ≥ 14 sp và tương phản cao.

**Mục tiêu**

1. Ghi một khoản mua ngay sau khi thanh toán, **≤ 25 giây**, không phải chọn danh mục.
2. Hiểu điều gì khiến mình mua: sale, mệt, hay cần thật.
3. Nhìn lại mà không bị "la mắng".

**Pain point**

| Pain point | Bằng chứng |
|---|---|
| Nhập lâu, nhiều trường nên bỏ app | Q9: 10/16; I1: "Chọn danh mục, ví, ngày… lười lắm" |
| Hay quên ghi | Q9: 12/16 |
| Thấy cảnh báo đỏ thì thấy tội lỗi rồi tắt app | Q12: 1,79 ở nhóm 18–25; I1 |
| Bị đồng hồ đếm ngược của flash sale thúc mua | Q7: khuyến mãi 21/30; D2: FOMO → mua bốc đồng (β = 0,931); I1 |

**Câu nói (I1):**

> "Thấy màu đỏ là em tắt app. Biết là tiêu nhiều rồi, nhìn thêm chỉ thấy tội lỗi."

**Kịch bản dùng app**

1. 23:10, Nam đặt một ly trà sữa nướng 45.000 ₫.
2. Thanh toán xong, Nam mở Why I Buy?, chạm "Ghi khoản mua".
3. Bước 1: nhập số tiền và tên món; thời điểm đã điền sẵn "Hôm nay 23:10".
4. Bước 2: chọn động cơ "Cảm xúc", rồi chạm "Lưu".
5. Cuối tuần, Nam mở Mô hình và thấy phần lớn khoản sau 22h gắn với Cảm xúc và Khuyến mãi.

**Tiêu chí thành công (đo được bằng kiểm thử)**

- Ghi một khoản mua kèm động cơ trong **≤ 25 giây** (T1).
- Thêm một món vào Danh sách mong muốn trong **< 20 giây** (T2).
- Chọn động cơ **chủ động** ở 100% lần ghi, không lưu theo lựa chọn có sẵn (xem phát hiện F1 trong `usability-test.md`).

**Nguồn dữ liệu:** S02, S12, S15 · Q6, Q8, Q9, Q12, Q13 · I1 · D1, D2.

## 4. P2 – Trần Thu Linh, 26 (phụ)

**Thông tin cơ bản:** nhân viên hành chính văn phòng, thu nhập 10–12 triệu/tháng, sống ở Hà Nội.

**Một ngày:** làm 8:00–17:30; tuần nào chạy việc gấp thì về muộn. Tối thứ Sáu và cuối tuần là lúc "thưởng cho bản thân".

**Hành vi mua**

- Mua theo cảm xúc sau ngày mệt: skincare, quần áo trên TikTok Shop và Shopee.
- Không dùng app ghi chi tiêu. Từng ghi vào Notes vài ngày.

**Thiết bị và accessibility:** điện thoại Android, dùng hai tay khi ngồi, một tay khi đi lại. Không có nhu cầu đặc biệt.

**Mục tiêu**

1. Hiểu vì sao mình cứ lặp lại kiểu mua "thưởng cho mình".
2. Xem tổng hợp theo tháng, so sánh tháng này với tháng trước.

**Pain point**

- Cuối tháng không biết tiền đi đâu (I2).
- Không muốn bị giảng giải, chỉ muốn thấy số (I2; Q11 TB 3,83 ở nhóm 26–30).

**Câu nói (I2):**

> "Em không cần ai nhắc là em tiêu quá tay, em cần biết vì sao em cứ lặp lại."

**Kịch bản:** cuối tháng 9, Linh mở Mô hình. Thấy Cảm xúc đứng thứ hai (3 khoản, 27%), Linh mở Góc nhìn, rồi viết vài dòng ở Chiêm nghiệm tháng.

**Tiêu chí thành công:** tìm được động cơ nhiều nhất của tháng trước trong **≤ 10 giây** (T3).

**Nguồn dữ liệu:** S10, S17, S23 · Q7, Q11 · I2 · D2.

## 5. P3 – Lê Gia Huy, 19 (phụ)

**Thông tin cơ bản:** SV năm 2, gia đình gửi 4 triệu/tháng, làm thêm cuối tuần được khoảng 1 triệu.

**Một ngày:** học trên trường, tối đi chơi với nhóm bạn hoặc lướt TikTok.

**Hành vi mua**

- Mua theo nhóm bạn và theo TikToker mình hay xem (giày, quần áo).
- Hay săn mã giảm giá. Chỉ xem lịch sử giao dịch trong MoMo.

**Thiết bị và accessibility:** điện thoại Android tầm trung, dùng một tay. Không có nhu cầu đặc biệt.

**Mục tiêu**

1. Có chỗ "để đó" một món đang thèm, vài hôm sau xem lại.
2. Không mua theo đám đông rồi hết tiền giữa tháng.

**Pain point**

- Mua xong hết nửa tiền tháng, phải ăn mì (I3).
- 51% người trẻ chịu ảnh hưởng xu hướng MXH; 55% xem micro-influencer trước khi mua (D1, nguồn thật).

**Câu nói (I3):**

> "Nếu có chỗ để bỏ món vào rồi vài hôm xem lại thì hay. Em hay mua lúc đang hứng."

**Kịch bản:** Huy thấy "Bàn phím cơ" trên TikTok. Thay vì mua ngay, Huy thêm món vào Danh sách mong muốn với lý do "Ảnh hưởng MXH". Ba ngày sau xem lại và chọn "Không mua nữa".

**Tiêu chí thành công:** thêm một món trong **< 20 giây** (T2); trả lời 3 câu hỏi ở Trước khi mua mà không cần trợ giúp.

**Nguồn dữ liệu:** S03, S14 · Q7, Q14, Q15 · I3 · D1.

## 6. P4 – Phạm Ngọc Mai, 29 (phụ)

**Thông tin cơ bản:** kế toán ở công ty tư nhân, có con 2 tuổi, sống ở TP.HCM.

**Một ngày:** sáng đưa con đi gửi trẻ; giờ nghỉ trưa xem Shopee Live; tối lo cho con đến 21:30.

**Hành vi mua**

- Mua đồ cho con khi có giảm giá, kể cả khi con đã có đồ.
- Mua đồ ăn khi mệt.
- Từng bỏ app vì nhiều danh mục; giờ ghi Excel vào cuối tuần.

**Thiết bị và accessibility:** gần như lúc nào cũng **một tay** (tay kia bế con), bị ngắt quãng liên tục. Cần nút lớn ở nửa dưới màn hình, và ghi được nhanh trước khi bị gián đoạn.

**Mục tiêu**

1. Ghi được ngay lúc mua, bằng một tay, chừng 20 giây.
2. Cuối tháng xem lại cả tháng; không cần xem từng khoản.

**Pain point**

- Trong tuần quên ghi hết (I4; Q9: quên ghi 12/16).
- App cũ nhiều danh mục, chọn mãi (I4; Q9: 6/16).

**Câu nói (I4):**

> "Phải dùng được một tay. Mà phải nhanh, chừng 20 giây."

**Kịch bản:** đang bế con, Mai nhận thông báo nhắc lúc 21:00. Mai mở app, ghi khoản đồ cho bé bằng ngón cái, chọn "Khuyến mãi", rồi lưu. Cuối tháng, Mai mở Lịch sử, chuyển sang tháng 9.

**Tiêu chí thành công:**

- Hoàn thành T1 **bằng một tay** trong ≤ 25 giây.
- Bật lại nhắc nhở được mà không cần trợ giúp (T5).

**Nguồn dữ liệu:** S20, S21 · Q9, Q10, Q13 · I4 · D2 (Shopee Live).

## 7. P5 – Đỗ Văn Hùng, 58 (anti-persona)

**Thông tin cơ bản:** nhân viên văn phòng sắp nghỉ hưu, sống ở Đà Nẵng.

**Hành vi**

- Ít mua online; mua ở chợ, siêu thị, theo danh sách.
- Ghi chi tiêu bằng sổ tay hơn 20 năm.
- Muốn biết **tổng tiền** tháng này; ít quan tâm "vì sao mua".

**Thiết bị và accessibility:** phải phóng to chữ trên điện thoại; quen thao tác hai tay.

**Câu nói (I5):**

> "Có báo thì tốt chứ, để biết mà dừng."

**Vì sao không nhắm tới nhóm này:**

| Lý do | Bằng chứng |
|---|---|
| Ít mua ngoài dự định qua điện thoại | Q6: 0/5 người 31+ chốt đơn sau 22h; Q14: 3/5 không hối tiếc lần nào |
| Thấy cảnh báo đỏ **hữu ích**. Điều này ngược với quyết định cốt lõi "không cảnh báo đỏ" của app | Q12: TB 4,60 ở nhóm 31+; I5 |
| Cần ngân sách và tổng chi. Các app như MISA Sổ Thu Chi, Money Lover đã phục vụ tốt | C2, C3 |
| Ít quan tâm "vì sao mua" | Q11: TB 3,00 ở nhóm 31+; I5 |

**Trả lời câu "vì sao không làm cho người lớn tuổi":** không phải vì tuổi. App giải quyết vấn đề *mua theo cảm xúc và khuyến mãi qua điện thoại*, và dữ liệu cho thấy nhóm 31+ trong mẫu ít gặp vấn đề này. Thêm nữa, họ cần chính thứ app chủ động bỏ ra ngoài phạm vi (ngân sách, cảnh báo). Nếu sau này mở rộng sang nhóm lớn tuổi thì cần làm research riêng.

**Điều vẫn giữ để không loại trừ ai:** chữ ≥ 14 sp, tương phản ≥ 4,5 : 1, vùng chạm ≥ 48 dp. Người dùng lớn tuổi nếu muốn vẫn dùng được.

## 8. Persona → flow

● = dùng chính · ○ = có dùng · trống = ít liên quan

| Flow | P1 Nam | P2 Linh | P3 Huy | P4 Mai |
|---|:-:|:-:|:-:|:-:|
| 1 – Ghi nhanh một khoản mua | ● | ○ | ○ | ● |
| 2 – Mô hình → Góc nhìn → Chiêm nghiệm | ○ | ● | | ○ |
| 3 – Xem lại, sửa hoặc xóa (có hoàn tác) | ● | ○ | ○ | ○ |
| 4 – Xem theo tháng / năm | ○ | ● | | ● |
| 5 – Cá nhân & dữ liệu (nhắc nhở, xuất, xóa) | ○ | ○ | | ● |
| 6 – Danh sách mong muốn | ● | ○ | ● | |
| 7 – Khởi động, đăng nhập, tài khoản | ● | ● | ● | ● |
| 8 – Nhận định AI sau khi lưu | ● | ● | ○ | |
| 9 – Trước khi mua: 3 câu hỏi nhanh | ○ | ○ | ● | |
| 10 – AI phân tích mô hình và Góc nhìn | ○ | ● | | ○ |

## 9. Phát biểu vấn đề

> Người trẻ 18–25 tuổi như Nam hay mua ngoài dự định vào buổi tối và đêm khuya, chủ yếu vì khuyến mãi và cảm xúc. Họ đã bỏ các app ghi chi tiêu vì nhập lâu, hay quên và cảm thấy tội lỗi trước cảnh báo đỏ. Họ cần một cách ghi khoản mua **trong 25 giây, bằng một tay**, kèm **động cơ mua**, rồi nhìn lại mô hình của mình **mà không bị phán xét**, để tự hiểu trước khi thay đổi.

Bằng chứng: Q6, Q7, Q9, Q10, Q12, Q13 (mô phỏng); D1, D2 (thật); I1, I2.

## 10. Tiêu chí thành công đo được

| Chỉ số | Mục tiêu | Đo bằng | Kết quả hiện có |
|---|---|---|---|
| Thời gian ghi một khoản mua kèm động cơ | ≤ 25 giây | T1 | MÔ PHỎNG: 4/5 đạt, trung vị 21,7 giây (`usability-test.md`) |
| Thời gian thêm một món mong muốn | < 20 giây | T2 | MÔ PHỎNG: 5/5 đạt, trung vị 15,4 giây |
| Chọn động cơ chủ động | 100% lần ghi | Quan sát T1 | MÔ PHỎNG: 3/5 lưu theo lựa chọn có sẵn (F1) → sửa ở R4 |
| Mức dễ dùng tổng thể | SUS ≥ 68 (mức trung bình) | Bảng SUS | MÔ PHỎNG: 78,0 |

Đã bỏ các chỉ tiêu của bản cũ không đo được trong phạm vi Lab 2 (≥ 70% người dùng mở Mô hình 2 lần/tuần; điểm hối tiếc giảm 30% sau 30 ngày) và con số "> 60 giây ở app truyền thống" vì không có nguồn.
