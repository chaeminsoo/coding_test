# https://school.programmers.co.kr/learn/courses/30/lessons/42890#
from itertools import combinations

def solution(relation):
    column_num = len(relation[0])
    row_num = len(relation)
    combi = []
    for j in range(1,column_num+1):
        combi += list(combinations([i for i in range(column_num)],j))
    
    print(combi)
    candi = []
    for cb in combi:
        check_set = set()
        for r in relation:
            check_set.add(tuple(r[i] for i in [*cb]))
        
        if len(check_set) == row_num:
            candi.append(set(cb))
            
    k=0
    while k < len(candi):
        new_candi = []
        for cd in candi:
            if not candi[k].issubset(cd):
                new_candi.append(cd)
        candi = [candi[k]] + new_candi
        k+=1
                
    return len(candi)