# 블랙잭

n, m = tuple(map(int, input().split(" ")))
cards = list(map(int, input().split(" ")))

cardSum = 0
findCardSum = 0

for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            cardSum = cards[i] + cards[j] + cards[k]
            if (cardSum <= m):
                findCardSum = max(cardSum, findCardSum)

print(findCardSum)