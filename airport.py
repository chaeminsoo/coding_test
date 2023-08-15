# 10775
import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
gi = []
for _ in range(p):
    gi.append(int(input()))

parent = [i for i in range(g+1)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for i in gi:
    gate = find_parent(parent,i)
    if gate == 0:
        break
    ans += 1
    union_parent(parent,gate,gate-1)

print(ans)