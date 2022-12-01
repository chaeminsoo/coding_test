# 1507
n = int(input())
roads = []
check = [[1]*n for _ in range(n)]
ans = 0
for _ in range(n):
    roads.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or j == k:
                continue
            if roads[i][j] == roads[i][k] + roads[k][j]:
                check[i][j] = 0
            elif roads[i][j] > roads[i][k] + roads[k][j]:
                ans = -1

if ans == -1:
    print(ans)
else:
    for i in range(n):
        for j in range(n):
            if check[i][j] == 1:
                ans += roads[i][j]
    print(ans//2) # 양방향 도로