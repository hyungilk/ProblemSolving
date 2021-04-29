import sys
input = sys.stdin.readline

# 문제 입력값 
n = int(input())
times = list(map(int,input().split()))

# 아이디어 : 시간이 빠른 순서대로 sorting후 시간계산
times.sort()
# 초기 결과값 변수 생성
sum = 0
# i번쨰까지 시간소요 값의 합을 계속 계산해서 update 한다
for i in range(n):
    for j in range(i+1):
        sum += times[j]
# 결과 출력
print(sum)
