
n = int(input())

bool_3,bool_5 = True, True
# for문 최대 숫자 가능범위 출력 함수 정의
def counter(n, divider):
    bool_tmp = True
    cnt_tmp = 0
    while bool_tmp:
        if n < cnt_tmp * divider:
            bool_tmp = False
        else:
            cnt_tmp += 1
    return cnt_tmp

# 3, 5에 대한 숫자 가능 범위 획득
cnt_3 = counter(n, 3)
cnt_5 = counter(n, 5)

# 결과값 저장 변수
result = 0
# 이중 for문 탈출 boolean
breaker = False
# 바구니 수를 최소화하기 위해 5의 해를 먼저 찾고, 3의 해를 찾는다
for i in range(cnt_3+1):
    for j in range(cnt_5+1):
        if n == i*3 + j*5:
            result = i + j
            breaker = True
            break
    if breaker == True:
        break
# 결과값 출력, 해가 없을 경우 result = 0 이므로, -1 을 출력    
if result != 0:
    print(result)
else:
    print(-1)
    
    

