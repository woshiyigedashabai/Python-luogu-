"""
洛谷 P1010 - 幂次方
题目：输出 a^b mod p 的结果

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

a, b, p = map(int, input().split())

result = pow(a, b, p)
print(result)
