import sys

input_list = []
for i in range(int(input())):
    input_list.append(int(sys.stdin.readline()))



# input_list = [5,4,3,2,9,2,9,12,13,15,3]
# input_max = max(input_list)

avg_list = int(round(sum(input_list) / len(input_list),0))
med_list = sorted(input_list)[len(input_list)//2]

frq_dict = {}
for num in input_list:
    if str(num) not in frq_dict.keys():
        frq_dict[str(num)] = 1
    else:
        frq_dict[str(num)] += 1
frq_max_list = [int(k) for k,v in frq_dict.items() if max(frq_dict.values()) == v ]
if len(frq_max_list) == 1:
    frq_result = frq_max_list[0]
else:
    frq_result = sorted(frq_max_list)[1]
# print(sorted(frq_max_list))
range_list = max(input_list) - min(input_list)


print(avg_list)
print(med_list)
print(frq_result)
print(range_list)
