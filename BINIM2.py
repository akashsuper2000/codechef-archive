for i in range(int(input())):
    n,s = [j for j in input().split()]
    n = int(n)
    dee,dum=0,0
    for j in range(n):
        p = input()
        if(p[0]=='0'):
            dee+=1
            if(p[-1]=='1'):
                dum+=1
        else:
            dum+=1
            if(p[-1]=='0'):
                dee+=1


    if(s=='Dee'):
        if(dee==0 or dum>=dee):
            print('Dee')
        else:
            print('Dum')
    else:
        if(dum==0 or dee>=dum):
            print('Dum')
        else:
            print('Dee')
        
