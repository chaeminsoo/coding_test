# https://school.programmers.co.kr/learn/courses/30/lessons/12929
def solution(n):
    global ans
    ans = 0
    
    def dfs(cnt,open_num,close_num,n):
        global ans
        if open_num > n//2 or close_num > n//2:
            return
        if cnt == n:
            ans+=1
            return
        
        dfs(cnt+1,open_num+1,close_num,n)
        if open_num > close_num:
            dfs(cnt+1,open_num,close_num+1,n)
    
    dfs(1,1,0,n*2)
        
    return ans