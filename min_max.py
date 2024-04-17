# 2357
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

min_tree = [0]*4*n
max_tree = [0]*4*n

def init_min(node, start, end):
    if start == end:
        min_tree[node] = nums[start]
        return min_tree[node]
    mid = (start+end)//2
    min_tree[node] = min(init_min(node*2, start, mid), init_min(node*2+1, mid+1, end))
    return min_tree[node]

def init_max(node, start, end):
    if start == end:
        max_tree[node] = nums[start]
        return max_tree[node]
    mid = (start+end)//2
    max_tree[node] = max(init_max(node*2, start, mid), init_max(node*2+1, mid+1, end))
    return max_tree[node]

def find_min(node, start, end, left, right):
    if left > end or right < start:
        return 1e9
    if left <= start and end <= right:
        return min_tree[node]
    mid = (start+end)//2
    return min(find_min(node*2, start, mid, left, right), find_min(node*2+1, mid+1, end, left, right))

def find_max(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    mid = (start+end)//2
    return max(find_max(node*2, start, mid, left, right), find_max(node*2+1, mid+1, end, left, right))

init_min(1, 0, n-1)
init_max(1, 0, n-1)

for _ in range(m):
    a,b = map(int, input().split())
    print(find_min(1, 0, n-1, a-1, b-1), find_max(1, 0, n-1, a-1, b-1))