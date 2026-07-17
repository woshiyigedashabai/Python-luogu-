"""
洛谷 P1009 - 阶乘之和
题目：计算 1! + 2! + 3! + ... + n!

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n = int(input())

total = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    total += factorial

print(total)
