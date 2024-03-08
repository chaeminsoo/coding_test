# 3687
import sys
input = sys.stdin.readline
import math

t = int(input())

min_dp = [math.inf]*101
min_dp[2] = 1
min_dp[3] = 7
min_dp[4] = 4
min_dp[5] = 2
min_dp[6] = 6
min_dp[7] = 8

for i in range(8,101):
    for j in range(2,8):
        if j == 6:
            min_dp[i] = min(min_dp[i], min_dp[i-j]*10)
        else:
            min_dp[i] = min(min_dp[i], min_dp[i-j]*10 + min_dp[j])

def mx(n):
    if n%2 == 0:
        max_num = int('1'*(n//2))
    else:
        max_num = int('7'+'1'*((n-3)//2))

    return max_num

for i in range(t):
    n = int(input())
    print(min_dp[n], mx(n))