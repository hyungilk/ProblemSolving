n, target = map(int, input().split())
num_list = list(map(int, input().split()))

# n = 10
# target = 500
# num_list = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]

# 결과 저장 리스트 생성
result_list = []
# 카드 3장을 카드리스트에서 추출하여, tmp_sum을 생성
# 생성한 tmp_sum과 target 을 비교(작거나 같을경우 -> 결과 리스트에 저장)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tmp_sum = num_list[i]+num_list[j]+num_list[k]
            if tmp_sum <= target:
                result_list.append(tmp_sum)
                continue
# 결과 중 최대 값 출력
print(max(result_list))
