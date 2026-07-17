"""
洛谷 P1070 - 道路游戏
题目：动态规划，最优路径

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n = int(input())
dist = list(map(int, input().split()))

# dp[i] = 到达第i个位置的最少时间
dp = [float('inf')] * n
dp[0] = 0

for i in range(n - 1):
    # 从位置i到位置i+1
    time_cost = dist[i]
    dp[i + 1] = min(dp[i + 1], dp[i] + time_cost)
    
    # 从位置i跳跃到更远的位置
    for j in range(i + 2, n):
        time_cost = dist[i]
        dp[j] = min(dp[j], dp[i] + time_cost)

print(dp[n - 1])
