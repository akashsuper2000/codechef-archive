def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res

mod = int(1e9)+7

for i in range(int(input())):
    n,a = [int(j) for j in input().split()]
    c = a%mod
    p = (a**2)%mod
    for j in range(n-1):
        q = power(p,(j+2)**2-(j+1)**2,mod)
        c = (c+q)%mod
        p = (q*p)%mod
    print(c)
        
