import sys
import collections as col
def dijkstra(n,d,a):
    unvisited = {node+1: None for node in range(n)}
    visited = {}
    current = a
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in d[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return list(dict(col.OrderedDict(sorted(visited.items()))).values())
    



for i in range(int(input())):
    n = int(input())
    d = {j+1:{} for j in range(n)}
    a = [float(j) for j in input().split()]
    b = [float(j) for j in input().split()]
    for j in range(n):
        d[1][j+1] = a[j]
        d[j+1][1] = a[j]
        d[n][j+1] = b[j]
        d[j+1][n] = b[j]
    v1 = dijkstra(n,d,1)
    v2 = dijkstra(n,d,n)
    if(a!=v1 or b!=v2):
        print('No')
    else:
        print('Yes')
    
