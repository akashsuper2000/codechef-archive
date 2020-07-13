for i in range(int(input())):
    n = input()
    s = sum([int(j) for j in n])
    if s%10!=0:
        print(n+str(10-s%10))
    else:
        print(n+str(0))
