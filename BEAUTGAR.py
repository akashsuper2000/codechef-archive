for i in range(int(input())):
    s = input()
    f=0
    if(s=='RG' or s=='GR'):
        f=1
    elif(len(s)%2==0):
        a,b = -1,-1
        for j in range(len(s)-1):
            if(a!=-1 and b!=-1):
                break
            elif j==0:
                if(s[j]==s[-1]):
                    a=0
                elif(s[j]==s[j+1]):
                   if(a>=0):
                       b=j+1
                   else:
                       a=j+1
            else:
               if(s[j]==s[j+1]):
                   if(a>=0):
                       b=j+1
                   else:
                       a=j+1
        s = s[:a]+s[a:b][::-1]+s[b:]
        if('RR' in s or 'GG' in s or s[0]==s[-1]):
            f=0
        else:
            f=1
    if(f==0):
        print('no')
    else:
        print('yes')
