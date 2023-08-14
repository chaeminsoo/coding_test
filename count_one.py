# 9527
a,b = map(int,input().split())

i = 0
while b >= 2**i:
    i+=1

# 최상위 비트가 i보다 작거나 같은 수의 1의 개수
dp = [0]*i
dp[0] = 1
for j in range(1,i):
    dp[j] = dp[j-1]*2 + 2**j

dp = [0] + dp

def count_one(n):
    cnt = 0
    bin_num = bin(n)[2:]
    num_len = len(bin_num)

    for i in range(num_len):
        if bin_num[i] == '1':
            square = num_len-i-1
            cnt += dp[square]
            cnt += (n - 2**square + 1)
            n = n - 2**square
    
    return cnt

print(count_one(b) - count_one(a-1))