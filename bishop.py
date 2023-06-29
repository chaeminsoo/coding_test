# 1799
n = int(input())

board = []
cant = set()
for i in range(n):
    data = list(map(int,input().split()))
    board.append(data)
    for j in range(n):
        if data[j] == 0:
            cant.add((i,j))

def find_cant(x,y,n):
    rslt = set()
    dx = [-1,-1,1,1]
    dy = [-1,1,1,-1]

    for i in range(4):
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx >= 0 and nx < n and ny >=0 and ny < n:
                rslt.add((nx,ny))
            else:
                break
    
    return rslt

def nxt_loc(x,y,n, line_status):
    if y+2 <= n-1:
        return [x,y+2, False]
    if line_status:
        return [x+1,1, True]
    else:
        return [x+1,0, True]

ans = 0
rslt = 0
def dfs(now_loc, cant_loc, cnt, n, line_status):
    global rslt
    x,y = now_loc
    
    if [x,y] == [n-1,n-1] or [x,y] == [n-1,n-2]:
        if (x,y) in cant_loc:
            rslt = max(rslt, cnt)
            return
        else:
            rslt = max(rslt, cnt+1)
            return

    nxt_x, nxt_y, line_status_changed = nxt_loc(x,y,n, line_status)

    if line_status_changed:
        line_status = not line_status

    if board[x][y] == 1 and (x,y) not in cant_loc:
        new_cant_loc = find_cant(x,y,n)
        dfs([nxt_x, nxt_y], cant_loc|new_cant_loc, cnt+1,n, line_status)
        
    dfs([nxt_x, nxt_y], cant_loc, cnt,n, line_status)

dfs([0,0],cant,0,n,True)
ans += rslt
rslt = 0
dfs([0,1],cant,0,n,False)
print(ans+rslt)