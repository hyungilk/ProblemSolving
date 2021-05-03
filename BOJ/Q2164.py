from collections import deque
# 큐 리스트 생성
queue = deque([])
# n 입력
n = int(input())

# 큐에 숫자 입력
for i in range(1,n+1):
    queue.append(i)
# while문 종료 조건 : 문자가 하나 남았을 경우
while len(queue) > 1:
    # 가장 앞의 문자를 제거
    queue.popleft()
    # 가장 앞의 문자를 빼서 가장 뒤로 보낸다
    # 즉, popleft를 temp에 저장한 다음, append로 다시 큐에 마지막에 삽입한다
    tmp = queue.popleft()
    queue.append(tmp)

# 큐에 마지막 남은 숫자를 출력한다
print(queue.pop())
