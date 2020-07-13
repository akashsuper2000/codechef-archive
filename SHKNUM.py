def t(n):
    return str(bin(n)).count('1')
    
for i in range(int(input())):
    n = int(input())
    s = 1
    f = 0
    if t(n)==2:
        s = 0
    else:
        while(n-s>2):
            if t(n-s)==2 or t(n+s)==2:
                f = 1
                break
            else:
                s = s+1
        if f==0:
            while(1):
                if t(n+s)==2:
                    f=1
                    break
                else:
                    s = s+1
    print(s)
        
