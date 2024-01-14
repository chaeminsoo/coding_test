# https://school.programmers.co.kr/learn/courses/30/lessons/131703
def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    all_cases = []
    def make_col_case(c):
        if len(c) == m:
            all_cases.append(c[:])
            return
        
        c.append(0)
        make_col_case(c)
        c.pop()
        c.append(1)
        make_col_case(c)
        c.pop()
    
    make_col_case([])
    
    ans = 100
    for col_case in all_cases:
        cnt = 0
        ref = [i[:] for i in beginning]
        
        for c in range(m):
            if col_case[c] == 1:
                for i in range(n):
                    if ref[i][c] == 1: ref[i][c] = 0
                    elif ref[i][c] == 0: ref[i][c] = 1
        
        flag = True
        for i in range(n):
            reverse_ref = []
            for j in ref[i]:
                reverse_ref.append((j+1)%2)
            
            if ref[i] == target[i]:
                pass
            elif reverse_ref == target[i]:
                cnt+=1
            else:
                flag = False
                break
        
        if flag:
            ans = min(ans,sum(col_case)+cnt)
    
    if ans >= 100:
        return -1
    else:
        return ans