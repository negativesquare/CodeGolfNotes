# グラフ生成コード一覧(1行目に頂点数と辺数, 2行目以降すべて辺情報が 1-indexed で入力される無向グラフ想定)

## 普段使い用の(十分高速な)バージョン (1-indexed で出題される場合が多いので、下記は n+1 頂点)
# normal graph
(n,m),*e=[map(int,o.split())for o in open(0)];g=[[]for _ in[0]*-~n]
for x,y in e:g[x]+=y,;g[y]+=x,

# graph with weight
(n,m),*e=[map(int,o.split())for o in open(0)];g=[[]for _ in[0]*-~n]
for x,y,w in e:g[x]+=[y,w],;g[y]+=[x,w],

# 十分な個数の頂点(例: m>10**5)を作っておく場合
g=[[]for _ in[0]*7**6]
for e in[*open(0)][1:]:x,y=map(int,e.split());g[x]+=y,;g[y]+=x,

## 以下は遅いか長いので非推奨
# dict based graph with weight (参照時に文字数がかかる)
f=lambda:map(int,input().split());n,m=f();g=[{}for _ in[0]*-~n]
for _ in[0]*m:x,y,w=f();g[x][y]=g[y][x]=w

# eval(低速)による短縮
(n,m),*e=[map(int,o.split())for o in open(0)];*g,=eval('[],'*-~n)
for x,y in e:g[x]+=y,;g[y]+=x,

# 辺追加時のtuple再構成により O(m**2)
(n,m),*e=[map(int,o.split())for o in open(0)];g=[()]*-~n
for x,y in e:g[x]+=y,;g[y]+=x,

# グラフ生成コード一覧 ここまで

'''以下、(主に)「競技プログラミングの鉄則」参照の内容'''

# DFS
import sys;sys.setrecursionlimit(7**6);(n,_),*e=[map(int,o.split())for o in open(0)];v=[0]*n;g=[[]for _ in v]
for x,y in e:g[x]+=y,;g[y]+=x,
def dfs(pos):
 v[pos]=1
 for nex in g[pos]:v[nex]or dfs(nex)
# 別解 def dfs(f):v[f]=1;[dfs(t)for t in g[f]if 1-v[t]]
# DFS ここまで

# BFS without weight (重み付きの場合はダイクストラ法を使う)
(n,m),*e=[map(int,o.split())for o in open(0)];*g,=eval('[],'*n);q=[0];dist=[0]+[-1]*~-n
for x,y in e:g[x]+=y,;g[y]+=x,
for pos in q:
 for to in g[pos]:
  if dist[to]<0:dist[to]=dist[pos]+1;q+=to,
print(dist)
# BFS without weight ここまで

# BFS-based shortest path counting (in unweighted graph, cf. ABC021-C)
# step-by-step
(n,),(a,b),_,*e=[map(int,o.split())for o in open(0)];g=[()]*-~n;v=[0]*-~n;v[a]=1;q={a}
for x,y in e:g[x]+=y,;g[y]+=x,
while q:
 p,q=q,set()
 for i in p:
  for j in g[i]:
   if(j in q)==(v[j]>0):v[j]+=v[i];q|={j}
print(v[b])
# with distance
(n,),(a,b),_,*e=[map(int,o.split())for o in open(0)];g=[()]*-~n;*d,=v=[0]*-~n;v[a]=1;q=[a]
for x,y in e:g[x]+=y,;g[y]+=x,
for i in q:
 for j in g[i]:f=d[j]<1;q+=[j]*f;v[j]+=v[i]*(f+(d[i]<d[j]));d[j]+=f*-~d[i]
print(v[b])
# BFS-based shortest path counting ここまで

# ダイクストラ法 (O(E+VlogV)、重み負の辺を含む場合はBellman-Ford法を使う、今回のような長さ1以下のlistはheapify不要)
from heapq import*;(n,m),*e=[map(int,o.split())for o in open(0)];*g,=eval('[],'*n);heapify(q:=[(0,0)]);dist=[0]+[9e9]*~-n
for x,y,w in e:g[x]+=[y,w],;g[y]+=[x,w],
while q:
 d,pos=heappop(q)
 if dist[pos]>=d:
  for nex,cost in g[pos]:
   if(comp:=dist[pos]+cost)<dist[nex]:dist[nex]=comp;heappush(q,(comp,nex))
