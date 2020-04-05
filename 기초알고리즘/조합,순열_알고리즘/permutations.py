# prefix를 계속 덧붙여 나가서 우리가 원하는 길이 (r : 뽑는갯수) 가 되면 prefix를 출력하는 형식입니다. 
# 여기서 주의할건 arr[i],arr[k] = arr[k],arr[i] 인데요.  
# arr의 k번째 부터 마지막 원소까지 뽑으면서 k번째원소랑 i번째 원소랑 자리를 바꿔준다는 것입니다.
# 그리고 끝까지 돌면 다시 원상태로 돌려주는 백트래킹 알고리즘을 이용합니다. 

def permutations(prefix,k):
    if len(prefix) == r:
        yield prefix
    else:
        for i in range(k,len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutations(prefix + [arr[k]], k+1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]

# 아래는 순열함수를 실행하기 위한 코드 예시 입니다.
arr = [1,2,3,4,5]
r = 3
for perm in permutations([],0):
    print(perm)