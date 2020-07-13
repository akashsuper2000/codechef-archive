def fun(a,b,c,d,e,f):
    if(a>=d and b>=e and c>=f) and (a>d or b>e or c>f):
        return 1
    elif(a<=d and b<=e and c<=f) and (a<d or b<e or c<f):
        return 1
    return 0

for i in range(int(input())):
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    c = [int(j) for j in input().split()]
    if(fun(a[0],a[1],a[2],b[0],b[1],b[2]) and fun(a[0],a[1],a[2],c[0],c[1],c[2]) and fun(c[0],c[1],c[2],b[0],b[1],b[2])):
        print('yes')
    else:
        print('no')
