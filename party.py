# 1238
import heapq

n,m,x = map(int,input().split())
graph = [[] for _ in range(n)]
reverse_graph = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])
    reverse_graph[b-1].append([a-1,c])

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

go_home = dijk(x-1,graph,n)
go_party = dijk(x-1,reverse_graph,n)

ans = 0
for i in range(n):
    ans = max(ans, go_home[i]+go_party[i])
print(ans)