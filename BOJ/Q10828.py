import sys

# 스택 클래스 구현
class Stack:
    # 클래스 초기화 - 리스트 생성
    def __init__(self):
        self.stack = []
    # push 함수 생성 - 리스트 데이터 추가
    def push(self, data):
        self.stack.append(data)
    # pop 함수 생성 - 내장함수 pop 사용, len 판별조건 적용
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()
    # empty 함수 생성 - stack 리스트 원소 유무 판별
    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0
    # top 함수 생성 - pop과 달리 데이터 출력만 적용
    def top(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[-1]
    # size 함수 생성 - 리스트 길이 
    def size(self):
        result = len(self.stack)
        return result

# 함수 입력 받기 
input_list = []
for _ in range(int(input())):
    tmp = list(sys.stdin.readline().rstrip().split())
    input_list.append(tmp)

# 스택 리스트 생성
Exstack = Stack()

# 입력 리스트에 있는 함수를 func 조건에 따라 
for i in input_list:
    func = i[0]
    if func == 'push':
        Exstack.push(int(i[1]))
    elif func == 'top':
        print(Exstack.top())
    elif func == 'size':
        print(Exstack.size())
    elif func == 'empty':
        print(Exstack.empty())
    elif func == 'pop':
        print(Exstack.pop())
    else:
        print("func wrong input")

