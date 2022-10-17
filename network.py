# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3#

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:
                union_parent(parent, i,j)
    roots = []
    for i in range(n):
            roots.append(find_parent(parent, i))
				
    return len(set(roots))