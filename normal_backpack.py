# 12865
n,k = map(int,input().split())
items = []
for _ in range(n):
    items.append(list(map(int,input().split())))

# row : item 인덱스
# column : 가방의 최대 무게
dp = [[0]*(k+1) for _ in range(n)]

for item_idx in range(n):
    for bag_capability  in range(k+1):
        w,v = items[item_idx]
        if w >  bag_capability:
            dp[item_idx][bag_capability] = dp[item_idx-1][bag_capability]
        else:
            dp[item_idx][bag_capability] = max(dp[item_idx-1][bag_capability-w] + v, dp[item_idx-1][bag_capability])

print(dp[n-1][k])





# for i in dp:
#     print(i) 
# # =======================
# n,k = map(int,input().split())
# items = [[0,0]]
# for _ in range(n):
#     items.append(list(map(int,input().split())))

# # row : 가방의 최대 무게
# # column : item 인덱스
# dp = [[0]*(n+1) for _ in range(k+1)]

# for bag_capability  in range(k+1):
#     for item_idx in range(n+1):
#         w,v = items[item_idx]
#         if w >  bag_capability:
#             dp[bag_capability][item_idx] = dp[bag_capability][item_idx-1]
#         else:
#             dp[bag_capability][item_idx] = max(dp[bag_capability-w][item_idx-1] + v, dp[bag_capability][item_idx-1])

# print(dp[k][n])
# for i in dp:
#     print(i) 

# # [[1,1], [2,3], [5,3], [5,1], [4,5], [3,3], [3,2], [4,4], [4,4], [4,3]]


# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
# [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# [6, 7, 7, 7, 7, 7, 7, 7, 7, 7]
# [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
# [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
# [10, 11, 11, 11, 11, 11, 11, 11, 11, 11]
# [12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
# [13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# [14, 15, 15, 15, 15, 15, 15, 15, 15, 15]
# [16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
# [17, 17, 17, 17, 17, 17, 17, 17, 17, 17]
# [18, 19, 19, 19, 19, 19, 19, 19, 19, 19]
# [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]


# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4]
# [0, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 4, 4, 4, 6, 6, 6, 6, 6, 6]
# [0, 1, 4, 4, 4, 8, 8, 8, 8, 8, 8]
# [0, 1, 4, 6, 6, 9, 9, 9, 9, 9, 9]
# [0, 1, 4, 7, 7, 9, 9, 9, 9, 9, 9]
# [0, 1, 4, 7, 7, 9, 11, 11, 11, 11, 11]
# [0, 1, 4, 7, 7, 9, 12, 12, 12, 12, 12]
# [0, 1, 4, 7, 7, 11, 12, 12, 13, 13, 13]
# [0, 1, 4, 7, 7, 12, 12, 13, 13, 13, 13]
# [0, 1, 4, 7, 8, 12, 12, 14, 15, 15, 15]
# [0, 1, 4, 7, 8, 12, 14, 14, 16, 16, 16]
# [0, 1, 4, 7, 8, 12, 15, 15, 16, 17, 17]