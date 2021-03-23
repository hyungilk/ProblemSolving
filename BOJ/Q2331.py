# Q2231 분해합

n = int(input())
# n = 216

# 조건에 해당하는 값 저장하는 리스트
num_list = []
answer = 0
# 각자리의 숫자합 + 숫자 == 입력값 충족하는지 테스트
# 범위 1~n까지
for k in range(1,n+1):
    # 각 자리 숫자의 합
    each_num = 0
    # for문을 위해 string으로 형변환
    num = str(k)
    # 각 자리 숫자의 합 저장
    for ch in num:
        each_num += int(ch)
    # 각자리 숫자합 + 숫자 == n 체크, 일치할 경우 출력
    if (k+each_num) == n:
        answer = k
        break
#  정답 출력
if answer != 0:
    print(answer)
else:
    print(0)


