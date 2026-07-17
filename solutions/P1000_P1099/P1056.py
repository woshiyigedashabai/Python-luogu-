"""
洛谷 P1056 - 排座椅
题目：排列组合问题

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n, m = map(int, input().split())

# 计算排列数：n个人选m个位置的排列数
# A(n, m) = n! / (n-m)!

from math import factorial

result = factorial(n) // factorial(n - m)
print(result)
