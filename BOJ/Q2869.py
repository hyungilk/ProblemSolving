# author : hyungil ed kim
# date : 21.03.12
# Quiz from : https://www.acmicpc.net/problem/2869

up, down, h =map(int, input().split())

# 숫자 올림 함수 
def roundUp(num):
    if (num*10) % 10 > 0:
        num = int(num) + 1
    else:
        num = int(num)
    return num
# 계산 식 : 목표 높이에서 첫날 올라갈수 있는 만큼을 뺸 수를 up - down 으로 나눈다
# h - up 하는 이유 : 마지막 날 낮에 올라갈 경우를 미리 계산하여 +1을 통해 보상
# -> 낮+밤 이 지난 후 올라간 총 높이를 계산,
# 만약 그 날에 올라갈 경우는 +1 을 통해 보상 
calc = (h - up) / (up - down)
day = roundUp(calc) + 1

print(day)
