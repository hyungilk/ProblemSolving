# text = 'So when I die (the [first] I will see in (heaven) is a score list).'

# stack 클래스 생성
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)

    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]
    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            tmp = self.stack.pop()
            return tmp

# 반복구문 생성
while True:
    # 텍스트 입력 저장
    text = input().rstrip()
    # break 조건 입력
    if len(text) == 1 and text[0] == '.':
        break
    # 스택 생성자 호출
    stacks = Stack()
    # for문 종료 flag 생성
    flag_true = True
    # for문 설계
    # 1.text 내 있는 문자 호출
    # 2. (, [ 가 나올 경우 스택에 push
    # 3. ), ] 이 나올 경우 스택에 complement 기호가 있는지 파악하고(top 활용) 맞을 경우 pop
    # 4. 아닐 경우 for문 강제 종류 후 flag 판별
    for ch in text:
        if ch == '(':
            stacks.push(ch)
            continue
        if ch == '[':
            stacks.push(ch)
            continue
        
        if ch == ')' and stacks.top() != '(':
            flag_true = False
            break
        if ch == ']' and stacks.top() != '[':
            flag_true = False
            break
        
        if ch == ')' and stacks.top() == '(':
            stacks.pop()
            continue
        if ch == ']' and stacks.top() == '[':
            stacks.pop()
            continue

    if flag_true == True and len(stacks.stack) == 0:
        print('yes')
    else:
        print('no')




