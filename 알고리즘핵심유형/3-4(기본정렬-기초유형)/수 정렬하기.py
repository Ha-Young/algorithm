# 파이썬 정렬 라이브러리

# import sys
# input = sys.stdin.readline

# numList = []

# n = int(input())

# for _ in range(n):
#     numList.append(int(input()))

# numList.sort()

# for num in numList:
#     print(num)



# 선택 정렬

# import sys
# input = sys.stdin.readline

# numList = []

# n = int(input())

# for _ in range(n):
#     numList.append(int(input()))

# for i in range(0, n):
#     min_value = numList[i]
#     for j in range(i + 1, n):
#         if numList[j] < min_value:
#             min_value = numList[j]
#             numList[i], numList[j] = numList[j], numList[i]

# for num in numList:
#     print(num)


# 버블정렬

# from sys import stdin
# input = stdin.readline

# numList = []

# n = int(input())

# for _ in range(n):
#     numList.append(int(input()))

# for i in range(0, n - 1):
#     for j in range(0, n - i - 1):
#         if numList[j] > numList[j+1]:
#             numList[j], numList[j+1] = numList[j+1], numList[j]

# for num in numList:
#      print(num)


# 삽입정렬

# from sys import stdin
# input = stdin.readline

# numList = []

# n = int(input())

# for _ in range(n):
#     numList.append(int(input()))

# for i in range(1, n):
#     j = i
#     while(j > 0 and numList[j - 1] > numList[j]):
#         numList[j], numList[j - 1] = numList[j - 1], numList[j]
#         j -= 1

# for num in numList:
#     print(num)

# 퀵 정렬

def sort(numList):
    def quickSort(lowIdx, highIdx):
        if lowIdx >= highIdx:
            return
        
        midIdx = partition(lowIdx, highIdx)

        quickSort(lowIdx, midIdx - 1)
        quickSort(midIdx + 1, highIdx)
    
    def partition(lowIdx, highIdx):
        pivot = numList[lowIdx + (highIdx - lowIdx) // 2] # (lowIdx + highIdx) // 2 와 같으나 덧셈시 오버플로우 방지로 왼쪽과 같은 방법 사용

        while lowIdx < highIdx:
            while pivot > numList[lowIdx]:
                lowIdx += 1
            while pivot < numList[highIdx]:
                highIdx -= 1

            if lowIdx < highIdx:
                numList[lowIdx], numList[highIdx] = numList[highIdx], numList[lowIdx]
            
        return lowIdx

    return quickSort(0, len(numList) - 1)

n = int(input())

numList = []

for _ in range(n):
    numList.append(int(input()))

sort(numList)

for num in numList:
    print(num)

