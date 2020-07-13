for i in range(int(input())):
    p1,p2,k = [int(j) for j in input().split()]
    m = k*2
    p = (p1+p2)%m
    if(p<k):
        print('CHEF')
    else:
        print('COOK')
    
