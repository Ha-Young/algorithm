# from itertools import permutations

# def solution(numbers):
#     numsCase = list(map(int, (map(''.join, permutations(map(str, numbers))))))

#     numsCase.sort(reverse=True)

#     return str(numsCase[0])

#####################

# def solution(numbers): 
#     numbers = list(map(str, numbers)) 
#     numbers.sort(key=lambda x: x*3, reverse=True) 
#     return str(int(''.join(numbers)))

#####################

def solution(numbers):
    numbers = sorted(numbers, reverse=True, key= lambda x: (str(x)*4)[0:4])

    if numbers[0] == 0:
        return "0"

    return ''.join(map(str, numbers))

print(solution([0, 0, 0, 0]))

print("asdfasdf"[0:4])