print(dist)
# やや圧縮版
from heapq import*;(n,m),*e=[map(int,o.split())for o in open(0)];d=[9e9]*n;d[0]=0;q=[(0,0)];g=[[]for _ in d]
for x,y,w in e:g[x]+=[y,w],;g[y]+=[x,w],
while q:
 v,x=heappop(q)
 for y,w in g[x]:
  if v==d[x]<d[y]-w:d[y]=v+w;heappush(q,(v+w,y))
print(d)
# 別途圧縮版
from heapq import*;(n,m),*e=[map(int,t.split())for t in open(0)];d=[0]*-~n;g=[{}for _ in d];q=[(1,1)]
for x,y,w in e:g[x][y]=g[y][x]=w
while q:v,i=heappop(q);d[i]=d[i]or[d[j]or heappush(q,(v+g[i][j],j))for j in g[i]]and v
print([v-1 for v in d[1:]])
# ダイクストラ法 ここまで

# Bellman-Ford法 (O(VE))
f=lambda:map(int,input().split());(n,m),*e=[map(int,o.split())for o in open(0)];*g,=eval('[],'*n);dist=[0]+[9e9]*~-n
for x,y,w in e:g[x]+=[y,w],
for _ in[0]*n:
 updated=0
 for j in range(n):
  for nex,cost in g[j]:
   if(comp:=dist[j]+cost)<dist[nex]:dist[nex]=comp;updated=1
 if updated<1:print(dist);exit()
for j in range(n):
 for nex,cost in g[j]:
  if(comp:=dist[j]+cost)<dist[nex]:dist[nex]=-10**9
 if dist[j]>4e9:dist[j]=10**9
print(dist)
# Bellman-Ford法 ここまで

# warshall_floyd法 (全頂点探索、O(V**3))
(n,m),*e=[map(int,o.split())for o in open(0)];r=range(n);d=[[9e9*(i!=j)for j in r]for i in r]
for x,y,w in e:d[x][y]=w # "d[x][y]=min(d[x][y],w)","d[x][y]=d[y][x]=w"
for k in r:
 for i in r:
  for j in r:d[i][j]=min(d[i][j],d[i][k]+d[k][j])
# クエリ使用版
I=9**9;r=range(101);d=[[I*(i!=j)for j in r]for i in r]
for a in[*open(0)][1:]:q,a,b,c,*_=map(int,a.split()+[I]);q<1!=print(d[a][b]%I or-1);d=[[min(l[j],l[a]+c+d[b][j],l[b]+c+d[a][j])for j in r]for l in d]
# warshall_floyd法 ここまで

# Union-Find と 連結成分(connected component)
import sys;sys.setrecursionlimit(7**6)
class UnionFind:
 # The nominal initial value is N for both 0-based and 1-based cases.
 def __init__(self,N):self.par=[-1]*-~N;self.siz=[1]*-~N;self.comp=N
 # def root(self,x):
 #  if self.par[x]>-1:x=self.par[x]=self.root(self.par[x])
 #  return x
 def root(self,x):
  while self.par[x]>-1:
   if self.par[self.par[x]]>-1:self.par[x]=self.par[self.par[x]] #  2-step path compression
   x=self.par[x]
  return x
 # Unite two connected components
 def unite(self,u,v):
  if(ru:=self.root(u))-(rv:=self.root(v)):ru,rv=[[ru,rv],[rv,ru]][self.siz[ru]<self.siz[rv]];self.par[rv]=ru;self.siz[ru]+=self.siz[rv];self.comp-=1
 # Check if connected
 def same(self,u,v):return self.root(u)==self.root(v)

# 以下、圧縮版①
# from atcoder.dsu import* を使う手もあるが、実は下記(の②,③)を使った方が短い場合が多い
par=[*range(n)];siz=[1]*n;comp=n
def R(x):
 while par[x]-x:par[x]=x=par[par[x]] # At least in PyPy, same as par[x]=par[par[x]];x=par[x]
 return x
def U(u,v):
 if(u:=R(u))-(v:=R(v)):siz[u]<siz[v]and(u,v:=v,u);par[v]=u;siz[u]+=siz[v];comp-=1 # need 'global comp'?
# sameは事前準備せず適時同等操作で補う
# ②さらに圧縮 経路圧縮してれば(u<vなどの追加条件なしで)sizは不要 さらにnを連結成分数と再解釈
(n,m),*e=[map(int,o.split())for o in open(0)];P=[*range(-~n)]
def R(x):
 while P[x]-x:P[x]=x=P[P[x]]
 return x
