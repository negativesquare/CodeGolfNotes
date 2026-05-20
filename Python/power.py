# Code for values > 9**9. Modify the 4e8 part as needed.

# ? ** ??
print([f"{i}**{j} = {v}"for v,i,j in sorted([next((i**j,i,j)for j in range(9,100)if i**j>4e8)for i in range(2,10)])])
# print(sorted([next((v,i,j)for j in range(9,100)if(v:=i**j)>4e8)for i in range(2,10)]))

# ?? ** ?
m=4e8;print([f"{j}**{i} = {v}"for v,j,i in sorted([next((j**i,j,i)for j in range(9,100)if j**i>m)for i in range(5,10)if 99**i>m])])
# m=4e8;print(sorted([next((v,j,i)for j in range(9,100)if(v:=j**i)>m)for i in range(5,10)if 99**i>m]))


# Code for values from 10,000 up to 9**9.
for v,p in sorted([eval(s:=str(i//10)+"**"+str(i%10)),s]for i in range(100)):1e4>v or print(f"{p} = {v}")
# 5**6 = 15625
# 4**7 = 16384
# 7**5 = 16807
# 3**9 = 19683
# 8**5 = 32768
# 6**6 = 46656
# 9**5 = 59049
# 4**8 = 65536
# 5**7 = 78125
# 7**6 = 117649
# 4**9 = 262144
# 8**6 = 262144
# 6**7 = 279936
# 5**8 = 390625
# 9**6 = 531441
# 7**7 = 823543
# 6**8 = 1679616
# 5**9 = 1953125
# 8**7 = 2097152
# 9**7 = 4782969
# 7**8 = 5764801
# 6**9 = 10077696
# 8**8 = 16777216
# 7**9 = 40353607
# 9**8 = 43046721
# 8**9 = 134217728
# 9**9 = 387420489