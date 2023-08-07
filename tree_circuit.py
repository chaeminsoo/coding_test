# 2263
import sys
sys.setrecursionlimit(10**7)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

preorder = []

inorder_idx = {}
for i,j in enumerate(inorder):
    inorder_idx[j] = i

def dfs(in_st_idx,in_ed_idx,post_st_idx,post_ed_idx):
    if (in_st_idx > in_ed_idx) or (post_st_idx > post_ed_idx):
        return
    
    root = postorder[post_ed_idx]
    preorder.append(root)

    left_num = inorder_idx[root] - in_st_idx
    right_num = in_ed_idx - inorder_idx[root]
    dfs(in_st_idx,in_st_idx+left_num-1,post_st_idx,post_st_idx+left_num-1)
    dfs(in_ed_idx-right_num+1,in_ed_idx,post_ed_idx-right_num,post_ed_idx-1)

dfs(0,n-1,0,n-1)
print(*preorder)