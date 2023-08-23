# 1504
import heapq
import sys
input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])

v1,v2 = map(int,input().split())
v1-=1
v2-=1

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

from_v1_dist = dijk(v1,graph,n)
from_v2_dist = dijk(v2,graph,n)

st_v1_v2_ed = from_v1_dist[0]+from_v1_dist[v2]+from_v2_dist[n-1]
st_v2_v1_ed = from_v2_dist[0]+from_v2_dist[v1]+from_v1_dist[n-1]

ans = min(st_v1_v2_ed,st_v2_v1_ed)
if ans >= 1e9:
    print(-1)
else:
    print(ans)