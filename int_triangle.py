# https://school.programmers.co.kr/learn/courses/30/lessons/43105?language=python3
def solution(triangle):
    n = len(triangle)
    dp = [[0]*(i+1) for i in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1,n):
        for j in range(len(dp[i])):
            ref = []
            if j-1 >= 0:
                ref.append(dp[i-1][j-1])
            if j != len(dp[i])-1:
                ref.append(dp[i-1][j])

            dp[i][j] = triangle[i][j]+max(ref)
            
    return max(dp[-1])