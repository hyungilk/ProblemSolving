n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))


def padoban(num):
    pado_list = [0,1,1,1]
    if num in [1,2,3]:
        return pado_list[num]
    for i in range(4, num+1):
        tmp = pado_list[i-2] + pado_list[i-3]
        pado_list.append(tmp)
    return pado_list[num]

for num in num_list:
    print(padoban(num))
