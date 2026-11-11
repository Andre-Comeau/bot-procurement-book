"""One losing job is not a claim: the underwriters' chapter figure (schematic, not data).
Usage: python images/one_losing_job.py images/one-losing-job  (writes .svg and .html)
"""
import sys
import html
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a,b,f):
    A=[int(a[i:i+2],16) for i in (1,3,5)];B=[int(b[i:i+2],16) for i in (1,3,5)]
    return "#%02x%02x%02x"%tuple(round(A[i]+(B[i]-A[i])*f) for i in range(3))
D={k:mix(C[k],C["ink"],0.2) for k in ("action","sec","acc","ink2")}
W,H=1600,1300
TARGET=0.70; TRIG=0.55
def t(x,y,s,cls,fill=None,anchor="start"):
    f=f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'
def mug(x,ytop,w,h,level,good,steam=True):
    o=[]
    yb=ytop+h
    fill=C["sec"] if good else C["acc"]
    lvl=yb-h*level
    o.append(f'<path d="M{x+w},{ytop+h*0.25} q{w*0.38},0 {w*0.38},{h*0.25} t-{w*0.38},{h*0.25}" fill="none" stroke="{C["ink"]}" stroke-width="5"/>')
    o.append(f'<rect x="{x}" y="{lvl:.1f}" width="{w}" height="{yb-lvl:.1f}" fill="{fill}" opacity="0.85"/>')
    o.append(f'<rect x="{x}" y="{ytop}" width="{w}" height="{h}" rx="6" fill="none" stroke="{C["ink"]}" stroke-width="4"/>')
    if steam and good:
        for k in (0.35,0.65):
            sx=x+w*k
            o.append(f'<path d="M{sx},{ytop-10} q-8,-10 0,-20 t0,-20" fill="none" stroke="{C["ink2"]}" stroke-width="3" opacity="0.5"/>')
    return o
def row(y,levels,title,sub,avg,verdict,pays):
    o=[t(80,y,title,"lab",C["ink"]),t(80,y+30,sub,"note",C["ink2"])]
    x0,w,h,gap=80,70,120,52
    ytop=y+150
    for i,l in enumerate(levels):
        o+=mug(x0+i*(w+gap),ytop,w,h,l,l>=TARGET)
    xe=x0+len(levels)*(w+gap)-gap
    for lv,col,dash,lab in ((TARGET,D["sec"],"10 7","target margin"),(TRIG,D["acc"],"4 6","trigger")):
        yy=ytop+h-h*lv
        o.append(f'<line x1="{x0-12}" y1="{yy:.1f}" x2="{xe+12}" y2="{yy:.1f}" stroke="{col}" stroke-width="3" stroke-dasharray="{dash}"/>')
    o.append(t(xe+46,ytop+h/2+20,"=","big",C["ink"],"middle"))
    # average mug
    ax,aw,ah=xe+96,130,200; aty=ytop+h-ah
    yb=aty+ah
    for lv,col,dash in ((TARGET,D["sec"],"10 7"),(TRIG,D["acc"],"4 6")):
        yy=yb-ah*lv
        o.append(f'<line x1="{ax-14}" y1="{yy:.1f}" x2="{ax+aw+64}" y2="{yy:.1f}" stroke="{col}" stroke-width="3" stroke-dasharray="{dash}"/>')
    lvl=yb-ah*avg
    good=avg>=TRIG
    o.append(f'<path d="M{ax+aw},{aty+ah*0.25} q{aw*0.36},0 {aw*0.36},{ah*0.25} t-{aw*0.36},{ah*0.25}" fill="none" stroke="{C["ink"]}" stroke-width="6"/>')
    o.append(f'<rect x="{ax}" y="{lvl:.1f}" width="{aw}" height="{yb-lvl:.1f}" fill="{C["sec"] if avg>=TRIG else C["acc"]}" opacity="0.85"/>')
    if pays:
        ytr=yb-ah*TRIG
        gap_h=lvl-ytr
        ins=gap_h*0.8
        o.append(f'<rect x="{ax}" y="{ytr:.1f}" width="{aw}" height="{ins:.1f}" fill="{C["action"]}" opacity="0.8"/>')
        o.append(f'<rect x="{ax}" y="{ytr+ins:.1f}" width="{aw}" height="{gap_h-ins:.1f}" fill="{C["ink2"]}" opacity="0.45"/>')
    o.append(f'<rect x="{ax}" y="{aty}" width="{aw}" height="{ah}" rx="8" fill="none" stroke="{C["ink"]}" stroke-width="5"/>')
    o.append(t(ax+aw/2,yb+36,"the average","note",C["ink2"],"middle"))
    o.append(t(ax+aw+74,yb-ah*TARGET+8,"target margin","note",D["sec"]))
    o.append(t(ax+aw+74,yb-ah*TRIG+8,"trigger","note",D["acc"]))
    vx=ax+aw+74
    o.append(t(vx,yb-40,verdict[0],"verdict",D["sec"] if not pays else D["action"]))
    for k,line in enumerate(verdict[1:]):
        o.append(t(vx,yb-6+k*28,line,"note",C["ink2"]))
    return o
o=[f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append(t(80,86,"THE UNDERWRITERS' CHAPTER · THE INSURABLE EVENT","eyebrow"))
o.append(t(80,148,"One losing job is not a claim","title"))
o.append(t(80,190,"Each mug is a completed job, filled to the margin it made against the costs declared on bid day.","dek"))
o.append(t(80,218,"The policy only looks at the average across a broad spectrum of tenders.","dek"))
good=[0.82,0.76,0.40,0.88,0.72,0.79,0.35,0.85]
bad=[0.35,0.52,0.22,0.30,0.75,0.28,0.40,0.18]
avg_g=sum(good)/len(good); avg_b=sum(bad)/len(bad)
o+=row(290,good,"A normal year","A few jobs come up short. The bot still did its job on average.",avg_g,
       ["No payment","The average stays above","the trigger. The losses on","single jobs stay with the bidder."],False)
o+=row(760,bad,"A bad year","Most jobs fall short. The bot missed its promised margin.",avg_b,
       ["The policy pays","Blue: the insurer's share","of the shortfall below","the trigger. Grey: the","bidder's own share."],True)
o.append(t(80,H-40,"Schematic, not data: the levels show the idea, not test results.","foot",C["ink2"]))
css=f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 24px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.note{{font:400 21px "IBM Plex Sans",Arial,sans-serif}}
.verdict{{font:700 28px Georgia,serif}}
.big{{font:700 64px Georgia,serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}'+"".join(o)+"</svg>"
stem=sys.argv[1] if len(sys.argv)>1 else "one-losing-job"
open(stem+".svg","w").write(svg)
open(stem+".html","w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>'+svg+"</body></html>")
print(round(avg_g,3),round(avg_b,3))
