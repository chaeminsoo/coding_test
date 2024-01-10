# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 2024 카카오 겨울 인턴 코테 기출
from collections import defaultdict

def solution(friends, gifts):
    from_to = {i:defaultdict(int) for i in friends}
    gift_s = defaultdict(int)
    
    for i in gifts:
        f,t = i.split()
        from_to[f][t]+=1
        gift_s[f] += 1
        gift_s[t] -= 1
    
    ans = -1
    for i in friends:
        rslt = 0
        for j in friends:
            if i==j:
                continue
            
            if from_to[i][j] > from_to[j][i]:
                rslt+=1
            elif from_to[i][j] == from_to[j][i] and gift_s[i] > gift_s[j]:
                rslt+=1
        ans = max(ans,rslt)
    
    return ans