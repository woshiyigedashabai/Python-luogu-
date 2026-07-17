"""
洛谷 P1043 - 数字游戏
题目：模拟问题

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

def solve():
    numbers = input().split()
    
    # 进行操作
    while True:
        # 读取操作
        op = input().strip()
        
        if op == 'A':
            # 加法操作
            x = int(input())
            numbers = [str(int(n) + x) for n in numbers]
        elif op == 'B':
            # 乘法操作
            x = int(input())
            numbers = [str(int(n) * x) for n in numbers]
        elif op == 'C':
            # 求和并检查
            total = sum(int(n) for n in numbers)
            print(total)
            break

solve()
