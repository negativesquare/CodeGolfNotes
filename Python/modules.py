a=f=l=m=n=y=... # dummy to avoid undefined-name warnings
################

import sys;sys.setrecursionlimit(7**6) # enable deep recursion; change 7**6 to required limit

# Memoization: caching function results to avoid recomputation
from functools import cache
@cache # = (from functools import lru_cache) @lru_cache(maxsize=None)
def f(n):pass
# @lru_cache(maxsize=10**5) = @lru_cache(10**5) : stores 10**5 input-output pairs

from math import*;tau # import all; 2*pi
x=hypot(5,-12) # math.hypot, x=13, any dim
atan2 # [-pi,pi] math.atan2(y,x)
r=isqrt(n) # floor of sqrt(n) as an integer
r=int(n**.5) # it probably better
d=gcd(x,y);(y//d,x//d) # Unique rational representation
comb(n,r)

from random import*;randint(1,n)

import re

from sympy import* # <- @AtCoder, CPython is faster than PyPy
isprime(n)
[*primerange(n+1)] # [*generator]: get all prime numbers in range
divisors(n) # ordered list

# numpy(https://chokkan.github.io/python/17numpy2.html, https://atcoder.jp/contests/dp/submissions/30484080)
# CPython is maybe faster
# summed-area table (2-dim prefix sum)
from numpy import*;M=zeros((n+1,n+1),int) # zeros((n+1,n+1),dtype=int32)
for _ in[0]*m:a,b=map(int,input().split());M[a,b]+=1
M=M.cumsum(0).cumsum(1)
# ABC106-D (Count fully contained intervals)
from numpy import *;(n,m,_),*I=[map(int,o.split())for o in open(0)];M=zeros((n+1,n+1),int)
for l,r in I[:m]:M[n-l,r]+=1
M=M.cumsum(0).cumsum(1)
for p,q in I[m:]:print(M[n-p,q])
# 1-dim cumsum
print(*cumsum(d))

# https://atcoder.jp/contests/s8pc-3/tasks/s8pc_3_c
from numpy import*;n,k,*a=map(int,open(0).read().split());d=zeros((n+1,256),int);d[0,0]=1;M=10**9+7;A=arange
for v in a:d[1:]+=d[:-1,A(256)^v]*A(1,n+1)[:,None]%M
print(int(d[:,k].sum()%M))

################

# collections (Counter, defaultdict, deque)
# https://docs.python.org/ja/3/library/collections.html#deque-objects
# https://qiita.com/apollo_program/items/165fb01b52702274936c
from collections import*

# Counter can count any iterable
c=Counter('gallahad') # Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
c=Counter(['red','blue','red','green','blue','blue']) # Counter({'blue': 3, 'red': 2, 'green': 1})
print(c['any other']) # 0 : not error
c.total() # sum of values
# c+d : {x:c[x]+d[x]},    c-d : subtract (keeping only positive counts)
# c&d : {x:min(c[x],d[x])},    c|d : {x:max(c[x],d[x])}
# c==d all(c[x]==d[x]for x in c+d),    c<=d all(c[x]<=d[x]for x in c+d)

defaultdict(int);'default = 0'; defaultdict(list);'default = []'; defaultdict(set);'default = set()'
defaultdict(lambda:'default_you_like')

# deque
q=deque(l) # l:iterable
# appendleft -> (deque) <- append : O(1)
# popleft <- (deque) -> pop : O(1)
# usable: (x in q), len(q)
# Other methods include: count(x), extend(l), extendleft(l), index(x), insert(i,x), rotate(k)
[q.appendleft,q.append][f]((x,y,a+f)) # usecase: 0-1 BFS


# itertools
# https://qiita.com/anmint/items/37ca0ded5e1d360b51f3
# https://docs.python.org/ja/3/library/itertools.html
from itertools import*
[*accumulate(l)] # slow -> [sum(l[:i+1])for i in range(l)]
  # (if l is list of string, ''.join(l[:i+1]) or sum(l[:i+1],''))
[*permutations(range(n))] # Full permutation search
[*combinations(range(n),r)] # Full combination search

# more-itertools
# https://qiita.com/SaitoTsutomu/items/ddb5076ef62745f03b56
from more_itertools import*
set_partitions(l) # [1,2,3] -> [[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]], [[2], [1, 3]], [[1], [2], [3]]
partitions(l) # with order: [[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]], [[1], [2], [3]]

# example that considers all combinations (ABC 440-E)
from heapq import*;P=heappush;n,k,x,*a=map(int,open(0).read().split());a.sort();q=[(-a[-1]*k,n-1,0,k)]
while x:s,h,p,c=heappop(q);print(-s);p>0!=P(q,(s+a[h+1]-a[h],h,p-1,c+1));h>0!=P(q,(s+a[h]-a[h-1],h-1,c-1,1));x-=1
# sorted list can be used as a heap
q=sorted((v,i)for i,v in enumerate(l)) # shorter than heapify(q:=[(v,i)for i,v in enumerate(l)])

# binary search
from bisect import bisect as B # upper_bound (x=bisect(l,v))
from bisect import bisect_left as B # lower_bound
from bisect import insort # insort(l,v): sorted list l -> l with v inserted (still sorted)


# SortedSet (in sortedcontainers, exists SortedList, SortedDict)
from sortedcontainers import*
s=SortedSet('abracadabra') # <- s = SortedSet(['a', 'b', 'c', 'd', 'r']), s.bisect_left('c') = 2


from functools import cmp_to_key;a.sort(key=cmp_to_key(f)) # f(x,y):return <0 if x<y, 0 if x==y, >0 if x>y
# example
f=lambda x,y:x[0]*y[1]-y[0]*x[1]or x[2]-y[2] # x=[a,b,c],y=[u,v,w] -> a/b ? u/v, if same, c ? w
a=[[1,2,0],[-3,4,1],[1,3,2],[3,6,3]];a.sort(key=cmp_to_key(f)) # [[-3, 4, 1], [1, 3, 2], [1, 2, 0], [3, 6, 3]]


# atcoder.segtree : モノイドの区間積を得るライブラリ
# from atcoder.segtree import*

# T=SegTree(op,e,list or length) : 初期化
# -> op : モノイドの積演算, e : モノイドの単位元, list : 初期値, length : 初期値を [e]*length とする
# usecase(M as Inf): MinT=SegTree(min,M,l), MaxT=SegTree(max,-M,l), SumT=SegTree(lambda x,y:x+y,0,l)
# (SumTは int.__add__ も可, sumは遅い？)

# T.set(p,x) : list[p]=x
# T.get(p) : getting list[p]
# T.prod(l,r) : getting op(list[l],...,list[r-1])


# atcoder.lazysegtree : segtreeに、区間の要素に一括で特定の処理(※)を行う機能を追加したライブラリ
# ※: モノイド自己準同型からなるモノイドの元 すなわちモノイドS,集合Fに対し FF=F∋f→(FF(f):S∋x→f(x)∈S) で得られる FF(f)
# from atcoder.lazysegtree import*

# LazySegTree(op,e,mapping,composition,id,list or length)
# -> op, e, list, length : 同上, mapping : 入力に応じて処理(上記の自己準同型)を返す写像(※), composition : 処理間の積写像, id : 恒等処理
# ※: 正確には FF: F→(S_in→S_out) と同一視できる写像 (F×S_in)→S_out
# usecase(M as Inf, Sum-type nodes hold [segment_len,sum]):
# MinAddT=LazySegTree(min,M,lambda f,x:f+x,lambda f,g:f+g,0,list)
# MaxAddT=LazySegTree(max,-M,lambda f,x:f+x,lambda f,g:f+g,0,list)
# SumAddT=LazySegTree(lambda x,y:[x[0]+y[0],x[1]+y[1]],[0,0],lambda f,x:[x[0],x[1]+f*x[0]],lambda f,g:f+g,0,[[1,v]for v in list])
# MinUpdT=LazySegTree(min,M,lambda f,x:f if f<M else x,lambda f,g:f if f<M else g,M,list)
# MaxUpdT=LazySegTree(max,-M,lambda f,x:f if f<M else x,lambda f,g:f if f<M else g,M,list)
# MaxUpdT2=LazySegTree(max,-M,lambda f,x:f if f>-M else x,lambda f,g:f if f>-M else g,-M,list) : 定数を-Mしか使わない版
# SumUpdT=LazySegTree(lambda x,y:[x[0]+y[0],x[1]+y[1]],[0,0],lambda f,x:[x[0],f*x[0]]if f<M else x,lambda f,g:f if f<M else g,M,[[1,v]for v in list])
# (lambda式について、 f if f<M else g -> [f,g][f<M] などとした方が短いが、計算時間が増える)

# T.set(p,x), T.get(p), T.prod(l,r) : 同上
# T.apply(l,r,f) : for i in range(l,r):list[i]=f(list[i]) (上のusecaseなら(f<Mのとき)各要素にfを加算or上書き)


# Convolution
# Σ(a[i]*x**i)*Σ(b[j]*x**j) ≡ Σ(c[k]*x**k) mod M
# from atcoder.convolution import* -> c=convolution(M,a,b)
# from acl_cpp.convolution import* -> c=convolution(a,b,M) <- faster


# DSU = Disjoint Set Union = Union-Find : 実のところ、これを使わない方が短い場合が多い
# from atcoder.dsu import*;D=DSU(n) # n = size of the universal set (0-indexed)
# D.merge(a,b), D.same(a,b), D.size(a), D.groups() : self‑explanatory methods
