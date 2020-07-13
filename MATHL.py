modulo = pow(10,9)+7
l = pow(10,6)
a = [0]*l
a[0]=1
for j in range(1,l):
    a[j]=((j+1)*a[j-1])%modulo
for j in range(1,l):
    a[j]=(a[j]*a[j-1])%modulo

for i in range(int(input())):
    n = int(input())
    print(a[n-1])
