def sl(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    if(len(a)<3):
        if(min(a[0],a[1])>k):
            p = min(a[0],a[1])-k
            a[0]-=1
            a[1]-=1
        print(sum(a))
    else:
        b = a.pop(a.index(max(a)))
        while(min(sl(a),max(a))>k):
            a[a.index(sl(a))]-=1
            a[a.index(max(a))]-=1
        print(sum(a)+b)
    
