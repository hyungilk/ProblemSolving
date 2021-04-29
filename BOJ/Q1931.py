# n 입력이 많은 테스트 케이스 -> sys의 readline을 활용
# 미사용시 대비 시간단축 10배 이상(4268ms -> 368ms)

import sys
input = sys.stdin.readline

# 문제 입력 리스트 생성
n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int,input().split())))

# 문제풀이 아이디어 :
# 회의 종료 시점이 빠른 순서부터 고른 후 시작시점이 가장 빠른 회의를 선택한다
# -> sorting
meetings.sort(key=lambda x : (x[1], x[0]))

# sorting을 하였기 때문에 처음에 있는 회의가 무조건 선택되어야 한다
idx = 0
# 이미 1개의 회의가 선택되었으므로 counter는 1부터 시작된다
cnt = 1

for i in range(1,n):
    # 이전 회의 종료시점 이후에 새로운 회의가 시작되어야 선택할 수 있음
    # 단순 for문을 돌리더라도 이미 회의시작 시점이 빠른 순서대로 sorting이 되어 있음
    # for문에 먼저 선택된 회의의 순서를 바로 다음 index로 update 한다.
    if meetings[i][0] >= meetings[idx][1]:
        cnt += 1
        idx = i
    # print(meetings[idx],i, idx, cnt)

# 정답 출력
print(cnt)
