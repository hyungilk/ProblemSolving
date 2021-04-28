# 입력값 처리
# 총 처리 숫자 n, 연산 대상 list, + - * // 각 연산 횟수
n = int(input())
num_list = list(map(int,input().split()))
p, s, m, d = list(map(int, input().split()))

# 최대 최소 비교를 위한 기본 값
maxResult = -1000000000
minResult = 1000000000

# solver 함수 (백트래킹 개념 활용)
# 원리 : 
# 재귀함수 형태를 활용하여 각각의 연산 케이스에 다음 재귀함수를 호출
# 이때, 적절한 연산을 취해서 최대 최소값을 idx==n 경우에 확인해서 update

def solve(num, idx, p, s, m, d):
    global maxResult, minResult
    
    # solver 종료 조건
    if idx == n:
        # max, min 값 update
        maxResult = max(num, maxResult)
        minResult = min(num, minResult)
        # 함수 종료
        return maxResult, minResult
    
    else:
        # 연산기호가 남아있을때 각각 확인해서 연산을 수행, 그후 idx+1 과 각 연산자의 숫자를 1 줄인 후 재귀함수 다시 호출
        # (until idx == x)
        if p:
            solve(num+num_list[idx], idx+1, p-1, s, m, d)
        if s:
            solve(num-num_list[idx], idx+1, p, s-1, m, d)
        if m:
            solve(num*num_list[idx], idx+1, p, s, m-1, d)
        if d:
            # 문제 조건과 동일하게 음수를 나누어줄 때 결과 처리
            if num > 0:
                solve(num // num_list[idx], idx+1, p, s, m, d-1)
            else:
                tmp = (num*-1) // num_list[idx]
                solve(tmp*-1, idx+1, p, s, m, d-1)

solve(num_list[0], 1, p, s, m, d)
print(maxResult)
print(minResult)
