import math as mt
def kf(n): 
    a = 0
    while n % 2 == 0: 
        a+=1
        n = n // 2
    for i in range(3, mt.ceil(mt.sqrt(n)), 2): 
        while n % i == 0: 
            n = n // i
            a+=1 
    if n > 2: 
        a+=1
    return a


for i in range(int(input())):
    x,k = [int(j) for j in input().split()]
    if(2**k<=x and kf(x)>=k):
        print(1)
    else:
        print(0)
        
