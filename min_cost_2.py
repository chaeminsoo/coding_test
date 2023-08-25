# 11779
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])

st, ed = map(int,input().split())
st-=1
ed-=1

def dijk(st,graph,n,ed):
    dist = [1e9]*n
    visited = [False]*n
    dist[st] = 0
    path = [[] for _ in range(n)]
    
    q = []
    heapq.heappush(q,[0,st])
    while q:
        v,idx = heapq.heappop(q)
        visited[idx] = True
        if idx == ed:
            break

        for nxt_node, cost in graph[idx]:
            if cost+v < dist[nxt_node] and not visited[nxt_node]:
                dist[nxt_node] = cost+v
                path[nxt_node] = (path[idx]+[idx])
                heapq.heappush(q,[cost+v,nxt_node])
    
    return dist, path
dist, path = dijk(st,graph,n,ed)
print(dist[ed])
print(len(path[ed])+1)
for i in path[ed]+[ed]:
    print(i+1,end=' ')