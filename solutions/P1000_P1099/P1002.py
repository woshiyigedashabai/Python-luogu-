"""
洛谷 P1002 - 过河卒
题目：动态规划问题
卒从(0,0)走到(n,m)，但要避开马的位置及马能到达的位置

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及-
"""

n, m, x_horse, y_horse = map(int, input().split())

# 动态规划数组，dp[i][j]表示到达(i,j)的方案数
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 初始化
dp[0][0] = 1

# 马能攻击的所有位置
horse_attacks = [
    (x_horse + 2, y_horse + 1),
    (x_horse + 1, y_horse + 2),
    (x_horse - 1, y_horse + 2),
    (x_horse - 2, y_horse + 1),
    (x_horse - 2, y_horse - 1),
    (x_horse - 1, y_horse - 2),
    (x_horse + 1, y_horse - 2),
    (x_horse + 2, y_horse - 1),
    (x_horse, y_horse)  # 马的位置本身也不能走
]

# 标记被攻击的位置
blocked = set(horse_attacks)

# DP过程
for i in range(n + 1):
    for j in range(m + 1):
        if (i, j) in blocked:
            dp[i][j] = 0
        elif i == 0 and j == 0:
            dp[i][j] = 1
        else:
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

print(dp[n][m])
