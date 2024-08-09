n = int(input())
req = list(map(int,input().split()))
money = int(input())
if sum(req) <= money:
    print(max(req))
else:
    st = 1
    ed = money
    ans = 0
    while st <= ed:
        mid = (st+ed)//2
        rslt = 0
        r_max = 0
        for r in req:
            if r < mid:
                rslt += r
                r_max = max(r_max,r)
            else:
                r_max = max(r_max,mid)
                rslt += mid
        
        if rslt > money:
            ed = mid-1
        else:
            ans = max(ans,r_max)
            st =  mid+1
    
    print(ans)