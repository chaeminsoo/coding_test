# 1863
n = int(input())
ans = 0
stack = []
for _ in range(n):
    a,b = map(int,input().split())
    if not stack:
        stack.append(b)
        continue

    if b > stack[-1]:
        stack.append(b)
    else:
        ref_1 = set()
        while stack[-1] > b:
            ref_2 = stack.pop()
            ref_1.add(ref_2)
            if not stack:
                break
        stack.append(b)
        ans+=len(ref_1)

ans += len(set(stack)-{0})
print(ans)