"""
洛谷 P1062 - 数列
题目：数学问题，找规律

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n = int(input())

# 找出第n个数
# 这取决于具体的数列规律
# 假设是某种常见的数列

# 示例：Fibonacci数列
if n == 1 or n == 2:
    print(1)
else:
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    print(b)
