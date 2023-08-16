# 12850
d = int(input())

campus = [
    [0,1,1,0,0,0,0,0], # 정보과학관
    [1,0,1,1,0,0,0,0], # 전산관
    [1,1,0,1,1,0,0,0], # 미래관
    [0,1,1,0,1,1,0,0], # 신양관
    [0,0,1,1,0,1,0,1], # 한경직기념관
    [0,0,0,1,1,0,1,0], # 진리관
    [0,0,0,0,0,1,0,1], # 학생회관
    [0,0,0,0,1,0,1,0]  # 형남공학관
]

def mat_mul(a,b):
    return [[sum(a[i][j]*b[j][k]%1000000007 for j in range(8))%1000000007 for k in range(8)] for i in range(8)]

def do_power(c,n):
    if n == 1:
        return c
    else:
        x = do_power(c,n//2)
        x = mat_mul(x,x)
        if n%2 == 0:
            return x
        else:
            return mat_mul(x,c)

print(do_power(campus,d)[0][0])