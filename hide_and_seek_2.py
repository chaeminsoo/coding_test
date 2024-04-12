# 12851
from collections import deque

n,k = map(int,input().split())

times = [1e9]*100001
times[n] = 0

q = deque()
q.append(n)
status = [1e9,1]

while q:
    x = q.popleft()
    for nx in [x-1,x+1,x*2]:
        if 0<=nx<=100000:
            if times[nx] >= times[x]+1:
                times[nx] = times[x]+1
                q.append(nx)
                if times[x]+1 < status[0] and nx == k:
                    status = [times[x]+1,1]
                elif times[x]+1 == status[0] and nx == k:
                    status[1] += 1

print(times[k])
print(status[1])