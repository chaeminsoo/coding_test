# 1766
from collections import deque
from bisect import bisect_left

n,m = map(int,input().split())
dg = [0]*n
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    dg[b-1] += 1

q = deque()
for i, j in enumerate(dg):
    if j == 0:
        idx = bisect_left(q,i)
        q.insert(idx,i)
ans = []
while q:
    now = q.popleft()
    ans.append(now)
    while graph[now]:
        v = graph[now].pop()
        dg[v] -= 1
        if dg[v] == 0:
            q.insert(bisect_left(q,v),v)
for i in ans:
    print(i+1, end=' ')