# 1654
k, n = map(int,input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))
st = 1
ed = max(lines)
ans = 0

while st <= ed:
    mid = (st+ed)//2
    x = 0
    for l in lines:
        x += (l//mid)
        
    if x >= n:
        ans = max(ans,mid)
        st = mid+1
    else:
        ed = mid-1
        
print(ans)