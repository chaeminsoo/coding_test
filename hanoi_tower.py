# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):
    ans = []
    def hanoi(st,mid,ed,n):
        if n == 1:
            ans.append([st,ed])
            return
        
        hanoi(st,ed,mid,n-1)
        ans.append([st,ed])
        hanoi(mid,st,ed,n-1)
    
    hanoi(1,2,3,n)
    return ans
    