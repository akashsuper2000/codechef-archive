for i in range(int(input())):
    a = int(input(),2)
    b = int(input(),2)
    if(b==0):
        print(0)
    elif(a&b==0):
        print(1)
    else:
        if(a<b):
            a,b = b,a
        c = 0
        d = 0
        p = 0
        an = list(str(bin(a&b))[2:][::-1])
        x = list(str(bin(a^b))[2:][::-1])
        if(len(an)>len(x)):
            x.extend(['0' for j in range(len(an)-len(x))])
        else:
            an.extend(['0' for j in range(len(x)-len(an))])
        for j in range(len(an)):
            if(an[j]=='1'):
                p = 1
                c = max(c,d)
                d = 0
            elif(x[j]=='1' and p==1):
                d+=1
            else:
                p = 0
                c = max(c,d)
                d = 0
        c = max(c,d)+2
        print(c)
