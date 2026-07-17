"""
洛谷 P1061 - Jam的计数法
题目：进制转换问题

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

b = int(input())
n = int(input())

# 将十进制的n转换为b进制
if n == 0:
    print(0)
else:
    result = []
    while n > 0:
        result.append(str(n % b))
        n //= b
    print(''.join(reversed(result)))
