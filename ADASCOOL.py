for i in range(int(input())):
    a,b = [int(j) for j in input().split()]
    if(a%2==1 and b%2==1):
        print('NO')
    else:
        print('YES')
