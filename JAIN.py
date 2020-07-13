for i in range(int(input())):
    n = int(input())
    a = [0 for j in range(32)]
    for j in range(n):
        s = input()
        p = 0
        if('a' in s):
            p|=1
        if('e' in s):
            p|=2
        if('i' in s):
            p|=4
        if('o' in s):
            p|=8
        if('u' in s):
            p|=16
        a[p]+=1
    c = 0
    for j in range(32):
        for k in range(j+1,32):
            if(j|k==31):
                c+=a[j]*a[k]
    c+=int(a[31]*(a[31]-1)/2)
    print(c)
