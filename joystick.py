# https://school.programmers.co.kr/learn/courses/30/lessons/42860
from collections import deque

def solution(name):
    n = len(name)
    alpha = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}
    
    target = set()
    for i in range(n):
        if name[i] == 'A':
            target.add(i)
    
    q = deque()
    q.append([0,target,0,0])
    ans = 0
    while q:
        idx,status,m_cnt,c_cnt = q.popleft()
        if m_cnt > 2*n:
            continue
            
        if len(status) == n:
            ans = m_cnt + c_cnt
            break
        
        if idx in status:
            q.append([(idx+1)%n,status,m_cnt+1,c_cnt])
            if idx > 0:
                q.append([idx-1,status,m_cnt+1,c_cnt])
            else:
                q.append([n-1,status,m_cnt+1,c_cnt])
        else:
            ref = alpha[name[idx]]
            if len(status|{idx}) == n:
                ans = m_cnt + c_cnt + ref
                break
            
            q.append([(idx+1)%n,status|{idx},m_cnt+1,c_cnt+ref])
            if idx > 0:
                q.append([idx-1,status|{idx},m_cnt+1,c_cnt+ref])
            else:
                q.append([n-1,status|{idx},m_cnt+1,c_cnt+ref])
            
    return ans