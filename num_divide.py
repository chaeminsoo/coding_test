# 27172
n = int(input())
player_card = list(map(int,input().split()))

max_num = max(player_card)
does_this_num_exist = [-1]*(max_num+1)

for i in range(n):
    does_this_num_exist[player_card[i]] = i

ans = [0]*n
for idx in range(n):
    now_card = player_card[idx]
    mnt = 2
    cnt = 0
    check_card = now_card * mnt
    while check_card <= max_num:
        if does_this_num_exist[check_card] != -1:
            ans[idx] += 1
            ans[does_this_num_exist[check_card]] -= 1
        mnt += 1
        check_card = now_card * mnt

print(*ans)