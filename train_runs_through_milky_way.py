# 15787
n, m = map(int, input().split())
orders = []
for _ in range(m):
    orders.append(list(map(int, input().split())))

train = [[0]*20 for _ in range(n)]

for i in orders:
    if len(i) == 3:
        o, num, s = i
        num-=1
        s-=1
        if o == 1:
            train[num][s] = 1
        else:
            train[num][s] = 0
        
    else:
        o, num = i
        num-=1
        if o == 3:
            train[num] = [0] + train[num][:-1]
        else:
            train[num] = train[num][1:] + [0]
cnt = 0
trains = []
for i in train:
    if i in trains:
        continue
    else:
        cnt+=1
        trains.append(i)
print(cnt)