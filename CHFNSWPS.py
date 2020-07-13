for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    a.sort()
    b.sort()
    d = {}
    for j in a:
        if(j in d):
            d[j] += 1
        else:
            d[j] = 1
    for j in b:
        if(j in d):
            d[j] -= 1
            if(d[j] == 0):
                del d[j]
        else:
            d[j] = -1
    f = 1
    arr = []
    for j in d:
        if(d[j]%2 != 0):
            f = 0
            break
        arr.extend([j]*abs(d[j]//2))
    arr.sort()
    if(f == 1 and len(arr)%2 == 0):
        q = arr[0]*2
        s = 0
        for j in range(len(arr)//2):
            if(arr[j]<q):
                s+=arr[j]
            else:
                s+=q
        print(s)
    else:
        print(-1)