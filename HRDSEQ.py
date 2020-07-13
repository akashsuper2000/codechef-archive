a = [0,0]
d = {0:0}
for i in range(1,128):
    d[a[-2]] = i-1
    if(a[-1] in d):
        a.append(i-d[a[-1]])
    else:
        a.append(0)
print(a)
b=[a[:i+1].count(a[i]) for i in range(129)]
print(b)
        
        
