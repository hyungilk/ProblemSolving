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
m = int(input())

prime_list = []
for i in range(n, m+1):
    if is_prime(i) == True:
        prime_list.append(i)
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
