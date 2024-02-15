# 9935
s = input()
target = list(input())
l_t = len(target)

cursor = 0
ans = []

for i in s:
    ans.append(i)
    while ans[-l_t:] == target and len(ans) >= l_t:
        for _ in range(l_t):
            ans.pop()

if ans:
    print(''.join(ans))
else:
    print('FRULA')