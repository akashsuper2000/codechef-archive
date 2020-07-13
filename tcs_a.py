a,b = [i for i in input().split()]
f = 1
if(len(a)<len(b)):
    f = 0
else:
    c = [1 for i in range(len(a))]
    for i in range(len(b)):
