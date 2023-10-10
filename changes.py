# https://school.programmers.co.kr/learn/courses/30/lessons/12907
def solution(n, money):
    money.sort()
    dp = [0]*(n+1)
    dp[0] = 1
    for i in money:
        for j in range(i,n+1):
            dp[j]+=dp[j-i]
            dp[j] %= 1000000007
            
    return dp[n]