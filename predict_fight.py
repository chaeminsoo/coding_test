# https://school.programmers.co.kr/learn/courses/30/lessons/12985
def solution(n,a,b):
    ans = 1
    while True:
        if abs(a-b) == 1 and min(a,b)%2 != 0:
            break
        
        if a%2==0: a//=2
        else: a = (a+1)//2
        
        if b%2==0: b//=2
        else: b = (b+1)//2
        
        ans+=1
    return ans