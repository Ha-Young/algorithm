# 중복 순열
# combinations 비슷

def products(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in products(arr, r - 1):
                yield [arr[i]] + next

prod = products([1,2,3,4,5],2)

print(list(prod))