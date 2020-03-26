"""
친구 네트워크
3-3 08:50
https://www.acmicpc.net/problem/4195
"""
import sys
input=sys.stdin.readline # sys.stdin.readline을 사용하면 그냥 input보다 빠르다

def findNetwork(man):
    if friendsNetwork[man] == man:
        return man
    
    friendsNetwork[man] = findNetwork(friendsNetwork[man])
    return friendsNetwork[man]

def unionNetwork(man1, man2):
    
    man1 = findNetwork(man1)
    man2 = findNetwork(man2)

    if man1 != man2:
        friendsNetwork[man2] = man1
        friendsNetworkNum[man1] += friendsNetworkNum[man2]
 
test_case = int(input())

for _ in range(test_case):
    f = int(input())
    friendsNetwork = dict()
    friendsNetworkNum = dict()

    for _ in range(f):
        
        man1, man2 = input().split()

        if man1 not in friendsNetwork:
            friendsNetwork[man1] = man1
            friendsNetworkNum[man1] = 1
        
        if man2 not in friendsNetwork:
            friendsNetwork[man2] = man2
            friendsNetworkNum[man2] = 1

        unionNetwork(man1, man2)

        print(friendsNetworkNum[findNetwork(man1)])


# ==========================================================================================

# def isConnect(set1, set2):
#     intersection = set1.intersection(set2)

#     if len(intersection) != 0:
#         return True
#     else:
#         return False

# test_case = int(input())

# for _ in range(test_case):
#     netWorks = set()
#     relations = []

#     relationsNum = int(input())

#     for __ in range(relationsNum):
#         newRelation = set(input().split(' '))

#         if len(netWorks) == 0:
#             netWorks = netWorks.union(newRelation)

#         elif isConnect(netWorks, newRelation):
#             netWorks = netWorks.union(newRelation)

#             for existedRelation in relations:
#                 if isConnect(netWorks, existedRelation):
#                     netWorks = netWorks.union(existedRelation)
#         else:
#             relations.append(newRelation)
        
#         print(len(netWorks))