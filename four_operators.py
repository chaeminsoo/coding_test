# https://school.programmers.co.kr/learn/courses/30/lessons/1843?language=python3

# 여기 참고 : https://www.ai-bio.info/programmers/1843
def solution(arr):
    nums = []
    ops = []
    for i in arr:
        if i in {'+','-'}:
            ops.append(i)
        else:
            nums.append(int(i))
    
    # 최대, 최소
    M = {}
    m = {}
    # 자기자신
    for i in range(len(nums)):
        M[(i,i)] = nums[i]
        m[(i,i)] = nums[i]
    
    for d in range(1,len(nums)):
        for i in range(len(nums)):
            j = i+d
            if j >= len(nums):
                continue
            
            Mcandi, mcandi = [], []
            for k in range(i+1, j+1):
                if ops[k-1] == '-':
                    ref_max = M[(i,k-1)] - m[(k,j)]
                    ref_min = m[(i,k-1)] - M[(k,j)]
                    Mcandi.append(ref_max)
                    mcandi.append(ref_min)
                else:
                    ref_max = M[(i,k-1)] + M[(k,j)]
                    ref_min = m[(i,k-1)] + m[(k,j)]
                    Mcandi.append(ref_max)
                    mcandi.append(ref_min)
            
            M[(i,j)] = max(Mcandi)
            m[(i,j)] = min(mcandi)
    
    return M[(0,len(nums)-1)]