# https://school.programmers.co.kr/learn/courses/30/lessons/42897?language=python3

def solution(money):
    n = len(money)
    dp = [0]*n
    dp[0] = money[0]
    dp[1] = max(money[0],money[1])
    for i in range(2,n-1):
        dp[i] = max(dp[i-1],money[i]+dp[i-2])
    
    dp_2 = [0]*n
    dp_2[0] = 0
    dp_2[1] = money[1]
    for i in range(2,n):
        dp_2[i] = max(dp_2[i-1],money[i]+dp_2[i-2])
        
    return max(max(dp), max(dp_2))