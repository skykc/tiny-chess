import json,os,urllib.request as r
U=os.getenv("MAKEFUN_ENV_URL")
V=[0,100,320,330,500,900]*2+[0]
S=('PPPPUZZ<UKFPPPPdUUZiZZdn~~~~PPPP',' (22(<PP2PZ_2U_d2P_d2UZ_(<PU (22','<FFFFPPPFPUZFUUZFPZZFZZZFUPP<FFF','PPPPUZZZKPPPKPPPKPPPKPPPKPPPPPPU','<FFKFPPPFPUUKPUUKPUUFUUUFPUP<FFK','2(( 2(( 2(( 2(( <22(F<<<ddPPdnZP')
P=[[ord(s[(7-(q>>4))*4+min(q&7,7-(q&7))])-80 for q in range(128)] for s in S]
T=[[0]*128]+[[V[p]+P[(p-1)%6][q] if p<7 else -V[p]-P[(p-1)%6][q^112] for q in range(128)] for p in range(1,13)]
NS=[-33,-31,-18,-14,14,18,31,33]
DS=[-17,-15,15,17]
RS=[-16,-1,1,16]
KS=QS=DS+RS
K={0:13,7:14,4:12,112:7,119:11,116:3}
TT={};N=0;B=120000
def A(b,q,w):
 d=16-32*w;g=6*w
 for s in (q-d+1,q-d-1):
  if not s&136 and b[s]==1+g:return 1
 for D,p in ((NS,2),(KS,6)):
  for d in D:
   if not (q+d)&136 and b[q+d]==p+g:return 1
 for D,c in ((DS,3),(RS,4)):
  for d in D:
   x=q+d
   while not x&136:
    p=b[x]
    if p:
     if p==c+g or p==5+g:return 1
     break
    x+=d
 return 0
def G(b,w,c,e):
 m=[];u=w==0
 for s,p in enumerate(b):
  if not p or (p<7)!=u:continue
  t=p%6 or 6
  if t==1:
   d=16-32*w
   r=s>>4
   pr=5 if r==6-5*w else 0
   q=s+d
   if not b[q]:
    m.append(s|q<<7|pr<<14)
    if not pr and r==1+5*w and not b[q+d]:m.append(s|((q+d)<<7))
   for q in (s+d-1,s+d+1):
    if q&136:continue
    if b[q] and (b[q]<7)!=u:m.append(s|q<<7|pr<<14)
    elif q==e:m.append(s|q<<7)
  elif t==2 or t==6:
   for d in NS if t==2 else KS:
    q=s+d
    if q&136:continue
    if not b[q] or (b[q]<7)!=u:m.append(s|q<<7)
  else:
   for d in DS if t==3 else RS if t==4 else QS:
    q=s+d
    while not q&136:
     if b[q]:
      if (b[q]<7)!=u:m.append(s|q<<7)
      break
     m.append(s|q<<7);q+=d
 for f,t,k,x in ((4,6,1,5),(4,2,2,3),(116,118,4,117),(116,114,8,115)):
  if c&k and not(b[x] or b[t] or b[t-1]) and not(A(b,f,1-w) or A(b,x,1-w) or A(b,t,1-w)):m.append(f|t<<7)
 return m
def M(b,w,c,e,kw,kb,m):
 f=m&127;t=m>>7&127;pr=m>>14
 n=b[:];p=n[f];n[f]=0
 if p%6==1 and t==e and not n[t]:n[t-16+32*w]=0
 n[t]=pr+6*w if pr else p
 if p%6==0 and abs(t-f)==2:
  if t>f:n[f+1],n[f+3]=n[f+3],0
  else:n[f-1],n[f-4]=n[f-4],0
 return n,1-w,c&K.get(f,15)&K.get(t,15),(f+t)//2 if p%6==1 and abs(t-f)==32 else -1,t if p==6 else kw,t if p==12 else kb
def E(b,w):
 s=0
 for q,p in enumerate(b):s+=T[p][q]
 return (s+30*((b.count(3)>1)-(b.count(9)>1)))*(1-2*w)
def S(b,w,c,e,kw,kb,d,a,be,pl):
 global N
 N+=1
 if N>B:raise SystemExit
 KQ=(kw,kb)[w]
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
  mv=[m for m in mv if b[m>>7&127] or m>>14 or m>>7&127==e and b[m&127]%6==1]
 mv.sort(key=lambda m:(m==y[3] if y else 0)*1e6+V[b[m>>7&127]]*1024-V[b[m&127]],reverse=True)
 bs=st if q and not chk else -1e6
 bm=0;ao=a
 for m in mv:
  nb,nw,nc,ne,nkw,nkb=M(b,w,c,e,kw,kb,m)
  if A(nb,(nkw,nkb)[w],1-w):continue
  s=-S(nb,nw,nc,ne,nkw,nkb,d-1,-be,-a,pl+1)
  if s>bs:bs=s;bm=m
  if s>a:a=s
  if a>=be:break
 if not bm:
  if q and not chk:return st
  return pl-1e5 if A(b,KQ,1-w) else 0
 if not q:
  if len(TT)>1e5:TT.clear()
  TT[k]=(d,bs,0 if ao<bs<be else 1+(bs<=ao),bm)
 return bs
def Z(s):return ord(s[0])+16*ord(s[1])-881
def U2(u):
 p=5-"qrbn".find(u[4]) if len(u)>4 else 0
 return Z(u[:2])|Z(u[2:4])<<7|p<<14
def R(g):
 b=bytearray(128)
 for i,x in enumerate((4,2,3,5,6,3,2,4)):
  b[i]=x;b[i+16]=1;b[i+96]=7;b[i+112]=x+6
 w=0;c=15;e=-1;kw=4;kb=116
 for u in g["moves"]:
  b,w,c,e,kw,kb=M(b,w,c,e,kw,kb,U2(u))
 L=[[0,U2(u),u] for u in g["legal_moves"]]
 global N
 N=0
 try:
  for d in range(1,30):
   for x in L:
    x[0]=-S(*M(b,w,c,e,kw,kb,x[1]),d-1,-1e6,1e6,1)
   L.sort(key=lambda x:-x[0])
 except SystemExit:
  pass
 return L[0][2]
def J(p,y):
 try:return json.load(r.urlopen(U+p,json.dumps(y).encode(),timeout=5))
 except:return J(p,y)
while(g:=J("/game",{}))["status"]!="done":
 while g["status"]=="your_move":
  g=J("/move",{"game":g["game"],"move":R(g)})
