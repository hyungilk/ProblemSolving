import sys

# 스택 클
class Stack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

# Stack class 생성자
Exstack = Stack()

# iteration 횟수 입력
n = int(input())


for _ in range(n):
    tmp = int(sys.stdin.readline())
    # 입력이 0이 아닐경우 push
    if tmp != 0:
        Exstack.push(tmp)
    # 입력이 0일 경우 pop
    else:
        Exstack.pop()
# 최종 결과 리스트 저장
result = Exstack.stack
# 합계 
print(sum(result))
