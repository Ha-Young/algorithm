# 타일링 1793

import sys
input = sys.stdin.readline

d = [0] * 251

def dp(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 3
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = dp(n-1) + (2 * dp(n-2))
        return d[n]

while True:
    try:
        print(dp(int(input())))
    except:
        break
