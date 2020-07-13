from math import gcd
def sim(a,b):
    c = 0
    for i in range(len(a)):
        if(a[i]==b[i]):
            c = c+1
    return c
for i in range(int(input())):
    h1,w1 = [int(j) for j in input().split()]
    a = input()
    h2,w2 = [int(j) for j in input().split()]
    b = input()
    if(h1!=h2):
        lcm = int((h1*h2)/gcd(h1,h2))
        if(h1!=lcm):
            a = ''.join([j*int(lcm/h1) for j in a])
        if(h2!=lcm):
            b = ''.join([j*int(lcm/h2) for j in b])
    if(w1!=w2):
        lcm = int((w1*w2)/gcd(w1,w2))
        if(w1!=lcm):
            a = a*int(lcm/w1)
        if(w2!=lcm):
            b = b*int(lcm/w2)
    print(sim(a,b))
