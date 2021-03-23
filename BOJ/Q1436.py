# n = 1000
n = int(input())
# 666 부터 출발하기 위해서 초기값 665 세팅
i = 665
result_list = []


while n >= 1:
    i += 1
    if '666' in str(i):
        n -= 1
        result_list.append(i)
        continue

print(result_list[-1])
