# https://school.programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    alpha ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    str1_dict = {}
    str2_dict = {}
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)):
        if i+1 >= len(str1):
            break
        if str1[i] in alpha and str1[i+1] in alpha:
            if str1[i:i+2] in str1_dict:
                str1_dict[str1[i:i+2]] +=1
            else:
                str1_dict[str1[i:i+2]] = 1
            
    for i in range(len(str2)):
        if i+1 >= len(str2):
            break
        if str2[i] in alpha and str2[i+1] in alpha:
            if str2[i:i+2] in str2_dict:
                str2_dict[str2[i:i+2]] +=1
            else:
                str2_dict[str2[i:i+2]] = 1
    
    str1_set = set(str1_dict.keys())
    str2_set = set(str2_dict.keys())
    
    inter = str1_set&str2_set
    uni = str1_set|str2_set
    
    if len(inter) == 0 and len(uni) == 0:
        return 65536
    else:
        inter_cnt = 0
        uni_cnt = 0
        for i in inter:
            inter_cnt += min(str1_dict[i], str2_dict[i])
        for i in uni:
            ref = []
            if i in str1_dict:
                ref.append(str1_dict[i])
            if i in str2_dict:
                ref.append(str2_dict[i])
                
            uni_cnt += max(ref)
        return int((inter_cnt/uni_cnt)*65536)