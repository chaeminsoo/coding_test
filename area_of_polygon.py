# 2166
n = int(input())

Xs = []
Ys = []
for _ in range(n):
    x,y = map(int,input().split())
    Xs.append(x)
    Ys.append(y)

Xs.append(Xs[0])
Ys.append(Ys[0])

rslt_1 = 0
rslt_2 = 0
for i in range(n):
    rslt_1 += Xs[i]*Ys[i+1]
    rslt_2 += Ys[i]*Xs[i+1]

print(round(abs((rslt_1-rslt_2)/2),1))