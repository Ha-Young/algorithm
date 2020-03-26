# 백준 세수정렬

# 선택 정렬

numList = list(map(int, input().split(' ')))

for i in range(len(numList)):
    minValue = numList[i]
    for j in range(i + 1, len(numList)):
        if minValue > numList[j]:
            minValue = numList[j]
            numList[i], numList[j] = numList[j], numList[i]
        
print(' '.join(map(str,numList)))