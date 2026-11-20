import json,os,sys,urllib.request as r
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("MAKEFUN_ENV_URL is not set")
S="KKKKKKKKUUUUUUUUMMOQQOMMLLMPPMLLKKKOOKKKLJIKKIJLLMMGGMMLKKKKKKKKACEEEECACGKKKKGCEKMNNMKEELNOONLEEKNOONKEELMNNMLECGKLLKGCACEEEECAGIIIIIIGIKKKKKKIIKLMMLKIILLMMLLIIKMMMMKIIMMMMMMIILKKKKLIGIIIIIIGKKKKKKKKLMMMMMMLJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJKKKLLKKKGIIJJIIGIKKKKKKIIKLLLLKIJKLLLLKJKKLLLLKJILLLLLKIIKLKKKKIGIIJJIIGECCAACCEECCAACCEECCAACCEECCAACCEGEECCEEGIGGGGGGIOOKKKKOOOQMKKMQOACEGGECAEGIKKIGEEIOQQOIEEIQSSQIEEIQSSQIEEIOQQOIEEEKKKKEEAEEEEEEA"
V=[(ord(c)-75)*5 for c in S]
Y=[0,100,320,330,500,900,0]
KN=[-33,-31,-18,-14,14,18,31,33];KG=[-17,-16,-15,-1,1,15,16,17];BD=[-17,-15,15,17];RD=[-16,-1,1,16]
Z=[];x=987654321
for i in range(1561):
 x=(x*6364136223846793005+1442695040888963407)&(1<<64)-1;Z.append(x)
B=[0]*128;W=1;C=0;E=-1;H=0;K1=4;K2=116;N=[0];BG=70000;TT={};KL=[[0,0] for _ in range(64)];HP={};GI=-1
def J(p,s): return (p-1 if p>0 else 5-p)*128+s
def A(q,y):
 b=B
 if y>0:
  for t in (q-15,q-17):
   if not t&136 and b[t]==1: return 1
 else:
  for t in (q+15,q+17):
   if not t&136 and b[t]==-1: return 1
 for d in KN:
  t=q+d
  if not t&136 and b[t]==y*2: return 1
 for d in KG:
  t=q+d
  if not t&136 and b[t]==y*6: return 1
 for d in BD:
  t=q+d
  while not t&136:
   p=b[t]
   if p:
    if p==y*3 or p==y*5: return 1
    break
   t+=d
 for d in RD:
  t=q+d
  while not t&136:
   p=b[t]
   if p:
    if p==y*4 or p==y*5: return 1
    break
   t+=d
 return 0
def G():
 m=[];s=W
 for q in range(128):
  if q&136: continue
  p=B[q]
  if not p or (p>0)!=(s>0): continue
  a=abs(p)
  if a==1:
   d=16*s;pr=7 if s>0 else 0;t=q+d
   if not t&136 and not B[t]:
    if (t>>4)==pr:
     for v in (5,4,3,2): m.append(q|t<<7|v<<14)
    else:
     m.append(q|t<<7)
     if (q>>4)==(1 if s>0 else 6) and not B[q+2*d]: m.append(q|(q+2*d)<<7)
   for t in (q+d-1,q+d+1):
    if t&136: continue
    if (B[t] and (B[t]>0)!=(s>0)) or t==E:
     if (t>>4)==pr:
      for v in (5,4,3,2): m.append(q|t<<7|v<<14)
     else: m.append(q|t<<7)
  elif a==2 or a==6:
   for d in (KN if a==2 else KG):
    t=q+d
    if not t&136 and (not B[t] or (B[t]>0)!=(s>0)): m.append(q|t<<7)
  else:
   for d in (BD if a==3 else RD if a==4 else BD+RD):
    t=q+d
    while not t&136:
     if not B[t]: m.append(q|t<<7)
     else:
      if (B[t]>0)!=(s>0): m.append(q|t<<7)
      break
     t+=d
 if s>0 and K1==4:
  if C&1 and not B[5] and not B[6] and B[7]==4 and not A(4,-1) and not A(5,-1) and not A(6,-1): m.append(4|6<<7)
  if C&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and not A(4,-1) and not A(3,-1) and not A(2,-1): m.append(4|2<<7)
 elif s<0 and K2==116:
  if C&4 and not B[117] and not B[118] and B[119]==-4 and not A(116,1) and not A(117,1) and not A(118,1): m.append(116|118<<7)
  if C&8 and not B[115] and not B[114] and not B[113] and B[112]==-4 and not A(116,1) and not A(115,1) and not A(114,1): m.append(116|114<<7)
 return m
