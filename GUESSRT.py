from fractions import Fraction as fr
l = 10**9+7
def modi(a, m) : 
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

for i in range(int(input())):
    n,k,m = [int(j) for j in input().split()]
    sum = fr(1)/fr(n)
    mult = fr(n-1)/fr(n)
    n+=k
    for j in range(m-1):
        if(j<m-2 and n>k):
            n-=k
        else:
            sum=fr(sum)+(fr(mult)*(fr(1)/fr(n)))
            mult=fr(mult)*(fr(n-1)/fr(n))
            n+=k
    print(round((sum.numerator*modi(sum.denominator,l))%l))
