for i in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    for i in range(len(s)):
        if s[i] == '-':
            s = s[:i+1]+'('+s[i+1:]
            c = c+1
        elif s[i] == '+' and c>0:
            s = s[:i]+')'+s[i:]
            c = c-1
    s = s[:]+')'*c
    print(s)
    print(eval(s))
