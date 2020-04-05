#좌표 정렬하기

# 파이썬의 정렬 알고리즘은 튜플의 첫번째 인덱스가 같으면 그 다음 인덱스로 정렬이 된다. 그래서 기본 알고리즘 사용하면 된다.

n = int(input())

positionList = []

for _ in range(n):
    positionList.append(tuple(map(int, input().split())))

positionList = sorted(positionList)

for position in positionList:
    print(position[0], position[1])

