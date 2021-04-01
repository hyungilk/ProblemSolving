# a,b,c range is from 0 to 20
n = 21

# dp list 생성
dp = [[[0] * n for _ in range(n)] for _ in range(n)]

# w 생성함수 설계
def w(a,b,c):
    # dp 조건
    dp[0][0][0] = 1
    if a <= 0 or b <= 0 or c <= 0:
        return dp[0][0][0]
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

while True:
    a, b, c = list(map(int, input().split()))
    if a == -1 and b == -1 and c == -1:
        break
    print('w({0}, {1}, {2}) = {3}'.format(a,b,c,w(a,b,c,)))
