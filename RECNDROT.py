def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    lis = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
  
    return maximum 

for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    d = {}
    p = []
    for j in a:
        if(j not in d):
            p.append(j)
            d[j] = 1
    q = []
    d = {}
    for j in range(n-1,-1,-1):
        if(a[j] not in d):
            q.insert(0,a[j])
            d[a[j]] = 1
    print(min((len(p)-lis(p)+1),(len(q)-lis(q)+1)))
