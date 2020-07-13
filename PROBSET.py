for i in range(int(input())):
    n,m = input().split()
    n,m = int(n),int(m)
    f = 1
    for j in range(n):
        a=input().split()
        if a[0]=='correct' and '0' in a[1]:
            f=2
        elif f==1:
            if a[0]=='wrong' and '0' not in a[1]:
                f=3
    if f==1:
        print('FINE')
    elif f==2:
        print('INVALID')
    else:
        print('WEAK')
