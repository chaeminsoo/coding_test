# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3#

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

def solution(n, computers):
    parent = [i for i in range(n)]    # 처음 부모는 자기 자신으로 초기화
    for i in range(n):  
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:   # 돌아다니면서 연결되 있으면 
                union_parent(parent, i,j)  # 둘이 연결 -> 부모 통합

    roots = []
    for i in range(n):
        roots.append(find_parent(parent, i))   # parent에서 각 노드가 root 노드를 가리키지 않는 반례가 있어서 이렇게 해줌
				
    return len(set(roots))