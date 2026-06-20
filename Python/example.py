# -*- coding: utf-8 -*-
n=int(input())
a,b=map(int,input().split())
*l,=map(int,input().split()) # l=[*map(int,input().split())]
[int(input())for _ in[0]*n]
lines=[*open(0)]
n,*s=map(int,open(0)) # 1 row : 1 number
*l,=map(int,open(0).read().split()) # same as l=[*map(int,open(0).read().split())]
k,*l=map(int,open(0).read().split())
*l,=map(int,[*open(0)][1].split())
T,l,x,y,Q,*E=map(int,open(0).read().split());a=E[:T];b=E[T:] # e.g. T\nl x y\nQ\nE1\nE2...
# single-use:map(int,o.split()), reused:[*map(int,o.split())]
a=[[*map(int,o.split())]for o in open(0)] # a=[[*map(int, input().split())]for _ in[0]*n]
_,*a=[map(int,o.split())for o in open(0)]
(n,m),*I=[map(int,o.split())for o in open(0)]
(n,m),*I,x=[[*map(int,o.split())]for o in open(0)]
(r,c,s,d),(_,M,L),*I=[[*map(int,s.translate(str.maketrans('UDRL','0123')).split())]for s in open(0)] # replace 3 pairs or more
z=1j**'RULD'.find(c);i=x+int(z.real);j=y+int(z.imag) # find the next point to reach
print(input().translate({78:83,83:78,69:87,87:69})) # = print(input().translate(str.maketrans('NSEW','SNWE')))
r=str.replace # for 3+ replacements including non‑1→1 cases (else: 1–2 replacements → replace, 3+ all 1→1 → maketrans)
# r=str.replace;(r,c,s,d),(_,M,L),*I=[[*map(int,s.r(*'U0').r(*'D1').r(*'R2').r(*'L3').split())]for s in open(0)] # bad example
for o in open(0):a,*b=map(int,o.split());pass
for o in open(0):a,b,c=[*map(int,o.split())]+[0];pass
for o in[*open(0)][2::2]:a,*b=map(int,o.split());pass
for o in[*open(0)][2::2]:a,b,c=[*map(int,o.split())]+[0];pass
for l in[*open(0)][1:]:a,b,c=map(int,l.split());pass
for i,n in enumerate(map(int,input().split())):pass
for i,n in enumerate(sorted(map(int,input().split()))):pass
next(O:=open(0)) # continue to next row (this means: I=iter(open(0));next(I) )
for a,b in zip(O,O):pass
n=int(next(O:=open(0))) # when first row is needed 
for a,b,c,d,w,x,y,z in zip(*[O:=map(int,open(0).read().split())]*8):pass # or next(O:=map(int,open(0).read().split()))\n ... zip(*[O]*8):
(n,m),*E=[map(int,t.split())for t in open(0)];(k,T),D,q,*L=E[m:] # Extract additional parameters; earlier data E[:m] will be used later
_,s=open(c:=0) # initialize as 0, read second (and last) line
a,b=map(int,open(0))
s=input()
f=lambda:map(int,input().split());t,=f()
l=[];l+=int(input()),
a,b,c,x=[1+int(input())for _ in[0]*4]
for _ in[0]*n:pass
for a,b in l:pass # when l's element has two elements
digits=[*map(int,input())]
digits=[*map(int,str(n))]
digits=[int(d)for d in str(n)]
digits_map=[[*map(int,input())]for _ in l]
letters=[*input()]
l=[[*s]for s in[*open(0)][1:]]
print("{} {}".format(a+b+c,s))
print(a+b+c,s) # space-separated
print(a+b+c,s,sep=", ")
print(a+b+c,end="")
print(a+b+c,end=" ")
for s in l:print(s,end='') # same as print(''.join(l)) (except final '\n')
*_,=map(print,l) # same as for v in l:print(v)
print(+x) # x:(can) bool -> print number
print(*list)
print(([list]+[0])[0])
for c in s:f(c)and print(end=c) # same as print(''.join(c for c in s if f(c)))
print([f'{i:0{n}b}'for i in l]) # n-bit zero-padded (for all in l)
print(f'{x:.9f}') # Fixed decimal formatting applied to x
def L():return[*map(int,input().split())]

