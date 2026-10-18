# Research – Why I Buy?

> **Đọc trước:** tài liệu này có ba loại dữ liệu, ghi rõ ở từng mục.
>
> - **THẬT:** desk research (D1–D3) và rà app tương tự (C1–C4). Mọi số liệu đều có nguồn công khai, link ở cuối mỗi mục.
> - **MÔ PHỎNG bằng AI (14/10/2026):** khảo sát n = 30 (S01–S30) và 5 phỏng vấn (I1–I5), phục vụ hướng cũ (ghi khoản mua kèm động cơ). Làm theo hướng dẫn của thầy: được dùng người dùng mô phỏng nếu trình bày rõ câu hỏi nghiên cứu và quy trình. Script và seed nằm trong `research-pack/`. 30 dòng mô phỏng sau đó được nhập vào Google Form (biểu đồ ghi "Khảo sát MÔ PHỎNG (S01–S30, đã nhập vào Google Form)").
> - **CHƯA XÁC MINH NGUỒN GỐC (18/10/2026):** bảng câu trả lời 30 dòng cho bộ câu hỏi mới (hướng Smart Shopping Companion). Dấu thời gian cho thấy cả 30 câu trả lời được gửi trong 112 giây, cách nhau đều 3,7–4,1 giây. **Không được xem là khảo sát người dùng thật** cho đến khi nhóm xác nhận cách thu thập. Chỉ dùng số liệu tổng hợp (mục 9).
>
> Dữ liệu mô phỏng **không chứng minh** điều gì về người thật. Nó dùng để chạy đủ quy trình research → insight → persona và tạo hồ sơ cho phỏng vấn. Mọi con số mô phỏng khi đưa lên slide phải kèm nhãn "MÔ PHỎNG". Bảng tách các loại kết luận ở mục 10.
>
> **Cập nhật 18/10/2026:** sản phẩm đã chuyển sang hướng *Smart Shopping Companion* (đặc tả hợp nhất v1.0, 17/10). Một số hệ quả thiết kế ở mục 3 và 6 (ví dụ "ngân sách ngoài phạm vi") **đã được thay thế**; các chỗ đó có ghi chú *[Đã thay thế 18/10]*. Persona hiện hành ở [`persona.md`](persona.md) không còn dùng dữ liệu mục 4–5 làm bằng chứng.

## 1. Kế hoạch research

### 1.1. Mục tiêu

Kiểm chứng các giả định đứng sau thiết kế Why I Buy?:

- người trẻ có mua ngoài dự định thường xuyên không, và vì sao;
- vì sao họ bỏ các app ghi chi tiêu;
- họ có muốn hiểu "vì sao mình mua" không;
- nhóm người dùng nào nên được ưu tiên.

**Thứ tự thực tế.** Research được làm sau bản thiết kế đầu (brief → Stitch → Figma), với vai trò **research kiểm chứng**. Chỗ nào dữ liệu không khớp với giả định ban đầu được ghi ở mục 6.3 và mục 7.

### 1.2. Câu hỏi nghiên cứu

| Mã | Câu hỏi | Trả lời bằng |
|---|---|---|
| RQ1 | Người trẻ đang ghi chi tiêu bằng cách nào, và vì sao bỏ cuộc? | C1–C4, Q8–Q9, I1–I5 |
| RQ2 | Họ hay mua ngoài dự định lúc nào, ở đâu, do điều gì kích hoạt? | D1–D2, Q4–Q7, Q14, I1–I4 |
| RQ3 | Họ có muốn hiểu "vì sao mình mua" không, hay chỉ muốn biết "đã tiêu bao nhiêu"? | Q11, Q15, I1–I5 |
| RQ4 | Cảnh báo đỏ / vượt ngân sách khiến họ cảm thấy thế nào? | Q12, I1, I2, I5 |
| RQ5 | Họ chịu bỏ bao nhiêu thời gian để ghi một khoản? Cầm điện thoại một tay hay hai tay? | Q10, Q13, I1, I4 |

### 1.3. Phương pháp

| Bước | Phương pháp | Dữ liệu | Số lượng | Sản phẩm |
|---|---|---|---|---|
| 1 | Desk research: báo cáo thị trường, bài nghiên cứu khoa học | **THẬT** | 2 nguồn chính (D1, D2) | Mục 2 |
| 2 | Rà app tương tự từ nguồn công khai | **THẬT** | 4 app (C1–C4) | Mục 3 |
| 3 | Khảo sát 15 câu | **MÔ PHỎNG** (script Python, seed 2026) | n = 30 | Mục 4; biểu đồ trong `research-pack/` (file CSV đã gỡ khỏi repo ngày 14/10) |
| 4 | Phỏng vấn bán cấu trúc, khoảng 15 phút/người | **MÔ PHỎNG** (AI đóng vai theo hồ sơ khảo sát) | 5 người (I1–I5) | Mục 5 |
| 5 | Affinity mapping → insight | Tổng hợp từ bước 1–4 | 7 insight | Mục 6 |

**Vì sao khảo sát cả người ngoài 18–25 tuổi.** Để có dữ liệu so sánh khi chọn persona chính, và để trả lời câu hỏi "vì sao không nhắm tới người lớn tuổi" bằng số liệu thay vì cảm tính. Có 11/30 người từ 26 tuổi trở lên, trong đó 5 người từ 31 tuổi trở lên.

## 2. Desk research (THẬT)

| Mã | Nguồn | Số liệu dùng được | Liên quan |
|---|---|---|---|
| D1 | YouNet ECI / YouNet Media, *Vietnam e-Commerce Intelligence Report 2025*, khảo sát hơn 700 người tiêu dùng số ở đô thị (qua Brands Vietnam) | Gen Z chiếm **53,4%** người mua online hằng tuần. **69,5%** có giỏ hàng trung bình 100.000–500.000 ₫. **51%** bị ảnh hưởng bởi xu hướng trên mạng xã hội; **55%** xem micro-influencer trước khi mua. Livestream và video dùng thử của KOL là loại nội dung khiến họ mua ngay nhiều nhất; flash sale đứng thứ hai | RQ2; chọn nhóm tuổi; động cơ "Ảnh hưởng MXH", "Khuyến mãi" |
| D2 | Nguyễn Thanh Ý và cộng sự (HUTECH), *Các yếu tố ảnh hưởng đến hành vi mua sắm bốc đồng trên Shopee Live của Gen Z tại TP.HCM và vai trò trung gian của hội chứng sợ bỏ lỡ*, Tạp chí Nghiên cứu Kinh tế – Tài chính, 22/6/2026. n = 310 | Giảm giá, khan hiếm, lợi ích cảm nhận và động cơ hưởng thụ giải thích **53,5%** biến thiên của FOMO. FOMO giải thích **86,7%** biến thiên của mua bốc đồng (β = 0,931) | RQ2; động cơ "Khuyến mãi", "Cảm xúc" |
| D3 | MoMo, bài so sánh các app quản lý tài chính cá nhân (blog MoMo, nguồn mang tính quảng bá) | Xem bảng C1–C4 ở mục 3 | RQ1 |

