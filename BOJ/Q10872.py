import sys
sys.setrecursionlimit(100000)

n = int(input())

def fact(num):
    if num == 1 or num == 0:
        return 1
    return fact(num - 1) * num
print(fact(n))
