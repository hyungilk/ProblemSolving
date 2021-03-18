

'''
# 하노이 단순 카운트
def hanoiCount(n):
    if n == 1:
        return 1
    return 2*hanoiCount(n-1) + 1
result = hanoiCount(n)
print(result)
'''

n = int(input())

# tower title apply
t1 = '1'
t2 = '2'
t3 = '3'
# create empth history logging list
moveHist = []

# creat hanoiMove func. 
def hanoiMove(n, start, end, temp):
    # if n == 1, move only in start -> end
    if n == 1:
        moveHist.append([start, end])
    # else, there is sequences in 3 step 
    # 1) n-1 group moves at start -> temp tower | temp <- end tower
    # 2) n plate goes from start to end
    # 3) n-1 group moves at temp -> end tower | temp <- start tower
    else:
        hanoiMove(n-1, start, temp, end)
        moveHist.append([start, end])
        hanoiMove(n-1, temp, end, start)

# proceed hanoi movement
hanoiMove(n,t1,t3,t2)
# print counts
print(len(moveHist))
# print each element
for i in range(len(moveHist)):
    for j in moveHist[i]:
        print(j, end=' ')
    print()
