num = input()

num_list = []
for n in num:
    num_list.append(n)
num_list.sort(reverse=True)

print(''.join(num_list))
