for i in range(int(input())):
    s = input()
    if(len(s)==1 or (s[1:]+s[0]==s[-1]+s[:-1])):
        print('YES')
    else:
        print('NO')
