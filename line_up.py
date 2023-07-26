# 2252
from collections import deque

n, m = map(int,(input().split()))

degree = [0]*n
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,(input().split()))
    degree[b-1] += 1
    graph[a-1].append(b-1)

q = deque()
for i,j in enumerate(degree):
    if j == 0:
        q.append(i)

ans = []

while q:
    now_node = q.popleft()
    ans.append(now_node+1)

    for i in graph[now_node]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

for i in ans:
    print(i, end=' ')