# グラフ生成コード一覧 は graph_book.py 参照
import graph_book

# networkx で大抵のことはできるようだが、あえてそれは使わない
# (https://networkx.org/documentation/stable/tutorial.html , https://networkx.org/documentation/stable/reference/index.html)


# tree DFS
import sys;sys.setrecursionlimit(7**6);(n,),*e=[map(int,o.split())for o in open(0)];*g,=eval('[],'*n)
for x,y in e:g[x]+=y,;g[y]+=x,
def D(v,u):[('pre_order',D(w,v),'post_order')for w in g[v]if w-u]

# stack-based tree DFS
*P,=S=[0]*n;i=1
while i:
 i-=1;p=S[i] # post-order?
 for e in{*g[p]}-{P[p]}:S[i]=e;P[e]=p;i+=1 # pre-order

# flag-based tree DFS
p=[0,0]+[1]*~-n;q=[1]
for i in q:
 for j in g[i]:q+=[j]*p[j];p[j]=0;'pre-order'
for i in q[::-1]:'post-order'

# visited-flag-based tree BFS
(n,_),*I=[map(int,o.split())for o in open(0)];v=[0]*-~n;g=[[]for _ in v];Q=[1]
for a,b in I[:n-1]:g[a]+=b,;g[b]+=a,
for i in Q:
 for j in g[i]:
  if v[j]<1<j:v[j]=1;Q+=j, # process each vertex

# shortest_path (頂点間の辺の数＝重み1) with using queue (BFS)
def D(s,g):
 d=[-1]*len(g);q=[s];d[s]=0
 for f in q:
  for t in g[f]:
   if d[t]<0:d[t]=d[f]+1;q+=t,
 return d

# 文字迷路によるダイクストラ法
from heapq import*;f=lambda:map(int,input().split());h,w=f();s,S=f();g,G=f();d=[w*[9e9]for _ in[0]*h];m=[input()for _ in d];q=[(0,s-1,S-1)];d[s-1][S-1]=0
def U(v,x,y):
 if(h>x>-1<y<w)and'#'!=m[x][y]!=v<d[x][y]:d[x][y]=v;heappush(q,(v,x,y))
while q:v,x,y=heappop(q);v>d[x][y]or(U(v+1,x-1,y),U(v+1,x+1,y),U(v+1,x,y-1),U(v+1,x,y+1))
print(d[g-1][G-1])
# Ver. 1-dim
def U(v,f,t):
 if-1<t<h*w and(w<2 or{f%w,t%w}!={0,w-1})>0<v+1<d[t]!='#'!=M[t]:d[t]=v+1;heappush(q,(v+1,t))
while q:v,x=heappop(q);v>d[x]or[U(v,x,x+i)for i in(-w,-1,1,w)]

# 文字迷路によるBFS
t,*A=open(a:=0);h,w=map(int,t.split());A=''.join(A)+'#'*w;s={t:=A.find('S')};q=[(a,t)]
for v,x in q:
 for i in~-x,-~x,x+~w,x-~w:
  if(A[i]in'#\n')+(i in s)<1:s|={i};q+=(v+1,i),;'G'!=A[i]or(a:=v+1)
print(a)

# 文字迷路をはじめとした文字入力によるBFS(の例)
from collections import*;F=lambda x,y:0 # to-do
I,*s=open(0);h,w,x,y,X,Y=map(int,I.split());d=[4**9]*w*h;d[x*w+y+~w]=0;q=deque([(x-1,y-1,0)])
while q:
 x,y,v=q.popleft()
 for i in-2,4,5,9: # ((i%3-1),(i%4-1))=[(0,1),(0,-1),(1,0),(-1,0)]
  if(h>(a:=x+(i%3-1))>-1<(b:=y+(i%4-1))<w)and(e:=v+(f:=F(a,b)))<d[t:=a*w+b]:d[t]=e;[q.appendleft,q.append][f]((a,b,e))
print(d[X*w+Y+~w])

# 文字迷路によるDFS
m,n,*M=map(int,open(0).read().split());V=m*n*[1]
def D(f):V[f]=0;t=max((0<=t<m*n)and(m<2 or{f%m,t%m}!={0,m-1})*V[t]*M[t]and D(t)for t in(f+m,f-m,f+1,f-1));V[f]=1;return-~t
print(max(D(i)for i in range(m*n)if M[i]))

# 頂点を疑似的に削除できるグラフ(1-based,e[0]は頂点数)
e=[0]*-~n;g=[[]for _ in e]
def A(x,y):e[0]+=(e[x]<1)+(e[y]<1);g[x]+=y,;g[y]+=x,;e[x]+=1;e[y]+=1
def R(x):
 u=[];e[0]-=(e[x]>0);e[x]=0
 for y in g[x]:e[0]-=(e[y]==1);u+=[y]*(f:=e[y]>0);e[y]-=f
 return u
def N(x,include_removed=0):return[y for y in g[x]if include_removed+e[y]]

