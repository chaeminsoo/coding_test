# 11505
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(m+k)]

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(node*2, start, mid)*init(node*2+1, mid+1, end)%1000000007
    return tree[node]

def update(node, start, end, index, val):
    if index < start or index > end:
        return tree[node]
    if start == end:
        tree[node] = val
        return tree[node]
    mid = (start+end)//2
    tree[node] = update(node*2, start, mid, index, val)*update(node*2+1, mid+1, end, index, val)%1000000007
    return tree[node]

def find(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return find(node*2, start, mid, left, right)*find(node*2+1, mid+1, end, left, right)%1000000007

tree = [0]*4*n
init(1, 0, n-1)

for a,b,c in orders:
    if a == 1:
        update(1, 0, n-1, b-1, c)
    else:
        print(find(1, 0, n-1, b-1, c-1))