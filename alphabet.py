# 1987
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
board = []
for _ in range(r):
    board.append(list(input()))

passed = set(board[0][0])

dr = [-1,1,0,0]
dc = [0,0,-1,1]
ans = 0
def dfs(r,c,n,m,cnt):
    global ans
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if nr >= 0 and nr < n and nc >= 0 and nc < m and board[nr][nc] not in passed:
            passed.add(board[nr][nc])
            dfs(nr,nc,n,m,cnt+1)
            passed.remove(board[nr][nc])
        else:
            ans = max(ans,cnt)

dfs(0,0,r,c,1)
print(ans)