"""
洛谷 P1068 - 分数线划定
题目：排序问题，找到及格线

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

n, m = map(int, input().split())
scores = list(map(int, input().split()))

# 按照分数从高到低排序
scores.sort(reverse=True)

# 找到及格线
if n >= m:
    pass_score = scores[m - 1]
    # 统计有多少人达到这个分数
    count = 0
    for score in scores:
        if score >= pass_score:
            count += 1
    print(count)
else:
    print(n)
