n = int(input())
a = [int(j) for j in input().split()]
m1,m2 = 0,0
for i in a:
    if(i>m1):
        m2 = m1
        m1 = i
print(m2)
