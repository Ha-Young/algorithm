# 중복 조합
# combinations 에서 중복만 허용 i + 1 -> i
def combinations_with_replacement(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:], r - 1):
                yield [arr[i]] + next


combi = combinations_with_replacement([1,2,3,4,5],2)

print(list(combi))