for x,y in e:n-=R(x)!=R(y);P[R(y)]=R(x)
# ③別解(厳密・高速にやりたい場合は f=lambda x:0<P[x]and f(P[x])or x と a,b=sorted(map(f,l),key=lambda x:P[x]))
(n,_),*e=[map(int,o.split())for o in open(0)];P=[-1]*-~n;f=lambda x:x*(0>P[x])or f(P[x])
for l in e:
 a,b=sorted(map(f,l))
 if a-b:P[a]+=P[b];P[b]=a
# Union-Find と 連結成分 ここまで

# 最小全域木(MST)とクラスカル法
# : 貪欲法とUnion-Findによる最小コスト木の作成
#   クラスカル法：辺をコストの昇順でソート → Union-Findでサイクルを検出 → 最小コストの木を構築
import sys
sys.setrecursionlimit(7**6);f=lambda:map(int,input().split());n,m=f();g=[]
for _ in[0]*m:g+=[*f()],
class UnionFind:
 def __init__(self,N):self.par=[-1]*-~N;self.siz=[1]*-~N;self.comp=N
 def root(self,x):
  if self.par[x]>-1:x=self.par[x]=self.root(self.par[x])
  return x
 def unite(self,u,v):
  if(ru:=self.root(u))-(rv:=self.root(v)):ru,rv=[[ru,rv],[rv,ru]][self.siz[ru]<self.siz[rv]];self.par[rv]=ru;self.siz[ru]+=self.siz[rv];self.comp-=1
 def same(self,u,v):return self.root(u)==self.root(v)
def Kruskal(V,graph):
 # Sort by the third element in ascending order
 graph.sort(key=lambda e:e[2]);UF=UnionFind(V);total=0
 for u,v,w in graph:total+=w*(1-UF.same(u,v));UF.unite(u,v)
 return total
# 圧縮版(圧縮版Union-Findを使用)
(n,m),*g=[[*map(int,o.split())]for o in open(0)];P=[*range(-~n)];s=0
def R(x):
 while P[x]-x:P[x]=x=P[P[x]]
 return x
for x,y,c in sorted(g,key=lambda e:e[2]):s+=c*(t:=R(x)!=R(y));n-=t;P[R(y)]=R(x)
print(-(n>1)or s)
# 最小全域木(MST)とクラスカル法 ここまで

# 最大フロー問題 (Ford-Fulkerson algorithm)
class MaximumFlow:
 def __init__(self,n):
  self.used=[0]*-~n
  self.graph=[[]for _ in[0]*-~n]
  # self.init_graph=[[]for _ in[0]*-~n]
 def add_edge(self,start,end,capacity):
  self.graph[start].append([end,capacity,len(self.graph[end])])
  self.graph[end].append([start,0,len(self.graph[start])-1])
  # self.init_graph[start].append([end,capacity])
  # self.init_graph[end].append([start,0])
 def dfs(self,pos,goal,F):
  TO,CAP,REV=0,1,2 # destination, capacity, reverse index of edge
  if pos==goal:return F
  self.used[pos]=1
  for edge in self.graph[pos]:
   if(edge[CAP]<1)+self.used[edge[TO]]:continue
   if(flow:=self.dfs(edge[TO],goal,min(F,edge[CAP])))>0:
    edge[CAP]-=flow
    self.graph[edge[TO]][edge[REV]][CAP]+=flow
    return flow
  return 0
 def max_flow(self,start,end):
  total=0;F=1
  while F>0:
   self.used=[0]*len(self.used)
   total+=(F:=self.dfs(start,end,9e9))
  return total
# 最大フロー問題 (Ford-Fulkerson algorithm) ここまで

# 最大フロー問題(Edmonds-Karp algorithm)
class MaximumFlow:
 def __init__(self,n):
  self.used=[0]*-~n
  self.graph=[[]for _ in[0]*-~n]
  # self.init_graph=[[]for _ in[0]*-~n]
 def add_edge(self,start,end,capacity):
  self.graph[start].append([end,capacity,len(self.graph[end])])
  self.graph[end].append([start,0,len(self.graph[start])-1])
  # self.init_graph[start].append([end,capacity])
  # self.init_graph[end].append([start,0])
 def bfs(self,start,end):
  TO,CAP,REV=0,1,2 # [destination, capacity, reverse] index of edge
  V_PREV,V_NOW,E_NUM,REV_E_NUM,P_CAP=0,1,2,3,4 # index of prev
  if start==end:return 0
  Q=[start];q_ptr=0
  prev=[5*[-1]for _ in[0]*len(self.graph)]
  while(q_ptr<len(Q))*(prev[end][0]<0):
   pos=Q[q_ptr];q_ptr+=1
   for i,edge in enumerate(self.graph[pos]):
    t,c=edge[TO],edge[CAP]
    if prev[t][0]<0<c:
     prev[t]=[pos,t,i,edge[REV],c]
     Q.append(t)
  if prev[end][0]<0:return 0
  flow=prev[end][P_CAP];p=end;dir=[]
  while p!=start:
   flow=min(flow,prev[p][P_CAP])
   dir.append(p)
   p=prev[p][V_PREV]
  for i in dir:
   self.graph[prev[i][V_PREV]][prev[i][E_NUM]][CAP]-=flow
   self.graph[prev[i][V_NOW]][prev[i][REV_E_NUM]][CAP]+=flow
  return flow
 def max_flow(self,start,end):
  total=0;F=1
  while F>0:
   self.used=[0]*len(self.used)
   total+=(F:=self.bfs(start,end))
  return total
