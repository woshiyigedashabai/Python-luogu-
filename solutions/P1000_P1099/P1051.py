"""
洛谷 P1051 - 谁拿了最多奖学金
题目：排序问题，多条件排序

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

from functools import cmp_to_key

n = int(input())
students = []

for _ in range(n):
    parts = input().split()
    name = parts[0]
    chinese = int(parts[1])
    math = int(parts[2])
    english = int(parts[3])
    
    students.append({
        'name': name,
        'chinese': chinese,
        'math': math,
        'english': english,
        'total': chinese + math + english
    })

# 排序规则
def compare(x, y):
    # 先按总分降序
    if x['total'] != y['total']:
        return y['total'] - x['total']
    # 再按数学成绩降序
    if x['math'] != y['math']:
        return y['math'] - x['math']
    # 最后按语文成绩降序
    return y['chinese'] - x['chinese']

students.sort(key=cmp_to_key(compare))
print(students[0]['name'])
