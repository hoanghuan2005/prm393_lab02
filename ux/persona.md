# Persona – Why I Buy? · Smart Shopping Companion

> **Trạng thái: Proto-Persona [ASSUMED].** Bốn persona dưới đây là giả thuyết phân khúc của nhóm, chưa được kiểm chứng bằng nghiên cứu người dùng thật. Nguồn: *Why I Buy – Overview & Persona Guideline* v2.0 (17/10/2026) và *Final Unified Product & Technical Specification* v1.0 (17/10/2026), mục 1.4.
>
> Khảo sát n = 30, 5 phỏng vấn và kiểm thử khả dụng trong repo là **MÔ PHỎNG** (xem [`research.md`](research.md)); chúng không được dùng làm bằng chứng "Observed" hay "Reported" cho persona. Khảo sát ngày 18/10 chưa xác minh được nguồn gốc (xem `research.md` mục 9). Bản persona cũ (14/10, 5 persona) được lưu ở [`archive/before-2026-10-18/ux/persona.md`](../archive/before-2026-10-18/ux/persona.md).

## 1. Cấp chứng cứ dùng trong file này

| Cấp | Định nghĩa | Trong file này |
|---|---|---|
| Observed | Nhóm đã quan sát hành vi thật, có ghi chú được phép dùng | Chưa có |
| Reported | Người tham gia nói trong khảo sát / phỏng vấn thật | Chưa có |
| Inferred | Suy luận từ mẫu hành vi quan sát hoặc báo cáo, có chuỗi lập luận | Chưa có |
| **Assumed** | Giả định của nhóm từ tài liệu cũ hoặc đề xuất sản phẩm | **Hầu hết mọi trường của P1–P4** |
| Simulated | Lời nói, persona, số liệu do AI tạo cho demo | Chỉ minh họa, không làm chứng cứ |

## 2. Tổng quan và thứ tự ưu tiên

Mức ưu tiên thiết kế: **P1 → P3 → P2 → P4**. Mã P1–P4 giữ như tài liệu cũ để không làm vỡ liên kết với Figma, repo và slide.

| Mã · ưu tiên | Persona | Hành vi khác biệt | Nhiệm vụ cốt lõi | Rào cản riêng | Flow phụ trách |
|---|---|---|---|---|---|
| **P1 · Primary (1)** | Nguyễn Hải Nam, 22 – mua sắm trên Android, thao tác nhanh và cân nhắc | Ghét nhập liệu dài và lời nhắc phán xét | Lưu nhanh → cân nhắc → quyết định | Gián đoạn buổi tối, chưa có giá, thao tác một tay | F11, F12, Flow 1/6/9 |
| **P3 · Secondary (2)** | Lê Gia Huy, 19 – so sánh ưu tiên, ngân sách và đợt sale | Giữ nhiều món muốn mua; quan tâm ngân sách và sale | So sánh ưu tiên → Chờ → kiểm tra lại | Nhầm lịch sale với giá chắc chắn giảm | F11, F12 |
| **P2 · Secondary (3)** | Trần Thu Linh, 26 – nhìn lại động cơ sau mua | Quan tâm lý do và xu hướng chi tiêu sau mua hơn lúc lưu món | Ghi động cơ → xem mô hình → tự phản tư | Insight suy diễn quá mức hoặc nghe như phán xét | Flow 1/2/4/8–10 |
| **P4 · Supporting (4)** | Phạm Ngọc Mai, 29 – bối cảnh gián đoạn, thao tác một tay | Chỉ có những khoảng thao tác rất ngắn, thường bị ngắt quãng | Lưu dở → quay lại → tiếp tục | Mất nháp, nút nhỏ, thông báo quá nhiều | F11 offline/lỗi, Flow 1 |
| P5 · Anti-persona | Đỗ Văn Hùng – nhu cầu quản trị tài chính gia đình đầy đủ | — | — | — | Không (giới hạn phạm vi) |

