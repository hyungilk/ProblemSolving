# author : hyungil ed kim
# date : 21.03.12
# Quiz from : https://www.acmicpc.net/problem/10250

# H, W, N = 30, 50, 72

for _ in range(int(input())):
    H, W, N = map(int, input().split())
    
    room = N // H + 1
    floor = N % H

    if floor == 0:
        room -= 1
        floor = H

    if room < 10:
        print('{0}0{1}'.format(floor,room))
    else:
        print('{0}{1}'.format(floor,room))








