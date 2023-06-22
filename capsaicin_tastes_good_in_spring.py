# 15824
n = int(input())
data = list(map(int, input().split()))

data.sort()

maxs = 0
mins = 0

def do_power(c,n):
    if n == 0:
        return 1
    elif n == 1:
        return c
    else:
        x = do_power(c,n//2)
        if n%2 == 0:
            return x*x%1000000007
        else:
            return x*x*c%1000000007

for i, j in enumerate(data):
    mins += j*(do_power(2,n-(i+1)))
    maxs += j*(do_power(2,i))

print((maxs-mins)%1000000007)