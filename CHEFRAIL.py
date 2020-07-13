from math import sqrt
for i in range(int(input())):
    n,m = [int(j) for j in input().split()]
    x = [int(j) for j in input().split()]
    y = [int(j) for j in input().split()]
    sx = set(x)
    sy = set(y)
    px,nx = [],[]
    py,ny = [],[]
    c = 0

    for j in x:
        if(j>0):
            px.append(j)
        elif(j<0):
            nx.append(-j)
    for j in y:
        if(j>0):
            py.append(j)
        elif(j<0):
            ny.append(-j)
            
    for j in px:
        for k in nx:
            temp = sqrt(j*k)
            if(temp in sy):
                c+=1
            if(-temp in sy):
                c+=1
    for j in py:
        for k in ny:
            temp = sqrt(j*k)
            if(temp in sx):
                c+=1
            if(-temp in sx):
                c+=1
    if(0 in sx):
        c+=m*(n-1)
    elif(0 in sy):
        c+=n*(m-1)
    print(int(c))
