# https://school.programmers.co.kr/learn/courses/30/lessons/72414#

def solution(play_time, adv_time, logs):
    h,m,s = play_time.split(':')
    play_time = int(h)*60*60 + int(m)*60 + int(s)
    h,m,s = adv_time.split(':')
    adv_time = int(h)*60*60 + int(m)*60 + int(s)
    time_line = [0]*(play_time+2)
    for i in logs:
        st,et = i.split('-')
        h,m,s = st.split(':')
        st = int(h)*60*60 + int(m)*60 + int(s)
        h,m,s = et.split(':')
        et = int(h)*60*60 + int(m)*60 + int(s)
        
        time_line[st] += 1
        time_line[et] -= 1
        
    for i in range(1, len(time_line)-1):
        time_line[i] += time_line[i-1]
        
    ans = [0, 0]
    time_line_len = len(time_line)
    for ad_st_time in range(time_line_len):
        ad_ed_time = min(time_line_len-1,ad_st_time + adv_time)
        if ad_st_time == 0:
            ad_watch = sum(time_line[ad_st_time:ad_ed_time-1])
        else:
            ad_watch -= time_line[prev_st]
            ad_watch += time_line[ad_ed_time-1]
        
        prev_st = ad_st_time
        if ad_watch > ans[1]:
                ans[0] = ad_st_time
                ans[1] = ad_watch
                
    h = str(ans[0]//3600)
    if len(h) < 2:
        h = '0'+h
    ans[0] %= 3600
    m = str(ans[0]//60)
    if len(m) < 2:
        m = '0'+m
    ans[0] %= 60
    s = str(ans[0])
    if len(s) < 2:
        s = '0'+s
    
    return h+':'+m+':'+s