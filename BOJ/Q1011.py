# start = 45
# end = 50

for _ in range(int(input())):
    start, end = map(int,input().split())

    # 처음 거리 측정
    dist = end - start

    # 초기 변수 생성
    k = 0
    cnt = 0
    def stepupDistance(num):
        result = num + 0.5 * (num**2 - num)
        return result

    while True:
        # 잔여 거리가 0 이면 종료
        if dist == 0:
            break
        # 다음 스탭 가능여부 판단
        # 남은 거리가 k+1, k, k-1 움직임을 했을 때 충분한 거리인지를 판단

        if stepupDistance(k+1) <= dist:
            k += 1
            dist -= k   
        elif stepupDistance(k) <= dist:
            k += 0
            dist -= k
        else:
            k += (-1)
            dist -= k
        # 스탭 횟수 count
        cnt += 1
        # print('k:{0}, dist:{1}'.format(k,dist))

    # 결과 출력
    print(cnt)



