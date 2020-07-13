for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    c = 0
    f = a[0]
    if(n==1):
        print(a[0])
    elif(n==2):
        print(min(a))
    else:
        for j in range(1,max(a)+1):
            if(j in a):
                p = [0 for k in range(n)]
                if(a[0]==j):
                    p[0] = 1
                    p[1] = 1
                if(a[1]==j):
                    p[1] = 1
                for k in range(2,n):
                    if(a[k]==j):
                        p[k] = max(p[k-2]+1,p[k-1])
                    else:
                        p[k] = p[k-1]
                if(p[-1]>c):
                    c = p[-1]
                    f = j
        print(f)
                    