**Rút ra từ desk research:**

- Người mua online hằng tuần chủ yếu là người trẻ (D1). Đây là căn cứ để nhắm tới nhóm 18–25 tuổi.
- Mua bốc đồng có cơ chế rõ: khuyến mãi, khan hiếm và cảm xúc tạo ra FOMO, rồi FOMO dẫn tới mua (D2). Do đó động cơ là thứ đáng ghi lại, không chỉ số tiền.
- Mạng xã hội và KOL là một tác nhân lớn (D1). Đây là căn cứ để giữ động cơ "Ảnh hưởng MXH", dù khảo sát mô phỏng cho kết quả thấp (xem INS5).

Nguồn:

- D1: [brandsvietnam.com – Từ mạng xã hội đến giỏ hàng: giải mã hành vi mua sắm của Gen Z](https://www.brandsvietnam.com/congdong/topic/344635-tu-mang-xa-hoi-den-gio-hang-giai-ma-hanh-vi-mua-sam-cua-gen-z)
- D2: [nghiencuu.tapchikinhtetaichinh.vn – Hành vi mua sắm bốc đồng trên Shopee Live của Gen Z](https://nghiencuu.tapchikinhtetaichinh.vn/cac-yeu-to-anh-huong-den-hanh-vi-mua-sam-boc-dong-tren-shopee-live-cua-gen-z-tai-tp-ho-chi-minh-va-vai-tro-trung-gian-cua-hoi-chung-so-bo-lo-159588.html)
- D3: [momo.vn – Ứng dụng quản lý tài chính cá nhân phổ biến nhất](https://www.momo.vn/blog/ung-dung-quan-ly-tai-chinh-ca-nhan-pho-bien-nhat-c103dt2282)

## 3. Rà app tương tự (THẬT, theo nguồn công khai D3)

| Mã | App | Cách ghi khoản chi | Ngân sách / cảnh báo | Có hỏi "vì sao mua" không |
|---|---|---|---|---|
| C1 | MoMo (quản lý chi tiêu trong ví) | Tự phân loại giao dịch thanh toán qua MoMo bằng AI | Có ngân sách; báo khi "sắp vượt giới hạn" | Không thấy nhắc trong nguồn |
| C2 | Money Lover | Nhập tay từng giao dịch | Có ngân sách; đồng bộ và xuất dữ liệu là tính năng trả phí | Không thấy nhắc trong nguồn |
| C3 | MISA Sổ Thu Chi | Nhập tay, có nhập bằng giọng nói | Có ngân sách; xuất Excel / PDF miễn phí | Không thấy nhắc trong nguồn |
| C4 | Timo | Chỉ theo dõi giao dịch qua tài khoản Timo | Chia tiền vào các "hũ chi tiêu" | Không thấy nhắc trong nguồn |

**Khoảng trống cơ hội:**

1. Các app trên trả lời câu hỏi **"tiêu bao nhiêu, vào danh mục nào"**. Theo nguồn D3, không app nào hỏi **"vì sao mua"**. Why I Buy? lấy chỗ trống này làm trọng tâm.
2. Cơ chế chung là **ngân sách và cảnh báo vượt mức**. Q12 và I1, I2 (mô phỏng) cho thấy nhóm 18–25 tuổi khó chịu với cảnh báo (INS2). Vì vậy bản đầu của Why I Buy? để ngân sách và cảnh báo ra ngoài phạm vi. *[Đã thay thế 18/10]* Sau góp ý của giảng viên, ngân sách được đưa vào phạm vi dưới dạng **tùy chọn, mốc tham chiếu tự đặt, màu trung tính, không chặn mua** (đặc tả mục 1.5 #6, 7.1); vẫn không có cảnh báo đỏ.
3. App tự ghi (C1, C4) chỉ thấy giao dịch qua ví hoặc ngân hàng của chính nó, không biết khoản trả tiền mặt hay trả qua app khác. App nhập tay (C2, C3) thì tốn thời gian (Q9). Why I Buy? chọn cách nhập tay nhưng rút xuống 2 bước, mục tiêu ≤ 25 giây.

> 👥 **Nhóm cần làm thêm (10 phút):** cài thử Money Lover và MISA Sổ Thu Chi, chụp màn hình thêm một khoản chi và màn ngân sách. Ghép ảnh vào slide 4 để bảng này có bằng chứng hình ảnh. D3 là bài quảng bá của MoMo, nên khi nói hãy dùng cách diễn đạt "theo mô tả của nhà phát hành".

## 4. Khảo sát (MÔ PHỎNG bằng AI, n = 30)

### 4.1. Cách làm

1. Nhóm soạn 15 câu hỏi (mục 4.2). Bộ câu hỏi này dùng nguyên được cho Google Form thật.
2. Viết script `survey_sim.py` sinh 30 người trả lời (S01–S30), `random.seed(2026)`. Mỗi nhóm tuổi có một bộ xác suất trả lời riêng, đặt theo giả định ở bảng 4.1.
3. Xuất `survey-mo-phong.csv` (đã gỡ khỏi repo ngày 14/10), rồi vẽ 5 biểu đồ bằng `charts.py`. Mỗi biểu đồ có dòng chú thích "Khảo sát MÔ PHỎNG bằng AI, n = 30 (seed 2026)".
4. Seed được chốt **trước** khi chạy. Không chạy lại để "chọn" kết quả đẹp. Kết quả lệch giả định cũng được giữ nguyên (mục 4.5).

**Phân bố mẫu theo tuổi:** 18–21: 8 · 22–25: 11 · 26–30: 6 · 31–40: 3 · 41+: 2.

**Bảng 4.1. Giả định đầu vào của script.** Đây là chỗ thầy có thể hỏi "lấy số này ở đâu".

| Giả định (nhóm 18–25) | Mức đặt | Căn cứ |
|---|---|---|
| Kênh mua: Shopee, TikTok Shop, đồ ăn giao tận nơi | Trọng số cao | D1 |
| Chốt đơn sau 22h | 6/10 | Giả định của nhóm (persona ban đầu). **Chưa có nguồn** |
| Mua ngoài dự định do khuyến mãi | 0,7 | D1 (flash sale), D2 |
| … do mạng xã hội / KOL | 0,55 | D1 (51%) |
| Đã dùng app ghi chi tiêu rồi bỏ | 6/10 | Giả định của nhóm. **Chưa có nguồn** |
| Ghét cảnh báo đỏ (điểm 1–2) | 8/10 | Giả định của nhóm. **Chưa có nguồn** |

Hệ quả: những kết quả trùng với giả định "chưa có nguồn" (sau 22h, bỏ app, ghét cảnh báo đỏ) chỉ phản ánh lại đúng giả định đó. Muốn chứng minh, nhóm cần khảo sát thật (mục 7).

### 4.2. Bộ câu hỏi (dùng được cho Google Form)

| # | Câu hỏi | Loại |
|---|---|---|
| Q1 | Bạn bao nhiêu tuổi? | Một lựa chọn: 18–21 / 22–25 / 26–30 / 31–40 / 41+ |
| Q2 | Công việc hiện tại? | Sinh viên / SV làm thêm hoặc thực tập / Nhân viên văn phòng / Tự do / Nội trợ, khác |
| Q3 | Thu nhập hoặc tiền tiêu mỗi tháng? | < 3 triệu / 3–7 / 7–15 / > 15 triệu |
| Q4 | Bạn mua hàng hoặc đặt đồ ăn online bao lâu một lần? | Hằng ngày / 2–3 lần/tuần / 1 lần/tuần / Vài lần/tháng / Hiếm khi |
| Q5 | Bạn mua qua kênh nào nhiều nhất? | Shopee / TikTok Shop / Lazada / GrabFood, ShopeeFood / Livestream Facebook / Cửa hàng |
| Q6 | Bạn hay chốt đơn vào khung giờ nào? | Sáng / Trưa / Tối 18–22h / Sau 22h |
| Q7 | Lần gần nhất mua món **không định mua từ trước**, lý do là gì? | Chọn nhiều: Khuyến mãi, flash sale / Cảm xúc, stress / Bạn bè, KOL, MXH / Quảng cáo / Tiện lợi / Nhu cầu thật |
| Q8 | Bạn đã dùng app ghi chi tiêu chưa? | Đang dùng / Đã dùng rồi bỏ / Chưa dùng |
| Q9 | (Nếu đã bỏ) Vì sao bạn bỏ? | Chọn nhiều: Nhập lâu, nhiều trường / Hay quên ghi / Cảm giác tội lỗi khi thấy cảnh báo, số âm / Quá nhiều danh mục / Không thấy lợi ích |
| Q10 | Bạn chấp nhận mất bao lâu để ghi một khoản? | < 10 giây / 10–30 giây / 30–60 giây / > 60 giây |
| Q11 | Bạn muốn biết **vì sao** mình mua đến mức nào? | Thang 1–5 |
| Q12 | Khi app báo đỏ "vượt ngân sách", bạn thấy thế nào? | Thang 1 (rất khó chịu) – 5 (rất hữu ích) |
| Q13 | Khi mua online, bạn thường cầm điện thoại thế nào? | Một tay / Hai tay |
| Q14 | Tháng qua bạn hối tiếc vì một món đã mua bao nhiêu lần? | 0 / 1–2 / 3–5 / > 5 |
| Q15 | Bạn có muốn một danh sách để "để đó suy nghĩ thêm" trước khi mua không? | Thang 1–5 |

### 4.3. Kết quả chính (MÔ PHỎNG)

| Câu | Kết quả | Biểu đồ |
|---|---|---|
| Q6 Khung giờ chốt đơn | Tối 18–22h: 13 · Sau 22h: 13 · Trưa: 3 · Sáng: 1. Tối và khuya: **26/30** | `chart-q6-khung-gio.png` |
| Q7 Lý do mua ngoài dự định (chọn nhiều) | Khuyến mãi / flash sale **21** · Cảm xúc / stress **14** · Tiện lợi 11 · Nhu cầu thật 8 · Bạn bè / KOL / MXH 4 · Quảng cáo 4 | `chart-q7-ly-do-mua.png` |
| Q8 App ghi chi tiêu | Đã dùng rồi bỏ **16** · Chưa dùng 10 · Đang dùng 4 | — |
| Q9 Lý do bỏ app (n = 16, chọn nhiều) | Hay quên ghi **12 (75%)** · Nhập lâu, nhiều trường 10 (62%) · Cảm giác tội lỗi 10 (62%) · Quá nhiều danh mục 6 (38%) · Không thấy lợi ích 5 (31%) | `chart-q9-ly-do-bo-app.png` |
| Q10 Thời gian chấp nhận | < 10 giây: 5 · 10–30 giây: 17 · 30–60 giây: 7 · > 60 giây: 1. Chấp nhận ≤ 30 giây: **22/30** | `chart-q10-thoi-gian.png` |
| Q11 Muốn biết vì sao mua (1–5) | Trung bình 3,93. Có **24/30** người chọn 4–5 | — |
| Q12 Cảm giác với cảnh báo đỏ (1–5) | Trung bình **2,37**. Có **18/30** người chọn 1–2 (khó chịu) | `chart-q12-canh-bao-do.png` |
| Q13 Cầm điện thoại | Một tay **17** · Hai tay 13 | — |
| Q14 Hối tiếc tháng qua | 0 lần: 3 · 1–2 lần: 12 · 3–5 lần: 11 · > 5 lần: 4. Hối tiếc ít nhất 1 lần: **27/30** | — |
| Q15 Muốn danh sách suy nghĩ thêm (1–5) | Trung bình 3,8. Có **16/30** người chọn 4–5 | — |

Các câu khác: Q4 tần suất (2–3 lần/tuần: 9 · 1 lần/tuần: 9 · Vài lần/tháng: 5 · Hằng ngày: 4 · Hiếm khi: 3); Q5 kênh chính (Shopee 11 · GrabFood / ShopeeFood 8 · TikTok Shop 6 · Cửa hàng 2 · Livestream Facebook 2 · Lazada 1).

### 4.4. So sánh theo nhóm tuổi (MÔ PHỎNG)

Bảng này là căn cứ chọn persona chính và anti-persona.

| Chỉ số | 18–25 (n = 19) | 26–30 (n = 6) | 31+ (n = 5) |
|---|:-:|:-:|:-:|
| Mua online từ 2–3 lần/tuần trở lên | 10 | 3 | 0 |
| Chốt đơn sau 22h | **11** | 2 | 0 |
| Đã dùng app chi tiêu rồi bỏ | **12** | 4 | 0 |
| Cầm điện thoại một tay | 11 | 4 | 2 |
| Hối tiếc từ 3 lần/tháng trở lên | **13** | 2 | 0 |
| Chấp nhận ghi ≤ 30 giây | 15 | 6 | 1 |
| Q11 Muốn biết vì sao mua (TB) | **4,21** | 3,83 | 3,00 |
| Q12 Cảm giác với cảnh báo đỏ (TB, 1 = rất khó chịu) | **1,79** | 2,33 | **4,60** |
| Q15 Muốn danh sách suy nghĩ thêm (TB) | **4,11** | 3,67 | 2,80 |

**Đọc bảng:**

- Nhóm 18–25 chiếm 19/30 mẫu và dồn vào đúng vấn đề app giải quyết: mua khuya, bỏ app, hối tiếc nhiều, ghét cảnh báo đỏ.
- Nhóm 31+ ngược lại: không ai chốt đơn sau 22h, 3/5 không hối tiếc lần nào, và **thấy cảnh báo đỏ hữu ích** (4,60/5). Nhóm này cần app ngân sách có cảnh báo (như C1–C3), không cần Why I Buy?. Đây là cơ sở cho anti-persona P5.

### 4.5. Kết quả lệch giả định

Script đặt xác suất "Bạn bè / KOL / MXH" là 0,55 cho nhóm 18–25. Kết quả chỉ ra **3/19** (cả mẫu: 4/30), thấp hơn nhiều so với mức kỳ vọng khoảng 10/19.

Nhóm giữ nguyên kết quả, không chạy lại seed khác. Lý do:

- Đây là minh họa thật về việc mẫu n = 30 dao động mạnh.
- Thêm một lý do để làm khảo sát thật trước khi kết luận.
- Quyết định giữ động cơ "Ảnh hưởng MXH" dựa vào D1 (nguồn thật, hơn 700 người) và I3, không dựa vào khảo sát mô phỏng (xem INS5).

## 5. Phỏng vấn (MÔ PHỎNG bằng AI, 5 người)

### 5.1. Chọn người phỏng vấn

Mỗi người được dựng từ một hoặc hai dòng khảo sát có thật trong file CSV, để phỏng vấn đi sâu vào đúng hồ sơ đã khảo sát.

| Mã | Hồ sơ | Dựa trên dòng khảo sát | Vì sao chọn |
|---|---|---|---|
| I1 | Tuấn, 21, SV năm 3 Kinh tế, làm thêm ở quán cà phê | S02, S12 | Nhóm chính: mua khuya, đã bỏ app |
| I2 | Trang, 25, nhân viên marketing | S10, S17 | Mua theo cảm xúc sau giờ làm, hối tiếc > 5 lần |
| I3 | Khoa, 19, SV năm 2 | S03, S14 | Bị bạn bè / KOL kéo theo, ngân sách nhỏ |
| I4 | Hạnh, 29, kế toán, có con 2 tuổi | S20, S21 | Mua theo cảm xúc và tiện lợi, ít thời gian, dùng một tay, đã bỏ app |
| I5 | Cô Lan, 55, giáo viên | S29, S30 | Nhóm ngoài mục tiêu, để kiểm tra phạm vi |

### 5.2. Kịch bản phỏng vấn (dùng nguyên được cho phỏng vấn thật)

1. Kể lại lần gần nhất bạn mua một món mà trước đó không định mua.
2. Lúc đó là mấy giờ, bạn đang ở đâu, đang làm gì?
3. Điều gì khiến bạn bấm "mua"?
4. Sau đó bạn thấy thế nào về món đó?
5. Bạn đã từng ghi chi tiêu chưa? Bằng cách nào? Vì sao dừng (nếu đã dừng)?
6. Nếu một app báo đỏ "bạn đã vượt ngân sách", bạn sẽ làm gì?
7. Bạn có muốn biết vì sao mình hay mua không? Biết rồi thì để làm gì?
8. Ghi một khoản mất bao lâu thì bạn bỏ cuộc?

### 5.3. Prompt mô phỏng (đã dùng, nguyên văn)

```text
Bạn đóng vai một người tham gia phỏng vấn UX, không phải trợ lý AI.
Hồ sơ: {hồ sơ ở bảng 5.1, kèm nguyên văn dòng khảo sát {S..} trong CSV}.
Quy tắc:
- Trả lời bằng tiếng Việt nói hằng ngày, mỗi lượt 1–3 câu, có thể ngập ngừng.
- Bạn KHÔNG biết app "Why I Buy?" và không biết nhóm đang thiết kế gì.
- Không cố trả lời "đúng ý" người hỏi. Được nói "không nhớ", được mâu thuẫn nhẹ như người thật.
- Chỉ kể chi tiết phù hợp với hồ sơ; không bịa số liệu thống kê.
Người phỏng vấn sẽ hỏi lần lượt 8 câu. Chờ từng câu hỏi.
```

Người phỏng vấn (thành viên nhóm) hỏi theo kịch bản 5.2 và được hỏi thêm câu đào sâu ("vì sao?", "lúc đó cảm thấy thế nào?"). Dưới đây là bản rút gọn, giữ nguyên các câu trả lời dùng làm bằng chứng.

### 5.4. Transcript rút gọn (MÔ PHỎNG)

**I1 – Tuấn, 21, SV năm 3, làm thêm ở quán cà phê**

- *Lần gần nhất mua ngoài dự định?* "Tuần trước, gần 12 giờ đêm, Shopee có flash sale tai nghe. Em định để giỏ hàng thôi, mà thấy đồng hồ đếm ngược còn 10 phút là bấm luôn."
- *Lúc đó đang làm gì?* "Nằm trên giường lướt điện thoại sau ca làm, một tay cầm máy."
- *Sau đó?* "Tai nghe cũng được, nhưng em có một cái rồi. Hơi tiếc tiền."
- *Ghi chi tiêu?* "Có cài Money Lover hồi năm nhất. Ghi được hai tuần. Mỗi lần phải chọn danh mục, ví, ngày… lười lắm, rồi quên luôn."
- *Báo đỏ vượt ngân sách?* "Thấy màu đỏ là em tắt app. Biết là tiêu nhiều rồi, nhìn thêm chỉ thấy tội lỗi."
- *Muốn biết vì sao mình mua?* "Có. Em nghĩ phần lớn là do sale, nhưng không chắc."
- *Bao lâu thì bỏ?* "Quá 30 giây là thôi. Tốt nhất bấm vài cái là xong."

**I2 – Trang, 25, nhân viên marketing**

- *Lần gần nhất?* "Hôm thứ Sáu, chạy deadline xong mệt, về đặt ngay một set skincare trên TikTok Shop. Kiểu thưởng cho mình."
- *Điều gì khiến bấm mua?* "Một phần là video review, nhưng chủ yếu là đang mệt, muốn có cái gì đó vui."
- *Sau đó?* "Tháng đó em mua kiểu này chắc phải sáu, bảy lần. Cuối tháng nhìn lại thấy không hiểu tiền đi đâu."
- *Ghi chi tiêu?* "Chưa dùng app. Có thử ghi Notes điện thoại được mấy ngày."
- *Báo đỏ?* "Nghe áp lực. Em không cần ai nhắc là em tiêu quá tay, em cần biết vì sao em cứ lặp lại."
- *Muốn biết vì sao mình mua?* "Rất muốn. Nhưng đừng giảng đạo lý cho em, cứ cho em thấy số là được."
- *Bao lâu thì bỏ?* "Chắc 20, 30 giây. Ghi lúc vừa thanh toán xong thì được."

**I3 – Khoa, 19, SV năm 2**

- *Lần gần nhất?* "Đôi giày. Mấy đứa trong nhóm đều có, rồi thấy một bạn TikToker em hay xem cũng mang."
- *Điều gì khiến bấm mua?* "Sợ mỗi mình không có. Với lại có mã giảm 50 nghìn."
- *Sau đó?* "Hết gần nửa tiền tháng mẹ gửi. Hai tuần sau phải ăn mì."
- *Ghi chi tiêu?* "Em chỉ xem lịch sử trong MoMo, không ghi gì thêm."
- *Có danh sách để suy nghĩ thêm thì sao?* "Nếu có chỗ để bỏ món vào rồi vài hôm xem lại thì hay. Em hay mua lúc đang hứng."
- *Muốn biết vì sao mình mua?* "Có, nhưng đừng kiểu dạy đời."
- *Bao lâu thì bỏ?* "Mười mấy giây thôi."

**I4 – Hạnh, 29, kế toán, có con 2 tuổi**

- *Lần gần nhất?* "Giờ nghỉ trưa xem Shopee Live bán đồ cho bé, chốt ba bộ quần áo. Bé có đồ rồi nhưng đang giảm giá, mà cả buổi sáng bị sếp hối nên muốn mua cho vui."
- *Lúc đó đang làm gì?* "Một tay bế con, một tay cầm điện thoại. Hầu như lúc nào cũng vậy."
- *Ghi chi tiêu?* "Em từng dùng một app, bỏ vì nhiều danh mục quá, ghi một món phải chọn mãi. Giờ ghi Excel, nhưng chỉ ghi được cuối tuần, trong tuần quên hết."
- *Báo đỏ?* "Cũng được, nhưng đồ cho con thì vẫn phải mua."
- *Muốn biết vì sao mình mua?* "Tò mò thôi. Em muốn xem cả tháng thì hơn, xem từng món thì không cần."
- *Bao lâu thì bỏ?* "Phải dùng được một tay. Mà phải nhanh, chừng 20 giây."

**I5 – Cô Lan, 55, giáo viên**

- *Lần gần nhất?* "Cô ít mua online lắm. Thường ra chợ hoặc siêu thị, mua theo danh sách."
- *Ghi chi tiêu?* "Cô ghi sổ tay hơn hai mươi năm rồi, cuối tháng cộng lại."
- *Báo đỏ?* "Có báo thì tốt chứ, để biết mà dừng."
- *Muốn biết vì sao mình mua?* "Cô mua vì cần thôi. Cô cần xem tổng tháng này tiêu bao nhiêu."
- *Ghi trên điện thoại?* "Chữ trên điện thoại nhỏ, cô hay phải phóng to. Ghi sổ vẫn nhanh hơn."

## 6. Tổng hợp: affinity → insight

### 6.1. Affinity map

Mỗi ghi chú lấy từ một nguồn có mã (D = desk research, C = rà app, Q = câu khảo sát, I = phỏng vấn).

| Nhóm | Ghi chú (nguồn) |
|---|---|
| **A. Ghi chi tiêu quá phiền** | "Chọn danh mục, ví, ngày… lười lắm" (I1) · Ghi Notes được mấy ngày (I2) · Chỉ ghi cuối tuần (I4) · Hay quên ghi 12/16, nhập lâu 10/16 (Q9) · App nhập tay (C2, C3) |
| **B. Màu đỏ = tội lỗi** | "Thấy đỏ là tắt app" (I1) · "Nghe áp lực" (I2) · Q12 TB 1,79 ở nhóm 18–25 · Cảm giác tội lỗi 10/16 (Q9) · Các app đều có ngân sách và cảnh báo (C1–C4) |
| **C. Khuya, mệt, sale** | Flash sale gần 12 giờ đêm (I1) · Thưởng cho mình sau deadline (I2) · Q7: khuyến mãi 21, cảm xúc 14 · Q6: 26/30 tối hoặc khuya · FOMO → mua bốc đồng, β = 0,931 (D2) |
| **D. Muốn hiểu, không muốn bị dạy** | "Cho em thấy số là được" (I2) · "Đừng kiểu dạy đời" (I3) · Q11: 24/30 chọn 4–5 · Không app nào hỏi "vì sao" (C1–C4) |
| **E. Bạn bè và KOL** | Đôi giày vì cả nhóm đều có (I3) · Video review (I2) · 51% chịu ảnh hưởng MXH, 55% xem micro-influencer (D1) · Q7 chỉ 4/30 (mô phỏng, lệch) |
| **F. Cần chỗ để nghĩ thêm** | "Bỏ món vào rồi vài hôm xem lại" (I3) · Q15 TB 4,11 ở nhóm 18–25 · Q14: 27/30 hối tiếc ít nhất 1 lần |
| **G. Một tay, ít thời gian** | Một tay cầm máy trên giường (I1) · Bế con (I4) · Q13: 17/30 một tay · Q10: 22/30 chấp nhận ≤ 30 giây |
| **H. Ngoài nhóm mục tiêu** | Mua theo danh sách, ghi sổ tay (I5) · Muốn có cảnh báo (I5, Q12 TB 4,60 ở nhóm 31+) · Chữ nhỏ khó đọc (I5) · Nhóm 31+: 0 người chốt đơn sau 22h (Q6) |

> 👥 Nên dựng lại bảng này thành affinity board (FigJam hoặc giấy note), chụp ảnh đưa lên slide 5.

### 6.2. Insight

| Mã | Insight | Bằng chứng | Hệ quả thiết kế (đã có trong Figma) |
|---|---|---|---|
| INS1 | Người trẻ bỏ app chi tiêu vì **quên** và vì **nhập lâu**, không phải vì không muốn biết | Q9 (12/16, 10/16), Q10 (22/30 ≤ 30 giây), I1, I2, I4, C2–C3 | Ghi khoản mua 2 bước, mục tiêu ≤ 25 giây; chip số tiền nhanh; thời điểm điền sẵn; nhắc lúc 21:00 (05a) |
| INS2 | Cảnh báo đỏ tạo cảm giác **tội lỗi** ở nhóm 18–25, khiến họ né app | Q12 (1,79 ở 18–25; 18/30 chọn 1–2), Q9 (10/16), I1, I2 | Không cảnh báo đỏ; màu đỏ chỉ dành cho lỗi nhập liệu và xóa; giọng văn trung lập. *[Đã thay thế 18/10]* "Không ngân sách" → ngân sách tùy chọn, màu trung tính (31, 31b) |
| INS3 | Mua ngoài dự định chủ yếu do **khuyến mãi** và **cảm xúc**, dồn vào **buổi tối và khuya** | Q7 (21, 14), Q6 (26/30), D2, I1, I2 | 8 động cơ, trong đó có Khuyến mãi và Cảm xúc; Mô hình theo động cơ và khung giờ (Flow 2, 4) |
| INS4 | Họ muốn hiểu "vì sao" nhưng **không muốn bị giảng giải** | Q11 (24/30 chọn 4–5), I2, I3 | Góc nhìn viết dạng quan sát có số liệu, không lời khuyên (Flow 2, 8, 10) |
| INS5 | Bạn bè, KOL và mạng xã hội là tác nhân lớn, dù khảo sát mô phỏng ra thấp | D1 (51%, 55%), I3, I2. Q7 chỉ 4/30 (lệch, mục 4.5) | Giữ động cơ "Ảnh hưởng MXH"; cần khảo sát thật để kiểm lại |
| INS6 | Cần một chỗ để **dừng lại suy nghĩ** trước khi mua | Q15 (4,11 ở 18–25), Q14 (27/30), I3 | Danh sách mong muốn (Flow 6); Trước khi mua: 3 câu hỏi nhanh (Flow 9) |
| INS7 | Thường dùng **một tay**, thời gian ngắn | Q13 (17/30), I1, I4 | Nút chính cao 56 dp ghim ở đáy, vùng chạm ≥ 48 dp, lưới động cơ 2 × 4 trong nửa dưới màn hình |

### 6.3. Đối chiếu với giả định ban đầu

| Giả định khi viết brief | Kết quả research | Quyết định |
|---|---|---|
| Người dùng là sinh viên 22 tuổi, mua khuya | Đúng với nhóm 18–25 (11/19 chốt sau 22h). Nhưng 26–30 tuổi cũng có nhu cầu (Q11 TB 3,83) | Giữ P1. Thêm P2 (26 tuổi) làm persona phụ |
| Mạng xã hội là động cơ lớn | Mô phỏng: thấp. Nguồn thật D1: cao | Giữ, ghi rõ cần kiểm lại |
| Không ai thích cảnh báo đỏ | Sai với nhóm 31+ (4,60/5) | Giới hạn phạm vi ở người trẻ; nhóm 31+ thành anti-persona P5 |
| Người dùng muốn xem từng khoản | I4 muốn xem cả tháng hơn | Chiêm nghiệm tháng, xem theo tháng (Flow 2, 4) phục vụ P4 |

## 7. Hạn chế và việc nên làm tiếp

1. **Khảo sát và phỏng vấn là mô phỏng.** Kết quả trùng giả định "chưa có nguồn" ở bảng 4.1 là do chính giả định đó tạo ra, không phải bằng chứng.
2. **n = 30 quá nhỏ** để so sánh nhóm tuổi một cách thống kê. Nhóm 31+ chỉ có 5 người. Bảng 4.4 chỉ dùng để mô tả.
3. **D3 là nguồn quảng bá** của MoMo. Cần cài thử app để xác nhận.
4. **Câu hỏi tự báo cáo** (Q7, Q14) dễ lệch vì người trả lời ít nhận mình bị KOL ảnh hưởng. Có thể đây là một lý do khiến Q7 cho kết quả MXH thấp.
5. Việc nên làm nếu còn thời gian: gửi Google Form thật (bộ câu ở mục 4.2) cho 15–30 người, rồi thay số mô phỏng ở mục 4.3–4.4 bằng số thật.
6. *(18/10)* Hướng sản phẩm đã đổi. Theo yêu cầu của giảng viên (07:53 trong bản ghi: đổi hướng thì phải research lại), nhóm cần nghiên cứu lại cho hướng mới (mục 11). Dữ liệu mục 4–5 giữ nguyên làm lịch sử, luôn ghi [Mô phỏng], không trộn với kết quả mới.

## 8. Tệp đi kèm (`research-pack/`)

| Tệp | Nội dung |
|---|---|
| `survey_sim.py` | Script sinh khảo sát mô phỏng (seed 2026), chứa toàn bộ giả định |
| `charts.py` | Script vẽ biểu đồ. Script đọc `survey-summary.json`, file này **không có trong repo**, nên hiện không vẽ lại được biểu đồ từ repo |
| `chart-q1-tuoi.png` … `chart-q15-danh-sach.png` (16 ảnh, Q1–Q15 và `chart-q12-phan-bo.png`) | Biểu đồ khảo sát 14/10, ghi nhãn "Khảo sát MÔ PHỎNG (S01–S30, đã nhập vào Google Form)". Số trên biểu đồ có thể khác bảng 4.3 nếu nhóm đã vẽ lại từ bảng Google Form; **cần nhóm đối chiếu** |
| `usability_sim.py`, `usability-sim.json` | Số liệu kiểm thử mô phỏng (xem `usability-test.md`) |

**Không có trong repo (cố ý):** `survey-mo-phong.csv` (gỡ ngày 14/10) và các file `.xlsx` câu trả lời Google Form. File `.xlsx` của khảo sát 14/10 từng được commit (`35b981c`) và được bỏ theo dõi ngày 18/10; file vẫn còn trong lịch sử git. Dữ liệu thô không đưa lên GitHub công khai (`.gitignore` chặn `*.xlsx`, `*.csv`).

## 9. Khảo sát ngày 18/10/2026 – CHƯA XÁC MINH NGUỒN GỐC

### 9.1. Cấu trúc

Bảng câu trả lời Google Form *"Bạn mua sắm vì điều gì? – Khảo sát cho ứng dụng Why I Buy?"*, nhóm cung cấp ngày 18/10. 30 dòng, 1 cột dấu thời gian và 26 câu hỏi. **Không có cột định danh** (không email, tên, số điện thoại). File gốc không đưa vào repo.

Bộ câu hỏi bám theo hướng mới: thiết bị mua Shopee (điện thoại / máy tính), nơi lưu món "để xem lại", có quay lại xem không, muốn danh sách "để đó suy nghĩ thêm", nhắc trước đợt sale, sẵn sàng tự ghi giá, hạn mức theo nhóm, so sánh hai câu chữ Decision Card, chia sẻ giá ẩn danh, sẵn sàng thử prototype.

### 9.2. Kiểm tra nguồn gốc (chạy ngày 18/10)

| Kiểm tra | Kết quả | Ý nghĩa |
|---|---|---|
| Thời điểm gửi | Cả 30 câu trả lời nằm trong 18/10/2026 12:46–12:47, tổng **111,6 giây** | Không phải thời gian thu thập tự nhiên từ 30 người |
| Khoảng cách giữa hai lần gửi | Nhỏ nhất 3,7 s · trung vị 3,8 s · lớn nhất 4,1 s | Nhịp đều như script gửi tự động hoặc nhập lại dữ liệu có sẵn |
| So với file 14/10 | File 14/10 (15 câu, đã ghi là MÔ PHỎNG) cũng có 30 dòng trong 82 giây, cách nhau 2,6–3,3 s; hai file không trùng dòng nào | Cùng kiểu nhập; file 18/10 là bộ câu hỏi khác |
| Câu trả lời tự do (cột cuối) | Nhiều câu gần như trùng lời pain point của persona ("Thấy màu đỏ cảnh báo là muốn tắt app.", "Đang nhập thì bị gọi, quay lại mất hết.") | Dấu hiệu dữ liệu được dựng theo persona |
| Mẫu | 18–25 tuổi: 12/30; 26–30: 11/30; trên 30: 7/30 | Nhóm mục tiêu 18–25 chỉ chiếm 40% |

**Kết luận:** chưa có bằng chứng về quá trình thu thập. Dữ liệu này được xếp **NEEDS VERIFICATION, nhiều khả năng là mô phỏng nhập vào Google Form**. Đây không phải kết luận gian lận. Nhóm cần ghi lại: ai tạo các câu trả lời, bằng công cụ gì, có người thật nào trả lời không. Nếu là mô phỏng, đổi nhãn thành [Mô phỏng] như mục 4.

### 9.3. Số liệu tổng hợp (chỉ mô tả, không phải bằng chứng về người dùng thật)

n = 30 dòng. Câu chọn nhiều đáp án có tổng lớn hơn 30.

| Chủ đề | Kết quả tổng hợp |
|---|---|
| Thiết bị mua Shopee | Chủ yếu điện thoại, đôi khi máy tính 14 · Chỉ điện thoại 11 · Không dùng Shopee 3 · Chủ yếu máy tính 1 · Cả hai như nhau 1 |
| Khi thấy món muốn mua nhưng chưa chắc | Thêm vào giỏ, xem lại sau 12 · Chụp màn hình 6 · Mua luôn 5 · Bấm thích/lưu 4 · Bỏ qua 3 |
| Nơi lưu món "để xem lại" (chọn nhiều) | Giỏ hàng Shopee 18 · Ảnh chụp màn hình 11 · Nhắn cho chính mình 5 · Mục Thích 4 · Không lưu 4 · Ghi chú 3 |
| Có quay lại xem món đã lưu | Hiếm khi 12 · Thỉnh thoảng 7 · Hay quên mất 7 · Hay quay lại 4 |
| Muốn danh sách "để đó suy nghĩ thêm" (1–5) | 5: 8 · 4: 13 · 3: 6 · 2: 3 · 1: 0 |
| Nhắc trước đợt sale có thật (1–5) | 5: 3 · 4: 9 · 3: 7 · 2: 5 · 1: 6 |
| Sẵn sàng tự ghi giá khi lưu | Chỉ khi app gợi ý sẵn giá gần đây 9 · Không, sẽ bỏ qua 8 · Có, nếu chỉ vài giây 8 · Chỉ khi chụp màn hình là đủ 5 |
| Tự đặt hạn mức theo nhóm | Có nghĩ nhưng chưa làm 13 · Có, thường xuyên 8 · Chưa nghĩ tới 6 · Không cần 3 |
| Câu Decision Card dễ chịu hơn | A "Món này chiếm khoảng 44% phần còn lại của nhóm Công nghệ tháng này." 14 · Cả hai như nhau 12 · B "Bạn sắp vượt ngân sách nhóm Công nghệ." 2 · Không muốn thấy câu nào 2 |
| Cảm giác với báo đỏ "vượt ngân sách" (1 khó chịu – 5 hữu ích) | 1: 4 · 2: 14 · 3: 9 · 4: 2 · 5: 1 |
| Chia sẻ ẩn danh giá đã thấy | Có 12 · Có, nếu chắc chắn ẩn danh 8 · Chưa rõ 7 · Không 3 |
| Lý do mua ngoài dự định (chọn nhiều) | Khuyến mãi, flash sale 14 · Cảm xúc 8 · Mong muốn 7 · Bạn bè 7 · KOL, MXH 7 · Nhu cầu thực tế 3 · Tiện lợi 2 · Quảng cáo 1 |
| Thời gian chấp nhận để ghi một khoản mua | Dưới 10 s 4 · 10–20 s 13 · 20–30 s 4 · 30–60 s 7 · Trên 1 phút 2 |
| Sẵn sàng dành 10 phút thử prototype | Có 17 · Không 13 |

### 9.4. Có thể và không thể kết luận gì

- **Có thể:** bộ câu hỏi đã bao phủ các giả định chính của hướng mới (H: lưu món phân tán, quên quay lại, ngân sách theo nhóm, nhắc sale, tự ghi giá, extension). Bộ câu này **dùng lại được** cho khảo sát thật.
- **Không thể:** dùng các số trên để nói "người dùng muốn Smart Wishlist", "người dùng mua trên máy tính ít" hay "câu A dễ chịu hơn câu B". Mọi con số ở 9.3 không được đưa lên slide như kết quả thật; nếu đưa, phải kèm nhãn "Chưa xác minh / mô phỏng".

## 10. Tách loại kết luận (18/10/2026)

| Loại | Nội dung | Dùng thế nào |
|---|---|---|
| **Nguồn thật** | D1 (Gen Z 53,4% mua online hằng tuần; 51% chịu ảnh hưởng xu hướng MXH); D2 (FOMO giải thích 86,7% biến thiên mua bốc đồng trên Shopee Live, n = 310); C1–C4 (các app chi tiêu đều xoay quanh ngân sách và danh mục, theo mô tả nhà phát hành); lịch sale công khai của Shopee VN (blog chính thức, 25/9/2026) và điều khoản dịch vụ Shopee VN mục 3.1 (đặc tả Phụ lục A) | Được trích dẫn có nguồn |
| **Nghiên cứu mô phỏng (14/10)** | Khảo sát S01–S30, phỏng vấn I1–I5, kiểm thử khả dụng 5 người, INS1–INS7 | Minh họa quy trình; luôn ghi [Mô phỏng]; không làm bằng chứng persona |
| **Dữ liệu chưa xác minh (18/10)** | Khảo sát 30 dòng ở mục 9 | Chỉ số liệu tổng hợp, ghi "chưa xác minh"; chờ nhóm xác nhận cách thu thập |
| **Giả định nhóm đang dùng** | Người trẻ lưu món phân tán và quên quay lại; muốn tự cân nhắc theo ngân sách tự đặt; flash sale buổi tối là tác nhân; mua Shopee chủ yếu trên điện thoại (extension là kênh phụ – H6); sẵn sàng tự ghi hoặc xác nhận giá nếu nhanh; câu chữ trung tính tốt hơn cảnh báo | Ghi [ASSUMED] trong persona; đưa vào backlog kiểm chứng (mục 11) |
| **Kết luận được dữ liệu hỗ trợ** | Mua bốc đồng có cơ chế khuyến mãi/khan hiếm → FOMO (D2); người trẻ là nhóm mua online hằng tuần chính (D1); không thể lấy dữ liệu Shopee tự động một cách hợp lệ ở MVP (điều khoản 3.1, không có API cho người mua) | Căn cứ cho định vị và ràng buộc kỹ thuật |
| **Chưa thể kiểm chứng** | Tỉ lệ người mua Shopee trên máy tính; mức sẵn sàng cài extension; số thông báo chấp nhận được; phản ứng thật với Decision Card; có thật sự chờ sale và quay lại không; Shopee có kèm giá trong chữ chia sẻ không | Nghiên cứu thật (mục 11) |

## 11. Kế hoạch nghiên cứu cho hướng mới

Theo đặc tả mục 13.4 và Overview mục 11–12. Quy mô tối thiểu **chưa được giảng viên xác nhận**: đề xuất khảo sát 30–50 người 18–25 tuổi, phỏng vấn 5–8 người, kiểm thử prototype F11–F13 với 5 người.

| Mức | Giả định cần kiểm | Phương pháp | Dấu hiệu cần chứng minh |
|---|---|---|---|
| R1 · Critical | Người dùng có gặp khó khi lưu món? | Phỏng vấn tình huống gần nhất + quan sát thao tác | Mô tả nơi lưu thật; thời gian và lỗi khi lưu |
| R2 · Critical | Android Share với Shopee có dễ dùng không? | Prototype / thiết bị thật, 5–8 ca lưu | Thành công, không rơi link, ≤ 20 s |
| R3 · Critical | Thẻ ngân sách có hữu ích hay bị thấy là phán xét? | Think-aloud với 2 kiểu câu chữ | Hiểu số tiền tính từ dữ liệu nào; phản ứng cảm xúc |
| R4 · High | Có thật sự chờ sale và quay lại? | Phỏng vấn + test nhắc xem lại ngắn | Khả năng quay lại; không nhầm lịch sale với giá giảm |
| R5 · High | Nhìn lại có giúp hiểu động cơ không? | Prototype insight với dữ liệu thiếu và đủ | Giải thích đúng, không suy diễn |
| R6 · High | Bao nhiêu người mua Shopee trên máy tính? | Câu hỏi khảo sát thiết bị, tần suất, tình huống | Quyết định giữ hay thu hẹp extension |
| R7 · Medium | Gián đoạn có tạo nhu cầu riêng? | Interrupted-task + offline task | Tiếp tục được; không mất dữ liệu |
| R8 · Medium | Có sẵn sàng tự xác nhận giá? | Task nhập giá, quan sát chọn bỏ qua | Công sức nhập, tỉ lệ bỏ lưu, cách hiểu giá cũ |

Câu hỏi phỏng vấn mẫu (không dẫn dắt) ở Overview mục 12. Bảng bằng chứng sau nghiên cứu: `participantCode | method | date | situation | quote/action | observed/reported/inferred | persona | impact | design change`. Lấy đồng ý tham gia, ẩn danh, không đưa dữ liệu thô lên GitHub.
