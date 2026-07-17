"""
洛谷 P1045 - 麦森数
题目：判断一个数是否是梅森素数

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

p = int(input())

# 梅森数：2^p - 1
mersenne = 2**p - 1

# 检查是否是梅森素数
if is_prime(mersenne):
    print(f"2^{p}-1 is prime.")
else:
    print(f"2^{p}-1 is not prime.")
