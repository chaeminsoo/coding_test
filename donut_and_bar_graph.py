# https://school.programmers.co.kr/learn/courses/30/lessons/258711
from collections import defaultdict, deque


def solution(edges):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    n = 0
    for i,j in edges:
        n = max(n,i,j)
        
        graph[i].append(j)
        out_degree[i] += 1
        in_degree[j] += 1
    
    ans = [0,0,0,0]
    visited = [False]*(n+1)
    
    for i in range(1,n+1):
        if in_degree[i] == 0 and out_degree[i] >= 2:
            ans[0] = i
            visited[i] = True
            
            for j in graph[i]:
                in_degree[j]-=1
            break
    
    def bfs(st):
        q = deque()
        q.append(st)
        visited[st] = True
        
        while q:
            now = q.popleft()
            
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
    
    
    for i in range(1,n+1):
        if in_degree[i] == 2 and out_degree[i] == 2 and not visited[i]:
            ans[3]+=1
            bfs(i)
    
    for i in range(1,n+1):
        if in_degree[i] == 0 and not visited[i]:
            ans[2]+=1
            bfs(i)
    
    for i in range(1,n+1):
        if in_degree[i] == 1 and out_degree[i] == 1 and not visited[i]:
            ans[1]+=1
            bfs(i)
            
    return ans