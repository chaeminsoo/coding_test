# 2631
from bisect import bisect_left

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

used_num = set()
dp = [1e9]*n

for i in nums:
    idx = bisect_left(dp,i)
    dp[idx] = i

cnt=0
for i in dp:
    if i == 1e9:
        break
    cnt+=1

print(n-cnt)