# https://school.programmers.co.kr/learn/courses/30/lessons/87946
def solution(k, dungeons):
    n = len(dungeons)
    new_d = []
    for i,j in dungeons:
        new_d.append([i-j,i,j])
    new_d.sort()
    dp = [[0]*(k+1) for _ in range(n)]
    
    for i in range(n):
        for j in range(1,k+1):
            if j >= new_d[i][1]:
                dp[i][j] = max(dp[i-1][j-new_d[i][2]]+1,dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n-1][k]