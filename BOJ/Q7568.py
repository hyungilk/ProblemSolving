hList = []
wList = []
for i in range(int(input())):
  h, w = map(int, input().split())
  hList.append(h)
  wList.append(w)

# hList = [55, 58, 88, 60 ,46]

# wList = [85, 83, 86 ,75, 55]

def cntBigger(hList, wList):
  if len(hList) == 1:
    return [1]
  resultList = []
  for i in range(len(hList)):
   cnt = 0
    for j in range(len(hList)):
     if hList[i] < hList[j] and wList[i] < wList[j]:
      cnt += 1
    resultList.append(cnt+1)
  return resultList

for num in cntBigger(hList, wList):
  print(num, end=' ')