**Vì sao 4 persona, không phải 5.** Mỗi persona được giữ vì đại diện một nhiệm vụ khác nhau trong hành trình *lưu → cân nhắc → quyết định → nhìn lại*. Anti-persona chỉ dùng để giới hạn phạm vi và không được đếm vào số persona. **Quy tắc gộp sau nghiên cứu:** nếu P4 không cho thấy nhu cầu hay quyết định UI khác P1, gộp P4 vào phần ràng buộc của P1. Nếu hành vi mua trên máy tính tạo ra việc cần làm rõ ràng khác điện thoại, cân nhắc thêm một persona máy tính dựa trên bằng chứng thật, không tự tạo để biện minh cho extension.

## 3. P1 · Nguyễn Hải Nam (Primary)

Persona đại diện vòng trải nghiệm đầy đủ: đường vào trên Android, số bước lưu, ngôn ngữ trung tính và tính nhất quán Wishlist → khoản mua. **[ASSUMED]**

| # | Trường | Nội dung |
|---|---|---|
| 01 | Hồ sơ / vai trò | 22 tuổi · sinh viên năm cuối CNTT kiêm thực tập · Android là thiết bị chính |
| 02 | Ưu tiên | 1 – đại diện hành trình sản phẩm |
| 03 | Bối cảnh sử dụng | Có những khoảng thời gian ngắn sau giờ học, giờ làm để xem Shopee trên Android; hay gặp flash sale buổi tối, sau 22:00; có thể thao tác một tay, trong ánh sáng yếu |
| 04 | Mục tiêu | Lưu món mà không mua ngay; xem tác động lên mức chi tự đặt; tự quyết định; nhìn lại lý do sau mua |
| 05 | Việc cần làm (JTBD) | Khi gặp một sản phẩm hấp dẫn trên điện thoại, tôi muốn lưu và cân nhắc trong ít bước để quyết định theo nhu cầu thực tế, không bị cản trở hay phán xét |
| 06 | Hành vi hiện tại | Có thể chụp màn hình hoặc bỏ vào giỏ hàng; từng bỏ app chi tiêu nhiều bước; đôi lúc mua vào lúc khuyến mãi. Toàn bộ là giả thuyết kế thừa persona cũ |
| 07 | Nỗi đau | Nhập nhiều trường; giọng trách móc, cảnh báo đỏ; món đã lưu bị quên; không biết giá đã ghi có bị tính vào chi tiêu không |
| 08 | Động lực | Muốn tự kiểm soát quyết định mà không bị bắt giảm chi; thích thao tác nhanh, minh bạch, riêng tư |
| 09 | Ràng buộc và accessibility | Android 360–412 dp; một tay, ngón cái chỉ với tới nửa dưới màn hình; cận 2 độ nên cần chữ ≥ 14 sp, tương phản ≥ 4,5 : 1, nút ≥ 48 dp. Chưa khẳng định thói quen mua trên máy tính |
| 10 | Kịch bản chính | **F11:** chia sẻ tai nghe từ Shopee → bottom sheet có tên nhưng thiếu giá → lưu thành công → Decision Card → Chờ 3 ngày. **F12:** được nhắc, mở lại, cập nhật giá, tự chọn Mua hoặc Bỏ qua |
| 11 | Tiêu chí thành công | Trong bài test 5 người: lưu món ≤ 20 giây; hiểu Wishlist không phải đã chi; giải thích đúng ba nút Mua · Chờ · Bỏ qua; không mất dữ liệu khi để trống giá |
| 12 | Bằng chứng và trạng thái | PROTO-PERSONA / ASSUMED. Nguồn: persona cũ, Overview mục 07, đặc tả mục 1.4, 4, 9, 11. Chưa có phỏng vấn hay quan sát thật |

**Kịch bản S1 – "Lưu món rồi xem lại, không phải mua ngay"** *(dữ liệu trong kịch bản là MÔ PHỎNG)*