# 最大フロー問題(Edmonds-Karp algorithm) ここまで

# 二部マッチング問題(Bipartite Matching, DFSでOK)
# use above MaximumFlow
all_mem=int(input());is_endside=[0]*(all_mem+1);links=[]
graph=MaximumFlow(all_mem+2)
  # Input data of links and grouping data
for x,y in links:
 if is_endside[x]==is_endside[y]:continue
 if is_endside[y]:x,y=y,x
 graph.add_edge(x,y,1)
for i in range(len(is_endside)):
 if is_endside[i]:graph.add_edge(i,all_mem+2,1)
 else:graph.add_edge(all_mem+1,i,1)
print(graph.max_flow(all_mem+1,all_mem+2))
# Dinic法を利用する場合(全体, M[i]=j means (i,j)-pair)
(l,r),*e=[[*map(int,o.split())]for o in open(0)];S=l+r;T=S+1;N=S+2;g=[[] for _ in[0]*N];R=range;a=0;M=[-1]*r
for f,t in[(S,u)for u in R(l)]+[(l+v,T)for v in R(r)]+[(u,l+v)for u,v in e]:g[f].append([t,1,len(g[t])]);g[t].append([f,0,len(g[f])-1])
def D(v,f):
 if v==T:return f
 while(i:=I[v])<len(g[v]):
  t,c,j=g[v][i]
  if c>0<=L[v]<L[t]and(d:=D(t,min(f,c))):g[v][i][1]-=d;g[t][j][1]+=d;return d
  I[v]+=1
 return 0
while 1:
 L=[-1]*N;q=[S];L[S]=0
 for v in q:
  for t,c,_ in g[v]:
   if L[t]<0<c:L[t]=L[v]+1;q.append(t)
 if L[T]<0:break
 I=[0]*N;f=-1
 while f:a+=(f:=D(S,l))
for u in R(l):
 for t,c,_ in g[u]:M[t-l]=[M[t-l],u][l<=t<S>c==0]
print(a);print(*M)
# Hopcroft-Karp Algorithm: O(E*sqrt(V))
# 参考: https://tjkendev.github.io/procon-library/python/max_flow/hopcroft-karp.html
(N1,N2),*I=[map(int,o.split())for o in open(0)]
import sys;sys.setrecursionlimit(7**6);a=f=0;N0=2+N1+N2;G=[[]for _ in[0]*N0]
def E(u,v):G[u].append([v,1,len(G[v])]);G[v].append([u,0,len(G[u])-1])
for i in range(N1):E(0,2+i)
for i in range(N2):E(2+N1+i,1)
for i,j in I:E(2+i,2+N1+j)
def D(v,t):
 if v!=t:
  for e in G[v]:
   w,c,r=e
   if L[v]<L[w]>=c>0<D(w,t):e[1]=0;G[w][r][1]=1;return 1
 return v==t
while~-f:
 L=[-1]*N0;q=[0];L[0]=0
 for v in q:
  for w,c,_ in G[v]:
   if L[w]<0<c:L[w]=L[v]+1;q.append(w)
 f=L[1]<0
 while D(0,1):a+=1
M=[(i,w-2-N1)for i,l in enumerate(G[2:2+N1])for w,c,_ in l if c<1<w]
print(a,M)
# 二部マッチング問題 ここまで

