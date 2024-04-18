# 11689
n = int(input())

prime_factors = set()

def prime_factorization(n):
    i = 2
    sqrt = int(n**0.5)+1
    while i <= sqrt:
        if n % i == 0:
            prime_factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.add(n)

prime_factorization(n)

for i in prime_factors:
    n //= i
    n *= i-1

print(n)