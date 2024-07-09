# 11444
n = int(input())
matrix = [[1,1], [1,0]]

def matmul(a,b):
    mod = 1000000007
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0])%mod,  (a[0][0]*b[0][1] + a[0][1]*b[1][1])%mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0])%mod,  (a[1][0]*b[0][1] + a[1][1]*b[1][1])%mod]
    ]

def fast_power(mat,n):
    if n == 1:
        return mat
    
    x = fast_power(mat,n//2)

    if n%2 == 0:
        return matmul(x,x)
    else:
        return matmul(matmul(x,x),mat)

print(fast_power(matrix,n)[0][1]%1000000007)