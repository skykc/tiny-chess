import json,os,urllib.request as r
U=os.environ["MAKEFUN_ENV_URL"]
V=[0,100,320,330,500,900]*2+[0]
S=('PPPPUZZ<UKFPPPPdUUZiZZdn~~~~PPPP',' (22(<PP2PZ_2U_d2P_d2UZ_(<PU (22','<FFFFPPPFPUZFUUZFPZZFZZZFUPP<FFF','PPPPUZZZKPPPKPPPKPPPKPPPKPPPPPPU','<FFKFPPPFPUUKPUUKPUUFUUUFPUP<FFK','2(( 2(( 2(( 2(( <22(F<<<ddPPdnZP')
P=[[ord(s[(7-(q>>4))*4+min(q&7,7-(q&7))])-80 for q in range(128)] for s in S]
NS=[-33,-31,-18,-14,14,18,31,33]
DS=[-17,-15,15,17]
RS=[-16,-1,1,16]
KS=sorted(DS+RS)
QS=DS+RS
K=[15]*128
K[0]=13;K[7]=14;K[4]=12;K[112]=7;K[119]=11;K[116]=3
TT={};N=0;B=120000
def A(b,q,w):
 d=16-32*w
 for s in (q-d+1,q-d-1):
  if not s&136 and b[s]==1+6*w:return 1
 for D,p in ((NS,2),(KS,6)):
  for d in D:
   if not (q+d)&136 and b[q+d]==p+6*w:return 1
 for D,c in ((DS,3),(RS,4)):
  for d in D:
   x=q+d
   while not x&136:
    p=b[x]
    if p:
     if p==c+6*w or p==5+6*w:return 1
     break
    x+=d
 return 0
def G(b,w,c,e):
 m=[]
 for s in range(128):
  p=b[s]
  if not p or (p<7)!=(w==0):continue
  t=p%6 or 6
  if t==1:
   d=16-32*w
   r=s>>4
   pr=5 if r==6-5*w else 0
   q=s+d
   if not b[q]:
    m.append(s|(q<<7)|(pr<<14))
    if not pr and r==1+5*w and not b[q+d]:m.append(s|((q+d)<<7))
   for q in (s+d-1,s+d+1):
    if q&136:continue
    if b[q] and (b[q]<7)!=(w==0):m.append(s|(q<<7)|(pr<<14))
    elif q==e:m.append(s|(q<<7))
  elif t==2 or t==6:
   for d in NS if t==2 else KS:
    q=s+d
    if q&136:continue
    if not b[q] or (b[q]<7)!=(w==0):m.append(s|(q<<7))
  else:
   for d in DS if t==3 else RS if t==4 else QS:
    q=s+d
    while not q&136:
     if b[q]:
      if (b[q]<7)!=(w==0):m.append(s|(q<<7))
      break
     m.append(s|(q<<7));q+=d
 for f,t,rr,k,x in ((4,6,7,1,5),(4,2,0,2,3),(116,118,119,4,117),(116,114,112,8,115)):
  if c&k and not(b[x] or b[t] or b[t-1]) and not(A(b,f,1-w) or A(b,x,1-w) or A(b,t,1-w)):m.append(f|(t<<7))
 return m
def M(b,w,c,e,kw,kb,m):
 f=m&127;t=m>>7&127;pr=m>>14
 n=b[:];p=n[f];n[f]=0
 if p%6==1 and t==e and not n[t]:n[t-16+32*w]=0
 n[t]=pr+6*w if pr else p
 if p%6==0 and abs(t-f)==2:
  if t>f:n[f+1],n[f+3]=n[f+3],0
  else:n[f-1],n[f-4]=n[f-4],0
 return n,1-w,c&K[f]&K[t],(f+t)//2 if p%6==1 and abs(t-f)==32 else -1,t if p==6 else kw,t if p==12 else kb
def E(b,w):
 s=0;B=[0,0]
 for q in range(128):
  p=b[q]
  if p:
   t=p%6 or 6
   s+=V[p]+P[t-1][q] if p<7 else -V[p]-P[t-1][q^112]
   B[p>6]+=t==3
 s+=30*((B[0]>1)-(B[1]>1))
 return s*(1-2*w)
def S(b,w,c,e,kw,kb,d,a,be,pl):
 global N
 N+=1
 if N>B:raise SystemExit
 KQ=kw if w==0 else kb
 q=d<1
 if q:
  chk=A(b,KQ,1-w)
  st=E(b,w)
  if not chk:
   a=max(a,st)
   if a>=be:return be
  y=None
 else:
  k=(bytes(b),w,c,e);y=TT.get(k)
  if y and y[0]>=d and y[2]==0:return y[1]
 mv=G(b,w,c,e)
 if q and not chk:
  mv=[m for m in mv if b[m>>7&127] or m>>14 or (m>>7&127)==e and b[m&127]%6==1]
 mv.sort(key=lambda m:(m==y[3] if y else 0,V[b[m>>7&127]],-V[b[m&127]]),reverse=True)
 bs=st if q and not chk else -999999
 bm=0;ao=a
 for m in mv:
  nb,nw,nc,ne,nkw,nkb=M(b,w,c,e,kw,kb,m)
  if A(nb,nkw if w==0 else nkb,1-w):continue
  s=-S(nb,nw,nc,ne,nkw,nkb,d-1,-be,-a,pl+1)
  if s>bs:bs=s;bm=m
  if s>a:a=s
  if a>=be:break
 if not bm:
  if q and not chk:return st
  return pl-100000 if A(b,KQ,1-w) else 0
 if not q:
  if len(TT)>99999:TT.clear()
  TT[k]=(d,bs,0 if ao<bs<be else 1 if bs>=be else 2,bm)
 return bs
def Z(s):return ord(s[0])-97+(ord(s[1])-49)*16
def U2(u):
 p=(5-"qrbn".find(u[4]))%6 if len(u)>4 else 0
 return Z(u[:2])|(Z(u[2:4])<<7)|(p<<14)
def R(g):
 b=bytearray(128)
 for i in range(8):
  b[i]=(4,2,3,5,6,3,2,4)[i];b[i+16]=1;b[i+96]=7;b[i+112]=b[i]+6
 w=0;c=15;e=-1;kw=4;kb=116
 for u in g["moves"]:
  b,w,c,e,kw,kb=M(b,w,c,e,kw,kb,U2(u))
 L=[[0,U2(u),u] for u in g["legal_moves"]]
 global N
 N=0
 try:
  for d in range(1,30):
   for x in L:
    x[0]=-S(*M(b,w,c,e,kw,kb,x[1]),d-1,-999999,999999,1)
   L.sort(key=lambda x:-x[0])
 except SystemExit:
  pass
 return L[0][2]
def J(p,y):
 return json.load(r.urlopen(U+p,json.dumps(y).encode()))
while(g:=J("/game",{}))["status"]!="done":
 while g["status"]=="your_move":
  g=J("/move",{"game":g["game"],"move":R(g)})
