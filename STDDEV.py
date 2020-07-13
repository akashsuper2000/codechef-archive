from statistics import stdev
for i in range(int(input())):
    n,sigma = [int(j) for j in input().split()]
    a = [0]*n
    k,l=0,0
    while(abs(sigma-stdev(a))>0.01):
        k+=1
        if(sigma<stdev(a)):
            a[l]+=1
        else:
            a[l]-=1
            l+=1
        if(l==n):
            l=0
        if(k==10000):
            break
    if(k==10000):
        print(-1)
    else:
        print(' '.join([str(j) for j in a]))
