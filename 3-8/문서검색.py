inputStr = input()
searchStr = input()

count = 0
index = 0

while len(inputStr) - index >= len(searchStr):
    if inputStr[index:index + len(searchStr)] == searchStr:
        count += 1
        index += len(searchStr)
    else:
        index += 1

print(count)