def printDivisors(n) :
    m = 0
    i = n
    while i>0:
        if (n % i==0):
            if(i%2==1):
                m = i
                break
        i = i-1
    return m
s = 0
for i in range(1,100000):
    s+=get odd divisor(i)/i**2
print(s)
