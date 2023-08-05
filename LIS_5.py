# 14003
from bisect import bisect_left

n = int(input())
As = list(map(int,input().split()))

dp = [1e9+10]*n
dp_2 = [1e9]*n

for i,j in enumerate(As):
    idx = bisect_left(dp,j)
    dp[idx] = j
    dp_2[i] = idx

cnt = 0
for i in dp:
    if i == 1e9+10:
        break
    cnt+=1

print(cnt)

cnt-=1
ans = []
for i in range(n-1,-1,-1):
    if cnt < 0:
        break
    if dp_2[i] == cnt:
        ans.append(As[i])
        cnt-=1

print(*ans[::-1])