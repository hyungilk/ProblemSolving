n, m = list(map(int,input().split()))

# n, m = 4, 3

# 출력용 리스트, used 확인용 리스트 생성
arr = [0] * 9
used = [False] * 9

def solve(num):
    # 재귀함수 종료 조건 
    if num == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    # 반복숫자 출력
    for i in range(1,n+1):
        # used 확인용 리스트 조건 불필요 
        # if used[i]:
        #     continue
        used[i] = True
        arr[num] = i
        solve(num+1)

        for j in range(n+1):
            used[j] = False

    return
solve(0)


