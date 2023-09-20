# 19236
board = [[0]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int,input().split()))
    for j in [0,2,4,6]:
        board[i][j//2] = [data[j],data[j+1]]

dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

def fish_move(b):
    ref_board = [[bbb[:] for bbb in bb] for bb in b] 
    for fn in range(1,17):
        flag = False
        for i in range(4):
            for j in range(4):
                if ref_board[i][j][0] == fn:
                    while True:
                        nx = i + dx[ref_board[i][j][1]]
                        ny = j + dy[ref_board[i][j][1]]

                        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and ref_board[nx][ny][0] != -1:
                            ref_board[nx][ny], ref_board[i][j] = ref_board[i][j], ref_board[nx][ny]
                            flag = True
                            break
                        ref_board[i][j][1] = ref_board[i][j][1]+1 if ref_board[i][j][1] < 8 else 1
                if flag:
                    break
                    
            if flag:
                break

    return ref_board
                
def shark_move(shark,b):
    x,y = shark

    nxt_loc = []
    nx = x + dx[b[x][y][1]]
    ny = y + dy[b[x][y][1]]
    
    while True:
        if nx >=0 and nx < 4 and ny >=0 and ny < 4:
            if b[nx][ny][0] != 0:
                nxt_loc.append([nx,ny])
            nx += dx[b[x][y][1]]
            ny += dy[b[x][y][1]]
        else:
            if nxt_loc:
                return True,nxt_loc
            else:
                return False,nxt_loc

ans = 0
def dfs(shark,b,cnt):
    global ans

    mov_b = fish_move(b)
    check, nxt_shark = shark_move(shark,mov_b)
    if check:
        for ns in nxt_shark:
            mov_b[shark[0]][shark[1]][0] = 0
            ref = mov_b[ns[0]][ns[1]][0]
            mov_b[ns[0]][ns[1]][0] = -1
            dfs(ns,mov_b,cnt+ref)
            mov_b[shark[0]][shark[1]][0] = -1
            mov_b[ns[0]][ns[1]][0] = ref
    else:
        ans = max(ans,cnt)
        return

ref = board[0][0][0]
board[0][0][0] = -1
dfs([0,0],board,ref)

print(ans)