def M(m):
 global W,C,E,H,K1,K2
 f=m&127;t=(m>>7)&127;v=m>>14;p=B[f];s=W;cs=t;cp=B[t]
 if abs(p)==1 and t==E and not cp: cs=t-16*s;cp=B[cs]
 u=(m,cp,cs,C,E,H,K1,K2)
 if C: H^=Z[1537+C]
 if E>=0: H^=Z[1553+(E&7)]
 H^=Z[1536];B[f]=0
 if cp: H^=Z[J(cp,cs)];B[cs]=0
 H^=Z[J(p,f)];np=v*s if v else p;H^=Z[J(np,t)];B[t]=np
 if abs(p)==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1) if t>f else (f-4,f-1);rp=B[rf];H^=Z[J(rp,rf)];B[rf]=0;H^=Z[J(rp,rt)];B[rt]=rp
 if p==6: K1=t
 if p==-6: K2=t
 c=C
 if f==0 or t==0: c&=~2
 if f==7 or t==7: c&=~1
 if f==112 or t==112: c&=~8
 if f==119 or t==119: c&=~4
 if p==6: c&=~3
 if p==-6: c&=~12
 C=c;E=-1
 if abs(p)==1 and abs(t-f)==32: E=(f+t)//2
 if C: H^=Z[1537+C]
 if E>=0: H^=Z[1553+(E&7)]
 W=-s;return u
def X(u):
 global W,C,E,H,K1,K2
 m,cp,cs,c,e,h,k1,k2=u;f=m&127;t=(m>>7)&127;v=m>>14;p=B[t]
 if abs(p)==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1) if t>f else (f-4,f-1);B[rf]=B[rt];B[rt]=0
 B[f]=v and (1 if p>0 else -1) or p;B[t]=0
 if cp: B[cs]=cp
 C=c;E=e;H=h;K1=k1;K2=k2;W=-W
def L():
 o=[]
 for m in G():
  u=M(m);k=K1 if W<0 else K2
  if not A(k,W): o.append(m)
  X(u)
 return o
def V_():
 sc=0;ph=0;wb=0;bb=0;wm=0;we=0;bm=0;be=0
 for q in range(128):
  if q&136: continue
  p=B[q]
  if not p: continue
  a=abs(p);r=q>>4;f=q&7
  if p>0:
   i=(7-r)*8+f
   if a==6: wm=V[320+i];we=V[384+i]
   else: sc+=Y[a]+V[(a-1)*64+i]
   if a==3: wb+=1
  else:
   i=r*8+f
   if a==6: bm=V[320+i];be=V[384+i]
   else: sc-=Y[a]+V[(a-1)*64+i]
   if a==3: bb+=1
  if a==2 or a==3: ph+=1
  elif a==4: ph+=2
  elif a==5: ph+=4
 ph=min(ph,24);sc+=(wm*ph+we*(24-ph)-bm*ph-be*(24-ph))//24
 if wb>1: sc+=30
 if bb>1: sc-=30
 return (sc if W>0 else -sc)+10
def O(mv,pl,tm):
 f=mv&127;t=(mv>>7)&127;v=mv>>14;cp=B[t];s=0
 if mv==tm: s+=1000000
 if cp: s+=Y[abs(cp)]*10-Y[abs(B[f])]//10
 if v: s+=900+v*100
 if KL[pl][0]==mv: s+=5000
 elif KL[pl][1]==mv: s+=4000
 return -s
def Q(a,b,pl):
 N[0]+=1
 if N[0]>BG: raise StopIteration
 if HP.get(H,0)>1: return 0
 st=V_()
 if st>=b: return b
 if st>a: a=st
 if pl>24: return a
 ic=A(K1 if W>0 else K2,-W)
 if ic: mv=L()
 else:
  mv=[m for m in G() if B[m>>7&127] or m>>14 or (m>>7&127)==E]
 mv.sort(key=lambda m:O(m,pl,0))
 for m in mv:
  u=M(m);k=K1 if W<0 else K2
  if A(k,W): X(u);continue
  try: s=-Q(-b,-a,pl+1)
  except StopIteration: X(u);raise
  X(u)
  if s>=b: return b
  if s>a: a=s
 return a
