for i in range(int(input())):
    s = input()
    r = input()
    if(len(s)==1):
        if(s[0]==r[0]):
            print(0)
        else:
            print(1)
    elif(s==r):
        print(0)
    else:
        g = 0
        f = 0
        n = []
        p = 0
        gp = 0
        for j in range(len(s)):
            if(s[j]==r[j]):
                f = 1
                p+=1
                gp+=1
            else:
                if(p!=0):
                    g+=1
                    n.append(p)
                    p = 0
                    f = 0
        if(p!=0):
            g+=1
            n.append(p)
        g+=1
        if(s[0]==r[0]):
            g-=1
            n.pop(0)
        if(s[-1]==r[-1]):
            g-=1
            n.pop(-1)
        c = len(s)-gp
        p = min(len(s),c*g)
        n.sort()
        for j in range(len(n)):
            g-=1
            c+=n[j]
            p = min(p,c*g)
        print(p)
