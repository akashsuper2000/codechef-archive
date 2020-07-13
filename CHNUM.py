for i in range(int(input())):
    n = int(input())
    ar = [int(j) for j in input().split()]
    a,b,c = 0,0,0
    for j in range(n):
        if(ar[j]>0):
            a+=1
        elif(ar[j]<0):
            b+=1
        else:
            c+=1
    if(b==0):
        b = a
    if(a==0):
        a = b
    print(max(a,b)+c,min(a,b)+c)
