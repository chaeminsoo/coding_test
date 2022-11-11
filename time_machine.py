# 11657
n,m = map(int,input().split())
edges = []
dist = [1e9]*(n+1) # 인덱스 편게 할려고

# 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def bf(st):
    global n,m
    dist[st] = 0  # 출발 노드
    # n번의 라운드를 반복
    for r in range(n):
        # 모든 간선을 확인
        for j in range(m):
            from_node = edges[j][0]
            to_node = edges[j][1]
            cost = edges[j][2]
            if dist[from_node] != 1e9 and dist[from_node] + cost < dist[to_node]:
                dist[to_node] = dist[from_node] + cost
                if r == n-1:
                    return True
    return False

n_cycle = bf(1)
if n_cycle:
    print(-1)
else:
    for i in range(2,n+1): # 1번노드 빼고 n까지
        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])