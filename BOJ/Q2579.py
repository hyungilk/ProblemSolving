import sys

n = int(input())
step_list = []
# step list 입력 받기
for _ in range(n):
    step_list.append((int(sys.stdin.readline())))

# 계단 출력 함수
def stepPrint(arr):
  # 계단 숫자 세기
    n = len(arr)
  # dp 테이블 생성
    dp = [0] * (n+1)
  # 입력 list의 길이가 1일때
    if n ==1:
        return arr[0]
  # 입력 list의 길이가 2일때
    elif n == 2:
        return arr[0] + arr[1]
  # 나머지 경우  
    else:
        dp[0] = 0
        dp[1] = arr[0]
        dp[2] = arr[0] + arr[1]
        #계단이 3이상 인 경우 점화식 성립
        for i in range(3, n+1):
            dp[i] = max(dp[i-2]+arr[i-1], dp[i-3]+arr[i-2]+arr[i-1])
        return dp[n]

print(stepPrint(step_list))
