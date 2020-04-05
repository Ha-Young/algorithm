
def seeTropyNum(tropyList):
    seeCount = 0
    highest = -1

    for high in tropyList:
        if high > highest:
            seeCount += 1
            highest = high

    return seeCount

N = int(input())

tropyList = []

for _ in range(N):
    tropyList.append(int(input()))

print(seeTropyNum(tropyList))
print(seeTropyNum(tropyList[::-1]))