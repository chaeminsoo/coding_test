# 1800
import heapq

n, p, k = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(p):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])

def dijk(s, graph, n, target_cost):
    dist = [2000000]*n
    visited = [False]*n
    dist[s] = 0

    q = []
    heapq.heappush(q,[0,s])
    while q:
        v, idx = heapq.heappop(q)
        visited[idx] = True
        
        for nxt_node, cost in graph[idx]:
            if cost > target_cost:
                cost = 1
            else:
                cost = 0

            if v+cost < dist[nxt_node] and not visited[nxt_node]:
                dist[nxt_node] = v+cost
                heapq.heappush(q,[v+cost, nxt_node])
    
    return dist[n-1]

st = 0
ed = 1000000

while st <= ed:
    mid = (st+ed)//2
    rslt = dijk(0,graph,n,mid)  
    if rslt > k:
        st = mid+1
    else:
        ed = mid-1

if st > 1000000:
    print(-1)        
else:
    print(st)