for i in[0]*input():...
while i:...;i-=1 # i:initial->1
while-~i:...;i-=1 # i:initial->0
d=~-2**n # 2**n-1
d=a+b>>1 #(a+b)//2
x=x>=10**k or x
m=max(b.bit_count(),m)
len([i for i in a for j in b if i+j==n])
sum(i for i in a for j in b if i+j==n)
l=[*zip(*l)] # transpose l (but [(),()])
l=[[*r]for r in zip(*l)] # transpose l as [[],[]]
for x,y in l:m[-x]|={n-y};m[-y]|={n-x}
for z in L:e,x,y,t,*_=*z,0,T,0
if(n:=len(a))>2:pass
(print('A1'),print('A2'))if b else(print('C1'),print('C2'))
print(max((x-u)**2+(y-v)**2 for x,y in a for u,v in a)**.5)
# sum(i*(a<=sum(map(int,str(i)))<=b)for 0<i<=n) # special ver (Python (Cython 0.29.34))
sum(n*(a<=sum(map(int,str(n)))<=b)for n in range(n+1))
sum(i*(((s:=sum(map(int,str(i))))-a)*(s-b)<1)for i in range(n+1))

*b,=a=[0]*n # independent lists same as a=[0]*n;b=a[:]
n,*c=d=[0]*5**9 # not sharing memory 
l+=n, # add element
a=[0];a+=[a[-1]+x]
(a if c<1 else b)[i]=x
[b*[0]for _ in[0]*a]
*l,=eval('[],'*n) # l=[[],[],...], len(l)=n
l+=l[0], # treated as a tuple, then appended to the list.
range(n-1,-1,-1) # reverse range(n)
range(1,n-~n) # 1,2,...,2*n
m=int(1e9+7)
ord('a') # 97
chr(97)
for c in range(26):c=chr(c+97);... # from 'a' to 'z'
# ord('#')==35, ord('.')==46
b=f'{i:b}' # decimal to binary (= bin(int(s))[2:])
b=f'{i:0{n}b}' # n-digits
i=int(b,2) # binary to decimal
f*=f<(x:=s.find(c,x+1)) # s="abcdefabc",x=1 -> x:=6 [super-speed-searcher@Cpython! O(n)]
mr=[*zip(*s[::-1])] # clockwise rotation, list of tuples
ml=[*zip(*m)][::-1] # counterclockwise rotation, list of tuples
while chr(i)in s:i+=1
l[1:]=sorted(l[1:])
R=range # add if 3~ ranges

# When ";X=(something)" is efficient?:
# Let the length be n, and the number of occurrences be t,It is enough that 3+n+t<n*t <-> t>(n+3)/(n-1)
# So n=2 -> min(t)=6, n=3 -> min(t)=4, n=4,5 -> min(t)=3, n>=6 -> min(t)=2

s=set()
{*s[i:]}&{*s[:i]} # and of set of string
{*s}|{*s} # or of set of string
s|={x} # add x in set
s|={(*l,)} # set of list cannot exist! change to tuple!
sorted({*l[:-i]}) # output of sorted is LIST
s.discard(x) # if d in s:s.remove(x)
t=s.pop() # get (and remove) one element

# dict example
d={}
for a in input().split():d[a]=d.get(a,0)+1
sum(d.values())
l=sum(v>2 for v in d.values());print("YNeos"[(l>1)+l*(2 in d.values())<1::2])
print(max(*[k for k,v in d.items()if v<2],-1))
d.pop(a,0) # if d in s:del d[a]

