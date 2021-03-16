#재귀함수 run time error 제한
import sys
sys.setrecursionlimit(1000)

# 입력 
n = int(input())
# n = 3
# 크기에 맞는 list 생성 - 초기값 '*' 로 채우기
star = [['*']*n for _ in range(n)]
# print(star) 

# 3의 제곱수 체크 -> 
expo_chk = n
cnt = 0
while expo_chk != 1:
    expo_chk // 3
    cnt += 1

for n in range(cnt):
    index = [i for i in range(n) if (i // 3**n) % 3== 1 ]
    for i in index:
        for j in index:
            star[i][j] = ' '
print(star)
