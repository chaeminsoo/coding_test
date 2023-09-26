# 21611
n,m = map(int,input().split())
N = n*n
n_ = n//2
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
bliz = []
for _ in range(m):
    bliz.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

board_num = [[0]*n for _ in range(n)]
board_line = [0]
x = n_
y = n_
d = 0
cnt = 1
flag = False
for i in range(1,n+2):
    for _ in range(2):
        for j in range(i):
            if x == 0 and y == 0:
                flag = True
                break
            x += dx[d]
            y += dy[d]
            board_num[x][y] = cnt
            cnt+=1
            board_line.append(board[x][y])

        if flag:
            break
        d = (d+1)%4

    if flag:
        break

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

ans_1 = 0
ans_2 = 0
ans_3 = 0


def plus_ans(num,n):
    global ans_1, ans_2, ans_3
    if num == 1:
        ans_1 += n
    elif num == 2:
        ans_2 += n
    elif num == 3:
        ans_3 += n

for d,s in bliz:
    x = n_
    y = n_

    # 블리자드
    for _ in range(s):
        x += dx[d]
        y += dy[d]
        if board_num[x][y] >= N:
            continue
        board_line[board_num[x][y]] = 0
        
    # 폭파
    flag = True
    while flag:
        flag = False
        cnt = 0
        num_idx = []
        prev = -1
        for i in range(1,N):
            if board_line[i] == 0:
                continue
            if board_line[i] != 0 and prev == -1:
                cnt+=1
                num_idx.append(i)
                prev = board_line[i]
                continue

            if board_line[i] == prev:
                num_idx.append(i)
                cnt+=1
            else:
                if cnt >= 4:
                    plus_ans(prev,cnt)
                    flag = True
                    while num_idx:
                        idx = num_idx.pop()
                        board_line[idx] = 0
                
                num_idx = [i]
                prev = board_line[i]
                cnt = 1
                
        if cnt >= 4:
            plus_ans(prev,cnt)
            flag = True
            while num_idx:
                idx = num_idx.pop()
                board_line[idx] = 0
        
        num_idx = [board_line[i]]
        prev = board_line[i]
        cnt = 1

        if not flag:
            break
    
    # 땡기기
    new_line = [0]
    znt = 0
    for i in range(1,N):
        if board_line[i]:
            new_line.append(board_line[i])
        else:
            znt+=1
    new_line += [0]*znt
    if new_line[1] == 0:
        break
    
    # print(new_line)

    # 변환
    ref = [0]
    ref_len = 1
    num = new_line[1]
    cnt = 0
    for i in range(1,N):
        if new_line[i] == 0:
            break
        if new_line[i] == num:
            cnt+=1
        else:
            ref.append(cnt)
            ref.append(num)
            ref_len += 2
            if ref_len > N:
                break
            num = new_line[i]
            cnt = 1
    if cnt:
        ref.append(cnt)
        ref.append(num)
        ref_len += 2
    
    if ref_len > N:
        for _ in range(ref_len-N):
            ref.pop()
        board_line = ref
    elif ref_len == N:
        board_line = ref
    else:
        board_line = ref + [0]*(N-ref_len)
    
print(ans_1 + ans_2*2 + ans_3*3)