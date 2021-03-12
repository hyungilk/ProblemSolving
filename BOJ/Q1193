# author : hyungil ed kim
# date : 21.03.12
# Quiz from : https://www.acmicpc.net/problem/1193

n = int(input())
# n = 14
k = 0
# 1,1 also included as '1'st time

# find group index with 1/2n(n+1)
while True:
    if .5*(k**2+k) >= n:
        index = k
        break
    else:
        k += 1
        continue
target = int(.5*(index**2 + index) - n)

# odd even condition split
if index % 2 == 0:
    x = index - target
    y = 1 + target
else:
    x = 1 + target
    y = index - target

# print result
print('{0}/{1}'.format(x,y))
