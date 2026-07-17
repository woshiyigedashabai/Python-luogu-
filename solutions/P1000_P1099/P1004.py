"""
洛谷 P1004 - 方格取数
题目：往返取数，每个格子的数字只计算一次，求最大总分

这是一个经典的动态规划问题。
可以转化为两条路径同时从左上走到右下，求能经过的最大权值。

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

n = int(input())

# 读取方格数据
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 使用DP求解
# dp[i1][j1][i2][j2] 表示两条路径分别到达(i1,j1)和(i2,j2)的最大得分
# 由于两条路径步数相同，可以优化为 dp[i1][j1][i2]
# 其中 j2 = i1 + j1 - i2

# 初始化DP数组
dp = [[[-1] * n for _ in range(n)] for _ in range(n)]

def solve(i1, j1, i2):
    """递归求解"""
    j2 = i1 + j1 - i2
    
    # 边界检查
    if i1 >= n or j1 >= n or i2 >= n or j2 >= n:
        return -float('inf')
    
    # 两条路都到达终点
    if i1 == n - 1 and j1 == n - 1:
        return grid[i1][j1]
    
    # 记忆化
    if dp[i1][j1][i2] != -1:
        return dp[i1][j1][i2]
    
    # 当前格子的值
    current = grid[i1][j1]
    if i1 != i2 or j1 != j2:  # 两条路径不在同一个点
        current += grid[i2][j2]
    
    # 四种移动方式
    result = max(
        solve(i1 + 1, j1, i2 + 1),      # 两条都向下
        solve(i1 + 1, j1, i2),          # 第一条向下，第二条向右
        solve(i1, j1 + 1, i2 + 1),      # 第一条向右，第二条向下
        solve(i1, j1 + 1, i2)           # 两条都向右
    )
    
    if result != -float('inf'):
        result += current
    
    dp[i1][j1][i2] = result
    return result

print(solve(0, 0, 0))
