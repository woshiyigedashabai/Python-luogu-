"""
洛谷 P1044 - 栈
题目：栈的应用问题

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

# 这是一个关于栈应用的问题
# 需要计算通过栈可以产生多少种排列

n = int(input())

# Catalan数列：第n个Catalan数
# C(n) = C(n-1) * 2 * (2n-1) / (n+1)

def catalan(n):
    if n <= 1:
        return 1
    
    # 使用动态规划
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    
    return dp[n]

print(catalan(n))
