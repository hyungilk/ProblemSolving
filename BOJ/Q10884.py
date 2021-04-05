n = int(input())

# 2차원 list 생성
dp = [[[0] for _ in range(10)] for _ in range(n+1)]

# 초기값 생성 : 1자리수 는 각자리 계단수가 모두 1
for k in range(10):
    dp[1][k] = 1

# 계단수 계산 : 2자리수 이상부터 예외 (0, 9) 를 제외하고 점화식 생성
# 0, 9 의 경우 i-1자리수의 1과 8의 결과를 입력
# 예시 4단계 3 -> 3단계 2 + 3단계 4 | 4단계 9 -> 3단계 8 only
for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

# 첫자리가 0인경우는 결과값 계산 시 제외
result = dp[n][1:]

# 결과값 출력
print(sum(result)%1000000000)
