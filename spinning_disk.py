# 17822
from collections import deque

n,m,t = map(int,input().split())
disk = []
for _ in range(n):
    d = deque(map(int,input().split()))
    disk.append(d)

orders = []
for _ in range(t):
    orders.append(list(map(int,input().split())))

def spin_disk(disk, x, d, k, n):
    new_disk = []
    for i in range(n):
        ref_disk = disk[i]
        if (i+1)%x == 0:
            if d == 0: # 시계방향
                for _ in range(k):
                    num = ref_disk.pop()
                    ref_disk.appendleft(num)
            else: # 반시계방향
                for _ in range(k):
                    num = ref_disk.popleft()
                    ref_disk.append(num)
        new_disk.append(ref_disk)
    return new_disk

def find_num(disk,n,m):
    remove_loc = set()
    for i in range(n):
        for j in range(m):
            if disk[i][j] != 0:
                near = []
                left = [i,j-1] if j != 0 else [i,m-1]
                near.append(left)
                right = [i,j+1] if j != m-1 else [i,0]
                near.append(right)
                if i != n-1:
                    up = [i+1,j]
                    near.append(up)
                if i != 0:
                    down = [i-1,j]
                    near.append(down)

                for x,y in near:
                    if disk[i][j] == disk[x][y]:
                        remove_loc.add((x,y))
                        remove_loc.add((i,j))

    if remove_loc:
        for x,y in remove_loc:
            disk[x][y] = 0
        return disk
    else:
        num_cnt = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if disk[i][j] != 0:
                    num_cnt+=1
                    cnt += disk[i][j]
        
        if num_cnt != 0:
            ref = cnt/num_cnt
        else:
            ref = 0

        for i in range(n):
            for j in range(m):
                if disk[i][j] != 0:
                    if disk[i][j] > ref:    
                        disk[i][j] -= 1
                    elif disk[i][j] < ref:
                        disk[i][j] += 1

        return disk

for x,d,k in orders:
    disk = spin_disk(disk,x,d,k,n)
    disk = find_num(disk,n,m)

ans = 0
for i in disk:
    ans += sum(i)

print(ans)