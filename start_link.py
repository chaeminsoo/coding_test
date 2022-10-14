# 5014
from collections import deque

f, s, g, u, d = map(int,input().split())

floor_cnt = [1e9]*(f+1)
visited = [False]*(f+1)
visited[s] = True
floor_cnt[s] = 0

q = deque()
q.append((s,0))
while q:
    now, cnt = q.popleft()
    if now == g:
        break

    for i in [u, -d]:
        nxt = now+i

        if nxt > 0 and nxt <= f and not visited[nxt]:
            visited[nxt] = True
            floor_cnt[nxt] = cnt+1
            q.append((nxt,cnt+1))
            
ans = floor_cnt[g]
if ans == 1e9:
    print('use the stairs')
else:
    print(ans)