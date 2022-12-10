# 1753
import heapq

v, e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
distance = [1e9]*(v+1)

for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijk(st):
    q = []
    heapq.heappush(q,(0,st))
    distance[st] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijk(k)
for i in range(1,v+2):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])