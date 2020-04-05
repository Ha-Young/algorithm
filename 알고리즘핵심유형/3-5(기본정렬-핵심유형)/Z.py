# Z

import sys
input = sys.stdin.readline

result = 0

def solution(n, x, y):
    global result
    if n == 1:
        if x == r and y == c:
            print(result)
            return
        result += 1
    else:
        solution(n / 2, x, y)
        solution(n / 2, x, y + n / 2)
        solution(n / 2, x + n / 2, y)
        solution(n / 2, x + n / 2, y + n / 2)


n, r, c = map(int, input().split())

solution(2 ** n, 0, 0)