| # | Nam làm | App phản hồi | Nhánh lỗi / phục hồi |
|---|---|---|---|
| 1 | Chọn Chia sẻ → Why I Buy? trên app Shopee | 19a đang lấy thông tin → 19 bottom sheet Lưu món | Không tách được link → 19e lưu thủ công hoặc nhập tay |
| 2 | Xác nhận tên, có thể bỏ qua giá | Món ở trạng thái Đang cân nhắc; 19g snackbar "Đã lưu" | Mất mạng → lưu trên máy, không báo "đã đồng bộ" |
| 3 | Mở món → Decision Card | Hiện giá có nguồn và ngày, phần trăm ngân sách nếu đã đặt | Chưa đặt ngân sách → không tính phần trăm, có "Thiết lập" và "Để sau" |
| 4 | Bấm Chờ, chọn "Sau 3 ngày" | Lưu ngày xem lại, đặt nhắc cục bộ nếu được cấp quyền | Chưa cấp quyền thông báo → vẫn có mục "Cần xem lại" trong app |
| 5 | Đến hẹn, mở lại, chọn Mua hoặc Bỏ qua | Mua → Ghi khoản mua điền sẵn, chỉ thành Đã mua khi lưu xong | Thoát trước khi lưu → món vẫn Đang cân nhắc; Bỏ qua có Hoàn tác |

## 4. P3 · Lê Gia Huy (Secondary)

Giúp nhóm xác định ngân sách theo nhóm hàng, so sánh nhiều món và cách thể hiện sale mà không hứa món sẽ giảm. Khác Nam ở chỗ phải chọn giữa nhiều món trong một hạn mức. **[ASSUMED]**

| # | Trường | Nội dung |
|---|---|---|
| 01 | Hồ sơ / vai trò | 19 tuổi · sinh viên · thiết bị Android và mức chi cần khảo sát |
| 02 | Ưu tiên | 2 – đại diện so sánh lựa chọn và chờ sale |
| 03 | Bối cảnh sử dụng | Xem nhiều món cùng nhóm, theo dõi các đợt sale; cân nhắc giữa phụ kiện, quần áo và nhu cầu khác trong tháng |
| 04 | Mục tiêu | Đặt ưu tiên cho nhiều món; biết món nào ảnh hưởng hạn mức tự đặt; được nhắc xem lại đúng lúc; không nhầm lịch sale với giá chắc chắn giảm |
| 05 | Việc cần làm (JTBD) | Khi có nhiều món muốn mua trong một mức chi cố định, tôi muốn lưu, so sánh và xem lại giá đúng lúc để chọn món phù hợp nhất, thay vì quyết định theo cảm giác "sắp hết sale" |
| 06 | Hành vi hiện tại | Có thể lưu nhiều món vào giỏ hàng / mục Thích rồi quên; theo dõi ngày sale trên mạng xã hội. Cần phỏng vấn xác thực |
| 07 | Nỗi đau | FOMO; nhiều món tranh cùng ngân sách; đánh đồng thông báo ngày sale với cam kết món sẽ rẻ; giá đã ghi bị cũ |
| 08 | Động lực | Muốn không bỏ lỡ nhưng vẫn tự quyết và ưu tiên nhu cầu quan trọng |
| 09 | Ràng buộc | Nguồn tiền (gia đình hỗ trợ, làm thêm) là giả thuyết, không bắt nhập thu nhập. Giá có thể thiếu hoặc khác phân loại, phải gắn ngày |
| 10 | Kịch bản chính | **F11:** lưu áo từ Shopee, chọn động cơ Khuyến mãi; Decision Card (28c) cho thấy 2 món cùng nhóm và phần trăm ngân sách. **F12:** Chờ đến đợt sale đã công bố, cập nhật giá có nguồn rồi Mua hoặc Bỏ qua |
| 11 | Tiêu chí thành công | Phân biệt được lịch sale với dự báo giảm giá; so sánh hai món không cần hướng dẫn; hiểu phần trăm ngân sách tính từ khoản đã ghi; quyết định mà không thấy bị thúc ép |
| 12 | Bằng chứng và trạng thái | PROTO-PERSONA / ASSUMED. Nguồn: persona cũ, đặc tả mục 7–9. Không có dữ liệu thật xác nhận hành vi chờ sale |

## 5. P2 · Trần Thu Linh (Secondary)

