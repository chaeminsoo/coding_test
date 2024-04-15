# 14938
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
items = [0] + items
graph = [[1e9]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = 0
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        if graph[i][j] <= m:
            temp += items[j]
    ans = max(ans,temp)

print(ans)