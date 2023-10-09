# 2023 현대모비스 알고리즘 경진대회 예선 상담원 인원

import heapq

def solution(k, n, reqs):
    all_mentor_cases = []
    
    def make_all_m(cnt,left,m,k,m_sum,n):
        if cnt == k:
            if m_sum == n:
                all_mentor_cases.append(m[:])
            return
        
        for i in range(1,left+1):
            m.append(i)
            make_all_m(cnt+1,left-i,m,k,m_sum+i,n)
            m.pop()
            
        
    make_all_m(0,n,[],k,0,n)
    
    ans = 1e9
    for m_case in all_mentor_cases:
        flag = False
        rslt = 0
        m_status = {}
        for i in range(k):
            m_status[i] = [0]*m_case[i]
            heapq.heapify(m_status[i])
        
        for a,b,c in reqs:
            c-=1
            fast_m = heapq.heappop(m_status[c])
            if fast_m <= a:
                heapq.heappush(m_status[c],a+b)
            else:
                rslt += (fast_m-a)
                if rslt > ans:
                    flag = True
                    break
                heapq.heappush(m_status[c],fast_m+b)
        
        if flag:
            continue
        ans = rslt
        
    return ans