# https://school.programmers.co.kr/learn/courses/30/lessons/17678#
from bisect import bisect_right

def num_to_time(num):
    h = str(num//60)
    if len(h) < 2:
        h = '0'+h
    m = str(num%60)
    if len(m) < 2:
        m = '0'+m
    return h+':'+m

def solution(n, t, m, timetable):
    crews = []
    for i in timetable:
        h_ = int(i[:2])
        m_ = int(i[3:])
        crews.append((h_*60)+m_)
    crews.sort()
    
    crew_idx = 0
    
    for i in range(n-1):
        bus = 540 + i*t
        bus_idx = bisect_right(crews, bus)
        crew_idx = min(bus_idx, crew_idx+m)
        
    remain_crews = crews[crew_idx:]
    try:
        last_crew = remain_crews[m-1]
    except IndexError:
        return num_to_time(540 + (n-1)*t)
    
    if last_crew > 540 + (n-1)*t:
        return num_to_time(540 + (n-1)*t)
    else:
        return num_to_time(last_crew-1)