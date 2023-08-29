# 5639
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except EOFError:
        break

ans = []
def solution(tree):
    if len(tree) <= 1:
        for i in tree:
            ans.append(i)
        return
    
    root = tree[0]
    left = []
    right = []
    for i in tree[1:]:
        if i < root:
            left.append(i)
        else:
            right.append(i)
    solution(left)
    solution(right)
    ans.append(root)

solution(tree)
for i in ans:
    print(i)