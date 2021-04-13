n = int(input())

# 첫번째 소수를 찾는 함수 생성
# 에라토스테네스 체에 따라 소수를 찾는 범위는 sqrt(num) + 1
# 나누어 떨어지는 수를 찾으면 for문을 즉시 종료하고 해당 값을 출력, 나눠지는 값이 없을 경우 0을 출력
def firstPrime(num):
    cnt = int(num ** 0.5) + 1
    result = 0
    for i in range(2,cnt):
        if num % i == 0:
            result = i
            break
    return result


# 반복문 종료조건:n=1
while n > 1:
    # n에 대한 소수를 탐색
    tmp = firstPrime(n)
    # 소수를 찾았을 경우 : 출력 후 n//소수 후 계속 진행
    if tmp != 0:
        print(tmp)
        n //= tmp
    # 소수를 찾지 못할 경우(tmp=0) : 자기자신(n)을 출력하고 while문 
    else:
        print(n)
        break

