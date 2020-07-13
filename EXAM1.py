for i in range(int(input())):
    n = int(input())
    s = input()
    u = input()
    c = 0
    j = 0
    while(j<n):
        if(u[j]=='N'):
            pass
        elif(u[j]!=s[j]):
            j+=1
        else:
            c+=1
        j+=1
            
    print(c)
