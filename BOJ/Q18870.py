# index 내장함수 사용시 시간초과 -> index 함수 수행 시 O(n) 시간 소요
# dictionary 사용하는 방식으로 변경

# index 사용 시
'''
import sys
n = int(input())
num_list = list(map(int, input().split()))
sort_set = sorted(set(num_list))
result_list = []
# print(sort_set)
for i in range(n):
    idx = sort_set.index(num_list[i])
    result_list.append(idx)
print(*result_list)
'''

# dictionary 사용 시
import sys
n = int(input())
num_list = list(map(int, input().split()))
sort_set = sorted(set(num_list))
dict = {}
# print(sort_set)
for i in range(len(sort_set)):
    dict[sort_set[i]] = i

for i in range(n):
    print(dict[num_list[i]], end=" ")
