import math

# 문제 입력값 처리
n = int(input())
arr = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

# combiation nCn//2 계산 - DFS 이용 (파이썬의 경우 내장함수 combination을 통해 구현 가능)
combArr = [0] * (n+1)
combArr[0] = 1

used = [False]*(n+1)
combResult = []

def solve(num):
    if num == n//2:
        tmp = []
        for i in range(n//2):
            tmp.append(combArr[i])
        combResult.append(tmp)
        return

    for i in range(1,n+1):
        if not used[i]:
            used[i] = True
            combArr[num] = i
            solve(num+1)
            for j in range(i+1, n+1):
                used[j] = False
    return

# combination 결과 생성
solve(0)



# 초기 min gap값 생성 
min_gap = 100000

# 조합이 순서대로 생성되었을 경우 :
# combination의 1번째 결과와 n번째 결과는 서로 상호보완적이다(complementary 관계)
# ex, 1~6의 조합 -> [1,2,3] <-> [4,5,6]
# 위의 이유로 n개의 조합 결과 중 n//2 개만 사용한다 
for i in range(len(combResult)//2):
    # 1~n//2까지 조합이 A팀일 경우 n~n//2 가 complementary 인 집합이다
    a_team = combResult[i]
    # 팀a의 stat 합 구하기
    stat_a = 0
    for j in range(len(a_team)):
        member = a_team[j]
        for k in a_team:
            stat_a += arr[member-1][k-1]
    # a팀을 제외한 멤버들의 합 구하기
    b_team = combResult[-i-1]
    stat_b = 0
    for j in range(len(b_team)):
        member = b_team[j]
        for k in b_team:
            stat_b += arr[member-1][k-1]
    # 최소값 구한 후 최소값으로 swap
    min_gap = min(min_gap, abs(stat_a-stat_b))
# 최소값 
print(min_gap)





