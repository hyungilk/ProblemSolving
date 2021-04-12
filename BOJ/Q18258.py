from collections import deque
import sys

class dequeList():
    def __init__(self):
        self.deques = deque([])
    
    def push(self, data):
        self.deques.append(data)

    def pop(self):
        if len(self.deques) == 0:
            return -1
        else:
            return self.deques.popleft()
    def size(self):
        return len(self.deques)
    def empty(self):
        if len(self.deques) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.deques) == 0:
            return -1
        else:
            return self.deques[0]
    def back(self):
        if len(self.deques) == 0:
            return -1
        else:
            return self.deques[-1] 

deques = dequeList()

n = int(input())
for _ in range(n):
    inputOrder = list(sys.stdin.readline().rstrip().split())
    func = inputOrder[0]
    if func == "push":
        deques.push(int(inputOrder[1]))
    elif func == "pop":
        print(deques.pop())
    elif func == "size":
        print(deques.size())
    elif func == "empty":
        print(deques.empty())
    elif func == "front":
        print(deques.front())
    elif func == "back":
        print(deques.back())
    else:
        print("wrong input")
        break
