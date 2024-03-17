# https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=python3
from collections import deque

def check(s):
    stack = []
    other = {')':'(', '}':'{', ']':'['}
    for i in s:
        if not stack:
            stack.append(i)
            continue
        
        if i in {'[', '{', '('}:
            stack.append(i)
        else:
            if stack[-1] == other[i]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
            

def solution(s):
    ans = 0
    s = deque(s)
    n = len(s)
    for _ in range(n):
        if check(s):
            ans+=1
        s.append(s.popleft())
    
    return ans