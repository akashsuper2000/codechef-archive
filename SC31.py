for i in range(int(input())):
    n = int(input())
    a = 0
    for j in range(n):
        a = a^int(input(),2)
    print(str(bin(a)).count('1'))
