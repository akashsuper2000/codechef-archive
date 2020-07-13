import numpy as np
for i in range(int(input())):
    n = int(input())
    ca,cb = 0,0
    a,b = np.zeros(26), np.zeros(26)
    da,db = np.zeros(26), np.zeros(26)
    
    for j in range(n):
        arr = np.zeros(26)
        p = list(input())
        for k in p:
            arr[ord(k)-97]+=1
        if(arr[0]+arr[4]+arr[8]+arr[14]+arr[20]>=np.sum(arr)-(arr[0]+arr[4]+arr[8]+arr[14]+arr[20])):
            da+=arr
            arr[arr!=0]=1
            a+=arr
            ca+=1
        else:
            db+=arr
            arr[arr!=0]=1
            b+=arr
            cb+=1
    print((np.prod(a[a!=0])*pow(np.prod(db[db!=0]),cb))/(np.prod(b[b!=0])*pow(np.prod(da[da!=0]),ca)))
