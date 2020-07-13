def modi(a, m) :
    if(a==0):
        return 1
    return power(a, m - 2, m) 
      
# To compute x^y under modulo m 
def power(x, y, m) : 
      
    if (y == 0) : 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m) 

mod = int(1e9)+7
mods = [0]
ans = 1
for i in range(int(1e5)+1):
    ans = (ans*(i+1))%mod
    mods.append(ans)

for i in range(int(input())):
    p = int(input())
    a1 = input()
    a2 = input()
    n,m = a1.count('1'),a2.count('1')
    ans = 0
    if(n<m):
        n,m = m,n
    s,t = n-m,n+m
    if(n+m>p):
        t = p-(n+m-p)
    for j in range(s,t+1,2):
        ans = (ans+(mods[p]*modi(mods[p-j],mod)*modi(mods[j],mod))%mod)%mod
    print(int(ans))
