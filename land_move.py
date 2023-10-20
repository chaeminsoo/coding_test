# https://school.programmers.co.kr/learn/courses/30/lessons/62050
def solution(land, height):
    n = len(land)
    parent = [i for i in range(n**2)]
    path = []
    
    def find_p(parent,x):
        if parent[x] != x:
            parent[x] = find_p(parent,parent[x])
        return parent[x]
    
    def union_p(parent,a,b):
        a = find_p(parent,a)
        b = find_p(parent,b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b            
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(n):
        for j in range(n):
            block_num = i*n + j
            
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                
                n_block_num = nx*n + ny
                
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if abs(land[i][j]-land[nx][ny]) <= height:
                        union_p(parent,block_num,n_block_num)
                    else:
                        path.append([abs(land[i][j]-land[nx][ny]),block_num,n_block_num])
                        
    path.sort()
    ans = 0
    for cost, b1, b2 in path:
        if find_p(parent,b1) != find_p(parent,b2):
            ans+=cost
            union_p(parent,b1,b2)
    return ans