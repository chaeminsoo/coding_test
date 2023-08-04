# 13460
n,m = map(int,input().split())
board =[]
for i in range(n):
    data = list(input())
    for j in range(m):
        if data[j] == 'O':
            exit_ = [i,j]
        if data[j] == 'R':
            red = [i,j]
        if data[j] == 'B':
            blue = [i,j]
    board.append(data)

def move(rr,rc,br,bc,d):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    rnt = 0
    bnt = 0

    red_goal = False
    blue_goal = False

    while True:
        rr += dr[d]
        rc += dc[d]
        rnt += 1
        if board[rr][rc] == '#':
            rr -= dr[d]
            rc -= dc[d]
            break
        elif board[rr][rc] == 'O':
            red_goal = True
            break

    while True:
        br += dr[d]
        bc += dc[d]
        bnt += 1
        if board[br][bc] == '#':
            br -= dr[d]
            bc -= dc[d]
            break
        elif board[br][bc] == 'O':
            blue_goal = True
            break
    
    if blue_goal:
        return -1,rr,rc,br,bc
    
    if red_goal:
        return 1,rr,rc,br,bc
    
    if rr == br and rc == bc:
        if rnt > bnt:
            rr -= dr[d]
            rc -= dc[d]
        else:
            br -= dr[d]
            bc -= dc[d]
    
    return 0,rr,rc,br,bc

ans = 1e9
def dfs(board,rr,rc,br,bc,step):
    global ans
    if step >= 10:
        return
    
    for i in range(4):
        status, nrr,nrc, nbr,nbc = move(rr,rc,br,bc,i)
        if status == -1:
            continue
        elif status == 0:
            dfs(board,nrr,nrc,nbr,nbc,step+1)
        elif status == 1:
            ans = min(ans,step+1)
            return
        
board[red[0]][red[1]] = '.'
board[blue[0]][blue[1]] = '.'

dfs(board,red[0],red[1],blue[0],blue[1],0)
if ans == 1e9:
    print(-1)
else:
    print(ans)