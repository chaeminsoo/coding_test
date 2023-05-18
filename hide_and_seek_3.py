# 13549
import heapq

n,k = map(int,input().split())

if n == k:
    print(0)
elif n > k:
    print(n-k)
else:
    visited = [False]*100001
    dist = [1e9]*100001

    visited[n] = True
    dist[n] = 0

    q = []
    heapq.heappush(q,(0,n))
    while q:
        v, idx = heapq.heappop(q)
        
        if idx == k:
            print(v)
            break

        visited[idx] = True

        if idx*2 <= 100000:
            if v < dist[idx*2] and not visited[idx*2]:
                dist[idx*2] = 0
                heapq.heappush(q,[v,idx*2])

        nxt_node = [idx-1, idx+1]
        for nxt_n in nxt_node:
            if nxt_n <= 100000 and nxt_n >= 0:
                if v+1 < dist[nxt_n] and not visited[nxt_n]:
                    dist[nxt_n] = v+1
                    heapq.heappush(q,[v+1,nxt_n])

