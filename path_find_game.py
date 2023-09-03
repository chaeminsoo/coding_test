# 2019 KAKAO BLIND RECRUITMENT 길 찾기 게임
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    nodes = []
    node_s_x = {}
    for i,j in enumerate(nodeinfo):
        nodes.append([j[0],j[1],i+1])
        node_s_x[i+1] = j[0]
        
        
    nodes.sort(key = lambda x:(-x[1],x[0]))
    tree = {}
    tree[nodes[0][2]] = [0,0]
    
    def tree_insert(x,node):
        if node_s_x[x] < node_s_x[node]:
            if tree[node][0]:
                tree_insert(x,tree[node][0])
            else:
                tree[node][0] = x
                tree[x] = [0,0]
        else:
            if tree[node][1]:
                tree_insert(x,tree[node][1])
            else:
                tree[node][1] = x
                tree[x] = [0,0]
    
    for i in nodes[1:]:
        tree_insert(i[2],nodes[0][2])
    
    pre_ = []
    def preorder(node):
        if node == 0:
            return
        pre_.append(node)
        l,r = tree[node]
        preorder(l)
        preorder(r)
    
    post_ = []
    def postorder(node):
        if node == 0:
            return
        l,r = tree[node]
        postorder(l)
        postorder(r)
        post_.append(node)
    
    preorder(nodes[0][2])
    postorder(nodes[0][2])
    
    return [pre_, post_]