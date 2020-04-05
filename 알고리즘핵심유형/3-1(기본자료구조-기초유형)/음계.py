# 음계

inputList = list(map(int, input().split(" ")))

ascending = True
descending = True

for i in range(1, 8):
    if inputList[i] < inputList[i-1]:
        ascending = False
    elif inputList[i] > inputList[i-1]:
        descending = False
    
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")

