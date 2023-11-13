# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    times.sort()
    st = times[0]
    ed = times[-1]*n
    
    ans = ed
    while st <= ed:
        mid = (st+ed)//2
        how_many = 0
        for i in times:
            how_many += mid//i
        
        if how_many >= n:
            ans = min(ans,mid)
            ed = mid-1
        else:
            st = mid+1
    
    return ans