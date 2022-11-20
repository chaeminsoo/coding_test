# 9625
k = int(input())
status = [1,0]
for _ in range(k):
    ref_a = 0
    ref_b = 0
    ref_b += status[0]
    ref_a += status[1]
    status = [ref_a, ref_b+status[1]]
for i in status:
    print(i, end=' ')