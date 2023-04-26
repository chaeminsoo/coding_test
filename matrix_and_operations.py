# https://school.programmers.co.kr/learn/courses/30/lessons/118670#
from collections import deque

def solution(rc, operations):
    rows = deque()
    for i in rc:
        rows.append(deque(i[1:-1]))
        
    outter_columns = [deque(),deque()]
    for i in [0,-1]:
        for j in rc:
            outter_columns[i].append(j[i])
    
    for i in operations:
        if i == "Rotate":
            r_ = outter_columns[0].popleft()
            rows[0].appendleft(r_)
            
            t_ = rows[0].pop()
            outter_columns[1].appendleft(t_)
            
            l_ = outter_columns[1].pop()
            rows[-1].append(l_)
            
            b_ = rows[-1].popleft()
            outter_columns[0].append(b_)
            
        else:
            b_ = rows.pop()
            rows.appendleft(b_)
            
            b_ = outter_columns[0].pop()
            outter_columns[0].appendleft(b_)
            
            b_ = outter_columns[1].pop()
            outter_columns[1].appendleft(b_)
        
    ans = []
    for i in range(len(rows)):
        l_ = outter_columns[0][i]
        r_ = outter_columns[1][i]
        
        rows[i].appendleft(l_)
        rows[i].append(r_)
        
        ans.append(list(rows[i]))
        
    return ans