# 피보나치 수

# import sys
# input = sys.stdin.readline

# def getFibonachi(index):
#     if index == 0:
#         return 0
#     elif index == 1:
#         return 1
    
#     return getFibonachi(index - 1) + getFibonachi(index - 2)

# n = int(input())

# num = getFibonachi(n)

# print(num)

import sys
input = sys.stdin.readline

n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)
