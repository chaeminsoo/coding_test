# https://school.programmers.co.kr/learn/courses/30/lessons/131704
def solution(order):
    n = len(order)
    sub_stack = []
    stack = [n-i for i in range(n)]
    ans = 0
    for target in order:
        if sub_stack:
            if sub_stack[-1] == target:
                ans+=1
                sub_stack.pop()
                continue
        
        flag = False
        while stack:
            if stack[-1] == target:
                ans+=1
                stack.pop()
                flag = True
                break
            else:
                ref = stack.pop()
                sub_stack.append(ref)
        
        if not flag:
            break
    
    return ans