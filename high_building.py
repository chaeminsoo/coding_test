# 1027
n = int(input())
buildings = list(map(int,input().split()))

gradi = [[0]*n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        gradi[i][j] = (buildings[i]-buildings[j])/(i-j)

left_see = [0]*n
right_see = [0]*n

for i in range(n):
    now_max = -1e9
    cnt = 0
    for j in range(i+1,n):
        if now_max < gradi[i][j]:
            cnt+=1
            now_max = gradi[i][j]
    right_see[i] = cnt
    
    now_min = 1e9
    cnt = 0
    for j in range(i-1,-1,-1):
        if now_min > gradi[i][j]:
            cnt+=1
            now_min = gradi[i][j]
    left_see[i] = cnt

ans = 0
for i in range(n):
    ans = max(ans,left_see[i]+right_see[i])
print(ans)