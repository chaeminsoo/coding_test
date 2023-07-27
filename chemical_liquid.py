# 2467
n = int(input())
liquid = list(map(int,input().split()))

left = 0
right = n-1

status = float('inf')
ans = [0,n-1]
while left < right:
    if liquid[left] + liquid[right] == 0:
        ans = [left, right]
        break
    elif liquid[left] + liquid[right] > 0:
        if abs(status) > abs(liquid[left] + liquid[right]):
            status = liquid[left] + liquid[right]
            ans = [left, right]
        right -= 1
    elif liquid[left] + liquid[right] < 0:
        if abs(status) > abs(liquid[left] + liquid[right]):
            status = liquid[left] + liquid[right]
            ans = [left, right]
        left += 1

print(liquid[ans[0]], liquid[ans[1]])