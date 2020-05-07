# 타일 채우기 2133

d = [0] * 31
def dp(n):
    if n % 2 != 0:
        return 0

    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 3
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = 3 * dp(n-2)
        m = n
        while m >= 4 and m % 2 == 0:
            d[n] += 2 * dp(m-4)
            m -= 2
        return d[n]
    
n = int(input())
print(dp(n))