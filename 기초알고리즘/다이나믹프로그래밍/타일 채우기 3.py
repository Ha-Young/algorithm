# 타일 채우기 3 14852

d = [0] * 1000001


def dp(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 7
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = 2 * dp(n-1) + 3 * dp(n-2)
        i = 3
        while n - i >= 0:
            d[n] += 2 * dp(n - i)
            i += 1

        return d[n]


try:
    n = int(input())

    print(dp(n) % 1000000007)

except Exception as e:
    print(e)
