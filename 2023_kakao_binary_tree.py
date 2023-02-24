# 2023 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/150367
import math 
import math 

def checking(bin_num):
    global rslt
    if len(bin_num) != 1:
        root = bin_num[len(bin_num)//2]
        left = bin_num[:len(bin_num)//2]
        right = bin_num[(len(bin_num)//2)+1:]
        
        if root == '0':
            if left[len(left)//2] == '0' and right[len(right)//2] == '0':     
            # if all(child=='0' for child in bin_num):      
                pass
            else:
                rslt = False            
                return 
        
        checking(left)
        checking(right)
            
def make_tree(bn):
    l_bn = len(bn)
    h = math.ceil(math.log2(l_bn+1))
    tree_len = (2**h)-1
    return '0'*(tree_len-l_bn) + bn
    
def solution(numbers):
    global rslt
    answer = []
    for n in numbers:
        rslt = True
        bin_num = bin(n)[2:]
        
        bin_num = make_tree(bin_num)
        rslt = True
        checking(bin_num)
        if rslt:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

print(solution([4]))