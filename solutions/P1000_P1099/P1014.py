"""
洛谷 P1014 - Cantor表
题目：输出Cantor表中第n个数的坐标

Cantor表是一个对角线遍历的矩阵

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n = int(input())

# 找到n所在的对角线
diag = 1
count = 0
while count + diag < n:
    count += diag
    diag += 1

# n在第diag条对角线上
# 对角线从左上到右下
pos_in_diag = n - count

if diag % 2 == 1:
    # 奇数对角线：从(1,diag)到(diag,1)
    x = pos_in_diag
    y = diag + 1 - pos_in_diag
else:
    # 偶数对角线：从(diag,1)到(1,diag)
    x = diag + 1 - pos_in_diag
    y = pos_in_diag

print(x, y)
