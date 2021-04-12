n = int(input())

num_list = list(map(int, input().split()))
# 결과 출력 리스트 초기화
result_list = [-1 for _ in range(n)]
stacks = []


for i in range(n):
    # stack에 원소가 있고, stack.top을 인덱스로 하는 num_list가 num_list[i] 보다 작을 경우 
    # : 결과list의 해당 index에 해당하는 위치에 num_list[i] 값을 할당 (오큰수 를 찾았다)
    while stacks and num_list[stacks[-1]] < num_list[i]:
        result_list[stacks.pop()] = num_list[i]
    # stack이 비었을 경우, 현재 idx를 push
    stacks.append(i)

print(*result_list)

# 이중 for문으로 문제 풀었을 떄, -> 시간초과
