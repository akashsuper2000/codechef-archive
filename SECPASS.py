for i in range(int(input())):
    n = int(input())
    s = input()
    l = 0
    c = 0
    st = ''
    m = ''
    for j in range(n):
        m+= s[j]
        f = s.count(m)
        if(f>=c and j+1>l):
            st = m
            c = f
            l = j+1
    print(st)
