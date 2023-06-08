# 17472
from collections import deque

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

lands = {}

visited = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,num):
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    board[x][y] = num
    rslt = []

    while q:
        r,c = q.popleft()
        rslt.append([r,c])
        
        for i in range(4):
            nx = r +dx[i]
            ny = c +dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = num
                q.append([nx,ny])
    
    return rslt

def make_bridge(x,y,d):
    s = board[x][y]
    cnt = 0
    while True:
        x += dx[d]
        y += dy[d]
        cnt += 1

        if x >= 0 and x < n and y >=0 and y < m:
            if board[x][y] == s:
                return [s,-1,-1]
            if board[x][y] != 0 and cnt < 3:
                return [s,-1,-1]
            if board[x][y] != 0 and cnt >= 3:
                return [s,board[x][y],cnt-1]
        else:
            return [s,-1,-1]

def find_parent(parent, x):   # 노드의 부를 찾아주는 함수
    if parent[x] != x:     # 부모가 자기 자신이 아니면 
        return find_parent(parent, parent[x])  # 가장 꼭대기에 있는 부모까지 찾아감
    return x

def union_parent(parent, a, b):   # 부모를 같게 해는 함수 (숫자가 더  작은 부모 통합) == 2개가 서로 연결
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

land_cnt = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            lands[land_cnt] = bfs(i,j,land_cnt)
            land_cnt+=1

bridge = []
for l in range(1,land_cnt):
    for r,c in lands[l]:
        for d in range(4):
            st,ed,cost = make_bridge(r,c,d)
            if ed != -1:
                bridge.append([cost,st,ed])

bridge.sort()

ans = 0
parent = [i for i in range(land_cnt)]
for c,a,b in bridge:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += c

roots = []
for i in range(1,land_cnt):
    roots.append(find_parent(parent,i))

if len(set(roots)) == 1:
    print(ans)
else:
    print(-1)