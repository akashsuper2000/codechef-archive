l = 10**9+7
def modi(a, m=l) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x

def power(x, y, p=l) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res

for i in range(int(input())):
    n,k,m = [int(j) for j in input().split()]
    p = int(m/2)
    if(m%2==0):
        frac = 1+(power(n-1,p)*modi(power(n,p)))*((1-n-k)*modi(n+k))%l
    else:
        frac = (1-(power(n-1,p+1))*modi(power(n,p+1)))%l
    print(frac)