Đại diện công việc sau mua: hiểu động cơ, giới hạn của dữ liệu không đầy đủ, cách diễn giải không gây cảm giác bị phán xét. **[ASSUMED]**

| # | Trường | Nội dung |
|---|---|---|
| 01 | Hồ sơ / vai trò | 26 tuổi · nhân viên văn phòng · thiết bị mua sắm cần xác nhận |
| 02 | Ưu tiên | 3 – đại diện giá trị sau mua |
| 03 | Bối cảnh sử dụng | Có thể xem lại khoản chi cuối tuần, cuối tháng sau giai đoạn làm việc căng thẳng; bối cảnh mua quần áo, mỹ phẩm là giả thuyết |
| 04 | Mục tiêu | Tự quan sát động cơ, so sánh các tháng, đối chiếu mức hài lòng sau mua mà không bị phê phán |
| 05 | Việc cần làm (JTBD) | Khi nhìn lại những món đã mua, tôi muốn thấy các mẫu động cơ có cơ sở trong dữ liệu đã ghi, để hiểu và tự điều chỉnh thói quen theo cách của mình |
| 06 | Hành vi hiện tại | Có thể ghi chi tiêu rời rạc hoặc chỉ nhìn tổng tiền cuối tháng; chưa có số liệu xác thực về công cụ đang dùng |
| 07 | Nỗi đau | Chỉ thấy tổng tiền mà quên hoàn cảnh lúc mua; câu khuyên mang tính phán xét; báo cáo suy diễn từ dữ liệu thiếu |
| 08 | Động lực | Muốn hiểu khuynh hướng mua của chính mình hơn là được chấm điểm tiết kiệm |
| 09 | Ràng buộc | Thiết bị cần khảo sát; biểu đồ phải có chữ giải thích, không chỉ dùng màu |
| 10 | Kịch bản chính | Ghi một khoản mua với động cơ Cảm xúc (Flow 1) → một tháng sau vào Góc nhìn → xem nhận định AI (Flow 8–10) → đánh giá nhận định đó có đáng tin không |
| 11 | Tiêu chí thành công | Ghi khoản mua ≤ 25 giây; chỉ ra đúng dữ liệu nào được tính; giải thích được insight mà không thấy bị phán xét |
| 12 | Bằng chứng và trạng thái | PROTO-PERSONA / ASSUMED. Nguồn: persona cũ, đặc tả mục 4, 7. Dữ liệu phỏng vấn gốc là MÔ PHỎNG, không xem là Reported |

## 6. P4 · Phạm Ngọc Mai (Supporting)

Ca kiểm tra tác vụ bị ngắt quãng: lưu cục bộ, giữ nháp, phục hồi lỗi, thao tác một tay. Nếu nghiên cứu không xác nhận khác biệt với P1, nên gộp thay vì giữ persona tượng trưng. **[ASSUMED]**

| # | Trường | Nội dung |
|---|---|---|
| 01 | Hồ sơ / vai trò | 29 tuổi · làm văn phòng, có trách nhiệm gia đình · dùng smartphone |
| 02 | Ưu tiên | 4 – ràng buộc thao tác ngắn và phục hồi |
| 03 | Bối cảnh sử dụng | Chỉ có những khoảng thao tác ngắn; có thể chuyển app, mất mạng hoặc dừng giữa chừng |
| 04 | Mục tiêu | Lưu nháp nhanh; tiếp tục đúng chỗ đang làm; không mất tên, giá đã nhập; thấy rõ trạng thái đồng bộ |
| 05 | Việc cần làm (JTBD) | Khi bị ngắt quãng lúc lưu món hay ghi khoản mua, tôi muốn app giữ thông tin và giúp tiếp tục dễ dàng để không phải làm lại từ đầu |
| 06 | Hành vi hiện tại | Có thể để việc ghi khoản mua đến cuối ngày và thao tác khi đang bận; chưa xác minh thói quen thực tế |
| 07 | Nỗi đau | Mất dữ liệu sau khi chuyển app; form nhiều trường; nút khó chạm; thông báo sai thời điểm; mạng yếu |
| 08 | Động lực | Giảm công sức, tránh quên, tự kiểm soát thời điểm nhận nhắc |
| 09 | Ràng buộc | Một tay; nội dung rõ; thử gián đoạn, offline, 360/412 dp. Không dùng tuổi làm lý do loại trừ |
| 10 | Kịch bản chính | **F11:** mở Chia sẻ → nhập tên → bị ngắt quãng → quay lại → lưu cục bộ. **Flow 1:** ghi khoản mua rồi chuyển app giữa chừng → quay lại, dữ liệu còn nguyên |
| 11 | Tiêu chí thành công | Không mất trường đã nhập khi bị gián đoạn; hoàn thành bằng một tay; nhận biết được "đã lưu trên máy / chưa đồng bộ"; không gặp ngõ cụt |
| 12 | Bằng chứng và trạng thái | PROTO-PERSONA / ASSUMED. Persona hỗ trợ, có thể gộp vào P1 |

