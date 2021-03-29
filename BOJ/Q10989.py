import sys

n = int(input())
num_list = [0] * (10000 + 1) 
for i in range(n):
    idx = int(sys.stdin.readline().rstrip())
    # print(idx)
    num_list[idx] += 1

for i in range(1, len(num_list)):
    if num_list[i] > 0:
        for j in range(num_list[i]):
            print(i)
