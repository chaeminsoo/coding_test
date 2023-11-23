# https://school.programmers.co.kr/learn/courses/30/lessons/138475
def solution(e, starts):
    # dp[n] : n의 약수의 개수
    dp = [0]*(e+1)
    for i in range(1,e+1):
        if i*i <= e:
            dp[i*i] += 1
        for j in range(i+1,e+1):
            ref = i*j
            if ref > e: 
                break
            dp[ref] += 2
    
    # dp_2[n] : n에서부터 e(문제에서 주어진것) 사이의 가장 약수가 많은 수
    dp_2 = [0]*(e+1)
    dp_2[e] = e
    for i in range(e-1,-1,-1):
        if dp[i] >= dp[dp_2[i+1]]:
            dp_2[i] = i
        else:
            dp_2[i] = dp_2[i+1]
    
    ans = []
    for i in starts:
        ans.append(dp_2[i])
    return ans