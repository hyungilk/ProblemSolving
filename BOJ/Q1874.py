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
# iteration 횟수
n = int(input())
# 순서 입력 리스트 생성
seq_list = []
# 숫자 임시 저장 리스트 생성(처음값 비교를 위해 최대값보다 큰수 입력)
num_list = [100001]

# seq(수열) 리스트 입력 생성 및, 숫자 역순 리스트 생성
for i in range(n):
    seq_list.append(int(input()))
    num_list.append(n-i)

#stack 생성자 생성
stacks = Stack()
# cnt 값 초기화
i = 0
# 결과값 저장 리스트 생성
result = []
# 정상 작동 flag 값
flag = True

# while문 num_list값이 존재할 때 까지 while문
while num_list:
    # seq_list의 index overflow 방지
    if i == n:
        break
    # stack top과 seq_list(순서 리스트) 값이 같을 경우
    # : stack에서 pop 후 '-' 출력 -> i++ 로 넘어감
    if seq_list[i] == stacks.top():
        stacks.pop()
        result.append('-')
        i += 1
        continue
    # seq_list 값이 num_list의 마지막 값보다 크거나 같을 경우
    # : num_list의 값을 stack에 넣고 '+'를 출력한다
    if seq_list[i] >= num_list[-1]:
        stacks.push(num_list.pop())
        result.append('+')
        continue
    # 위 두가지 케이스가 불가능한 경우 -> 수열 생성 불가능 flag
    else:
        flag = False
        break
# 출력값 
if flag == False:
    print('NO')
else:
    for ch in result:
        print(ch)







