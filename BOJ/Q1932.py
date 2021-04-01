import sys

# 삼각형 line 크기 
n = int(input())

# 삼각형 각 line별 데이터 리스트 생성
num_list = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    num_list.append(tmp)

 #dp 리스트 생성 : 삼각형 데이터 리스트와 동일한 사이즈로 생성
dp = [[0]]
for i in range(1,n):
    dp.append([0]*(i+1))

# 삼각형 최대값 counting 함수 생성
def countTriangle(arr):
    # 1층 초기값 입력
    dp[0][0] = arr[0][0]
    # 2 ~ n층까지 최대값 계산
    # 방법 : i-1층까지 온 값이 max라 가정할 때, 두 방향에서 오는 결과값 중 더 큰값과 i층에서의 데이터 리스트 값을 더해서 i층의 counting 리스트를 계산
    # 단, 처음과 마지막의 경우 가능한 max값은 i-1층의 처음 혹은 마지막 값이다 -> i-1층의 값 + i층의 데이터 값
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            elif j == len(arr[i])-1:
                dp[i][j] = dp[i-1][j-1] + arr[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]
    # n층의 최대값 계산 및 return
    result = max(dp[len(arr)-1])
    return result

print(countTriangle(num_list))
