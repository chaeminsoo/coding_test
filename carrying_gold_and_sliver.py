# https://school.programmers.co.kr/learn/courses/30/lessons/86053?language=python3
def solution(a, b, g, s, w, t):
    n = len(g)
    st = 1
    ed = (1e9*1e5)*4
    ans = ed
    while st <= ed:
        mid = (st+ed)//2
        g_max = 0
        s_min = 0
        s_max = 0
        g_min = 0
        for i in range(n):
            move_time = mid // t[i]
            if move_time % 2 == 0:
                go_num = move_time//2
            else:
                go_num = move_time//2 +1
            
            move_amount = w[i]*go_num
            if move_amount >= g[i]:
                g_max += g[i]
                s_min += min(move_amount-g[i],s[i])
            else:
                g_max += move_amount
                
            if move_amount >= s[i]:
                s_max += s[i]
                g_min += min(move_amount-s[i],g[i])
            else:
                s_max += move_amount
        
        if a <= g_max and b <= s_max and a+b <= g_max+s_min:
            ans = min(ans,mid)
            ed = mid-1
        else:
            st = mid+1
            
    return ans