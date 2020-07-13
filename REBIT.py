def modi(a, m = 998244353) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) :  
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
    return x

mod = 998244353
d = {'|':1, '^':1, '&':1, '(':0, ')':0}
for i in range(int(input())):
    s = input()
    r = [1 for j in range(4)]
    c = 4
    a = []
    for j in s:
        if(j=='('):
            a.append(j)
        elif(j=='#'):
            continue
        elif(j==')'):
            while(len(a)!=0 and a[-1]!='('):
                if(a[-1]=='&'):
                    p = r[3]*2+r[1]
                    r[2] = p
                    r[3] = p
                    c*=4
                    r[0] = c-sum(r)+r[0]
                elif(a[-1]=='|'):
                    p = r[3]*2+r[0]
                    r[2] = p
                    r[3] = p
                    c*=4
                    r[1] = c-sum(r)+r[1]
                elif(a[-1]=='^'):
                    r = [c for k in range(4)]
                    c*=4
                a.pop()
            if(len(a)!=0):
                a.pop()
        else:
            while(len(a)!=0 and d[j]<d[a[-1]]):
                while(len(a)!=0 and a[-1]!='('):
                    if(a[-1]=='&'):
                        p = r[3]*2+r[1]
                        r[2] = p
                        r[3] = p
                        c*=4
                        r[0] = c-sum(r)+r[0]
                    elif(a[-1]=='|'):
                        p = r[3]*2+r[0]
                        r[2] = p
                        r[3] = p
                        c*=4
                        r[1] = c-sum(r)+r[1]
                    elif(a[-1]=='^'):
                        r = [c for k in range(4)]
                        c*=4
                    a.pop()
            a.append(j)
        while(len(a)!=0 and a[-1]!='('):
            if(a[-1]=='&'):
                p = r[3]*2+r[1]
                r[2] = p
                r[3] = p
                c*=4
                r[0] = c-sum(r)+r[0]
            elif(a[-1]=='|'):
                p = r[3]*2+r[0]
                r[2] = p
                r[3] = p
                c*=4
                r[1] = c-sum(r)+r[1]
            elif(a[-1]=='^'):
                r = [c for k in range(4)]
                c*=4
            a.pop()
    p = modi(c)
    print(*[(p*j)%mod for j in r])
    
