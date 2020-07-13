def t(n):
    return str(bin(n)).count('1')
    
for i in range(int(input())):
    n = int(input())
    s = 0
    c = str(bin(n))
    if n == 0:
        s = 3
    elif n==1:
        s = 2
    elif c.count('1')==1:
        s = 1
    else:
        j = c.index('1')
        try:
            c = c[c.index('1',j+1)+1:]
        except:
            c = '0'
        m = int(c,2)
        p = int('1'+'0'*len(c),2)-m
        s = min([m,p])
        
    print(s)
        
