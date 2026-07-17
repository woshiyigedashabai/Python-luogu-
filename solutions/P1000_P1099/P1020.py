"""
洛谷 P1020 - 导弹拦截
题目：动态规划问题，最长递减子序列

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

import sys

# 第一问：最长递减子序列
heights = []
while True:
    try:
        h = int(input())
        heights.append(h)
    except EOFError:
        break

n = len(heights)

# 最长递减子序列（LDS）
dp_lds = [1] * n
for i in range(n):
    for j in range(i):
        if heights[j] > heights[i]:
            dp_lds[i] = max(dp_lds[i], dp_lds[j] + 1)

max_lds = max(dp_lds)

# 最小拦截系统数（贪心）
from bisect import bisect_left

systems = []
for h in heights:
    pos = bisect_left(systems, -h)  # 用负数维护递减序列
    if pos == len(systems):
        systems.append(-h)
    else:
        systems[pos] = -h

print(max_lds)
print(len(systems))
