# 11000
import heapq

n = int(input())
sted = []
for _ in range(n):
    s,e = map(int,input().split())
    sted.append([s,e])

sted.sort()
rooms = []
heapq.heappush(rooms,sted[0][1])

for i in range(1,n):
    if sted[i][0] < rooms[0]:
        heapq.heappush(rooms,sted[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms,sted[i][1])
print(len(rooms))