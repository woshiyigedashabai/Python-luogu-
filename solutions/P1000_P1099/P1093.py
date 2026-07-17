"""
洛谷 P1093 - 奖学金
题目：排序问题，按照多个条件排序

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

from functools import cmp_to_key

n = int(input())
students = []

for i in range(n):
    name = input().strip()
    score = int(input())
    c_score = int(input())
    m_score = int(input())
    students.append((name, score, c_score, m_score, i))

# 按照题目要求排序
def compare(x, y):
    # 先按总分降序
    if x[1] + x[2] + x[3] != y[1] + y[2] + y[3]:
        return (y[1] + y[2] + y[3]) - (x[1] + x[2] + x[3])
    # 再按语文成绩降序
    if x[1] != y[1]:
        return y[1] - x[1]
    # 最后按输入顺序升序
    return x[4] - y[4]

students.sort(key=cmp_to_key(compare))

for i in range(min(5, n)):
    print(students[i][0])
