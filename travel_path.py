# https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=python3#

def solution(tickets):
    n = len(tickets)
    status = {}
    for i,j in tickets:
        if i in status:
            status[i].append([j,0])
        else:
            status[i] = [[j,0]]
    
    for i in status:
        status[i].sort()
        
    ans = []
    def dfs(now,passed,cnt):
        if cnt >= n:
            ans.append(passed[:])
            return
        if now in status:
            for i,nxt_port_v in enumerate(status[now]):
                nxt_port,v = nxt_port_v
                if v: continue

                passed.append(nxt_port)
                status[now][i][1] = 1
                dfs(nxt_port,passed,cnt+1)
                status[now][i][1] = 0
                passed.pop()
            
    dfs('ICN',['ICN'],0)        
    
    return ans[0]