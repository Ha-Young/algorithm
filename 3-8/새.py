N = int(input())

count = 0
K = 1

while N > 0:
    if N < K:
        K = 1

    N -= K
    count += 1
    K += 1

print(count)