def S(d,a,b,pl):
 global W,E,H
 N[0]+=1
 if N[0]>BG: raise StopIteration
 if HP.get(H,0)>1: return 0
 if d<=0: return Q(a,b,pl)
 ic=A(K1 if W>0 else K2,-W);e=TT.get(H);tm=0
 if e and e[0]>=d:
  if e[2]==0: return e[1]
  if e[2]==1 and e[1]>=b: return e[1]
  if e[2]==2 and e[1]<=a: return e[1]
  tm=e[3]
 if d>=3 and not ic and pl>0:
  hm=0
  for q in range(128):
   if not q&136 and B[q] and (B[q]>0)==(W>0) and abs(B[q])>1: hm=1;break
  if hm:
   oe=E;oh=H
   if E>=0: H^=Z[1553+(E&7)]
   E=-1;H^=Z[1536];W=-W
   try: s=-S(d-3,-b,-b+1,pl+1)
   except StopIteration: E=oe;H=oh;W=-W;raise
   E=oe;H=oh;W=-W
   if s>=b: return b
 mv=L()
 if not mv: return -100000+pl if ic else 0
 mv.sort(key=lambda m:O(m,pl,tm));best=-10**9;bm=mv[0];oa=a
 for i,m in enumerate(mv):
  u=M(m)
  try:
   if not i: s=-S(d-1,-b,-a,pl+1)
   elif i>3 and d>=3 and not ic and not u[1] and not m>>14:
    s=-S(d-2,-a-1,-a,pl+1)
    if s>a: s=-S(d-1,-b,-a,pl+1)
   else:
    s=-S(d-1,-a-1,-a,pl+1)
    if s>a: s=-S(d-1,-b,-a,pl+1)
  except StopIteration: X(u);raise
  X(u)
  if s>best: best=s;bm=m
  if s>a:
   a=s
   if a>=b:
    if KL[pl][0]!=m: KL[pl]=(m,KL[pl][0])
    break
 TT[H]=(d,best,1 if best>=b else 2 if best<=oa else 0,bm)
 return best
def R():
 global TT,KL
 TT={};KL=[[0,0] for _ in range(64)];mv=L()
 if not mv: return 0
 if len(mv)==1: return mv[0]
 best=mv[0];bs=-10**9
 for d in range(1,9):
  N[0]=0;cur=best;al=-10**9
  mv.sort(key=lambda m:0 if m==best else 1)
  try:
   for m in mv:
    u=M(m);s=-S(d-1,-10**9,-al,1);X(u)
    if s>al: al=s;cur=m
  except StopIteration: break
  best=cur;bs=al
  if N[0]>=BG: break
 return best
def F(fen):
 global B,W,C,E,H,K1,K2
 B=[0]*128;H=0;mp={'P':1,'N':2,'B':3,'R':4,'Q':5,'K':6,'p':-1,'n':-2,'b':-3,'r':-4,'q':-5,'k':-6}
 z=fen.split();rows=z[0].split('/')
 for ri,row in enumerate(rows):
  rk=7-ri;f=0
  for ch in row:
   if ch.isdigit(): f+=int(ch)
   else:
    q=rk*16+f;pc=mp[ch];B[q]=pc;H^=Z[J(pc,q)]
    if pc==6: K1=q
    if pc==-6: K2=q
    f+=1
 W=1 if z[1]=='w' else -1;C=0
 for ch in z[2]: C|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
 E=-1
 if z[3]!='-': E=(ord(z[3][0])-97)+(int(z[3][1])-1)*16
 if C: H^=Z[1537+C]
 if E>=0: H^=Z[1553+(E&7)]
 if W<0: H^=Z[1536]
 HP[H]=HP.get(H,0)+1
def P(p,bo):
 q=r.Request(U+p,data=json.dumps(bo).encode(),headers={"content-type":"application/json"})
 try:
  with r.urlopen(q) as s: return json.load(s)
 except Exception as ex: sys.exit(str(ex))
def uci(m):
 f=m&127;t=(m>>7)&127;v=m>>14
 return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+("qrbn"[5-v] if v else "")
if __name__=="__main__":
 while True:
  g=P("/game",{})
  if g["status"]=="done": break
  if g["game"]!=GI: HP.clear();GI=g["game"]
  while g["status"]=="your_move":
   F(g["fen"]);g=P("/move",{"game":g["game"],"move":uci(R())})
  print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
 print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
