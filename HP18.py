for i in range(int(input())):
    n,a,b = [int(j) for j in input().split()]
    m = [int(j) for j in input().split()]
    c = 0
    na, nb = 0,0
    for j in m:
        if(j%a==0 and j%b==0):
            c+=1
        elif(j%a==0):
            na+=1
        elif(j%b==0):
            nb+=1
    if c>0:
        na+=1
    if(na<=nb):
        print('ALICE')
    else:
        print('BOB')
