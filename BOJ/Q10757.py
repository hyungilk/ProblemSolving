
num_1, num_2 = list(input().split())
# num_1 = '9223372036854775807'
# num_2 = '9223372036854775807'

# num1에 무조건 큰 숫자가 오게 스왑
if len(num_1) < len(num_2):
    num_1, num_2 = num_2, num_1
# num1, num2의 자리수가 다른 경우, num2 앞자리에 0을 채워줌
num_2 = num_2.zfill(len(num_1))

# zfill 출력값 확인
# print(num_1, num_2)

# 값 저장 리스트 생성
num_list = []
# 임시 결과값 저장 변수
tmp = 0

# 일의자리 부터 계산하기 위해 리스트의 마지막에서 앞쪽으로 for문 계산
for i in range(len(num_1)-1,-2,-1):
    # 입력 숫자까지 계산, 덧셈에 의해 자리수가 커지게되면 리스트 index 에러 발생
    if i >= 0:
        tmp += int(num_1[i])+int(num_2[i])
    # index error 발생을 막기 위해 tmp를 그대로 유지
    # 하지만 tmp가 0일 경우에는 더이상 리스트에 append하지 않고 for문 종료
    else:
        if tmp == 0:
            continue
    
    # append 시 string으로 하는 이유? -> 리스트 int 원소는 join 불가능
    if tmp >= 10:
        num_list.append(str(tmp%10))
        tmp = tmp//10
    else:
        num_list.append(str(tmp))
        tmp = 0
    # step별 결과값 체크
    # print('i:{0}, num_list {1}'.format(i, num_list))

# 출력을 위해 결과 리스트 순서 반전 
num_list.reverse()
# 리스트의 숫자를 다시 합친 후 출력
print(''.join(num_list))
