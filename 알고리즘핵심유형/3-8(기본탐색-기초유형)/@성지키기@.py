
def isExistColumn(array, column):
    for row in range(len(array)):
        if array[row][column] == 'X':
            return True
    
    return False

def findEmptyRowIndex(array):
    for rowIdx in range(len(array)):
        findX = False

        for colIdx in range(len(array[0])):
            if array[rowIdx][colIdx] == 'X':
                findX = True
                break
        
        if not findX:
            return rowIdx
    
    return 0


N, M = map(int, input().split(' '))

arr = []
count = 0

for row in range(N):
    arr.append(list(input()))

for c in range(M):
    if isExistColumn(arr, c):
        continue
    else:
        emptyRowIdx = findEmptyRowIndex(arr)
        arr[emptyRowIdx][c] = 'X'
        count += 1

print(count)




# n, m = map(int, input().split())

# array = []

# for _ in range(n):
#     array.append(input())

# rowCountArr = [0] * n
# colCountArr = [0] * m

# for i in range(n):
#     for j in range(m):
#         if array[i][j] == 'X':
#             rowCountArr[i] = 1
#             colCountArr[j] = 1

# row_count = 0
# for i in range(n):
#     if rowCountArr[i] == 0:
#         row_count += 1

# col_count = 0
# for i in range(m):
#     if colCountArr[i] == 0:
#         col_count += 1

# print(max(row_count, col_count))