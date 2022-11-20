# 1309
n = int(input())
arr = [[0,0,0] for _ in range(n)]
arr[0] = [1,1,1]
for i in range(1,n):
    arr[i][0] = sum(arr[i-1]) % 9901
    arr[i][1] = (arr[i-1][0] + arr[i-1][2]) % 9901
    arr[i][2] = (arr[i-1][0] + arr[i-1][1]) % 9901
print(sum(arr[n-1])%9901)