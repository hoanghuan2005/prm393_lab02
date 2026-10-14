# Khảo sát MÔ PHỎNG (synthetic) — sinh 30 người trả lời theo giả định nêu trong research.md mục 3.2
import random, csv, json, collections
random.seed(2026)
AGE_GROUPS = [("18–21",8),("22–25",11),("26–30",6),("31–40",3),("41+",2)]
def pick(d):  # d: {option: weight}
    r = random.random()*sum(d.values()); s=0
    for k,w in d.items():
        s+=w
        if r<=s: return k
    return k
def multi(d):  # independent probabilities
    return [k for k,p in d.items() if random.random()<p]
rows=[]; rid=0
for age,n in AGE_GROUPS:
    for _ in range(n):
        rid+=1; young = age in ("18–21","22–25"); mid = age=="26–30"; older = age in ("31–40","41+")
        job = pick({"Sinh viên":6,"Sinh viên làm thêm / thực tập":5,"Nhân viên văn phòng":1,"Tự do":1} if age=="18–21" else
                   {"Sinh viên làm thêm / thực tập":6,"Nhân viên văn phòng":4,"Tự do":1} if age=="22–25" else
                   {"Nhân viên văn phòng":7,"Tự do":2,"Nội trợ / khác":1} if mid else
                   {"Nhân viên văn phòng":5,"Nội trợ / khác":3,"Tự do":2})
        inc = pick({"< 3 triệu":5,"3–7 triệu":4,"7–15 triệu":1} if age=="18–21" else
                   {"3–7 triệu":4,"7–15 triệu":5,"< 3 triệu":1} if age=="22–25" else
                   {"7–15 triệu":6,"> 15 triệu":3,"3–7 triệu":1} if mid else
                   {"7–15 triệu":4,"> 15 triệu":4,"3–7 triệu":2})
        freq = pick({"Hằng ngày":3,"2–3 lần/tuần":5,"1 lần/tuần":2,"Vài lần/tháng":1} if young else
                    {"2–3 lần/tuần":4,"1 lần/tuần":4,"Vài lần/tháng":2} if mid else
                    {"1 lần/tuần":3,"Vài lần/tháng":4,"Hiếm khi":3})
        chan = pick({"Shopee":4,"TikTok Shop":4,"GrabFood / ShopeeFood":3,"Lazada":1} if young else
                    {"Shopee":4,"GrabFood / ShopeeFood":3,"TikTok Shop":2,"Lazada":1} if mid else
                    {"Livestream Facebook":3,"Shopee":3,"Cửa hàng":4})
        hour = pick({"Sau 22h":6,"Tối 18–22h":3,"Trưa":1} if young else
                    {"Tối 18–22h":5,"Sau 22h":3,"Trưa":2} if mid else
                    {"Tối 18–22h":4,"Trưa":3,"Sáng":3})
        why = multi({"Khuyến mãi / flash sale":0.7,"Cảm xúc / stress":0.5,"Bạn bè / KOL / MXH":0.55,"Quảng cáo":0.3,"Tiện lợi":0.35,"Nhu cầu thật":0.2} if young else
                    {"Khuyến mãi / flash sale":0.55,"Cảm xúc / stress":0.6,"Bạn bè / KOL / MXH":0.3,"Quảng cáo":0.25,"Tiện lợi":0.4,"Nhu cầu thật":0.3} if mid else
                    {"Khuyến mãi / flash sale":0.6,"Cảm xúc / stress":0.2,"Bạn bè / KOL / MXH":0.15,"Quảng cáo":0.35,"Tiện lợi":0.3,"Nhu cầu thật":0.6}) or ["Nhu cầu thật"]
        app = pick({"Đã dùng rồi bỏ":6,"Chưa dùng":3,"Đang dùng":1} if young else
                   {"Đã dùng rồi bỏ":5,"Đang dùng":3,"Chưa dùng":2} if mid else
                   {"Chưa dùng":5,"Đang dùng":2,"Đã dùng rồi bỏ":3})
        quit = multi({"Nhập lâu, nhiều trường":0.7,"Hay quên ghi":0.6,"Cảm giác tội lỗi khi thấy cảnh báo / số âm":0.5,"Quá nhiều danh mục":0.4,"Không thấy lợi ích":0.35}) if app=="Đã dùng rồi bỏ" else []
        if app=="Đã dùng rồi bỏ" and not quit: quit=["Hay quên ghi"]
        acc = pick({"< 10 giây":3,"10–30 giây":6,"30–60 giây":1} if young else
                   {"10–30 giây":6,"< 10 giây":2,"30–60 giây":2} if mid else
                   {"30–60 giây":4,"10–30 giây":4,"> 60 giây":2})
        why_interest = pick({5:4,4:4,3:2} if young or mid else {3:3,2:4,4:2,1:1})
        red_alert = pick({1:4,2:4,3:2} if young else {2:4,3:4,4:2} if mid else {4:4,5:3,3:3})
        hand = pick({"Một tay":7,"Hai tay":3} if young or mid else {"Hai tay":7,"Một tay":3})
        regret = pick({"3–5 lần":4,"1–2 lần":4,"> 5 lần":2} if young else {"1–2 lần":5,"3–5 lần":3,"0 lần":2} if mid else {"0 lần":5,"1–2 lần":5})
        wishlist = pick({5:3,4:4,3:3} if young else {4:5,3:3,5:2} if mid else {3:4,2:4,4:2})
        rows.append({"ID":f"S{rid:02d}","Q1 Tuổi":age,"Q2 Nghề":job,"Q3 Thu nhập":inc,"Q4 Tần suất mua online":freq,"Q5 Kênh chính":chan,
          "Q6 Khung giờ hay chốt đơn":hour,"Q7 Lý do lần mua ngoài dự định":"; ".join(why),"Q8 App ghi chi tiêu":app,"Q9 Lý do bỏ app":"; ".join(quit),
          "Q10 Thời gian chấp nhận ghi 1 khoản":acc,"Q11 Muốn biết vì sao mua (1–5)":why_interest,"Q12 Cảm giác với cảnh báo đỏ (1 rất khó chịu – 5 hữu ích)":red_alert,
          "Q13 Cầm điện thoại khi mua":hand,"Q14 Số lần hối tiếc tháng qua":regret,"Q15 Muốn danh sách để suy nghĩ thêm (1–5)":wishlist})
