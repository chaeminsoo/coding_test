# 1197
v, e = map(int,input().split())
graph = [[] for _ in range(v)]
edges = []
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])
    edges.append([c,a-1,b-1])

edges.sort()

def find_parent(parent,a):
    if parent[a] != a:
        return find_parent(parent,parent[a])
    return a

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(v)]

ans = 0
for c,a,b in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += c

print(ans)