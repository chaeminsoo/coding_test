# 16564
import sys
input  = sys.stdin.readline

n,k = map(int,input().split())
levels = []
for _ in range(n):
    levels.append(int(input()))

st = min(levels)
ed = max(levels) + k
mid = (st+ed)//2
ans = 0
while st <= ed:
    x = 0
    for l in levels:
        x += max(mid-l,0)
    
    if k >= x:
        ans = max(ans,mid)
        st = mid+1
        mid = (st+ed)//2
    elif k < x:
        ed = mid-1
        mid = (st+ed)//2
print(ans)