# 1167
import sys
import heapq
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    data = list(map(int,input().split()))
    cursor_ = 1
    while True:
        if data[cursor_] == -1:
            break
        
        tree[data[0]].append([data[cursor_],data[cursor_+1]])
        cursor_ += 2

def dijk(s,grahp,n):
    very_far = [0,0]
    dist = [1e9]*(n+1)
    visited = [False]*(n+1)
    dist[s] = 0

    q = []
    heapq.heappush(q, [0,s])
    while q:
        v, idx = heapq.heappop(q)
        visited[idx] = True

        if v > very_far[0]:
            very_far[0] = v
            very_far[1] = idx

        for nxt_node, cost in grahp[idx]:
            if cost+v < dist[nxt_node] and not visited[nxt_node]:
                dist[nxt_node] = cost+v
                heapq.heappush(q,[cost+v,nxt_node])
    
    return very_far

st_node = dijk(1,tree,v+1)
ed_node = dijk(st_node[1],tree,v+1)

print(ed_node[0])