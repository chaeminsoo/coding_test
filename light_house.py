# https://school.programmers.co.kr/learn/courses/30/lessons/133500
import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    graph = [[] for _ in range(n)]
    for i,j in lighthouse:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
    
    # [꺼졌을때,켜졌을때]
    dp = [[1e9,1e9] for _ in range(n)]
    visited = [False]*n
    
    def dfs(node):
        if len(graph[node]) == 1 and visited[graph[node][0]]:
            dp[node] = [0,1]
            return [0,1]
        
        ref = 0 # 지금 노드가 켜져있을때
        ref_2 = 0 # 지금 노드가 꺼져있을때
        visited[node] = True
        for i in graph[node]:
            if visited[i]:
                continue
            rslt = dfs(i)
            ref += min(rslt[0],rslt[1])
            ref_2 += rslt[1]
                         
        dp[node][1] = ref+1
        dp[node][0] = ref_2
        visited[node] = False
        
        return dp[node]
    
    dfs(0)
    
    return min(dp[0])