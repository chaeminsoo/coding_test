# 2533
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n)]
visited = [False]*n

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dp = [[0,1] for _ in range(n)]

def dfs(node):
    visited[node] = True
    for nxt_node in graph[node]:
        if visited[nxt_node]:
            continue
        dfs(nxt_node)
        dp[node][0] += dp[nxt_node][1]
        dp[node][1] += min(dp[nxt_node])

dfs(0)
print(min(dp[0]))