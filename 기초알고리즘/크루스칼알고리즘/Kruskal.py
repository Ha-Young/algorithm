# 최소비용 신장트리를 만드는 알고리즘.
# 간선을 거리순으로 오름차순으로 정렬 한 후 
# 간선의 최소거리 노드끼리 연결하는데, 
# 사이클을 형성(union-find)하면 무시하고 다음 최소거리를 본다.
# 연결한 간선 개수가 노드개수 -1 이면 중단

# 최소비용 신장트리의 목적은 얼마나 적은 값으로 모든 노드를 연결 할 수 있는가이다.
# 해당 구현은 최소비용을 출력한다.

def union(node1, node2):
    node1 = getParrent(node1)
    node2 = getParrent(node2)

    if node1 != node2:
        nodeParrentList[node2] = node1
    
def getParrent(node1):
    if nodeParrentList[node1] == node1:
        return node1
    else:
        nodeParrentList[node1] = getParrent(nodeParrentList[node1])
        return nodeParrentList[node1]

def findParrent(node1, node2):
    node1 = getParrent(node1)
    node2 = getParrent(node2)

    if node1 == node2:
        return True
    else:
        return False

class Edge:
    """간선 클래스"""
    def __init__(self, node1, node2, distance):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance

n = 7 # 노드 개수
m = 11 # 간선 개수

edgeList = []

# 간선 정보 세팅
edgeList.append(Edge(1, 7, 12))
edgeList.append(Edge(1,4,28))
edgeList.append(Edge(1,2,67))
edgeList.append(Edge(1,5,17))
edgeList.append(Edge(2,4,24))
edgeList.append(Edge(2,5,62))
edgeList.append(Edge(3,5,20))
edgeList.append(Edge(3,6,37))
edgeList.append(Edge(4,7,13))
edgeList.append(Edge(5,6,45))
edgeList.append(Edge(5,7,73))

# 간선 길이 오름차순으로 세팅
edgeList = sorted(edgeList, key=lambda edge: edge.distance)

# 사이클 확인을 위한 parrentNodeList 세팅
# 간선의 키가 string일 수도 있으니 딕셔너리로 설정.
nodeParrentList = {}
# 현재 구현은 숫자, 1~7의 수로 노드의 키를 두므로 이렇게 구현.
for i in range(1, 8):
    nodeParrentList[i] = i

sum = 0
for edge in edgeList:
    # 사이클이 발생하지 않는 경우
    if not findParrent(edge.node1, edge.node2):
        sum += edge.distance
        union(edge.node1, edge.node2)

# 최소 거리 출력
print(sum)