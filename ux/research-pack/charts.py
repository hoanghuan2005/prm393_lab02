import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
S=json.load(open("survey-summary.json",encoding="utf-8"))
INK="#1A2320"; MUTED="#545E59"; BAR="#2E4A9E"; GRID="#E3E6E1"; BG="#FFFFFF"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11})
def hbar(data, title, subtitle, fname, order=None, n=30):
    items = [(k,data[k]) for k in order] if order else sorted(data.items(), key=lambda x:x[1])
    if not order: pass
    labels=[k for k,_ in items]; vals=[v for _,v in items]
    fig,ax=plt.subplots(figsize=(7.2,0.55*len(items)+1.4),dpi=200); fig.patch.set_facecolor(BG)
    bars=ax.barh(labels,vals,color=BAR,height=0.55)
    for b,v in zip(bars,vals):
        ax.text(b.get_width()+0.25,b.get_y()+b.get_height()/2,f"{v}  ({round(100*v/n)}%)",va="center",color=INK,fontsize=10)
    ax.set_xlim(0,max(vals)*1.35)
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID); ax.tick_params(colors=MUTED,length=0); ax.xaxis.grid(True,color=GRID,lw=0.8); ax.set_axisbelow(True)
    ax.set_xticks([])
    fig.text(0.02,0.97,title,fontsize=13,fontweight="bold",color=INK,va="top")
    fig.text(0.02,0.90,subtitle,fontsize=9.5,color=MUTED,va="top")
    plt.tight_layout(rect=(0,0,1,0.86)); fig.savefig(fname,facecolor=BG); plt.close(fig)
note="Khảo sát MÔ PHỎNG bằng AI, n = 30 (seed 2026) · Why I Buy? – Lab 2"
hbar(S["Q6 Khung giờ hay chốt đơn"],"Khung giờ hay chốt đơn online",note,"chart-q6-khung-gio.png",order=["Sáng","Trưa","Tối 18–22h","Sau 22h"])
hbar(S["Q7"],"Lý do của lần mua ngoài dự định gần nhất (chọn nhiều)",note,"chart-q7-ly-do-mua.png")
hbar(S["Q9"],f"Vì sao bỏ app ghi chi tiêu (n = {S['Q9 (n bỏ app)']} người đã bỏ, chọn nhiều)",note,"chart-q9-ly-do-bo-app.png",n=S['Q9 (n bỏ app)'])
hbar(S["Q10 Thời gian chấp nhận ghi 1 khoản"],"Thời gian chấp nhận để ghi 1 khoản mua",note,"chart-q10-thoi-gian.png",order=["> 60 giây","30–60 giây","10–30 giây","< 10 giây"])
# Q12 by age group: two bars, single hue + muted
fig,ax=plt.subplots(figsize=(7.2,2.6),dpi=200)
grp=["18–25 (n=19)","26+ (n=11)"]; v=[S["Q12 Cảm giác với cảnh báo đỏ (1 rất khó chịu – 5 hữu ích)"]["18–25"],S["Q12 Cảm giác với cảnh báo đỏ (1 rất khó chịu – 5 hữu ích)"]["26+"]]
b=ax.barh(grp[::-1],v[::-1],color=BAR,height=0.5)
for bb,val in zip(b,v[::-1]): ax.text(bb.get_width()+0.05,bb.get_y()+bb.get_height()/2,f"{val:.2f} / 5",va="center",color=INK,fontsize=10)
ax.set_xlim(0,5.6); ax.set_xticks([1,2,3,4,5]); ax.set_xticklabels(["1\nrất khó chịu","2","3","4","5\nhữu ích"],color=MUTED,fontsize=9)
for s in ["top","right","left"]: ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID); ax.tick_params(length=0,colors=MUTED)
fig.text(0.02,0.97,"Cảm giác khi thấy cảnh báo đỏ / vượt ngân sách (trung bình)",fontsize=13,fontweight="bold",color=INK,va="top")
fig.text(0.02,0.86,note,fontsize=9.5,color=MUTED,va="top")
plt.tight_layout(rect=(0,0,1,0.80)); fig.savefig("chart-q12-canh-bao-do.png",facecolor=BG); plt.close(fig)
print("ok")
