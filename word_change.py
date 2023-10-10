# https://school.programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):
    global ans
    ans = 1e9
    wn = len(words[0])
    def check(a,b,n):
        cnt = 0
        for i in range(n):
            if a[i] != b[i]:
                cnt+=1
                if cnt >= 2:
                    return False
        return True
    
    def dfs(now,cnt,target,left_w,n):
        global ans
        if now == target:
            ans = min(ans,cnt)
            return
        
        for i,j in enumerate(left_w):
            if check(now,j,n):
                ref = left_w.pop(i)
                dfs(j,cnt+1,target,left_w,n)
                left_w.append(ref)
    
    dfs(begin,0,target,words,wn)
    
    if ans == 1e9:
        return 0
    else:
        return ans