"""
洛谷 P1011 - 车站
题目：贪心算法，从某点出发，每次加油一定量，到达目标地点

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高-
"""

n = int(input())
stations = []
for _ in range(n):
    x, y = map(int, input().split())
    stations.append((x, y))

# 贪心：每次选择能到达的最远的站
current_fuel = 0
current_pos = 0
refills = 0

for i in range(len(stations)):
    next_station = stations[i]
    distance = next_station[0] - current_pos
    
    if distance > current_fuel:
        # 需要加油
        if i == 0:
            current_fuel = next_station[1]
            refills += 1
        else:
            # 回到前一个站加油
            pass
    
    current_fuel -= distance
    current_pos = next_station[0]

print(refills)