# BFSで木の直径(通過する辺の数が最大となるもの)を求める
(n,),*e=[map(int,o.split())for o in open(0)];*g,=eval('[],'*-~n)
for x,y in e:g[x]+=y,;g[y]+=x,
def B(a):
 q=[a];d=[-1]*-~n;d[a]=0
 for x in q:
  for y in g[x]:
   if d[y]<0:d[y]=d[x]+1;q+=y,
 return(d[q[-1]],q[-1])
print(B(B(1)[1])[0])

# 転倒数(inversion number, BITの応用)
# 各要素が正整数かつ値がメモリ圧迫しない場合、座標圧縮部分は省略可
c={v:i for i,v in enumerate(sorted(set(a)),1)};n=len(c);T=[s:=0]*-~n
def U(i):
 while-~n>i:T[i]+=1;i+=i&-i
def S(i,v=0):
 while i:v+=T[i];i-=i&-i
 return v
for v in a:s+=S(c[v]-1);U(c[v])

# ビット列を使ったDPによる巡回セールスマン問題(隣接行列の場合)
def tsp(dist,is_cyclic):
 c=9e9;r=range;n=len(dist);R=r(n);d=[n*[c]for _ in[0]*(1<<n)]
 for i in r(n-is_cyclic*~-n):d[1<<i][i]=0
 for b in r(1<<n):
  for u in R:
   for v in R:
    if b>>u&b>>v&1:d[b][v]=min(d[b][v],d[1<<v^b][u]+dist[u][v])
 for e in R:c=min(c,d[-1][e]+is_cyclic*dist[e][0])
 return c
# 超短縮版(ABC 073-D)
import itertools as o;print(min(sum(int(l[i][j])for i,j in zip(a,a[1:]))for a in o.permutations(range(n))))

# ビット列を使ったDPによるTSP(Traveling Salesman Problem = 巡回セールスマン問題, 重み付き隣接リストの場合)
# cyclic
I=1<<60;r=range;n=len(g);d=[n*[I]for _ in[0]*2**n];d[0][0]=0
for b in r(1<<n):
 for u in r(n):
  for v,c in g[u]:d[b][v]=min(d[b][v],[I,d[1<<v^b][u]+c][b>>v&1])
print(-~d[-1][0]%-~I-1)
# linear
I=1<<60;r=range;n=len(g);d=[n*[I]for _ in[0]*2**n]
for i in r(n):d[1<<i][i]=0
for b in r(1<<n):
 for u in r(n):
  for v,c in g[u]:d[b][v]=min(d[b][v],[I,d[1<<v^b][u]+c][b>>u&b>>v&1])
print(-~min(d[-1])%-~I-1)

# 強連結成分(Strongly Connected Components, SCC)および、そのトポロジカルソートを求める(gは有向グラフの隣接リスト)
# https://inzkyk.xyz/algorithms/depth_first_search/strong_components_in_linear_time/
# 強連結成分① Kosarajuのアルゴリズム
def kosaraju_scc(g):
 r=range(n:=len(g));v=[0]*n;stack=[]
 # First DFS: record finishing times
 def dfs1(i):
  v[i]=1
  for j in g[i]:v[j]or dfs1(j);stack+=i,
 for i in r:v[i]or dfs1(i)
 # Reverse the graph
 rg=[[]for _ in v]
 for i in r:
  for j in g[i]:rg[j]+=i,
 # Second DFS: extract SCCs
 v=[0]*n;L=[]
 def dfs2(i,C):
  v[i]=1;C+=i,
  for j in rg[i]:v[j]or dfs2(j,C)
 while stack:
  if v[i:=stack.pop()]^1:dfs2(i,C:=[]);L+=C,
 return L

# 強連結成分② Tarjanのアルゴリズム
def tarjan_scc(g):
 n=len(g);visitID=[-1]*n;lowlink=[-1]*n;fixed=[0]*n;stk=[];SCCs=[];c=[0]
 def dfs(i):
  visitID[i]=lowlink[i]=c[0];c[0]+=1;stk.append(i)
  for j in g[i]:
   if visitID[j]<0:dfs(j);lowlink[i]=min(lowlink[i],lowlink[j])
   elif fixed[j]^1:lowlink[i]=min(lowlink[i],visitID[j])
  if lowlink[i]==visitID[i]:
   scc=[];p=-1
   while p-i:p=stk.pop();fixed[p]=1;scc+=p,
   SCCs+=scc,
 for i in range(n):fixed[i]or dfs(i)
 return SCCs[::-1]

# グラフの縮約(contraction: ABC 411-F)
(n,m),*l,_,q=[map(int,o.split())for o in open(0)];r=[*range(n+1)];p=[[i]for i in r];e=[set()for _ in r];u=[0];v=[0]
for x,y in l:e[x]|={y};e[y]|={x};u+=x,;v+=y,
for i in q:
 if(x:=r[u[i]])-(y:=r[v[i]]):
  if len(e[x])+len(p[x])>len(e[y])+len(p[y]):x,y=y,x
  for j in p[x]:p[y]+=j,;r[j]=y
  for z in e[x]:
   if(z==y)+(z in e[y]):m-=1
   else:e[y]|={z};e[z]|={y}
   e[z].remove(x)
  p[x]=[];e[x]=set() # not necessary
 print(m)

