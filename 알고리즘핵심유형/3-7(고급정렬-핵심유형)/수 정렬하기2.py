def mergeSort(numList):
    def mergeSort_(fstIdx, endIdx):
        if endIdx - fstIdx < 2:
            return
        
        midIdx = (fstIdx + endIdx) // 2
        
        mergeSort_(fstIdx, midIdx)
        mergeSort_(midIdx, endIdx)

        merge(fstIdx, midIdx, endIdx)
    
    def merge(fstIdx, midIdx, endIdx):
        i = fstIdx
        j = midIdx
        tmpList = []

        while i < midIdx and j < endIdx:
            if numList[i] < numList[j]:
                tmpList.append(numList[i])
                i += 1
            else:
                tmpList.append(numList[j])
                j += 1
        
        while i < midIdx:
            tmpList.append(numList[i])
            i += 1
        
        while j < endIdx:
            tmpList.append(numList[j])
            j += 1

        for i in range(fstIdx, endIdx):
            numList[i] = tmpList[i - fstIdx]

    return mergeSort_(0, len(numList))

N = int(input())

numList = []

for _ in range(N):
    numList.append(int(input()))

mergeSort(numList)

for num in numList:
    print(num)