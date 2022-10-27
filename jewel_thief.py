# 1202
import sys
input = sys.stdin.readline
import heapq

n,k = map(int,input().split())
jewels = []
for _ in range(n):
    m,v = map(int,input().split())
    jewels.append((m,v))
bags = []
for _ in range(k):
    bags.append(int(input()))

jewels.sort()
bags.sort()
able_j = []
jdx = 0
ans = 0
for b in bags:
    while jdx < n:
        if b >= jewels[jdx][0]:
            heapq.heappush(able_j, -jewels[jdx][1])
            jdx+=1
        else:
            break
    if able_j:
        ans += abs(heapq.heappop(able_j))
print(ans)