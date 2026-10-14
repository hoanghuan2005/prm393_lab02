# Kiểm thử MÔ PHỎNG – Why I Buy? Lab 2. Seed cố định để tái lập.
import json, random
random.seed(393)
M,P,K = 1.35, 0.6, 0.33
R_SAVE = 1.2
klm = {
 "T1": dict(M=4,P=5,K=21,R=R_SAVE),   # Hub→03 nhập 45+000, tên 18 phím Telex → 04 chọn Cảm xúc → Lưu → đang lưu 1,2 s
 "T2": dict(M=3,P=5,K=14,R=0),        # Hub→11→Thêm món→12: tên 14 phím Telex, chọn 1 lý do, Lưu món
 "T3": dict(M=2,P=1,K=0,R=0),         # 07 Mô hình (tháng 10) → ‹ → đọc động cơ đầu bảng tháng 9
 "T4": dict(M=1,P=2,K=8,R=0),         # 07a lỗi: đọc lỗi → chạm ô mật khẩu → gõ 8 ký tự → Đăng nhập
 "T5": dict(M=2,P=2,K=0,R=0),         # 10 Cá nhân (chưa cấp quyền) → "Mở cài đặt" → nút bật ở 05a
}
base = {t: round(v["M"]*M + v["P"]*P + v["K"]*K + v["R"],2) for t,v in klm.items()}
target = {"T1":25,"T2":20}
# Người tham gia mô phỏng: hệ số làm quen (lần đầu dùng prototype) theo hồ sơ
U = {
 "U1": dict(hs="Nam, 22, SV năm cuối, dùng Shopee hằng ngày", gan="P1", f=1.15),
 "U2": dict(hs="Nữ, 26, nhân viên văn phòng", gan="P2", f=1.25),
 "U3": dict(hs="Nam, 19, SV năm 2", gan="P3", f=1.20),
 "U4": dict(hs="Nữ, 30, kế toán, có con nhỏ, test bằng một tay", gan="P4", f=1.35),
 "U5": dict(hs="Nam, 28, làm tự do, ít dùng app tài chính", gan="P1/P2", f=1.45),
}
# Phạt thời gian (giây) gắn với vấn đề quan sát được (xem usability-test.md mục 5)
pen = {
 ("U3","T1"): (5.0,"F2: phân vân Mong muốn / Cảm xúc, không thấy nút ?"),
 ("U5","T1"): (6.5,"F2: dừng ở bước 2, đọc lần lượt 8 thẻ"),
 ("U4","T3"): (4.0,"F3: dùng chip kỳ, mở sheet chọn tháng (cách đúng thứ hai)"),
 ("U5","T3"): (7.0,"F3: vào tab Lịch sử trước rồi mới quay lại"),
 ("U2","T5"): (1.4,"F4: chạm công tắc → sang 05a, dừng lại đọc vì tưởng công tắc bật ngay"),
 ("U4","T5"): (1.4,"F4: chạm công tắc → sang 05a, dừng lại đọc vì tưởng công tắc bật ngay"),
 ("U5","T5"): (2.7,"F4: đọc dòng chữ nhỏ, không chắc bấm vào đâu, chạm công tắc → sang 05a"),
 ("U3","T2"): (3.0,"Cuộn tìm ô giá, hỏi có bắt buộc không"),
}
fail = {}
rows=[]
for u,info in U.items():
  for t in klm:
    if (u,t) in fail:
      rows.append(dict(u=u,t=t,time=None,ok=False,note=fail[(u,t)])); continue
    noise = random.uniform(-0.6,0.9)
    p,note = pen.get((u,t),(0,""))
    tm = round(base[t]*info["f"] + noise + p,1)
    rows.append(dict(u=u,t=t,time=tm,ok=True,note=note))
# F1 quan sát ở T1: ai bấm Lưu khi chưa chủ động chạm thẻ động cơ (Cảm xúc chọn sẵn)
f1 = {"U1":True,"U2":True,"U3":False,"U4":True,"U5":False}
# SEQ 1–7 (dễ = 7)
seq = {"U1":[7,7,6,7,6],"U2":[6,6,6,7,5],"U3":[5,6,6,7,5],"U4":[6,6,5,6,5],"U5":[5,6,4,6,5]}
# SUS 10 câu (1–5)
sus_raw = {
 "U1":[5,1,5,1,4,2,5,1,4,1],
 "U2":[4,2,4,1,4,2,5,2,4,2],
 "U3":[4,2,4,2,4,2,4,2,4,1],
 "U4":[4,2,4,1,3,2,4,2,4,2],
 "U5":[3,2,4,2,3,3,4,2,3,2],
}
def sus(a): return sum((a[i]-1) if i%2==0 else (5-a[i]) for i in range(10))*2.5
sus_score={u:sus(a) for u,a in sus_raw.items()}
summary={}
for t in klm:
  ts=[r["time"] for r in rows if r["t"]==t and r["ok"]]
  okn=sum(r["ok"] for r in rows if r["t"]==t)
  srt=sorted(ts); n=len(srt)
  med = srt[n//2] if n%2 else round((srt[n//2-1]+srt[n//2])/2,1)
  d=dict(base=base[t],ok=f"{okn}/5",mean=round(sum(ts)/n,1),median=med,min=min(ts),max=max(ts))
  if t in target: d["dat_muc_tieu"]=f"{sum(x<=target[t] for x in ts)}/{n}"
  d["seq_tb"]=round(sum(seq[u][list(klm).index(t)] for u in U)/5,1)
  summary[t]=d
out=dict(klm=klm,base=base,participants=U,rows=rows,f1=f1,seq=seq,sus_raw=sus_raw,sus=sus_score,
         sus_mean=round(sum(sus_score.values())/5,1),summary=summary)
json.dump(out,open("usability-sim.json","w"),ensure_ascii=False,indent=1)
print(json.dumps(base,ensure_ascii=False)); print(json.dumps(summary,ensure_ascii=False,indent=1))
for r in rows: print(r)
print(sus_score, out["sus_mean"])
