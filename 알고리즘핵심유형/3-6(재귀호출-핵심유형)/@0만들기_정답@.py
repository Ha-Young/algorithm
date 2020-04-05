import copy

def product(baseList, repeat):
    def getRecursiveProduct(op, addedList, repeat):
        addedList.append(op)
        
        if repeat == 0:
            productList.append(addedList)
            return
        
        getRecursiveProduct(baseList[0], addedList[:], repeat - 1)
        getRecursiveProduct(baseList[1], addedList[:], repeat - 1)
        getRecursiveProduct(baseList[2], addedList[:], repeat - 1)

    productList = []
    tmpList = []
    
    getRecursiveProduct(baseList[0], [], repeat - 1)
    getRecursiveProduct(baseList[1], [], repeat - 1)
    getRecursiveProduct(baseList[2], [], repeat - 1)

    return productList


def getExpression(numArr, operatorArr):
    string = ""
    for i in range(len(operatorArr)):
        string += str(numArr[i])
        string += operatorArr[i]
    string += str(numArr[len(numArr) - 1])

    return string

test_case = int(input())

operators = [' ', '+', '-']

for _ in range(test_case):
    N = int(input())

    operatorLists = product(operators, N-1)
    numList = [i for i in range(1, N + 1)]

    for operatorList in operatorLists:
        strExpression = getExpression(numList, operatorList)
        if eval(strExpression.replace(' ', '')) == 0:
            print(strExpression)

    print("")