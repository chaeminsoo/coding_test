# https://school.programmers.co.kr/learn/courses/30/lessons/42627#

import heapq

def solution(jobs):
    ans = []
    jobs.sort(reverse = True)
    prev_ed = jobs[-1][0] + jobs[-1][1]
    ans.append(jobs[-1][1])
    jobs.pop()
    q = []
    while jobs:
        st,t = jobs.pop()
        if st <= prev_ed:
            heapq.heappush(q,[t,st])
            continue
        
        if not q:
            prev_ed = st
            jobs.append([st,t])
            continue
        
        t_,st_ = heapq.heappop(q)
        ans.append(prev_ed+t_-st_)
        prev_ed += t_
        jobs.append([st,t])
    
    
    while q:
        t,st = heapq.heappop(q)
        ans.append(prev_ed+t-st)
        prev_ed += t
    
    return sum(ans)//len(ans)