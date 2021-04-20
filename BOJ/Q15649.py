
# n, m 값 입력
n, m = list(map(int, input().split()))

# 수열 저장용 리스트 생성
num_list = [0] * 9
# 방문여부 저장 리스트 생성
used = [False] * 9

# num의 의미 -> 각 자리수에 적합한 숫자 입력
def solve(num):
    # 숫자 입력이 종료된경우 : 수열의 숫자를 출력
    if num == m:
        for i in range(m):
            print(num_list[i], end=' ')
        print()
        return

    # for문 로직 순서
    # 1) 1~n 숫자가 used 리스트에 있는지 확인
    # 2) 사용되지 않은 경우 used 표시
    # 3) 해당 자리의 num_list에 해당 숫자를 삽입
    # 4) 다음 자리수에 숫자를 테스트하도록 재귀함수 호출
    # 5) 재귀함수 호출 종료 후 숫자 방문여부 초기화
    
    # 2-2) 숫자가 사용된 경우 : 바로 return 처리 하여 그 이후를 탐색하지 않음(num == m 조건에 부합하지 않으므로 출력값 없음)
    for i in range(1,n+1):
        if not used[i]:
            used[i] = True
            num_list[num] = i
            solve(num+1)
            used[i] = False
    return

solve(0)




