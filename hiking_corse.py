# https://school.programmers.co.kr/learn/courses/30/lessons/118669

import heapq

def dijk(graph,n, gates, summits, summits_set,gates_set):
    intensity = [1e9]*n
    
    q = []
    for g in gates:
        heapq.heappush(q,[0,g-1])
        intensity[g-1] = 0
        
    while q:
        v, idx = heapq.heappop(q)
        if idx+1 in summits_set or v > intensity[idx]:
            continue
            
        for dest, cost  in graph[idx]:
            new_inten = max(v,cost)
            if new_inten < intensity[dest] and (dest+1 not in gates_set):
                intensity[dest] = new_inten
                heapq.heappush(q,[new_inten,dest])
        
    ans = [0, 1e9]
    for s in summits:
        inten = intensity[s-1]
        if ans[1] > inten:
            ans = [s,inten]
    return ans
            
def solution(n, paths, gates, summits):
    summits_set = set(summits)
    gates_set = set(gates)
    summits.sort()
    
    graph = [[] for _ in range(n)]
    for i,j,k in paths:
        graph[i-1].append([j-1,k])
        graph[j-1].append([i-1,k])
    
    return dijk(graph,n, gates, summits, summits_set,gates_set)