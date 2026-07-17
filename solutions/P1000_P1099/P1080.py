"""
洛谷 P1080 - 国王游戏
题目：贪心算法，找到最优的国王排列顺序

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

from functools import cmp_to_key

king = list(map(int, input().split()))
n = int(input())

players = []
for _ in range(n):
    a, b = map(int, input().split())
    players.append((a, b))

# 自定义排序：按照a[i]*(max(b[i],a[i+1]))最小排列
def compare(x, y):
    # x和y都是(a,b)对
    # 比较x放在前面和y放在前面的结果
    if x[0] * max(x[1], y[0]) > y[0] * max(y[1], x[0]):
        return 1
    else:
        return -1

players.sort(key=cmp_to_key(compare))

# 计算最坏情况
min_win = king[0]
for a, b in players:
    if min_win < a:
        min_win = b
    else:
        min_win = a * min_win + a + b

print(min_win)
