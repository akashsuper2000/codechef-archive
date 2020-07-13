for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    p,q = a.count(2),a.count(0)
    print(int(max(0,p*(p-1)/2)+max(0,q*(q-1)/2)))
