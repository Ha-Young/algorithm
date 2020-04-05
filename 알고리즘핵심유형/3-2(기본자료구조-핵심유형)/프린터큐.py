# 프린터 큐

def getMaxLargeNum(queue):
    largeNum = 0

    for item in queue:
        if largeNum < item[1]:
            largeNum = item[1]

    return largeNum

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(idx, i) for idx, i in enumerate(queue)]

    count = 0

    while True:
        largestNum = getMaxLargeNum(queue)
        if queue[0][1] != largestNum:
            queueItem = queue[0]
            queue.remove(queueItem)
            queue.append(queueItem)
        elif queue[0][1] == largestNum:
            count += 1
            if m == queue[0][0]:
                print(count)
                break
            else:
                queue.remove(queue[0])
