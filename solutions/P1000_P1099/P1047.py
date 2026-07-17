"""
洛谷 P1047 - 校门外的树
题目：模拟问题，标记和计数

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

l, m = map(int, input().split())

# 标记要砍掉的树
remove = set()

for _ in range(m):
    x, y = map(int, input().split())
    for i in range(x, y + 1):
        remove.add(i)

# 统计剩余的树
remaining = l + 1 - len(remove)
print(remaining)
