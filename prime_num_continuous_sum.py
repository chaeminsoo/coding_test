# 1644
import math

n = int(input())
if n == 1:
    print(0)
    exit()

prime_num = [True]*(n+1)
nums = []

for i in range(2, int(math.sqrt(n))+1):
    if prime_num[i]:
        j = 2
        while i*j <= n:
            prime_num[i*j] = False
            j += 1

nums_len = 0
for i in range(2,n+1):
    if prime_num[i]:
        nums_len+=1
        nums.append(i)

ans = 0
st = 0
ed = 0

ref = nums[st]
while st <= ed:
    if ref < n:
        ed += 1
        if ed >= nums_len:
            break
        ref += nums[ed]
    elif ref == n:
        ans += 1
        ref -= nums[st]
        st += 1
        ed += 1
        if ed >= nums_len:
            break
        ref += nums[ed]
    else:
        ref -= nums[st]
        st += 1

print(ans)