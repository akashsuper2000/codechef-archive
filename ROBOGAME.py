for i in range(int(input())):
    s = input()
    n = [[0]*2 for j in range(len(s))]
    for j in range(len(s)):
        if(s[j]!='.'):
            n[max(0,j-int(s[j]))][0]+=1
            n[min(len(s)-1,j+int(s[j]))][1]-=1
    c = 0
    f = 0
    for j in range(len(n)):
        c+=n[j][0]
        if(c>1):
            f = 1
        c+=n[j][1]
    if(f==1):
        print('unsafe')
    else:
        print('safe')
