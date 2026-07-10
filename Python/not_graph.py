# The following prime-related code has "sympy" equivalents; see modules.py
# primes by eratosthenes
def e(n):
 t=[0,0]+[1]*n
 for i in range(2,int(n**.5)+1):
  if t[i]:t[i*i:n+1:i]=[0]*len(t[i*i:n+1:i])
 return[i for i in range(n+1)if t[i]]
# prime factorization
n=8**8;b=[*range(n+1)]
for i in range(2,8**4):
 if b[i]==i:b[i:n:i]=[i]*len(b[i:n:i])
d={}
while~-v:d[t:=b[v]]=d.get(t,0)+1;v//=t
# prime number check(@AtCoder, CPython is probably faster)
import sympy;f=lambda n:sympy.isprime(n)
import sympy;f=lambda n:sympy.isprime(n);r=range;print(*sorted((i**j+k,str(i)+'**'+str(j)+'+'*(k>=0)+str(k))for i in r(3,10)for j in r(3,10)for k in r(-9,10)if(i**j+k>10**6)*f(i**j+k)))
# (1679609,'6**8-7'),(2097143,'8**7-9'),(4782961,'9**7-8'),(4782971,'9**7+2'),(4782977,'9**7+8'),(5764793,'7**8-8'),(5764799,'7**8-2'),(10077689,'6**9-7'),(16777213,'8**8-3'),(40353601,'7**9-6'),(40353611,'7**9+4')


# Longest Increasing Subsequence (LIS, v is used in somewhere else)
# ver 1
from bisect import*;n,*a=map(int,open(0).read().split());d=[]
for x in a:i=bisect(d,x-1);d+=[x]*(i==len(d));d[i]=x
print(len(d))
# ver 2
from bisect import*;n,*a=map(int,open(0).read().split());d=[9e9]*n
for x in a:d[bisect(d,x-1)]=x
print(n-d.count(9e9))
# ver 1 (with Levels)
from bisect import*;n,*a=map(int,open(0).read().split());v=[p:=0]*n;d=[]
for x in a:i=bisect(d,x-1);i-len(d)or(d:=d+[x]);d[i]=x;v[p]=i;p+=1
print(len(d))
# ver 2 (with Levels)
from bisect import*;n,*a=map(int,open(0).read().split());v=[];d=[9e9]*n
for x in a:v+=[i:=bisect(d,x-1)];d[i]=x
print(n-d.count(9e9))


# IntervalSet :half-open, [x,y)
from sortedcontainers import*;S=SortedSet()
G=lambda x:(i:=S.bisect((x,)))<len(S)and S[i][0]<=x<S[i][1]
def U(x,y):
 i=S.bisect((x,));i-=0<i and x<=S[i-1][1]
 while i<len(S)and(y,)>S[i]:u,v=S[i];x=min(x,u);y=max(y,v);S-={S[i]}
 S|={(x,y)}
def E(x,y):
 I=[];i=S.bisect((x,))
 while i<len(S)and(y,)>S[i]:u,v=S[i];I+=[(y,v)]*(y<v)+[(u,x)]*(u<x);S-={S[i]}
 S|={*I}


# ordered stack
l=...
o=[-1<<30]
for v in l:
 while v<l[-1]:l.pop()
 l+=v,;"do something"


def _Young(sets,seed,n,p):
#  if p<0:return
#  if p<1:sets.append([n]);return
 if p<2:seed[0]=n;sets.append(seed[:]);return
 mv=seed[p];Mv=n//p
 for i in range(mv,Mv+1):
  seed[p-1]=i
  if p<3:seed[0]=n-i;sets.append(seed[:])
  else:_Young(sets,seed,n-i,p-1)
def Young(n,m):
#  if m<2:return[[n]]
 sets=[];seed=[0]*m
 for i in range(1,n//m+1):seed[m-1]=i;_Young(sets,seed,n-i,m-1)
 return sets
n,t,m,k=map(int,input().split());d=[1]+[0]*k;C=Young(m,n)
for _ in[0]*t:d=[max(sum(d[max(i-j,0)]for j in l)for l in C)/m for i in range(k+1)]
print(d[k])


# Digit DP (count numbers in 0..n that satisfy conditions)
f=...;g=... # state update/condition functions
d={(1,0):1} # in practice, use integer keys to avoid TLE
for c in map(int,input()):
 d,e={},d
 for(p,t),v in e.items():
  i=[9,c][p] # free->free:0..9, max->max:c, max->free:0..c-1
  while-~i:d[k]=d.get(k:=(p,f(i,t)),0)+v;p=0;i-=1
print(sum(v for(_,t),v in d.items()if g(t)))

