import sys
input = sys.stdin.readline

result = 0

def solution(n, x, y):
    global result
    if n == 1:
        if x == r and y == c:
            print(result)
            return True
        result += 1
    else:
        if solution(n / 2, x, y):
            return True
        if solution(n / 2, x, y + n / 2):
            return True
        if solution(n / 2, x + n / 2, y):
            return True
        if solution(n / 2, x + n / 2, y + n / 2):
            return True

n, r, c = map(int, input().split())

solution(2 ** n, 0, 0)