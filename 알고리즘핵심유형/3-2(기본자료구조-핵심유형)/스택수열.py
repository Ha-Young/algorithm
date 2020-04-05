# 스택수 열

class Stack():
    def __init__(self):
        self.__stack = []
        self.__pushPopLog = []

    def push(self, data):
        self.__stack.append(data)
        self.__pushPopLog.append("+")

    def pop(self):
        self.__pushPopLog.append("-")
        return self.__stack.pop()

    def top(self):
        if self.count == 0:
            return None

        return self.__stack[self.count - 1]

    @property
    def count(self):
        return len(self.__stack)

    @property
    def pushPopLog(self):
        return self.__pushPopLog    

n = int(input())
stack = Stack()
inputNum = 1
checkComplete = True

for i in range(n):
    num = int(input())
    if num > inputNum:
        while stack.count == 0 or stack.top() < num:
            stack.push(inputNum)
            inputNum += 1

        stack.pop()

    elif num == inputNum:
        stack.push(inputNum)
        stack.pop()
        inputNum += 1

    elif num < inputNum:
        if stack.top() == num:
            stack.pop()
        else:
            print("NO")
            exit(0)
    

print('\n'.join(stack.pushPopLog))
