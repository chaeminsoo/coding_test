# 13144
n = int(input())
nums = list(map(int,input().split()))

st = 0
ed = 0
used_num = set()

ans = 0
while st<=ed:
    if ed >= n:
        ed = n-1
        ref = ed-st+1
        ans += (ref+1)*ref//2
        break

    if nums[ed] not in used_num:
        used_num.add(nums[ed])
        ed+=1
    else:
        ref = ed-st
        ans += ref
        used_num.remove(nums[st])
        st+=1

print(ans)