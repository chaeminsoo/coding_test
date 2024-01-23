# 12919
s = input()
t = input()

ans = False
def dfs(now,s):
    global ans
    if now == s:
        ans = True
        return
    if now == '':
        return
    if now[-1] == 'B' and now[0] == 'A':
        return
    if len(now) < len(s):
        return
    
    if now[-1] == 'A':
        dfs(now[:-1],s)
    if now[0] == 'B':
        dfs(now[1:][::-1],s)

dfs(t,s)
if ans:
    print(1)
else:
    print(0)