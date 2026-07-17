"""
洛谷 P1094 - 纪念品分组
题目：将n个纪念品分成若干组，每组2个，使得每组的价值差最小

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

n = int(input())
prices = list(map(int, input().split()))

# 排序后配对
prices.sort()

total_diff = 0
for i in range(0, n, 2):
    if i + 1 < n:
        total_diff += prices[i + 1] - prices[i]

print(total_diff)