## 7. P5 · Anti-persona (giới hạn phạm vi)

**Đỗ Văn Hùng** đại diện nhu cầu **quản trị tài chính gia đình đầy đủ**: đối soát ngân hàng, tự phân loại mọi giao dịch, lập báo cáo tài chính chi tiết. Why I Buy? không nhằm vào nhu cầu này. Anti-persona được xác định theo **nhu cầu, không theo tuổi tác**: người lớn tuổi có nhu cầu lưu món và cân nhắc trước khi mua vẫn nằm trong phạm vi, và sản phẩm giữ accessibility phù hợp (chữ ≥ 14 sp, tương phản ≥ 4,5 : 1, vùng chạm ≥ 48 dp).

## 8. Ma trận persona → flow

● = dùng chính · ○ = có dùng · trống = ít liên quan. F11–F13 là flow của hướng mới (xem [`user-flow.md`](user-flow.md)).

| Flow | P1 Nam | P3 Huy | P2 Linh | P4 Mai |
|---|:-:|:-:|:-:|:-:|
| 1 – Ghi nhanh một khoản mua | ● | ○ | ● | ● |
| 2 – Mô hình → Góc nhìn → Chiêm nghiệm | ○ | | ● | |
| 3 – Xem lại, sửa hoặc xóa (có hoàn tác) | ○ | | ○ | ○ |
| 4 – Xem theo tháng / năm | | | ● | |
| 5 – Cá nhân & dữ liệu | ○ | ○ | ○ | ○ |
| 6 – Danh sách mong muốn (v1) | ● | ● | | |
| 7 – Khởi động, đăng nhập, tài khoản | ● | ● | ● | ● |
| 8 – Nhận định AI sau khi lưu | ○ | | ● | |
| 9 – Trước khi mua: 3 câu hỏi nhanh | ● | ○ | | |
| 10 – AI phân tích mô hình | | | ● | |
| **F11 – Android Share → Wishlist → Decision Card** | ● | ● | | ● (offline, lỗi) |
| **F12 – Chờ → nhắc đợt sale → quyết định** | ● | ● | | |
| **F13 – Extension → ghép thiết bị → đồng bộ** | ○ (chưa xác minh) | ○ (chưa xác minh) | | |

F13 chưa có persona phụ trách chính: nhu cầu mua sắm trên máy tính **chưa được xác minh** (giả định H6 trong Overview). Extension là kênh phụ cho tới khi có khảo sát thật.

## 9. Persona → nhu cầu → quyết định UI → cách kiểm chứng

