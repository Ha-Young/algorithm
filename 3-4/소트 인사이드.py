# 소트인사이드


# inputData = input()
# numList = []

# for num in inputData:
#     numList.append(int(num))

# numList.sort(reverse=True)

# print(''.join(map(str, numList)))


array = input()

for i in range(9, -1, -1):
    for num in array:
        if int(num) == i:
            print(i, end='')

