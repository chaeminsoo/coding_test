# 1253
n = int(input())
nums = list(map(int,input().split()))
nums.sort()
ans = 0
for i in range(n):
    l = 0
    r = n-1
    while l < r:
        if l == i:
            l+=1
            continue
        if r == i:
            r -= 1
            continue

        if nums[i] == nums[l] + nums[r]:
            ans += 1
            break
        elif nums[i] > nums[l] + nums[r]:
            l += 1
        elif nums[i] < nums[l] + nums[r]:
            r -= 1

print(ans)