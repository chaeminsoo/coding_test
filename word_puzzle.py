# https://school.programmers.co.kr/learn/courses/30/lessons/12983?language=python3
def solution(strs, t):
    n = len(t)
    dp = [1e9]*(n+1)
    dp[n] = 0
    for i in range(n-1,-1,-1):
        for j in range(1,6):
            if i+j > n:
                break
            if t[i:i+j] in strs:
                dp[i] = min(dp[i],dp[i+j]+1)
    if dp[0] == 1e9:
        return -1
    else:
        return dp[0]