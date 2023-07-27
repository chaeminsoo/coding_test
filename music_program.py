# 2623
from collections import deque

n,m = map(int,input().split())

degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    data = list(map(int,input().split()))
    len_data = len(data)
    for i in range(len_data):
        if i == 0 or i == len_data-1:
            continue

        graph[data[i]].append(data[i+1])
        degree[data[i+1]] += 1

q = deque()
for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)

ans = []
while q:
    now_node = q.popleft()
    ans.append(now_node)

    for i in graph[now_node]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

if len(ans) < n:
    print(0)
else:
    for i in ans:
        print(i)