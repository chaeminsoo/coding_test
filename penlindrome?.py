# 10942
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for i in range(n):
    for j in range(n):
        if i+j >= n:
            continue

        if j == i+j or j+1 == i+j:
            continue

        if nums[j] == nums[i+j]:
            if dp[j+1][i+j-1]:
                dp[j][i+j] = 1

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])