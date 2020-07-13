for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    f = 1
    p = 5
    for j in range(n):
        if(a[j]==0):
            p+=1
        else:
            if(p<5):
                print('NO')
                break
            p = 0
    else:
        print('YES')
