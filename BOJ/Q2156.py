import sys

n = int(input())
# wine, dp 리스트 생성
wine = [0] * 10001
dp = [0] * 10001
for i in range(1,n+1):
    wine[i] = int(sys.stdin.readline().rstrip())

# winecount 함수 생성
def wineCount(wine):
    # dp 입력값 초기화
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    dp[3] = max(wine[1], wine[2]) + wine[3]
    # 로직 : 
    '''
    i-th case :
    1) ? ? O X O --> dp[i]= dp[i-2] + wine[i]
    2) ? O X O O -->      = dp[i-3] + wine[i-1] + wine[i]
    3) O X X O O -->      = dp[i-4] + wine[i-1] + wine[i]
    3) case가 들어가는 이유? : 2번 케이스가 OOO을 보장하지 않기 문???
    '''
    for i in range(4, n+1):
        dp[i] = max(dp[i-2], dp[i-3]+wine[i-1],dp[i-4]+wine[i-1]) + wine[i]
    # dp 리스트 중 최대값 선택    
    return max(dp)
    

print(wineCount(wine))

