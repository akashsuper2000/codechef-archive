for i in range(int(input())):
    n = int(input())
    for j in range(n):
        a = [int(k) for k in input().split()]
    print(sum(a[1:len(a)//2+1]))
