import sys

input_list = []
for i in range(int(input())):
    input_list.append(int(sys.stdin.readline()))



# input_list = [5,4,3,2,9,2,9,12,13,15,3]
# input_max = max(input_list)


avg_list = int(round(sum(input_list) / len(input_list),0))
med_list = sorted(input_list)[len(input_list)//2]

# couting 용 dictionary 생성
frq_dict = {}
for num in input_list:
    if str(num) not in frq_dict.keys():
        frq_dict[str(num)] = 1
    else:
        frq_dict[str(num)] += 1
frq_max_list = [int(k) for k,v in frq_dict.items() if max(frq_dict.values()) == v ]
frq_dict = sorted(frq_max_list)
if len(frq_max_list) == 1:
    frq_result = frq_max_list[0]
else:
    frq_result = frq_max_list[1]
print(sorted(frq_max_list))

# dictionary max, min value 활용
range_list = max(frq_dict.keys()) - min(frq_dict.keys())


print(avg_list)
print(med_list)
print(frq_result)
print(range_list)
