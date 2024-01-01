# https://school.programmers.co.kr/learn/courses/30/lessons/43236
def solution(distance, rocks, n):
    rocks.sort()

    st = 0
    ed = distance
    ans = 0
    while st <= ed:
        mid = (st+ed)//2
        cnt = 0
        stnd_stone = 0
        # 출발점과 돌 사이, 돌과 돌 사이
        for i in rocks:
            if i-stnd_stone < mid:
                cnt+=1
            else:
                stnd_stone = i
        
        # 마지막 돌과 도착지 사이
        if distance-stnd_stone < mid:
            cnt+=1
                
        if cnt > n:
            ed = mid-1
        else:
            ans = max(ans,mid)
            st = mid+1
    
    return ans