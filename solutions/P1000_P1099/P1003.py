"""
洛谷 P1003 - 铺地毯
题目：给定多块地毯，查询一个点被哪块地毯覆盖

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n = int(input())
carpets = []

# 读取地毯信息
for i in range(n):
    x, y, w, h = map(int, input().split())
    carpets.append((x, y, w, h, i + 1))  # 保存地毯编号（1-indexed）

# 读取查询点
x, y = map(int, input().split())

# 倒序查找，找到覆盖该点的最上面的地毯
result = -1
for i in range(n - 1, -1, -1):
    carpet_x, carpet_y, carpet_w, carpet_h, carpet_id = carpets[i]
    
    # 检查点是否在地毯范围内
    if carpet_x <= x <= carpet_x + carpet_w and carpet_y <= y <= carpet_y + carpet_h:
        result = carpet_id
        break

print(result)
