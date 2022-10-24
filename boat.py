# 1092
import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int,input().split()))
m = int(input())
boxs = list(map(int,input().split()))

crane.sort(reverse=True)
boxs.sort(reverse=True)
if boxs[0] > crane[0]:
    print(-1)
else:
    ans = 0
    while boxs:
        for c in crane:
            for idx, b in enumerate(boxs):
                if c >= b:
                    del boxs[idx]
                    break
        ans += 1
    print(ans)