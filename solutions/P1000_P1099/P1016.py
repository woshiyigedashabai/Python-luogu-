"""
洛谷 P1016 - 旅行家的预算
题目：图论问题，最短路径

时间限制: 1000 ms
空间限制: 125 MB
难度: 提高
"""

import sys
from heapq import heappush, heappop

n, m = map(int, input().split())

# 构建图
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start, end = map(int, input().split())

# Dijkstra算法
dist = [float('inf')] * (n + 1)
dist[start] = 0
pq = [(0, start)]

while pq:
    d, u = heappop(pq)
    
    if d > dist[u]:
        continue
    
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heappush(pq, (dist[v], v))

print(dist[end])
