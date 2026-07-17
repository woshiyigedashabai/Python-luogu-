"""
洛谷 P1008 - 三连击
题目：输出所有满足abc*abc=abcabc的三位数

时间限制: 1000 ms
空间限制: 125 MB
难度: 普及
"""

# abc * abc = abcabc
# abc * abc = abc * 1001
# abc^2 = abc * 1001
# abc = 1001
# 但abc是三位数，所以要找满足条件的abc

# abc * abc = abcabc
# (100a + 10b + c) * (100a + 10b + c) = 100100a + 10010b + 1001c
# = 1001 * (100a + 10b + c)
# 
# 所以 abc^2 = 1001 * abc
# abc = 1001 不符合（4位数）
#
# 重新理解：abc是一个三位数，abcabc是将abc重复两次
# abcabc = abc * 1000 + abc = abc * 1001
# abc * abc = abc * 1001
# abc = 1001 不对

# 换个思路：找所有满足 n^2 的形式为 abc abc 的三位数n
# 即 n^2 = n * 1001，不可能
#
# 正确理解应该是：三位数abc，满足 abc * abc = abcabc
# 其中abcabc = 100000*a + 10000*b + 1000*c + 100*a + 10*b + c
# = 100100*a + 10010*b + 1001*c = 1001 * (100*a + 10*b + c) = 1001 * abc
#
# 所以需要 abc^2 = 1001 * abc
# 即 abc = 1001，不是三位数
#
# 题意应该是：找满足 abc * abc = defghi，且 defghi = abcabc 的三位数

for abc in range(100, 1000):
    product = abc * abc
    # 检查product是否为6位数且形式为abcabc
    if 100000 <= product <= 999999:
        # 获取product的各位数字
        s = str(product)
        if len(s) == 6:
            first_half = s[:3]
            second_half = s[3:]
            if first_half == second_half:
                print(abc)
