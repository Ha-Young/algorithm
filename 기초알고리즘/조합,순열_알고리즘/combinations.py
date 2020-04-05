# 조합 알고리즘
# 제네레이터 사용

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i + 1:], r - 1):
                yield [arr[i]] + next

combi = combinations([1,2,3,4,5],3)

print(list(combi))