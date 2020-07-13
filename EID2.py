for i in range(int(input())):
    a1, a2, a3, c1, c2, c3 = [int(j) for j in input().split()]
    f = 0
    if (a1>a2 and c1>c2) or (a1==a2 and c1==c2) or (a1<a2 and c1<c2):
        if (a2>a3 and c2>c3) or (a2==a3 and c2==c3) or (a2<a3 and c2<c3):
            if (a1>a3 and c1>c3) or (a1==a3 and c1==c3) or (a1<a3 and c1<c3):
                f = 1
    if(f==1):
        print('FAIR')
    else:
        print('NOT FAIR')
