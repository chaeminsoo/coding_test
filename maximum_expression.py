from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    opers = set()
    exp = []
    ref = ''
    for i in expression:
        if i in ['+', '-', '*']:
            exp.append(ref)
            exp.append(i)
            ref = ''            
            opers.add(i)
        else:
            ref+=i
    if ref:
        exp.append(ref)
        
    all_cases = list(permutations(opers,len(opers)))
    
    for case in all_cases:
        left = deque()
        right = deque(exp[:])
        
        for c in case:
            while right:
                r = right.popleft()
                if r == c:
                    l = left.pop()
                    rr = right.popleft()
                    rslt = str(eval(l+r+rr))
                    left.append(rslt)
                    continue
                left.append(r)
            right = left
            left = deque()
        answer = max(abs(int(''.join(right))), answer)
            
    return answer