# サイクル構造があればtrue
def has_cycle(g):
 d=[0]*(n:=len(g)) # in-degree
 for v in sum(g,[]):d[v]+=1
 q=[i for i in range(n)if d[i]<1]
 for v in q:
  for t in g[v]:d[t]-=1;q+=[t]*(d[t]<1)
 return sum(d)>0
# another way
V=set();F=set();c=[0] # visited, finished, has_cycle
def D(i):
 V.add(i)
 for j in g[i]:
  if(j in F)+c[0]<1:c[0]+=(j in V);D(j)
 F.add(i)


# 最適二分探索木(Optimal BST, https://atcoder.jp/contests/atc002/tasks/atc002_c)
# 順序を保ったまま Σw[i]*depth(i)を最小化
# O(nlogn)解法があるが、O(n^2)にしようとする罠が多いので最初からO(n^2)解法
# cut(a,b)<=cut(a,b+1)<=cut(a+1,b+1)より、1つ短い区間のcut位置の間だけ攻めれば良い(または同区間長でcut位置の尺取り法が可能)
# O(n**3)解法
n,*w=map(int,open(0).read().split());R=range;d=[n*[0]for _ in[0]*n]
for i in R(1,n):
 for j in R(n-i):t=i+j;d[j][t]=min(d[j][k]+d[k+1][t]for k in R(j,t))+sum(w[j:t+1])
print(d[0][-1])
# O(n**3)解法(2) 行番号 = 区間長
n,*w=map(int,open(0).read().split());R=range;d=[n*[0]]
for i in R(1,n):d+=[min(d[k][j]+d[i-k-1][j+k+1]for k in R(i))+sum(w[j:j+i+1])for j in R(n-i)],
print(*d[-1])

n,*w=map(int,open(0).read().split());R=range;d=[n*[0]]
for i in R(n):d+=[min(d[k][j]+d[i-k][j+k+1]for k in R(i+1))+sum(w[j:j+i+2])for j in R(~i+n)],
print(*d[-2])
# O(n**2)解法 (Knuth の最適化)
n,*w=map(int,open(0).read().split());R=range;s=[0]*(n+1)
d=[n*[0]for _ in[0]*n];c=[n*[0]for _ in[0]*n]
for i in R(n):s[i+1]=s[i]+w[i];c[i][i]=i
for l in R(1,n):
 for i in R(n-l):
  j=i+l;d[i][j]=9e9
  for k in R(c[i][j-1],c[i+1][j]+1):
   if(k<j)and(v:=d[i][k]+d[k+1][j]+s[j+1]-s[i])<d[i][j]:d[i][j]=v;c[i][j]=k
print(d[0][-1])

# 彩色数(chromatic number,O(n*n^n), graph gがグローバル定義済みなら省略可)
def C(v,g,M,k):
 for c in range(k):
  if all(c!=M[u]for u in g[v]):
   M[v]=c
   if v+2>len(g)or C(v+1,g,M,k):return 1
 M[v]=-1;return
def N(g,n=len(g),k=0):
 while(k:=k+1):
  if C(0,g,[-1]*n,k):break
 return k

# 最近共通祖先(Lowest Common Ancestor: LCA)
R=range;(N,),*L=[[*map(int,o.split())]for o in open(0)];i=j=1;M=[P:=[*R(N+1)]];S=[1]*-~N;D=S[:];r=S[:];G=[[] for _ in P];b=N.bit_length()-1;B=R(b,-1,-1)
for x,y in L[:N-1]:G[x]+=y,;G[y]+=x,
while i:
 i-=1;r[p:=S[i]]=j;j+=1
 for e in{*G[p]}-{P[p]}:S[i]=e;P[e]=p;i+=1;D[e]=D[p]+1
for d in R(b):M+=[M[d][M[d][i]]for i in R(N+1)],
def F(u,v):
 if D[u]>D[v]:u,v=v,u
 for d in B:1<<d<=D[v]-D[u]<(v:=M[d][v])
 if u-v:
  for d in B:M[d][u]!=M[d][v]!=(u:=M[d][u],v:=M[d][v])
  u=P[u]
 return u

# 各頂点の削除時に残る部分木の頂点数リスト (全方位木DP = Rerooting の例のつもりで書いたが、違うものになった)
(n,),*e=[map(int,o.split())for o in open(0)];g,l=[[[]for _ in[0]*-~n]for _ in'01'];i=1
for x,y in e:g[x]+=y,;g[y]+=x,
def f(u,v):
 for w in{*g[v]}-{u}:f(v,w);l[v]+=sum(l[w])+1,
f(0,1)
while i<n:i+=1;l[i]+=n+~sum(l[i]),
for v in l:print(*sorted(v)[::-1])
