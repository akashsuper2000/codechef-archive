for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    while(True):
        a.sort(reverse=True)
        b = (a[0]+a[1])/2
        a.remove(a[0])
        a.remove(a[0])
        a.append(b)
        if len(a) == 1:
            break
    
    print(a[0])
          