with open("survey-mo-phong.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
N=len(rows); young=[r for r in rows if r["Q1 Tuổi"] in ("18–21","22–25")]
def cnt(rs,key,multi=False):
    c=collections.Counter()
    for r in rs:
        vals=[v for v in r[key].split("; ") if v] if multi else [r[key]]
        c.update(vals)
    return c
S={}
for key in ["Q1 Tuổi","Q2 Nghề","Q4 Tần suất mua online","Q5 Kênh chính","Q6 Khung giờ hay chốt đơn","Q8 App ghi chi tiêu","Q10 Thời gian chấp nhận ghi 1 khoản","Q13 Cầm điện thoại khi mua","Q14 Số lần hối tiếc tháng qua"]:
    S[key]=dict(cnt(rows,key).most_common())
S["Q7"]=dict(cnt(rows,"Q7 Lý do lần mua ngoài dự định",True).most_common())
quitters=[r for r in rows if r["Q8 App ghi chi tiêu"]=="Đã dùng rồi bỏ"]
S["Q9 (n bỏ app)"]=len(quitters); S["Q9"]=dict(cnt(quitters,"Q9 Lý do bỏ app",True).most_common())
avg=lambda rs,k: round(sum(r[k] for r in rs)/len(rs),2)
for k in ["Q11 Muốn biết vì sao mua (1–5)","Q12 Cảm giác với cảnh báo đỏ (1 rất khó chịu – 5 hữu ích)","Q15 Muốn danh sách để suy nghĩ thêm (1–5)"]:
    S[k]={"tất cả":avg(rows,k),"18–25":avg(young,k),"26+":avg([r for r in rows if r not in young],k)}
S["18–25 (n)"]=len(young)
S["18–25 chốt đơn sau 22h"]=sum(r["Q6 Khung giờ hay chốt đơn"]=="Sau 22h" for r in young)
S["18–25 một tay"]=sum(r["Q13 Cầm điện thoại khi mua"]=="Một tay" for r in young)
S["18–25 đã bỏ app"]=sum(r["Q8 App ghi chi tiêu"]=="Đã dùng rồi bỏ" for r in young)
S["18–25 chấp nhận ≤30s"]=sum(r["Q10 Thời gian chấp nhận ghi 1 khoản"] in ("< 10 giây","10–30 giây") for r in young)
S["Q11≥4 tất cả"]=sum(r["Q11 Muốn biết vì sao mua (1–5)"]>=4 for r in rows)
S["Q12≤2 tất cả"]=sum(r["Q12 Cảm giác với cảnh báo đỏ (1 rất khó chịu – 5 hữu ích)"]<=2 for r in rows)
S["Q15≥4 tất cả"]=sum(r["Q15 Muốn danh sách để suy nghĩ thêm (1–5)"]>=4 for r in rows)
S["41+ (n)"]=sum(r["Q1 Tuổi"]=="41+" for r in rows)
json.dump(S,open("survey-summary.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(json.dumps(S,ensure_ascii=False,indent=1))