| Persona · nhiệm vụ | Nhu cầu | Quyết định UI (màn Figma) | Cách kiểm chứng |
|---|---|---|---|
| P1 · F11 chia sẻ rồi lưu | Không nhập nhiều, không mất link | Bottom sheet 19 có tên sửa được, giá không bắt buộc (19c), lưu trên máy | ≤ 20 giây; không mất dữ liệu; phân biệt "đã lưu" với "đã mua" |
| P1 + P3 · F12 chờ rồi quyết định | Xem lại vào lúc tự chọn | 29 Chờ (3 ngày / đến đợt sale), giá kèm ngày (30, 30b), ba lựa chọn bằng nhau ở 28 | Giải thích được kết quả và giới hạn của dữ liệu |
| P3 · Decision Card | Cân nhắc ngân sách và các món cạnh tranh | 31 Ngân sách theo nhóm, 28c món cùng nhóm, so sánh giá chỉ khi "so được" | Hiểu phần trăm và sự không chắc chắn của sale |
| P2 · Flow 1 + Góc nhìn | Nhớ động cơ, xem mẫu hành vi | Ô động cơ, Lịch sử, nhận định có câu "Gợi mở" | ≤ 25 giây ghi khoản mua; hiểu đúng số mẫu và kết luận |
| P4 · F11 lỗi | Quay lại sau khi bị ngắt | Lưu trên máy, trạng thái đồng bộ, thử lại | Không mất trường, không ngõ cụt |
| (chưa xác minh) · F13 | Nếu có nhu cầu: lưu trên máy tính rồi xem trên Android | Extension lưu cục bộ → ghép mã 6 số → đồng bộ; không bắt ghép mới được lưu | Khảo sát tỉ lệ mua trên máy tính; test ghép mã và xử lý mã sai |

## 10. Phát biểu vấn đề

> Người trẻ mua sắm trực tuyến như Nam muốn giữ lại những món đang cân nhắc, nhưng thiếu một quy trình ngắn, liên tục và dễ hiểu để nối món đó với ngân sách tự đặt, nhu cầu, động cơ mua và kết quả sau mua; các cách lưu rời rạc (giỏ hàng, ảnh chụp) hay nhật ký chi tiêu chỉ hỗ trợ một phần hành trình này.

*Đây là giả thuyết thiết kế, chưa phải phát hiện từ nghiên cứu thật.*

**How Might We:** Làm thế nào để người dùng lưu một món trong vài giây, tự cân nhắc trên những thông tin họ cung cấp và quay lại quyết định đúng lúc, mà không bị ép nhập nhiều hay cảm thấy bị chấm điểm?

## 11. Tiêu chí thành công đo được

Là **mục tiêu kiểm thử**, chưa phải kết quả (đặc tả mục 1.4).

| Mã | Mục tiêu | Đo bằng | Kết quả hiện có |
|---|---|---|---|
| KPI-01 | Lưu một món vào Wishlist dưới 20 giây (từ lúc bấm Chia sẻ hoặc icon extension đến khi thấy xác nhận) | Usability test F11 | Chưa có (chưa test thật) |
| KPI-02 | Ghi một khoản mua kèm động cơ trong 25 giây | Usability test Flow 1 | MÔ PHỎNG (Flow cũ): 4/5 đạt, trung vị 21,7 giây – [`usability-test.md`](usability-test.md) |
| KPI-03 | Người thử giải thích đúng ý nghĩa Mua · Chờ · Bỏ qua | Think-aloud F11/F12 | Chưa có |
| KPI-04 | Không người thử nào nhầm giá đã ghi của món chưa mua với tiền đã chi | Hỏi sau task F11 | Chưa có |
| KPI-05 | Ít nhất 80% người thử hoàn thành F11–F13 không cần hướng dẫn | Usability test 5 người | Chưa có |

## 12. Việc còn phải làm để persona có bằng chứng

Theo Overview mục 11, 16 và đặc tả mục 13.4:

1. Nhóm thống nhất 4 proto-persona và đồng ý rằng mọi đặc điểm hiện mới là ASSUMED.
2. Chạy workshop persona theo guideline và lưu ảnh, biên bản thật. **Không ghi "đã chạy workshop" khi chưa có biên bản.**
3. Nghiên cứu thật theo quy mô giảng viên duyệt (đề xuất: khảo sát 30–50 người 18–25 tuổi, phỏng vấn 5–8 người, kiểm thử prototype 5 người). Ghi Observed/Reported tách khỏi Simulated.
4. Kiểm thử kịch bản P1 với F11, F12, gồm nhánh thiếu giá, offline và Back trước khi mua.
5. Kiểm tra P1 và P3 có thật sự khác nhau không, và P4 có cần là persona riêng không.
