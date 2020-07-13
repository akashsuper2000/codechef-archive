for i in range(int(input())):
    n = int(input())
    n = str(n)
    f = 1
    for j in range(1,len(n)):
        if(n[j-1]>n[j]):
            n = n[:j-1]+n[j:]
            f = 0
            break
    if(f==1):
        n = n[:-1]
    print(int(n))
