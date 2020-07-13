for i in range(int(input())):
    d = {}
    p = set()
    n = int(input())
    for j in range(n):
        s = input()
        p = set()
        for k in s:
            if(k not in p):
                if(k in d):
                    d[k]+=1
                else:
                    d[k] = 1
                p.add(k)
    print(list(d.values()).count(n))
