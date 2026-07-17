"""
洛谷 P1007 - 独木桥
题目：模拟人在独木桥上行走，检查是否掉落

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n, m = map(int, input().split())
bridge = [0] * m  # 0表示桥面完整，1表示桥面断裂

# 标记断裂的位置
for _ in range(n):
    x = int(input())
    bridge[x - 1] = 1

# 模拟行走过程
pos = 0  # 当前位置（0-indexed）nfalls = 0  # 掉落次数

for step in range(m):
    if bridge[pos] == 1:
        nfalls += 1
    
    # 计算下一步位置
    direction_input = input().strip()
    if direction_input == 'L':
        if pos > 0:
            pos -= 1
        else:
            nfalls += 1
    else:  # 'R'
        if pos < m - 1:
            pos += 1
        else:
            nfalls += 1

print(nfalls)
