n,q = [int(i) for i in input().split()]
a = [0]+[int(i) for i in input().split()]
for i in range(1,n+1):
    a[i]=a[i]^a[i-1]
n+=1
for i in range(q):
    print(a[(int(input()))%n])
