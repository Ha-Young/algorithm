
def solution(array, commands):
    answer = []
    for command in commands:
        if len(command) != 3:
            return null
        
        i = command[0]
        j = command[1]
        k = command[2]
        
        if i < 0:
            return null
        if j > len(array):
            return null
        
        slicedArr = array[i - 1:j]
        
        if k > len(slicedArr):
            return null
        
        slicedArr.sort()
        answer.append(slicedArr[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))