# https://school.programmers.co.kr/learn/courses/30/lessons/12904?language=python3#

def solution(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i+1 < n and s[i] == s[i+1]:
            dp[i][i+1] = 1
    
    for j in range(1,n+1):
        for i in range(n+1-j):
            if i+j >= n:
                continue
            
            if s[i] == s[i+j] and dp[i+1][i+j-1]:
                dp[i][i+j] = 1
    
    ans = 1
    for i in range(n):
        for j in range(i,n):
            if dp[i][j] == 1:
                ans = max(ans,j-i+1)
    
    return ans