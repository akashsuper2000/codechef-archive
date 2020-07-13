k = 10**9 + 7
import queue as q
for i in range(int(input())):
    s = input()
    m = ''
    a = [j for j in s]
    n = len(a)
    l = q.Queue(maxsize = len(a))
    for j in range(n):
        l.put(a[j])
    for j in range(n):
        p = l.get()
        while(not l.empty()):
            m+=l.get()
            
