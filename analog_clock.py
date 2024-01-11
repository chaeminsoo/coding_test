# https://school.programmers.co.kr/learn/courses/30/lessons/250135
# PCCP 기출 3번

# 시침 : 360/3600*12 -> 초당 1/120 도
# 분침 : 360/3600 -> 초당 0.1 도
# 초침 : 360/60 -> 초당 6 도

def solution(h1, m1, s1, h2, m2, s2):
    ans = 0
    # 360*120도 = 한바퀴, 라고 가정
    # 소수점 계산 때문
    MOD = 360*120
    t_diff = (3600*h2 + 60*m2 + s2) - (3600*h1 + 60*m1 + s1)
    ref = 3600*h1 + 60*m1 + s1
    now = [(ref)%MOD, (ref*12)%MOD, (ref*720)%MOD]
    
    if now[2] == now[1] or now[2] == now[0]:
        ans+=1
    
    for _ in range(t_diff):
        cnt = 0
        nxt_h = now[0] + 1
        nxt_m = now[1] + 12
        nxt_s = now[2] + 720
        
        if now[2] < now[1] and nxt_s >= nxt_m:
            cnt += 1
        if now[2] < now[0] and nxt_s >= nxt_h:
            cnt += 1
        
        if cnt >= 2:
            if nxt_h == nxt_m:
                cnt-=1
        
        ans += cnt
        
        now = [(nxt_h)%MOD, (nxt_m)%MOD, (nxt_s)%MOD]
        
    return ans