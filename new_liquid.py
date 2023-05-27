# 2473
import sys

n = int(sys.stdin.readline())
liq = list(map(int,sys.stdin.readline().split()))

liq.sort()

ans = [liq[0],liq[1],liq[2]]
stand_sum = abs(sum(ans))
for i in range(n-2):
    st = i+1
    ed = n-1

    while st != ed:
        now_sum = liq[i] + liq[st] + liq[ed]
        if stand_sum > abs(now_sum):
            ans = [liq[i], liq[st], liq[ed]]
            stand_sum = abs(now_sum)

        if now_sum >= 0:
            ed-=1
        else:
            st+=1

print(*ans)