# 2138
n = int(input())
now = list(map(int,list(input())))
target = list(map(int,list(input())))

first_press = now[:]
first_press[0] = (first_press[0]+1)%2
first_press[1] = (first_press[1]+1)%2

first_not_press = now[:]

ans = 1e9
cnt = 1
for i in range(1,n):
    if first_press[i-1] != target[i-1]:
        cnt+=1
        first_press[i-1] = (first_press[i-1]+1)%2
        first_press[i] = (first_press[i]+1)%2
        if i != n-1:
            first_press[i+1] = (first_press[i+1]+1)%2

if first_press == target:
    ans = min(ans,cnt)

cnt = 0
for i in range(1,n):
    if first_not_press[i-1] != target[i-1]:
        cnt+=1
        first_not_press[i-1] = (first_not_press[i-1]+1)%2
        first_not_press[i] = (first_not_press[i]+1)%2
        if i != n-1:
            first_not_press[i+1] = (first_not_press[i+1]+1)%2

if first_not_press == target:
    ans = min(ans,cnt)

if ans == 1e9:
    print(-1)
else:
    print(ans)