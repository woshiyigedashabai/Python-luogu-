"""
洛谷 P1077 - 摆花
题目：0/1背包问题，将m朵花放入n个花瓶

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n, m = map(int, input().split())

# dp[i][j] = 用i个花瓶放j朵花的方案数
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 初始化：0朵花只有1种方案（什么都不放）
for i in range(n + 1):
    dp[i][0] = 1

# 每个花瓶可以放0到m朵花
for i in range(1, n + 1):
    for j in range(m + 1):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][j - k]

print(dp[n][m])
