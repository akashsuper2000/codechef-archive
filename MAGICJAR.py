for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    print(sum(a)-n+1)
