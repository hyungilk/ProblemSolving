# find prime number
# use technique : only search prime number until root n

def is_prime(num):
    if num == 1 or num == 0:
        return False
    else:
        n = int(num ** 0.5) + 1
    for i in range(2, n):
        if num % i == 0:
            return False
    return True

n = int(input())
num_list = list(map(int,input().split()))
prime_cnt = 0
for num in num_list:
    if is_prime(num) == True:
        prime_cnt += 1
print(prime_cnt)

