# 9328
from collections import deque

def solution(n, m, board, keys, out_doors, visited):
    ans = 0
    doors = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    key_check = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    key_changed = True

    door_stop_point = {}

    for o in out_doors:
        if board[o[0]][o[1]] in doors:
            if board[o[0]][o[1]].lower() not in keys:
                if board[o[0]][o[1]] in door_stop_point:
                    door_stop_point[board[o[0]][o[1]]].add((o[0],o[1]))
                else:
                    door_stop_point[board[o[0]][o[1]]] = {(o[0],o[1])}
                visited[o[0]][o[1]] = True
                continue

        if board[o[0]][o[1]] in key_check:
            keys.add(board[o[0]][o[1]])

        if board[o[0]][o[1]] == '$':
            ans += 1
        visited[o[0]][o[1]] = True
        q.append([o[0], o[1]])

    while key_changed:
        key_changed = False
        for k in keys:
            if k.upper() in door_stop_point:
                while door_stop_point[k.upper()]:
                    od = door_stop_point[k.upper()].pop()
                    q.append([od[0],od[1]])

        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and board[nx][ny] != '*':
                    if board[nx][ny] in doors:
                        if board[nx][ny].lower() in keys:
                            q.append([nx,ny])
                        else:
                            if board[nx][ny] in door_stop_point:
                                door_stop_point[board[nx][ny]].add((nx,ny))
                            else:
                                door_stop_point[board[nx][ny]] = {(nx,ny)}

                        visited[nx][ny] = True
                        continue

                    if board[nx][ny] == '$':
                        ans += 1

                    if board[nx][ny] in key_check:
                        key_changed = True
                        keys.add(board[nx][ny])

                    visited[nx][ny] = True
                    q.append([nx,ny])
    
    return ans

t = int(input())
for _ in range(t):
    h,w = map(int,input().split())
    visited = [[False]*w for _ in range(h)]
    board = []
    out_doors = deque()
    for i in range(h):
        data = list(input())
        if i == 0 or i == h-1:
            for j in range(w):
                if data[j] != '*':
                    out_doors.append([i,j])
        else:
            if data[0] != '*':
                out_doors.append([i,0])
            if data[w-1] != '*':
                out_doors.append([i,w-1])

        board.append(data)
    keys = input()
    if keys == '0':
        keys = set()
    else:
        keys = set(keys)

    print(solution(h,w, board, keys, out_doors, visited))