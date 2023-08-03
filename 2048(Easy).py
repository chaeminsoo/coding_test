# 12100
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def move(board,d,n):
    check = [[False]*n for _ in range(n)]

    if d == 0:
        for c in range(n):
            for r in range(1,n):
                if board[r][c] != 0:
                    now = board[r][c]
                    board[r][c] = 0
                    while r >= 0:
                        if r == 0:
                            board[r][c] = now
                            break
                        r -= 1
                        if board[r][c] != 0:
                            if board[r][c] == now and not check[r][c]:
                                board[r][c] = now*2
                                check[r][c] = True
                            else:
                                board[r+1][c] = now
                            break
    elif d == 1:
        for c in range(n):
            for r in range(n-2,-1,-1):
                if board[r][c] != 0:
                    now = board[r][c]
                    board[r][c] = 0
                    while r <= n-1:
                        if r == n-1:
                            board[r][c] = now
                            break
                        r += 1
                        if board[r][c] != 0:
                            if board[r][c] == now and not check[r][c]:
                                board[r][c] = now*2
                                check[r][c] = True
                            else:
                                board[r-1][c] = now
                            break
    elif d == 2:
        for r in range(n):
            for c in range(1,n):
                if board[r][c] != 0:
                    now = board[r][c]
                    board[r][c] = 0
                    while c >= 0:
                        if c == 0:
                            board[r][c] = now
                            break
                        c -= 1
                        if board[r][c] != 0:
                            if board[r][c] == now and not check[r][c]:
                                board[r][c] = now*2
                                check[r][c] = True
                            else:
                                board[r][c+1] = now
                            break
    if d == 3:
        for r in range(n):
            for c in range(n-2,-1,-1):
                if board[r][c] != 0:
                    now = board[r][c]
                    board[r][c] = 0
                    while c <= n-1:
                        if c == n-1:
                            board[r][c] = now
                            break
                        c += 1
                        if board[r][c] != 0:
                            if board[r][c] == now and not check[r][c]:
                                board[r][c] = now*2
                                check[r][c] = True
                            else:
                                board[r][c-1] = now
                            break

    return board

ans = 0
def dfs(board,step,n):
    global ans
    if step >= 5:
        for i in range(n):
            for j in range(n):
                ans = max(board[i][j],ans)
        return

    for d in range(4):
        dfs(move([i[:] for i in board],d,n),step+1,n)

dfs(board,0,n)
print(ans)