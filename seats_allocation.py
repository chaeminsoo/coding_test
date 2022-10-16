# 10157
c, r = map(int, input().split())
k = int(input())

if k > (r*c):
    print(0)
else:
    cnt = 1
    board = [[0]*c for _ in range(r)]
    board[0][0] = 1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    loc = [0,0]
    d = 0

    while True:
        if cnt == k or cnt > (r*c):
            break
        x,y = loc
        board[x][y] = cnt
        
        nx = x + dx[d]
        ny = y + dy[d]

        if nx >= 0 and nx < r and ny >=0 and ny < c and board[nx][ny] == 0:
            loc = [nx, ny]
            cnt+=1
        else:
            d = (d+1)%4

    print(str(loc[1]+1) + ' ' + str(loc[0]+1))