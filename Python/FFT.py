# https://atcoder.jp/contests/atc001/tasks/fft_c
# ../AtCoder_C++/FFT.cpp

# 1. 2^d = n > max(deg(g)+deg(h)) なる n,d を暗算
# 2. z=1^(2^-d) (mod p) が作れるような p,z
#    (pは素数 かつ p>max(ans) または pは問題文中のmod)を計算
#    (ここまでコード外の前計算)
# 3. d*n行列(または過去ログ上書きによる2*n行列)に添字だけ走らせ、
#    再帰の一番底で、どのindexが何次の係数かを表す配列を作成
#    (ビット列を逆から読んだものと同じ？→ならより短縮可能)
# 4. 上記配列に基づき係数を配列に格納
# 5. DP風の操作により再帰ステップを遡る。ここで、
#    f_0(w)+z*f_1(w) のパターンと f_0(w)-z*f_1(w) のパターン両方を同時計算すること

# z getter
d,p=map(int,input().split())
if~-p%2**d:print("input error");exit()
for i in range(1,p):
 t=i
 for _ in[0]*~-d:t=t*t%p
 if p-t<2:print(i);exit()
# p getter(l=lower limit)
d,l=map(int,input().split());n=2**d;c=int(2*l**.5)
t=[0,0]+[1]*c
for i in range(2,int(c**.5)+1):
 if t[i]:t[i*i:c+1:i]=[0]*len(t[i*i:c+1:i])
P=[i for i in range(c+1)if t[i]]
k=l//n;f=1
while-~k*n<c*c*f:
 k+=1;a=k*n+1
 if all(a%p for p in P):
  f=0
  for p in P:
   if a%p<1:f=1;break
   if a<p*p:break
print([(a,k),-1][f]) # a:wanted p, k:(a-1)/(2^d)

# 例: d,p,z=20,998244353,646


# 再帰関数を使う方法
def sub(l,p,z,n):
 if n<4:return[sum(l)%p,(l[0]-l[1])%p]
 a=[0]*n;y=z*z%p;n//=2;b=sub(l[::2],p,y,n);c=sub(l[1::2],p,y,n);x=1
 for i,j,k in zip(range(n),b,c):a[i]=(j+x*k)%p;a[n+i]=(j-x*k)%p;x=x*z%p
 return a
def FFT(l,r=0): # r:bool(is_inverse)
 p=257;z=11;d=6 # (p-1)%(1<<d)==0, z^(1<<d)=1 (mod p)
 if r:z=pow(z,-1,p)
 n=1<<d;a=sub(l+[0]*(n-len(l)),p,z,n)
 if r:a=[(1-p)//n*v%p for v in a]
 return a

# DP風配列を使う方法
def FFT(l,r=0): # r:bool(is_inverse)
 p=257;z=11;d=6 # (p-1)%(1<<d)==0, z^(1<<d)=1 (mod p)
 z=[pow(z,1-2*r<<i,p)for i in range(d)]
 n=1<<d;a=[0]*n;b=a[:];y=0;s=1
 for i,v in enumerate(l):a[int(f'{i:0{d}b}'[::-1],2)]=v
 while s<n:
  s*=2;y-=1;a,b=b,a;i=0
  for i in range(0,n,s):
   x=1
   for j in range(s//2):
    u=i+j;v=u+s//2
    a[u]=(b[u]+x*b[v])%p
    a[v]=(b[u]-x*b[v])%p
    x=x*z[y]%p
 if r:a=[(1-p)//n*v%p for v in a]
 return a


# 使用例
(n,),*l=[map(int,o.split())for o in open(0)];a,b=zip(*l)
A=FFT([0]+[*a]);B=FFT([0]+[*b]);X=FFT([i*j for i,j in zip(A,B)],1)
print(*X[1:2*n+1],sep='\n')
