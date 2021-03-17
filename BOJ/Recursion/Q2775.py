# 방의 사람 숫자 세는 재귀함수 호출
# 방법 : 바닥층(floor = 0) -> 호수(room) 가 사람수
# n층일 경우, n-1층의 k:1~i 번까지의 호수의 사람수 모두 더하기
# -> floor-1 후, for문을 통해 1~i까지의 재귀함수를 모두 더해서 return
'''
def peopleCount(floor, room):
    if floor == 0:
        return room
    temp = 0
    for i in range(room):
        temp += peopleCount(floor-1,i+1)
    return temp 
'''

n = int(input())
for _ in range(n):
    input_floor = int(input())
    input_room = int(input())
# 일반 for문 규칙 찾기

    # 2차원 list 생성 
    # floor 에 1을 더하는 이유 : 0층부터 시작해서 n층까지 -> n+1개층
    peopleArr = [[0]*(input_room) for _ in range(input_floor+1)]
    # floor, room에 따라서 계산 적용
    for f in range(input_floor+1):
        for r in range(input_room):
            # 0층일떄는 1,2,3,4 ... 대로 숫자 채우기
            if f == 0:
                peopleArr[f][r] = r+1
                continue
            # 1호(r=0)일때는 아래층의 1호의 값 그대로 가져 오기
            if r == 0:
                peopleArr[f][r] =peopleArr[f-1][r]
                continue
            # 나머지 케이스에는 f-1층의 1호 부터 n호까지(r=0 ~ r 까지 가져오기)
            for i in range(r+1):
                peopleArr[f][r] += peopleArr[f-1][i]
    # 최종값 출력 : index 맞추기 위해 room -1 적용, floor 은 n+1개 층이 포함 
    print(peopleArr[input_floor][input_room-1])
