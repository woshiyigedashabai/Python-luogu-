"""
洛谷 P1059 - 明明的随机数
题目：排序和去重

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n = int(input())
numbers = set()

for _ in range(n):
    num = int(input())
    numbers.add(num)

# 排序并输出
sorted_numbers = sorted(numbers)
print(len(sorted_numbers))
for num in sorted_numbers:
    print(num)
