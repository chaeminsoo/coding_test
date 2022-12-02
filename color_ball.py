# 10800
import sys
input = sys.stdin.readline

n = int(input())
ball = []
ans = [0]*n
color_sum = {}
size_sum = {}
color_size_sum = {}
for i in range(n):
    a,b = map(int,input().split())
    color_sum[a] = 0
    size_sum[b] = 0
    color_size_sum[(a,b)] = 0
    ball.append([i,a,b])

ball.sort(key= lambda x: (x[2], x[1]))
until_now_sum = 0

for b in ball:
    num, col, siz = b
    ans[num] += until_now_sum - color_sum[col] - size_sum[siz] + color_size_sum[(col,siz)]
    until_now_sum += siz
    color_sum[col] += siz
    size_sum[siz] += siz
    color_size_sum[(col,siz)] += siz
    
for i in ans:
    print(i)