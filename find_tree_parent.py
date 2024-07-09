# 11725
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
parent = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
visited[1] = True
q = deque()
q.append(1)

while q:
    node = q.popleft()
    for nxt in graph[node]:
        if not visited[nxt]:
            parent[nxt] = node
            visited[nxt] = True
            q.append(nxt)

for i in parent[2:]:
    print(i)