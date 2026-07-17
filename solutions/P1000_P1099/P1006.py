"""
洛谷 P1006 - 传纸条
题目：两个人从左上角到右下角传纸条，两条路径最多相同位置只能走一次

动态规划问题，类似于方格取数

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高
"""

n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# dp[i1][j1][i2] 表示两条路径分别到达(i1,j1)和(i2,j2)的最大纸条价值
# j2 = i1 + j1 - i2
dp = [[[-1] * n for _ in range(m)] for _ in range(n)]

def solve(i1, j1, i2):
    j2 = i1 + j1 - i2
    
    # 边界检查
    if i1 >= n or j1 >= m or i2 >= n or j2 >= m:
        return -float('inf')
    
    # 两条路都到达终点
    if i1 == n - 1 and j1 == m - 1:
        return grid[i1][j1]
    
    # 记忆化
    if dp[i1][j1][i2] != -1:
        return dp[i1][j1][i2]
    
    # 当前格子的纸条价值
    current = grid[i1][j1]
    if i1 != i2 or j1 != j2:  # 两条路不在同一位置
        current += grid[i2][j2]
    
    # 四种移动方式
    result = max(
        solve(i1 + 1, j1, i2 + 1),
        solve(i1 + 1, j1, i2),
        solve(i1, j1 + 1, i2 + 1),
        solve(i1, j1 + 1, i2)
    )
    
    if result != -float('inf'):
        result += current
    
    dp[i1][j1][i2] = result
    return result

print(solve(0, 0, 0))
