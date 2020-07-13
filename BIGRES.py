def rearrange(arr, n): 
    # Auxiliary array to hold modified array 
    temp = n*[None] 
  
    # Indexes of smallest and largest elements 
    # from remaining array. 
    small,large =0,n-1
  
    # To indicate whether we need to copy rmaining 
    # largest or remaining smallest at next position 
    flag = True
  
    # Store result in temp[] 
    for i in range(n): 
        if flag is True: 
            temp[i] = arr[large] 
            large -= 1
        else: 
            temp[i] = arr[small] 
            small += 1
  
        flag = bool(1-flag) 
  
    # Copy temp[] to arr[] 
    for i in range(n): 
        arr[i] = temp[i] 
    return arr 

for i in range(int(input())):
    n = int(input())
    s = 0
    ar = []
    d = []
    for j in range(n):
        a,b = [int(k) for k in input().split()]
        d.append(a)
        ar.append(b)
    ar.sort()
    ar = rearrange(ar,n)
    print(ar)
    if(n%2==0):
        for j in range(0,n-1,2):
            ar[j],ar[j+1] = ar[j+1],ar[j]
    else:
        for j in range(0,n//2,2):
            ar[j],ar[j+1] = ar[j+1],ar[j]
            ar[-j-1],ar[-j-2] = ar[-j-2],ar[-j-1]
    print(ar)
    a,b = d[0],ar[0]
    for j in range(1,n):
        s+=abs(d[j]-a)*abs(ar[j]-b)+2*min(b,ar[j])
        a,b = d[j],ar[j]
    print(s)
