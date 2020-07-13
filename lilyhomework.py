def fun(a):
    m = {}
    for i in range(len(a)):
        m[a[i]] = i
    b = sorted(a)
    ans = 0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            ans+=1
            ind = m[b[i]]
            m[a[i]] = m[b[i]]
            a[i],a[ind] = a[ind],a[i]
    return ans

n = int(input())
a = [int(i) for i in input().split()]
print(min(fun(list(a)),fun(list(reversed(a)))))
