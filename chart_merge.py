# 2023 KAKAO BLIND RECRUITMENT 표 병합
def find_num_loc(r,c):
    return int(c) + (50*(int(r)-1))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(commands):
    ans = []
    parent = [i for i in range(2610)]
    values = ['']*2610
    
    for c in commands:
        c = c.split()
        if c[0] == 'UPDATE' and len(c) == 4:
            loc = find_num_loc(c[1],c[2])
            p = find_parent(parent,loc)
            for i in range(2610):
                if find_parent(parent,i) == p:
                    values[i] = c[3]
                    
        elif c[0] == 'UPDATE' and len(c) == 3:
            for i in range(2610):
                if values[i] == c[1]:
                    values[i] = c[2]
                    
        elif c[0] == 'MERGE':
            loc_1 = find_num_loc(c[1],c[2])
            p_1 = find_parent(parent,loc_1)
            v_1 = values[p_1]
            loc_2 = find_num_loc(c[3],c[4])
            p_2 = find_parent(parent,loc_2)
            v_2 = values[p_2]
            if p_1 == p_2:
                continue
            
            union_parent(parent,loc_1,loc_2)
            p = find_parent(parent,loc_1)
            if v_1 == '' and v_2 != '':
                for i in range(2610):
                    if find_parent(parent,i) == p:
                        values[i] = v_2
            else:
                for i in range(2610):
                    if find_parent(parent,i) == p:
                        values[i] = v_1        
                
            
        elif c[0] == 'UNMERGE':
            loc = find_num_loc(c[1],c[2])
            p = find_parent(parent,loc)
            v_1 = values[p]
            for i in range(2610):
                if find_parent(parent,i) == p:
                    parent[i] = i
                    values[i] = ''
            values[loc] = v_1
            
            
        else:
            loc = find_num_loc(c[1],c[2])
            real_loc = find_parent(parent,loc)
            if values[loc] == '':
                ans.append('EMPTY')
            else:
                ans.append(values[loc])
        
    return ans