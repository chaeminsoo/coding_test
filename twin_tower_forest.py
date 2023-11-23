# https://school.programmers.co.kr/learn/courses/30/lessons/140105?language=python3
def solution(n, count):
    dp = [[0]*(count+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(2,n+1):
        for j in range(1,count+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]*(i-1)*2)%1000000007
    
    return dp[n][count]