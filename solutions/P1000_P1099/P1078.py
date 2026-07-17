"""
洛谷 P1078 - 文化之旅
题目：DFS/BFS搜索，找到满足条件的路径

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

def dfs(node, visited, graph, path):
    if len(path) == len(graph):
        return [path]
    
    results = []
    for next_node in graph[node]:
        if next_node not in visited:
            visited.add(next_node)
            path.append(next_node)
            results.extend(dfs(next_node, visited, graph, path))
            path.pop()
            visited.remove(next_node)
    
    return results

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j + 1)

# 从节点1开始DFS
visited = {1}
paths = dfs(1, visited, graph, [1])

if paths:
    print(len(paths))
    for path in paths:
        print(' '.join(map(str, path)))
else:
    print(0)
