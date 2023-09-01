# 2021 카카오 채용연계형 인턴십 표 편집
def solution(n, k, cmd):
    chart = [True]*n
    idx = k
    n_d = {i:[i-1,i+1] for i in range(n)}
    n_d[n-1][1] = -1
    
    stack = []
    for c in cmd:
        if c[0] == 'U':
            c1, c2 = c.split()
            for _ in range(int(c2)):
                idx = n_d[idx][0]                
            
        elif c[0] == 'D':
            c1, c2 = c.split()
            for _ in range(int(c2)):
                idx = n_d[idx][1]
                
        elif c[0] == 'C':
            chart[idx] = False
            pre,nxt = n_d[idx]
            stack.append([idx,pre,nxt])
            
            if nxt == -1:
                idx = n_d[idx][0]
                n_d[pre][1] = -1
            elif pre == -1:
                idx = n_d[idx][1]
                n_d[nxt][0] = -1
            else:
                idx = n_d[idx][1]
                n_d[pre][1] = nxt
                n_d[nxt][0] = pre
            
        elif c[0] == 'Z':
            ref_idx, ref_pre, ref_nxt = stack.pop()
            chart[ref_idx] = True
            if ref_pre == -1:
                n_d[ref_nxt][0] = ref_idx
            elif ref_nxt == -1:
                n_d[ref_pre][1] = ref_idx
            else:
                n_d[ref_nxt][0] = ref_idx
                n_d[ref_pre][1] = ref_idx
    
    ans = ''
    for i in chart:
        if i:
            ans+='O'
        else:
            ans+='X'
            
    return ans