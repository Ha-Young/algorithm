# 2xn 타일링 11726

import sys

d = [0] * 1001
def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    if d[n] != 0:
        return d[n]
    else:
        d[n] = dp(n-1) + dp(n-2)
        return d[n]


sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
print(dp(n) % 10007)
