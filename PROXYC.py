from math import ceil
for i in range(int(input())):
    d = int(input())
    s = input()
    need = ceil(d*0.75)
    have = s.count('P')
    c = 2
    f = 0
    while(c<d-2 and have<need):
        c+=1
        if(s[c-1]=='A' and ((s[c-2]=='P' or s[c-3]=='P') and (s[c]=='P' or s[c+1]=='P'))):
            have+=1
            f+=1
    if(have<need):
        print(-1)
    else:
        print(f)
