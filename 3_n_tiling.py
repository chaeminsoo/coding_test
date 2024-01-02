# https://school.programmers.co.kr/learn/courses/30/lessons/12902?language=python3

# 2에서 새로 생긴 것 -> 3
# 4에서 새로 생긴 것 -> 2
# 6에서 새로 생긴 것 -> 2
# ...
# dp[4] = (4에서 새로 생긴 타일) + dp[2]*(2에서 새로 생긴 타일) = 2 + 3*3 = 11
# dp[6] = (6에서 새로 생긴 타일) + dp[2]*(4에서 새로 생긴 타일) + dp[4](2에서 새로 생긴 타일)
# dp[n] = dp[0]*(n에서 새로 생긴 타일) + dp[2]*(n-2에서 새로 생긴 타일) + dp[4](n-4에서 새로 생긴 타일) + ... + dp[n-4](4에서 새로 생긴 타일) +dp[n-2](2에서 새로 생긴 타일)

# dp[n] = dp[0]*2 + dp[2]*2 + dp[4]2 + ... + dp[n-4]2 + dp[n-2]3
# dp[n] = dp[n-2]*3 + dp[n-4]*2 + dp[n-6]*2 + ... + dp[2]*2 + dp[0]*2
# dp[n+2] = dp[n]*3 + dp[n-2]*2 + dp[n-4]*2 + ... + dp[2]*2 + dp[0]*2

# dp[n+2] - dp[n] = dp[n]*3 +dp[n-2]*2 - dp[n-2]*3
# dp[n+2] = dp[n]*4 + dp[n-2]*2 - dp[n-2]*3
# dp[n] = dp[n-2]*4 + dp[n-4]*2 - dp[n-4]*3
# dp[n] = dp[n-2]*4 - dp[n-4]
def solution(n):
    dp = [1,0,3,0,11]
    if n < 5:
        return dp[n]
    
    for i in range(5,n+1):
        rslt = (dp[-2]*4 - dp[-4])%1000000007
        dp.append(rslt)
    
    return dp[-1]
    