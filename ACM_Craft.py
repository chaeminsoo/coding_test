# 1005
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def solution(n,b_time,graph,degree,w):
    pre_need_time = [0]*n
    q = deque()
    for i, j in enumerate(degree):
        if j == 0:
            q.append(i)

    while q:
        idx = q.popleft()
        for nxt_idx in graph[idx]:
            pre_need_time[nxt_idx] = max(pre_need_time[nxt_idx], b_time[idx]+pre_need_time[idx])
            degree[nxt_idx] -= 1
            if degree[nxt_idx] == 0:
                q.append(nxt_idx)

    return pre_need_time[w] + b_time[w]

for _ in range(t):
    n, k = map(int,input().split())
    b_time = list(map(int,input().split()))
    degree = [0]*n
    graph = [[] for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x-1].append(y-1)
        degree[y-1] += 1
    w = int(input())
    print(solution(n,b_time,graph,degree,w-1))