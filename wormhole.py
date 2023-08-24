# 1865
tc = int(input())

def solution(n,m,edges):
    dist = [1e9]*n

    def bf(st,n,m):
        dist[st] = 0

        for r in range(n):
            for j in range(m):
                from_node = edges[j][0]
                to_node = edges[j][1]
                cost = edges[j][2]
                # if dist[from_node] != 1e9 and dist[from_node] + cost < dist[to_node]:
                if dist[from_node] + cost < dist[to_node]:
                    dist[to_node] = dist[from_node] + cost
                    if r == n-1:
                        return True
        return False
    
    return bf(0,n,m)

for _ in range(tc):
    n,m,w = map(int,input().split())
    edges = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges.append((a-1,b-1,c))
        edges.append((b-1,a-1,c))
    for _ in range(w):
        a,b,c = map(int,input().split())
        edges.append((a-1,b-1,-c))

    if solution(n,(2*m)+w,edges):
        print('YES')
    else:
        print('NO')