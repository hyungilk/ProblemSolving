
'''
n = 1
    o : 1 1
    x : 0
n = 2
    o : 11 00 2
    x : 10 01
n = 3
    o : 100 001 111 n(1) + n(2) 3
    x : 010 101 110 011 000
n = 4
    o : 0011, 0000, 1001, 1100, 1111 5
홀수 : 홀수(i-2) + 짝수(i-2)
짝수 : 0 -> 짝수(i-1) + 1->홀수 (i-2)
'''
n = int(input())
fibo_list = [0] * (n + 1)
def fibo(num):
    fibo_list[0] = 1
    fibo_list[1] = 1
    if num == 0 or num == 1:
        return fibo_list[num]
    for i in range(2, num+1):
        fibo_list[i] = (fibo_list[i-1] + fibo_list[i-2]) % 15746
    return fibo_list[num]

print(fibo(n))

        
    
    
