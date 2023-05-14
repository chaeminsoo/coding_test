# 1753
import sys
input  = sys.stdin.readline
import heapq

V, e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(V)]
for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u-1].append([v-1,w])

def dijk(s,graph,n):
    dist = [1e9]*n
    visited = [False]*n
    dist[s] = 0

    q = []
    heapq.heappush(q,[0,s])
    while q:
        v, idx = heapq.heappop(q)
        visited[idx] = True

        for nxt_node, cost in graph[idx]:
            if cost+v < dist[nxt_node] and not visited[nxt_node]:
                dist[nxt_node] = cost+v
                heapq.heappush(q,[cost+v,nxt_node])
    
    return dist

dist = dijk(k-1,graph,V)
for d in dist:
    if d == 1e9:
        print('INF')
    else:
        print(d)