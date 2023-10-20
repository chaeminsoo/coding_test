def solution(cookie):
    N = len(cookie)
    half_cookie = sum(cookie)/2
    tree = [0]*(N+1)
    
    def update(i,num):
        while i <= N:
            tree[i] += num
            i += (i&-i)
    
    def prefix_sum_0(i):
        rslt = 0
        while i > 0:
            rslt += tree[i]
            i-=(i&-i)
        return rslt
    
    def prefix_sum(a,b):
        a = prefix_sum_0(a-1)
        b = prefix_sum_0(b)
        return b-a
    
    for i in range(N):
        update(i+1,cookie[i])
    
    ans = 0
    for stnd in range(1,N):
        st = 1
        ed = N
        left = prefix_sum(st,stnd)
        right = prefix_sum(stnd+1,ed)
        while st <= stnd and ed >stnd:
            if left == right:
                ans = max(ans,left)
                break
            elif left > right:
                left-=cookie[st-1]
                st+=1
            elif left < right:
                right-=cookie[ed-1]
                ed-=1
    return ans