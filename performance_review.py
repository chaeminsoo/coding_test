# https://school.programmers.co.kr/learn/courses/30/lessons/152995?language=python3#
def solution(scores):
    scores = [[i,j,0] for i,j in scores]
    wan = sum(scores[0])
    scores[0][2] = 1
    
    new_s = []
    scores.sort(key = lambda x:(-x[0],x[1]))
    stnd = -1
    
    for i,j,k in scores:
        if j >= stnd:
            new_s.append([i,j,k])
            stnd = j
    
    flag = False
    ans = 1
    for i,j,k in new_s:
        if k == 1:
            flag = True
            continue
        
        if i+j > wan:
            ans+=1
    
    if flag:
        return ans
    else:
        return -1