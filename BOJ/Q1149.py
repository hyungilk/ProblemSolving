import sys

n = int(input())

rgb_price_list = []

for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    rgb_price_list.append(tmp)

# print(rgb_price_list)
rgb_store = [[0,0,0] for _ in range(n+1)]

rgb_store[0][0] = rgb_price_list[0][0]
rgb_store[0][1] = rgb_price_list[0][1]
rgb_store[0][2] = rgb_price_list[0][2]
# print(rgb_store)

for i in range(1, n):
    for j in range(3):
        rgb_store[i][j] = min(rgb_store[i-1][(j+1)%3], rgb_store[i-1][(j+2)%3]) + rgb_price_list[i][j]

print(min(rgb_store[n-1]))
