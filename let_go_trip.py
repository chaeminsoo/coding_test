# 1976
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


n = int(input())
parent = [i for i in range(n)]
m = int(input())
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j]:
            union_parent(parent,i,j)

plan = list(map(int,input().split()))

now = 0
ans = True
for nxt in range(1,m):
    if find_parent(parent,plan[now]-1) == find_parent(parent,plan[nxt]-1):
        now = nxt
    else:
        ans = False
        break

if ans:
    print('YES')
else:
    print('NO')