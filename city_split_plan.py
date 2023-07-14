# 1647
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
roads = []
for _ in range(m):
    a,b,c = map(int,input().split())
    roads.append([c,a-1,b-1])

roads.sort()

parent = [i for i in range(n)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
most_expensive = 0
for c,a,b in roads:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += c
        most_expensive = c

print(ans - most_expensive)