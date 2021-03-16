

import sys
sys.setrecursionlimit(10000)

starArr = []
def starMark(n):
    global starArr
    for _ in range(n):
        starArr.append(['*']*n)
    
    # count '3' 
    cnt = 1
    cnt_temp = n
    while cnt_temp != 1:
        cnt += 1
        cnt_temp /= 3

    if n == 1:
        return starArr
    
    # 3의 지수 만큼 프랙탈이 반복
    # e.g. 
    # n = 9 일떄, 3**2 -> 9프랙탈, 3프랙탈
    # n = 27 일떄, 3**3 -> 27프랙탈, 9프랙탈, 3프랙탈
    for i in range(cnt):
        # 단위 프랙탈의 가운데가 비게 하는 index 찾기
        # e.g.
        # 27 일떄, 9/9/9 의 가운데가 비어야 함
        # 9 일때, 3/3/3/ 의 가운데가 비어야 함
        # 3 일때, 1/1/1/ 의 가운데가 비어야 함
        # -> 반복적으로 index를 표시
        index = [x for x in range(n) if (x // 3 ** i) % 3 == 1]
        
        # 찾은 index를 빈칸으로 변경
        for i in index:
            for j in index:
                starArr[i][j] = ' '
    return starArr


num = int(input())
    
result = starMark(num)
for _ in result:
    print("".join(_))

