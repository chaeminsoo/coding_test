# https://school.programmers.co.kr/learn/courses/30/lessons/68937
import heapq

def solution(n, edges):
    graph = [[] for _ in range(n)]
    for i,j in edges:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
    
    def dijk(st,graph,n):
        dist = [1e9]*n
        visited = [False]*n
        dist[st] = 0
        
        q = []
        heapq.heappush(q,[0,st])
        while q:
            v,idx = heapq.heappop(q)
            visited[idx] = True
            
            for nxt_node in graph[idx]:
                if v+1 < dist[nxt_node] and not visited[nxt_node]:
                    dist[nxt_node] = v+1
                    heapq.heappush(q,[v+1,nxt_node])
        
        return dist
    
    dist = dijk(0,graph,n)
    st_node = 0
    ref = -1
    for i in range(n):
        if ref < dist[i]:
            ref = dist[i]
            st_node = i
            
    dist = dijk(st_node,graph,n)
    ref_dist = dist[:]
    ref_dist.sort()
    if ref_dist[-1] == ref_dist[-2]:
        return ref_dist[-1]
    else:
        st_node = 0
        ref = -1
        for i in range(n):
            if ref < dist[i]:
                ref = dist[i]
                st_node = i

        dist = dijk(st_node,graph,n)
        dist.sort()
        if dist[-1] == dist[-2]:
            return dist[-1]
        else:
            return dist[-1]-1