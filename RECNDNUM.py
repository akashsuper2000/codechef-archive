mod = int(1e9)+7

for i in range(int(input())):
   n,k = [int(j) for j in input().split()]
   c = ((k-1)*k)%mod
