for i in range(int(input())):
    n = int(input())
    s,c = [j for j in input().split()]
    f = 0
    ans = 0
    for j in range(n):
       if(s[j]==c):
           ans+=(j+1-f)*(n-j)
           f = j+1
    print(ans)
           
