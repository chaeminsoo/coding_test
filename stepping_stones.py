def solution(stones, k):
    st,ed = min(stones), max(stones)
    mid = (st+ed)//2
    ans = 0
    while st <= ed:
        ref = 0
        for s in stones:
            if s < mid:
                ref += 1
            else:
                ref = 0
                
            if ref >= k:
                break
        
        if ref >= k:
            ed = mid-1
            mid = (st+ed)//2
        else:
            ans = max(ans,mid)
            st = mid +1
            mid = (st+ed)//2
            
    return  ans