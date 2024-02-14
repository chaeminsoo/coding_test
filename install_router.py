# 2110
import sys
input = sys.stdin.readline

n, c = map(int,input().split())
hs = []
for _ in range(n):
    hs.append(int(input()))

hs.sort()

st = 0
ed = max(hs)
ans = 0
while st <= ed:
    mid = (st+ed)//2

    cnt = 1
    for i in range(n):
        if i == 0:
            before_h = hs[i]
            continue

        if hs[i] >= before_h + mid:
            cnt+=1
            before_h = hs[i]
    
    if cnt >= c:
        ans = max(ans,mid)
        st = mid+1
    else:
        ed = mid-1
print(ans)