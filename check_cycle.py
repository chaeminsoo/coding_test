def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

nodes, edge = map(int,input().split())
parent= [0]*(nodes+1)

for i in range(1,nodes+1):
    parent[i]=i

cycle =False

for i in range(edge):
    a,b =map(int,input().split())

    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break

    else:
        union_parent(parent,a,b)
    
if cycle:
    print('A cycle has occurred')
else:
    print('No cycle has occured')