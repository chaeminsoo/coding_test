import sys
import heapq

input = sys.stdin.readline

T = int(input())

def dijk(s,graph,n):
    dist = [1e9]*n
    visited = [False]*n
    dist[s] = 0

    q = []
    heapq.heappush(q,[0,s])
    while q:
        v, idx = heapq.heappop(q)
        visited[idx] = True

        for desti, cost in graph[idx]:
            if v+cost < dist[desti] and not visited[desti]:
                dist[desti] = v+cost
                heapq.heappush(q,[v+cost, desti])

    return dist

for _ in range(T):
    rslt = []
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a-1].append((b-1,d))
        graph[b-1].append((a-1,d))
        
    desti = []
    for _ in range(t):
        dt = int(input())
        desti.append(dt-1)
        
    from_start = dijk(s-1,graph,n)
    from_g = dijk(g-1,graph,n)
    from_h = dijk(h-1,graph,n)

    for d in desti:
        if from_start[g-1] + from_g[h-1] + from_h[d] == from_start[d] or from_start[h-1] + from_h[g-1] + from_g[d] == from_start[d]:
            rslt.append(d+1)
    rslt.sort()
    for i in rslt:
        print(i, end=' ')
    print()