m = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}
for i in range(int(input())):
    a,b = [int(j) for j in input().split()]
    c = a+b
    s = 0
    for j in str(c):
        s+=m[j]
    print(s)
