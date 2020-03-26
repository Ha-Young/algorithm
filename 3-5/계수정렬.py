# 계수정렬

import sys
input = sys.stdin.readline

n = int(input())

numList = [0 for i in range(10001)]

for i in range(n):
    num = int(input())
    numList[num] += 1

for num, numCount in enumerate(numList):
    while numCount > 0:
        print(num)
        numCount -= 1

