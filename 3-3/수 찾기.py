# 수 찾기

n = int(input())

hashSet = set(map(int, input().split(' ')))

m = int(input())

checkList = list(map(int, input().split(' ')))

for checkValue in checkList:
    if checkValue in hashSet:
        print("1")
    else:
        print("0")