# セグメント木
# max(RMQ)
class RMQ:
 def __init__(self,n):
  self.dat=[-9e9]*(2<<n.bit_length()) # think about 1-based
 def update(self,pos,x):
  self.dat[pos:=pos+len(self.dat)//2]=x # think about 0-based
  while pos>1:pos>>=1;self.dat[pos]=max(self.dat[pos*2],self.dat[pos*2+1])
 # max(data[l:r-1])
 def _query(self,l,r,a,b,u):
  # if(t:=(r<=a or b-2<l)+(l<=a)*(b-2<r)*-~u):return self.dat[t-1]
  if(r<=a)+(b<=l):return -9e9
  if(l<=a)*(b<=r):return self.dat[u]
  m=(a+b)//2;return max(self._query(l,r,a,m,2*u),self._query(l,r,m,b,2*u+1))
 def query(self,l,r):return self._query(l,r,0,len(self.dat)//2,1)
# not using class
d=[-9e9]*2*(L:=1<<n.bit_length())
def U(i,x):
 d[i:=i+L]=x
 while~-i:d[i:=i>>1]=max(d[i],d[i+1])
def Q(l,r,a=0,b=L,u=1): # max(d[l:r]) = Q(l,r+1,0,L,1)
 if(r>a<=b>l)<=(f:=l<=a<=b<=r):return d[f*u]
 return max(Q(l,r,a,m:=a+b>>1,2*u),Q(l,r,m,b,2*u+1))

# sum(RSQ)
class RSQ:
 def __init__(self,n):
  self.dat=[0]*(2<<n.bit_length()) # think about 1-based
 def update(self,pos,x):
  self.dat[pos:=pos+len(self.dat)//2]=x # think about 0-based
  while pos>1:pos>>=1;self.dat[pos]=self.dat[pos*2]+self.dat[pos*2+1]
 # sum(data[l:r-1])
 def _query(self,l,r,a,b,u):
  # if(t:=(r<=a or b-2<l)+(l<=a)*(b-2<r)*-~u):return self.dat[t-1]
  if(r<=a)+(b<=l):return 0
  if(l<=a)*(b<=r):return self.dat[u]
  m=(a+b)//2;return self._query(l,r,a,m,2*u)+self._query(l,r,m,b,2*u+1)
 def query(self,l,r):return self._query(l,r,0,len(self.dat)//2,1)

# other RSQ
 def query(self,l,r): # [l,r)
  N=len(self.dat)//2;l+=N;r+=N;res=0
  while l<r:
   if l&1:res+=self.dat[l];l+=1
   if r&1:r-=1;res+=self.dat[r]
   l>>=1;r>>=1
  return res

# not using class
# 未検証(Fenwickがあるため)
d=[0]*2*(L:=1<<n.bit_length())
def U(i,x):
 d[i:=i+L]+=x
 while~-i:d[i:=i>>1]=d[i]+d[i+1]
def Q(l,r,a,b,u): # sum(d[l:r-1]) = Q(l,r,0,L,1)
 if(r>a<=b>l)<=(f:=l<=a<=b<=r):return d[f*u]
 return Q(l,r,a,m:=a+b>>1,2*u)+Q(l,r,m,b,2*u+1)
# not recursive
def Q(l,r): # [l,r)
 l+=L;r+=L;a=0
 while l<r:
  if l&1:a+=d[l];l+=1
  if r&1:r-=1;a+=d[r]
  l>>=1;r>>=1
 return a

# RMQ with RUQ(Range Updated Query=Lazy Segment Tree)
# 未検証 使ってもどうせ遅くてTLEするし、長くなるすぎるので省略 → atcoder.lazysegtree (modules.py に記載)を使用のこと
import modules
# セグメント木 ここまで

# BIT(Binary Indexed Tree, Fenwick Tree)
# 0には最下位ビットがないので1-basedにする必要がある → このため随所でindexに1加算
class Fenwick:
 def __init__(self,size):self.tree=[0]*(size+1)
 # add val
 def update(self,idx,val):
  idx+=1
  while idx<len(self.tree):
   self.tree[idx]+=val
   idx+=idx&-idx
 def sum(self,idx):
  res=0;idx+=1
  while idx>0:
   res+=self.tree[idx]
   idx-=idx&-idx
  return res
 # [l, r] (index is changed in "sum", so well-defined)
 def range_sum(self,l,r):return self.sum(r)-self.sum(l-1)
# 圧縮版
T=[0]*-~n
def U(i,v):
 i+=1
 while-~n>i:T[i]+=v;i+=i&-i
def S(i):
 v=0;i+=1
 while i:v+=T[i];i-=i&-i
 return v
# 元から i が 1-based の場合(または関数呼び出しで i+1 する場合)
T=[0]*-~n
def U(i,v):
 while-~n>i:T[i]+=v;i+=i&-i
def S(i,v=0):
 while i:v+=T[i];i-=i&-i
 return v
# BIT(Binary Indexed Tree, Fenwick Tree) ここまで
