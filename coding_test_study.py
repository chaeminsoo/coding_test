# https://school.programmers.co.kr/learn/courses/30/lessons/118668
def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for i in problems:
        max_alp = max(max_alp,i[0])
        max_cop = max(max_cop,i[1])
        
    dp = [[1e9]*(max_alp+1) for _ in range(max_cop+1)]
    
    cop = min(cop,max_cop)
    alp = min(alp,max_alp)
    
    dp[cop][alp] = 0
            
    for c in range(cop, max_cop+1):
        for a in range(alp, max_alp+1):
            if a+1 <= max_alp:
                dp[c][a+1] = min(dp[c][a]+1,dp[c][a+1])
            if c+1 <= max_cop:
                dp[c+1][a] = min(dp[c][a]+1,dp[c+1][a])
                
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if c >= cop_req and a >= alp_req:
                    nxt_a = min(max_alp, a + alp_rwd)
                    nxt_c = min(max_cop, c + cop_rwd)
                    
                    dp[nxt_c][nxt_a] = min(dp[nxt_c][nxt_a], dp[c][a]+cost)
    
    return dp[max_cop][max_alp]