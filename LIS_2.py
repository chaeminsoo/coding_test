# 12015
from bisect import bisect_left
n = int(input())
As = list(map(int,input().split()))

dp = [1e9]*n

for i in As:
    dp[bisect_left(dp,i)] = i

cnt = 0
for i in dp:
    if i == 1e9:
        break
    cnt+=1
print(cnt)