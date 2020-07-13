def w(a):
    if(len(a)==0):
        return 0
    elif(len(a)==1):
        return a[0]
    elif(len(a)==2):
        return (a[0]^a[1])-1
    else:
        return w(a[:2])+w(a[3:])           

for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    for j in range(n):
        print(w(a[:j]+a[j+1:]),end=' ')
