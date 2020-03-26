# 나이순정렬
from sys import stdin
input = stdin.readline

n = int(input())

userList = []

for _ in range(n):
    age, name = input().split()
    userList.append(((int(age), name)))

userList.sort(key=lambda user: user[0])

for item in userList:
    print(f'{item[0]} {item[1]}')