def solution(words):
    global ans
    tree = {'head':{'child':{},'num':0,'end':False}}
    words_set = set(words)
    
    def tree_add(w):
        now_loc = 'head'
        ref_tree = tree
        for i in w:
            if i in ref_tree[now_loc]['child']:
                ref_tree[now_loc]['num']+=1
                ref_tree = ref_tree[now_loc]['child']
                now_loc = i
            else:
                ref_tree[now_loc]['child'][i] = {'child':{},'num':0,'end':False}
                ref_tree[now_loc]['num']+=1
                ref_tree = ref_tree[now_loc]['child']
                now_loc = i
        ref_tree[now_loc]['end'] = True
    
    ans = 0
    for w in words:
        tree_add(w)
        
    ans = 0
    def dfs(t,node,cnt):
        global ans
        if t[node]['end'] == True:
            ans += cnt
        elif t[node]['num'] <= 1:
            ans += cnt
            return
        
        for i in t[node]['child']:
            dfs(t[node]['child'],i,cnt+1)
        
    dfs(tree,'head',0)
    return ans