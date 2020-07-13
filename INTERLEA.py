import heapq as heap
n = int(input())
q = [0 for i in range(10)]
poi = [1 for i in range(n)]
ful = []
h = []
a = []
for i in range(n):
    s = input()
    a.append(s)
    ful.append(len(s))
full = sum(ful)
c = 0
for i in range(n):
    q[a[i][0]]+=1
s = 0
m = 10
for i in range(10):
    for j in range(10):
        if(i==j):
            if(q[i]>1):
                m = 0
                s = i
                q[s]-=2
                print(i,i,end = ' ')
                c+=2
                break
        elif(q[i]>0 and q[j]>0):
            if(abs(i-j)<m):
                s = i
                m = abs(i-j)
    if(c>0):
        break
if(c==0):
    print(s,end = ' ')
    q[s]-=1
    c+=1
        
        
while(c<full-1):
    m = 10
    for i in range(10):
        if(q[i]>0 and abs(s-i)<m):
            m = abs(s-i)
            s = i
            
