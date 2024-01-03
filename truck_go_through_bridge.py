# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0]*bridge_length)
    ans = 0
    truck_weights.reverse()
    bw = 0
    while truck_weights:
        t = truck_weights.pop()
        if t+(bw-q[0]) <= weight:
            bw+=t
            q.append(t)
        else:
            truck_weights.append(t)
            q.append(0)
            
        out_t = q.popleft()
        bw-=out_t
        ans+=1
                
    return ans + len(q)