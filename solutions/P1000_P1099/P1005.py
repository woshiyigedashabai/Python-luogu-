"""
洛谷 P1005 - 矩阵取数游戏
题目：从矩阵的左右端取数，按取出顺序计分，求最大得分

第k个数计分为 数值 * 2^(k-1)

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高
"""

n = int(input())

# 读取矩阵
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 计算每行的长度
row_lengths = [len(matrix[i]) for i in range(n)]
total_numbers = sum(row_lengths)

# 使用记忆化搜索
# dp[row_states] 表示在当前状态下的最大得分
# 其中 row_states 是每一行已取出的数字个数

from functools import lru_cache

@lru_cache(maxsize=None)
def dp(state):
    """
    state是一个元组，表示每行已经取出的数字个数
    返回从这个状态开始能获得的最大得分
    """
    state = list(state)
    
    # 检查是否所有数字都已取出
    if all(state[i] == row_lengths[i] for i in range(n)):
        return 0
    
    # 当前是第几个数字（从1开始计数）
    current_number_index = sum(state) + 1
    power_of_2 = 1 << (current_number_index - 1)  # 2^(current_number_index-1)
    
    best_score = 0
    
    # 尝试从每一行的左端或右端取数
    for row in range(n):
        if state[row] < row_lengths[row]:
            # 从左端取
            left_index = state[row]
            number = matrix[row][left_index]
            new_state = state[:]
            new_state[row] += 1
            score = number * power_of_2 + dp(tuple(new_state))
            best_score = max(best_score, score)
            
            # 从右端取
            right_index = row_lengths[row] - 1 - state[row]
            number = matrix[row][right_index]
            new_state = state[:]
            new_state[row] += 1
            score = number * power_of_2 + dp(tuple(new_state))
            best_score = max(best_score, score)
    
    return best_score

initial_state = tuple([0] * n)
print(dp(initial_state))
