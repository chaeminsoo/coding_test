# https://school.programmers.co.kr/learn/courses/30/lessons/258709?language=python3
# 2024 카카오 겨울 인턴 코테 기출
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    
    all_cases = []
    def make_cases(l,num):
        if len(l) == n:
            if  num == n//2:
                all_cases.append(l[:])
            return
        
        l.append(0)
        make_cases(l,num)
        l.pop()
        l.append(1)
        make_cases(l,num+1)
        l.pop()
    
    make_cases([],0)
    
    ans = [-1,-1]
    for case in all_cases:
        As = [0]
        Bs = [0]
        for dice_num in range(n):
            if case[dice_num]:
                rslt = []
                for d in dice[dice_num]:
                    for a in As:
                        rslt.append(a+d)
                As = rslt[:]
            else:
                rslt = []
                for d in dice[dice_num]:
                    for b in Bs:
                        rslt.append(b+d)
                Bs = rslt[:]
        
        As.sort()
        Bs.sort()
        
        A_wins = 0
        for a in As:
            idx = bisect_left(Bs,a)
            A_wins += idx
        
        if A_wins > ans[0]:
            ans = [A_wins,case]
    
    rslt = []
    for i,j in enumerate(ans[1]):
        if j:
            rslt.append(i+1)
    
    return rslt