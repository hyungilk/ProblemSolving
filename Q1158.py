# 1158

import sys
from collections import deque

input = sys.stdin.readline

# Assign input variable
n, k = list(map(int, input().split()))

# create number list with deque
num_list = deque(list(range(1,n+1)))

# print first braket
print("<", end='')

# while loop with deque 
# process : before k, move the first element to the last slot
#           at k, pop the first element and re-run while loop 
while len(num_list)>1:
    for i in range(1,k+1):
        if i%k == 0:
            print(num_list.popleft(), end = ", ")
        else:
            num_list.append(num_list.popleft())

# print last element and braket
print(num_list.popleft(),end='')
print(">")





