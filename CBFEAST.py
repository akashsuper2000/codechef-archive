from sys import maxsize
def fun(a,c,k):
    size = len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i][1] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1

    for i in range(start,end+1):
        if(a[i][0]>c+k or a[i][0]<c-k):
            max_so_far-=a[i][1]
    return max(max_so_far,0)
        

q,k = [int(i) for i in input().split()]
a = []
ans = 0
for i in range(q):
    b = [int(j) for j in input().split()]
    if(b[0]==1):
        a.insert(0,[b[1]^ans,b[2]])
    elif(b[0]==2):
        a.append([b[1]^ans,b[2]])
    else:
        ans = fun(a,b[1]^ans,k)
        print(ans)
