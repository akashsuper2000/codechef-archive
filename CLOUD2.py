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

for i in range(int(input())):
    n,p,q = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    
