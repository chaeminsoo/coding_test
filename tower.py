# 2493
n = int(input())
towers = list(map(int,input().split()))
towers_loc = {}
for i in range(n):
    towers_loc[towers[i]] = i+1

stack = []
ans = []
for t in towers:
    if not stack:
        stack.append(t)
        ans.append(0)
    else:
        while stack:
            if stack[-1] > t:
                ans.append(towers_loc[stack[-1]])
                stack.append(t)
                break
            else:
                stack.pop()
        
        if not stack:
            ans.append(0)
            stack.append(t)

print(*ans)