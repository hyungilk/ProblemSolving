n = int(input())
num_list = list(map(int,input().split()))

# n = 10
# num_list = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]

dp_f = [0] * (n+1)
dp_b = [0] * (n+1)
dp_f[0] = 1
dp_b[n] = 1

# 주요 아이디어:
# 11053 문제의 가장긴 증가 부분 수열을 정방향으로 구한값과 역방향으로 구한값을 각각 계산하고
# 같은 index에서 그 값을 더해주어서 정방향(증가수열) 역방향(감소수열) 의 관계를 가지도록 계산한다.
# 정방향 : 숫자가 증가하는 수열
# 역방향 : (정방향 계산의 방향을 바꾸어줌)숫자가 감소하는 수열
# -1을 해주는 이유 : 방향이 바뀌는 순간(증가->감소) 해당 값이 2번 카운팅 되므로

# forward 계산
for i in range(1,n):
    for j in range(i):
        if num_list[i] > num_list[j] and dp_f[i] < dp_f[j]:
            dp_f[i] = dp_f[j]
    dp_f[i] += 1
# backward 계산
for i in range(n-1,-1,-1):
    for j in range(n-1, i,-1):
        if num_list[i] > num_list[j] and dp_b[i] < dp_b[j]:
            dp_b[i] = dp_b[j]
    dp_b[i] += 1

# 다른 방법
# forward 방식을 num_list를 reserver를 한 후 구하고 그 결과값을 다시 뒤집는다.
# 이떄 idx 자리를 유의하여 dp_f + dp_b - 1 계산을 수행한다.

dp = list(map(lambda x,y: x + y - 1, dp_b, dp_f))
print(max(dp))
