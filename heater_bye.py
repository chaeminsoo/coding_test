# 23289
from collections import deque

r,c,k = map(int,input().split())
board = []
heater_loc = []
check_loc = []
for i in range(r):
    data = list(map(int,input().split()))
    for j in range(c):
        if data[j] == 5:
            check_loc.append([i,j])
        if data[j] in {1,2,3,4}:
            heater_loc.append([i,j,data[j]])

tmp_board = [[0]*c for _ in range(r)]

w = int(input())
walls = set()
for _ in range(w):
    wx,wy,wd = map(int,input().split())
    walls.add((wx-1,wy-1,wd))

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

def nxt_heat(x,y,d):
    nxt = []
    if d == 1:
        drx = [-1,0,1]
        dry = [1,1,1]
        for i in range(3):
            nx = x + drx[i]
            ny = y + dry[i]
            if i == 0 and (x,y,0) not in walls and (x-1,y,1) not in walls:
                nxt.append([nx,ny])
            elif i == 1 and (x,y,1) not in walls:
                nxt.append([nx,ny])
            elif i == 2 and (x+1,y,0) not in walls and (x+1,y,1) not in walls:
                nxt.append([nx,ny])
    elif d== 2:
        dlx = [-1,0,1]
        dly = [-1,-1,-1]
        for i in range(3):
            nx = x + dlx[i]
            ny = y + dly[i]
            if i == 0 and (x,y,0) not in walls and (x-1,y-1,1) not in walls:
                nxt.append([nx,ny])
            elif i == 1 and (x,y-1,1) not in walls:
                nxt.append([nx,ny])
            elif i == 2 and (x+1,y,0) not in walls and (x+1,y-1,1) not in walls:
                nxt.append([nx,ny])
            
    elif d == 3:
        dux = [-1,-1,-1]
        duy = [-1,0,1]
        for i in range(3):
            nx = x + dux[i]
            ny = y + duy[i]
            if i == 0 and (x,y-1,1) not in walls and (x,y-1,0) not in walls:
                nxt.append([nx,ny])
            elif i == 1 and (x,y,0) not in walls:
                nxt.append([nx,ny])
            elif i == 2 and (x,y+1,0) not in walls and (x,y,1) not in walls:
                nxt.append([nx,ny])
            
    elif d == 4:
        ddx = [1,1,1]
        ddy = [-1,0,1]
        for i in range(3):
            nx = x + ddx[i]
            ny = y + ddy[i]
            if i == 0 and (x,y-1,1) not in walls and (x+1,y-1,0) not in walls:
                nxt.append([nx,ny])
            elif i == 1 and (x+1,y,0) not in walls:
                nxt.append([nx,ny])
            elif i == 2 and (x,y,1) not in walls and (x+1,y+1,0) not in walls:
                nxt.append([nx,ny])
            
    return nxt

def heat(r,c):
    for x,y,d in heater_loc:
        heat_loc = set()
        q = deque()
        q.append([x+dx[d],y+dy[d],5])
        while q:
            i,j,v = q.popleft()
            tmp_board[i][j] += v
            heat_loc.add((i,j))
            nxt = nxt_heat(i,j,d)
            for ni,nj in nxt:
                if ni >= 0 and ni < r and nj >= 0 and nj < c and (ni,nj) not in heat_loc and v > 1:
                    heat_loc.add((ni,nj))
                    q.append([ni,nj,v-1])        

def manage_heat(r,c):
    ref_board = [[0]*c for _ in range(r)]
    visited = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            visited[i][j] = True
            for d in range(1,5):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx >= 0 and nx < r and ny >= 0 and ny < c and not visited[nx][ny]:
                    if d == 1 and (i,j,1) in walls:
                        continue
                    elif d == 2 and (i,j-1,1) in walls:
                        continue
                    elif d == 3 and (i,j,0) in walls:
                        continue
                    elif d == 4 and (i+1,j,0) in walls:
                        continue

                    ref = int((tmp_board[i][j] - tmp_board[nx][ny])/4)
                    ref_board[i][j] -= ref
                    ref_board[nx][ny] += ref
    
    for i in range(r):
        for j in range(c):
            tmp_board[i][j] += ref_board[i][j]
            
def check(k):
    for i,j in check_loc:
        if tmp_board[i][j] < k:
            return False
    return True

ans = 0
while ans < 101:
    heat(r,c)
    manage_heat(r,c)
    # 테두리
    for i in range(r):
        for j in [0,c-1]:
            if tmp_board[i][j] > 0:
                tmp_board[i][j] -= 1
    for j in range(1,c-1):
        for i in [0,r-1]:
            if tmp_board[i][j] > 0:
                tmp_board[i][j] -= 1
    # 초코 +1
    ans += 1
    if check(k):
        break

print(ans)