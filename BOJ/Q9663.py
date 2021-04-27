# N-Queen

# 문제풀이 ideation : 
'''
체스판에 퀸이 행열(row, col)에 위치해있다고 생각하면,
row = 1 ~ n 까지 열의 위치를 col[row] = 열number(1~n)로 표현 할 수 있음
즉 2행 3열에 퀸이 있다고 생각하면, col[2] = 3이 된다.

퀸이 1행 부터 n행까지 각 행에 1개씩 배치되어야 하므로(한 줄에 2개의 퀸을 배치할 수 없음)
(main 함수)
1. 1행에 퀸을 위치한 후 -> for문을 돌려 1행에서의 퀸의 위치 탐색
(solve 함수)
2. 다음행에 퀸이 위치할 수 있는 경우에는 해당자리에 퀸을 위치하고(eg. col[2] = number 입력
3. 가능하면 solve 함수의 다음행을 call 하고, 그렇지 않으면 continue 한다.
종료조건 : 다른 backtracking 문제와 동일하게 row == n일떄, cnt++ 한 후 종료한다

(퀸check 함수)
k번째 row에 가능한 퀸의 위치는 k-1행까지의 퀸의 위치와 다르면서, 대각선으로도 마주치지 않는 자리를 의미한다.
즉, 1) col[k] != col[i] 
   2) |col[k] - col[i]| != (k - i) 
   (i는 1~k-1 의 숫자)


'''

import math

n = int(input())

cnt = 0
colArr = [0] * (15+1)

def queenChk(row):
    for i in range(1,row):
        if colArr[row] == colArr[i]:
           return False
        if abs(colArr[row]-colArr[i]) == row-i:
            return False
    return True

def solve(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for i in range(1,n+1):
        colArr[row+1] = i
        if queenChk(row+1):
            solve(row+1)
        

for i in range(1,n+1):
    colArr[1] = i
    solve(1)

print(cnt)

