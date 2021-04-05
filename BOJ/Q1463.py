n = int(input())

# dp 생성
dp = [0] * (n+1)
# dp 값 update
for i in range(2,n+1):
    # dp 기본 값 생성
    dp[i] = dp[i-1] + 1
    # 2와 3 모두 나누기가 가능한 경우 3가지 case 비교
    if i % 6 == 0:
        dp[i] = min(dp[i//3]+1, dp[i//2]+1, dp[i])
    # 3 나누기 가능한 경우 2가지 case 비교
    elif i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    # 2 나누기 가능한 경우 2가지 case 비교
    elif i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[n])

