# 13334
import heapq
import sys
input = sys.stdin.readline

n = int(input())

all_road = []
cur_end = 1e9+100
for _ in range(n):
    a,b = map(int,input().split())
    l = min(a,b)
    r = max(a,b)
    all_road.append([l,r])
    
rail = int(input())

road = []
for i,j in all_road:
    if j-i <= rail:
        road.append([i,j])
road.sort(key= lambda x:x[1])

if not road:
    print(0)
    exit()

ans = 0

q = []
cnt = 0
now_rail = road[0][0] + rail

for st,ed in road:
    if not q:
        heapq.heappush(q,[st,ed])
    else:
        while q:
            s,e = heapq.heappop(q)
            if ed - rail <= s:
                heapq.heappush(q,[s,e])
                break
        heapq.heappush(q,[st,ed])
    ans = max(ans,len(q))
print(ans)