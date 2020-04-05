# 키로거

def leftBtnClick(leftKeysOnCursor, rightKeysOnCusor):
    if leftKeysOnCursor == None or len(leftKeysOnCursor) == 0:
        return
    else:
        moveKey = leftKeysOnCursor.pop()
        rightKeysOnCusor.append(moveKey)

def rightBtnClick(leftKeysOnCursor, rightKeysOnCusor):
    if rightKeysOnCusor == None or len(rightKeysOnCusor) == 0:
        return
    else:
        moveKey = rightKeysOnCusor.pop()
        leftKeysOnCursor.append(moveKey)

def deleteBtnClick(leftKeysOnCursor):
    if leftKeysOnCursor == None or len(leftKeysOnCursor) == 0:
        return
    else:
        leftKeysOnCursor.pop()

def keyDown(ch):
    leftKeysOnCursor.append(ch)

test_case = int(input())

for _ in range(test_case):
    keyLogger = input().strip()
    
    leftKeysOnCursor = []    
    rightKeysOnCusor = []
    
    for ch in keyLogger:
        if ch == "<":
            leftBtnClick(leftKeysOnCursor, rightKeysOnCusor)
        elif ch == ">":
            rightBtnClick(leftKeysOnCursor, rightKeysOnCusor)
        elif ch =="-":
            deleteBtnClick(leftKeysOnCursor)
        else:
            keyDown(ch)

    leftKeysOnCursor.extend(reversed(rightKeysOnCusor))
    print(''.join(leftKeysOnCursor))