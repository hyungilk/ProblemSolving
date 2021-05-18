import sys
from collections import deque

input = sys.stdin.readline

# input creation
n, k = map(int, input().split())

# queue list call
queues = deque()
# append nums(1~n) into permutation
for i in range(n):
    queues.append(i+1)

# match question's output format
print("<", end='')

# problemsoloving :
# 1. move 1 to k-1 th elements to end of the queue
# 2. pop and print k th element 
# return and continue while statement
# finish at len(queue) == 1
while queues:
    if len(queues)==1:
        print(queues.pop(), end='')
        break
    for i in range(k-1):
        tmp = queues.popleft()
        queues.append(tmp)
    print(queues.popleft(), end=', ')
    continue

# match question's output format
print(">")
