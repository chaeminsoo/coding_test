# https://school.programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    ans = [0,0]
    n = len(arr)
    step = n
    visited = [[False]*n for _ in range(n)]
    
    while step > 0:
        for i in range(0,n,step):
            for j in range(0,n,step):
                if visited[i][j]:
                    continue
                    
                stnd = arr[i][j]
                flag = True
                for x in range(step):
                    for y in range(step):
                        if arr[i+x][j+y] != stnd:
                            flag = False
                            break
                    if not flag:
                        break

                if flag:
                    for x in range(step):
                        for y in range(step):
                            visited[i+x][j+y] = True
                    if arr[i][j]:
                        ans[1]+=1
                    else:
                        ans[0]+=1
        
        step //= 2
    
    return ans
