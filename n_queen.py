def solve(n):
    def dfs(y, col, diag1, diag2):
        nonlocal ans
        if y == n:
            ans += 1
            return
        
        for x in range(n):
            if col & (1 << x) or diag1 & (1 << (x + y)) or diag2 & (1 << (x - y + n - 1)):
                continue
            dfs(y + 1, col | (1 << x), diag1 | (1 << (x + y)), diag2 | (1 << (x - y + n - 1)))

    ans = 0
    dfs(0, 0, 0, 0)
    return ans

n = int(input())
print(solve(n))