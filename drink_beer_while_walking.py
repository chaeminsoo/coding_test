# 9205
import sys
input = sys.stdin.readline

t = int(input())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(t):
    n = int(input())
    node = []
    loc = list(map(int,input().split()))
    node.append([0,loc])
    for i in range(1,n+1):
        loc = list(map(int,input().split()))
        node.append([i,loc])

    loc = list(map(int,input().split()))
    node.append([n+1,loc])

    parent = [i for i in range(n+2)]

    for i in range(len(node)):
        for j in range(i,len(node)):
            dist = abs(node[i][1][0] - node[j][1][0]) + abs(node[i][1][1] - node[j][1][1])
            if dist > 1000:
                continue

            union_parent(parent,i,j)
    
    if find_parent(parent,0) == find_parent(parent,n+1):
        print('happy')
    else:
        print('sad')