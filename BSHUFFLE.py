n = int(input())
s = []
if n==3:
    s = [2,1,3]
elif n==1:
    s = [1]
else:
    for i in range(2,int(n/2)+1):
        s.append(i)
    s.append(1)
    for i in range(int(n/2)+2,n+1):
        s.append(i)
    s.append(int(n/2)+1)
print(' '.join(str(i) for i in s))
s=[]
s.append(n)
for i in range(1,n):
    s.append(i)
print(' '.join(str(i) for i in s))
