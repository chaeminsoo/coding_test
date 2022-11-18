# https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3
def solution(n, results):
    answer = 0
    records = [[0]*n for _ in range(n)]
    for a,b in results:
        records[a-1][b-1] = 1
        records[b-1][a-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i ==j or records[i][j] in [1,-1]:
                    continue

                if records[i][k] == records[k][j] == 1:
                    records[i][j] = 1
                    records[j][k] = records[k][i] = records[j][i] = -1

    for r in records:
        if r.count(0) ==1:
            answer+=1

    return answer