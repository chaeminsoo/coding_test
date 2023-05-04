# https://school.programmers.co.kr/learn/courses/30/lessons/72416
def solution(sales, links):
    dp = [[0,0] for _ in sales]
    graph = [[] for _ in sales]
    for i, j in links:
        graph[i-1].append(j-1)
    
    def dfs(i):
        sum_child = 0
        for k in graph[i]: # k는 i에 연결된 자식을 의미
            dfs(k)
            sum_child += min(dp[k][0], dp[k][1])
        
        # 팀장이 가는 경우
        dp[i][1] = sum_child + sales[i]
        
        # 팀장은 안가고 팀원 중 한명이 간다.
        if any(dp[k][0] > dp[k][1] for k in graph[i]): 
            dp[i][0] = sum_child
        # 팀장도 안가고 팀원도 아무도 지원 안 함
        else:
            dp[i][0] = sum_child + min((dp[k][1] - dp[k][0] for k in graph[i]), default=0)
    
    dfs(0)
            
    return min(dp[0][0], dp[0][1])