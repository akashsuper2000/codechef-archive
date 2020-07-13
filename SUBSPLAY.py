for i in range(int(input())):
    n = int(input())
    s = input()
    a,b = [-1 for j in range(26)],[1e5 for j in range(26)]
    for j in range(n):
        if(a[ord(s[j])-97]==-1):
            a[ord(s[j])-97] = j
        else:
            if(j-a[ord(s[j])-97]<b[ord(s[j])-97]):
                b[ord(s[j])-97] = j-a[ord(s[j])-97]
            a[ord(s[j])-97] = j
    print(max(n-min(b),0))
