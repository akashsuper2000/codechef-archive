n = int(input())
for i in range(int(n**2)):
    a = input()
for i in range(n):
    print(*[j+1 for j in range(n-1,-1,-1)])
