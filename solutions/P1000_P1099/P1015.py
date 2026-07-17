"""
洛谷 P1015 - 回文数
题目：判断一个数是否是回文数

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

number = input().strip()
k = int(input())

# 最多进行k次回文操作
for iteration in range(k + 1):
    if number == number[::-1]:
        print(f"YES")
        print(f"STEP={iteration}")
        exit()
    
    if iteration < k:
        # 执行一次回文操作：数字加上其反向的数字
        reversed_num = number[::-1]
        number = str(int(number) + int(reversed_num))

print(f"NO")
print(f"STEP={k}")
