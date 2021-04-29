# n, k = 10, 4200

# 문자 입력
n, k = list(map(int,input().split()))
# 동전 리스트 생성 및 입력 받기
coins = []
for _ in range(n):
    coins.append(int(input()))

# 메인 아이디어 : 그리디 알고리즘
# 단위가 가장 큰 동전부터 동전세기를 진행 -> 최적 알고리즘
# 이전 동전의 선택과 남은 잔돈은 독립적

# 큰 동전부터 카운팅 하기 위해 크기순서대로 sorting 진행
coins.sort(reverse=True)

# 동전 세는 목표 target 설정
target = k
# 동전 counter 변수 설정
cnt = 0
# coins 리스트의 인덱스 초기값 설정
idx = 0

# 반복문 종료조건 설정 : coins index range error방지 & target 0 이상
while (idx < len(coins)) and (target > 0):
    # target값 보다 빼줄 수 있는 동전의 단위가 적을 경우 : 
    # target값 동전세기 진행, counter ++
    if coins[idx] <= target:
        target -= coins[idx]
        cnt += 1
    # 동전의 단위가 더 큰경우 : 더 작은 동적으로 index 이동
    else:
        idx += 1
# counter     
print(cnt)