# the easiest queue
q=[0]
for i in q:
 # something
 q+=n, # q+=(n,) -> q=[...,[n]]

# integral image / summed-area table (2-dim prefix sum)
for i in range(n):
 for j in range(n):
  if i<n:M[i+1][j]+=M[i][j]
  if j:M[i][j]+=M[i][j-1] # m[i][j]+=m[i][j-1]*(j>0)
# can use numpy -> read modules

# eval can...
# "+, -, *, /, **, //, %", "<, >, <=, >=, ==, !=", "and, or, not", "&, |, ^, <<, >>"
# "[1,2]", "{1,2}", "1,2", "{'a':100, 'b':200}"
print(eval(input().replace(' ','*3+'))//2)
print('YNeos'[eval(input().replace(' ','*500<'))::2])
print(int(eval(input().replace(*' /'))+.5))
*e,=eval('[],'*7**6)

# Full permutation search (list(range(3)) -> [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]])
# can input list or tuple
p=lambda l,c=[]:sum([p(l[:i]+l[i+1:],c+[l[i]])for i in range(len(l))],[])if l else[c]
# cf. from itertools import*

d=lambda a,b,m:a*pow(b,m-2,m)%m # a/b mod m
class CombMod:
 def __init__(s,n,m):s.m=m;s.f=[t:=1]+[t:=t*-~i%m for i in range(n)]
 def c(s,a,b):return 0 if(a<b)+(b<0)else s.f[a]*pow(s.f[b]*s.f[a-b]%s.m,s.m-2,s.m)%s.m

# Combination (istead of "import math;math.comb", out of range -> 0)
C=lambda n,r:0<=r<=n and(r<1 or C(n-1,r-1)*n//r)
# or
F=[1]+[v:=v*i%M for i in range(1,4**9)];C=lambda n,r:0<=r<=n and F[n]*pow(F[r]*F[n-r],-1,M)%M

# Enumerate all subsets of bitmask n in decreasing order
while t:"do something";t=t-1&n

# Enumerate all bit patterns with bit_length=n and bit_count=k
x=2**k-1
while x<1<<n:"do something";i=x&-x;j=x+i;x=(x^j)//i>>2|j

# 2-way of gcd
from math import gcd
g=lambda a,b:g(b,a%b)if b else abs(a)

# Coordinate Compression
c=lambda a:[{v:i for i,v in enumerate(sorted(set(a)),1)}[x]for x in a]
c={v:i for i,v in enumerate(sorted(set(a)),1)} # map original value v -> compressed index c[v]

r[b],r[a]=x,y=r[a],r[b];I[x],I[y]=b,a # I[box]=label, r[label]=box (d[content]=box):index, reverse, dynamic (ABC 395-D)

# Interval Scheduling
_,*I=[[*map(int,o.split())][::-1]for o in open(0)];I.sort();e=0;print(*[e:=r for r,l in I if e<=l])

# flatten
f=lambda L:sum((f(l)if list==type(l)else[l]for l in L),[])

# A string S with len(S)==2*N is a "valid parenthesis sequence" if:
# all(S[:2*i+1].count("(") >= i for i in range(N)) and (S.count("(") == S.count(")") == N)
f=lambda p,n,s:n<1>p and print(s)or n and f(p+1,n-1,s+"(")or p*n and f(p-1,n-1,s+")")
f(0,int(input()),"")
# other way to check if "valid parenthesis sequence": use stack

l=[i for i in range(1<<n)if i>>1&i<1] # n-bit strings without '11', len(l)=Fibonacci(n+2)
# DP using previous column with using above ('\n'in s, (x-1,y)makes(x,y) c.f. bits of L)
h,*s=open(0);w=int(h.split()[1]);s=''.join(s);M=10**9+7;L=1<<w+1;n=len(B:=[i for i in range(L)if i>>1&i<1]);D={b:i for i,b in enumerate(B)};d=[1]+[0]*~-n
