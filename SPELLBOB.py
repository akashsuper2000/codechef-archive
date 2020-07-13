for i in range(int(input())):
    a = input()
    b = input()
    a1 = a[:1]
    a2 = a[1:2]
    a3 = a[2:]
    b1 = b[:1]
    b2 = b[1:2]
    b3 = b[2:]

    s = [a,b,a1+a2+b3,a1+b2+a3,a1+b2+b3,b1+a2+b3,b1+b2+a3,b1+a2+a3]
    m = [k for k in s if (k=='bob' or k=='obb' or k=='bbo')]
    if len(m)>0:
        print('yes')
    else:
        print('no')
    
