# 백준
# 수 정렬하기2

# import sys
# input = sys.stdin.readline

# # 수 정렬하기

# import sys
# input = sys.stdin.readline

# def mergeSort(arr):
#     def mergeSort_(low, high):
#         if high - low < 2:
#             return

#         mid = low + (high - low) //2

#         mergeSort_(low, mid)
#         mergeSort_(mid, high)

#         merge(low, mid, high)
    
#     def merge(low, mid, high):
#         temp = []
#         i = low
#         j = mid

#         while i < mid and j < high:
#             if arr[i] <= arr[j]:
#                 temp.append(arr[i])
#                 i += 1
#             else:
#                 temp.append(arr[j])
#                 j += 1
        
#         while i < mid:
#             temp.append(arr[i])
#             i += 1
        
#         while j < high:
#             temp.append(arr[j])
#             j += 1

#         for idx in range(low, high):
#             arr[idx] = temp[idx - low]

#     return mergeSort_(0, len(arr))

# n = int(input())

# numList = []

# for _ in range(n):
#     numList.append(int(input()))

# mergeSort(numList)

# for num in numList:
#     print(num)

# 퀵 소트
# import sys
# input = sys.stdin.readline
# def quickSort(arr):
#     def quickSort_(low, high):
#         if high - low < 1:
#             return

#         mid = partition(low, high)

#         quickSort_(low, mid - 1)
#         quickSort_(mid + 1, high)

#     def partition(low, high):
#         mid = low + (high - low) // 2
#         pivot = arr[mid]

#         while low < high:
#             while pivot > arr[low]:
#                 low += 1
#             while pivot < arr[high]:
#                 high -= 1
            
#             if low < high:
#                 arr[low], arr[high] = arr[high], arr[low]
        
#         return low

#     return quickSort_(0, len(arr) - 1)


# n = int(input())

# numList = []

# for _ in range(n):
#     numList.append(int(input()))

# quickSort(numList)

# for num in numList:
#     print(num)

# import sys
# input = sys.stdin.readline

# n = int(input())

# numList = []

# for _ in range(n):
#     numList.append(int(input()))

# numList = sorted(numList)

# for num in numList:
#     print(num)

# 힙소트

def heapSort(arr):
    def heapify(index, limit = len(arr)):
        child = index * 2 + 1

        if child >= limit:
            return
        
        if child + 1 < limit and arr[child] < arr[child + 1]:
            child += 1

        if arr[index] < arr[child]:
            arr[index], arr[child] = arr[child], arr[index]

        if child < limit // 2:
            heapify(child, limit)

    for i in range(len(arr) // 2, -1, -1):
        heapify(i)
    
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i)

n = int(input())

numList = []

for _ in range(n):
    numList.append(int(input()))

heapSort(numList)

for num in numList:
    print(num)