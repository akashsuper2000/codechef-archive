for i in range(int(input())):
    n = int(input())
    d = {}
    a = [int(j) for j in input().split()]
    for j in a:
        if(j in d):
            d[j]+=1
        else:
            d[j]=1
    if(max([j for j in list(d.values())]) <= int(n/2)):
        print('Yes')
        
    else:
        print('No')
    
