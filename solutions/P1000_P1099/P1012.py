"""
洛谷 P1012 - 拼数
题目：将给定的数字排列成最大的数

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

from functools import cmp_to_key

n = int(input())
numbers = list(map(int, input().split()))

# 自定义排序：比较拼接后的结果
def compare(x, y):
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return -1
    elif int(str(x) + str(y)) < int(str(y) + str(x)):
        return 1
    else:
        return 0

numbers.sort(key=cmp_to_key(compare))
print(''.join(map(str, numbers)))
