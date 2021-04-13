# 총 복잡도 O(n^0.5)
a,b = list(map(int,input().split()))
is_prime = [True] * (b+1)
# 1은 소수에 포함되지 않는다
is_prime[1] = False
for i in range(2, int(b**0.5)+1):
    # 이미 False로 판별된 경우에는 계산 대상에서 제외
    if is_prime[i]:
        # 소수(i)의 제곱수 이후 배수들을 모두 리스트에서 제거 -> 중복계산 방지
        is_prime[(i**2)::i] = [False] * ((b - i**2) // i + 1)

# 소수로 남아 있는 List 결과값들만 출력
for i in range(a, b+1):
    if is_prime[i]:
        print(i)

        
# 계산시간 과다 소요 -> 상위 코드로 개선
'''
a,b = list(map(int,input().split()))
# 소수 판단 함수
# O(sqrt(n))
def isPrime(num):
    if num == 1 or num == 0:
        return False
    cnt = int(num ** 0.5) + 1
    for i in range(2,cnt):
        if num % i == 0:
            return False
    return True

# start~end 탐색에 따른 시간 n이 소모 됨
# 결국 O(n^3/2) 복잡도가 발생하게 됨
for i in range(a,b+1):
    if isPrime(i) == True:
        print(i)
        continue
    '''


