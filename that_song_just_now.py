# https://school.programmers.co.kr/learn/courses/30/lessons/17683?language=python3

def x_shop(m):
    rslt = ""
    prev = ''
    for i in m:
        if prev in ['C','D','F','G','A'] and i == '#':
            rslt = rslt[:-1] + prev.lower()
            continue
        rslt += i
        prev = i
    return rslt

def time_num(t):
    h,m = t.split(':')
    return int(h)*60+int(m)

def solution(m, musicinfos):
    answer = ['(None)',0]
    m = x_shop(m)
    
    for i in musicinfos:
        st,ed,name,melody = i.split(',')
        melody = x_shop(melody)
        music_len = time_num(ed) - time_num(st)
        
        if music_len < len(m):
            continue
        
        if music_len >= len(melody):
            melody *= 1439
            melody = melody[:music_len]
        else:
            melody = melody[:music_len]
        
        if m in melody:
            if answer[0] == '(None)':
                answer = [name, music_len]
            elif answer[1] < music_len:
                answer = [name, music_len]
        
    return answer[0]