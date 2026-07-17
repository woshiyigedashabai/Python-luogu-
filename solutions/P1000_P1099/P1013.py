"""
洛谷 P1013 - 进制位
题目：进制转换问题

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

n, x = map(int, input().split())

# 找到第n个在x进制表示中各位数字之和最小的数
result = 0
for i in range(1, 100000):
    # 计算i在x进制表示中的数字之和
    temp = i
    digit_sum = 0
    while temp > 0:
        digit_sum += temp % x
        temp //= x
    
    if digit_sum == n:
        result = i
        break

print(result)
