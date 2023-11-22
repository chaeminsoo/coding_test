# https://school.programmers.co.kr/learn/courses/30/lessons/64063
import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    ans = []
    booked = set()
    nxt_room = {}
    
    def find_nxt_room(x):
        if x in nxt_room:
            if nxt_room[x] in booked:
                nxt_room[x] = find_nxt_room(nxt_room[x])
            return nxt_room[x]
        else:
            nxt_room[x] = x+1
            return nxt_room[x]
    
    for i in room_number:
        if i not in booked:
            ans.append(i)
            booked.add(i)
            find_nxt_room(i)
        else:
            nr = find_nxt_room(i)
            ans.append(nr)
            booked.add(nr)
            find_nxt_room(nr)
            
    return ans