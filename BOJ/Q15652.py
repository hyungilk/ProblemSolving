n, m = list(map(int,input().split()))

# n, m = 3, 3

# 결과 출력용 리스트 생성
arr = [0] * (m+1)

# solver 함수 정의
# 로직 : 1~n까지의 자연수를 m번 출력
# 조건 : 중복 추출 가능, arr[i] >= arr[i-1] 앞자리의 원소보다는 항상 크거나 같아야한다.
def solve(num):
    # solver 출력 조건
    if num == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    # 리스트의 첫번쨰 원소 -> 앞자리 원소 비교조건에 해당되지 않음 -> 예외 처리
    if num == 0:
        for j in range(1,n+1):
            arr[num] = j
            solve(num+1)
    # 두번째 원소 부터는 직전자리 원소와 비교조건 만족하는 결과만 출력하도록 함
    else:
        for j in range(1, n+1):
            if arr[num-1] <= j:
                arr[num] = j
                solve(num+1)

solve(0)




