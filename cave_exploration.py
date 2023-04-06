# https://school.programmers.co.kr/learn/courses/30/lessons/67260
from collections import deque

def solution(n, path, order):
    visited = [False]*n
    graph = {}
    pre_node = {}
    nxt_node = {}
    for i, j in path:
        try:
            graph[i].append(j)
        except KeyError:
            graph[i] = [j]
        try:
            graph[j].append(i)
        except KeyError:
            graph[j] = [i]
            
    for i, j in order:
        pre_node[j] = i
        nxt_node[i] = j
        
    q = deque()
    q.append(0)
    visited[0] = True
    stop_nodes = set()
    while q:
        now = q.popleft()
        if now in pre_node:
            pre_visit = pre_node[now]
            if visited[pre_visit]:
                visited[now] = True
            else:
                stop_nodes.add(now)
                continue
        else:
            visited[now] = True
                
        if now in nxt_node:
            if nxt_node[now] in stop_nodes:
                stop_nodes.remove(nxt_node[now])
                q.append(nxt_node[now])
            
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
    
    return all(visited)