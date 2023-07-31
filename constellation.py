# 4386
n = int(input())
stars = []
for i in range(n):
    a,b = map(float,input().split())
    stars.append([a,b,i])

def how_far(a,b,x,y):
    return ((a-x)**2 + (b-y)**2)**0.5

graph = []
for i in range(n):
    from_star = stars[i]
    for j in range(i+1,n):
        to_star = stars[j]
        dist = how_far(from_star[0],from_star[1],to_star[0],to_star[1])
        graph.append([dist, from_star[2], to_star[2]])

graph.sort()

parent = [i for i in range(n)]

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

ans = 0
for d,f,t in graph:
    if find_parent(parent,f) != find_parent(parent,t):
        union_parent(parent,f,t)
        ans += d

print(ans)