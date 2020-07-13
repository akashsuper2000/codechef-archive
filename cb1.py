def sod(n):
    return sum([int(i) for i in str(n)])

for i in  range(int(input())):
    l,r = [int(j) for j in input().split()]
    c = 0
    for j in range(l,r+1):
        if(sod(j)%7 in {2,3,5}):
            c+= 1
    print(c)
    
