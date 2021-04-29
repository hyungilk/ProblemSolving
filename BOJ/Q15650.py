n, m = list(map(int,input().split()))

# n, m = 4, 3

# 숫자 출력용 list 생성
arr = [0] * 9
# used 체크용 list 생성
used = [False] * 9

def solve(num):
    # list 출력 조건 (재귀함수 종료 조건)
    if num == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    # 
    for i in range(1,n+1):
        if used[i]:
            continue
        used[i] = True
        arr[num] = i
        solve(num+1)
        # i+1 부터는 다시 for 문을 돌리기 위해서 used리스트를 False로 초기화
        for j in range(i+1, n+1):
            used[j] = False

    return
solve(0)


