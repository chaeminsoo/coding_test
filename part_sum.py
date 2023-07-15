# 1806
n,s = map(int,input().split())
nums = list(map(int,input().split()))

ans = 1e9
st = 0
ed = 0
total = nums[st]
while st <= ed:
    if total < s:
        ed += 1
        if ed >= n:
            break
        total += nums[ed]
    else:
        ans = min(ans,ed-st+1)
        total -= nums[st]
        st+=1

if ans == 1e9:
    print(0)
else:
    print(ans)