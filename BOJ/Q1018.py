m, n =map(int, input().split())
mapOrigin = []
for _ in range(m):
    mapOrigin.append(input())


def countPaint(map):
# 8 x 8 color count
    map_firstW = map
    map_firstB = map
    count_firstW = 0
    count_firstB = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and map_firstW[i][j] == 'B':
                count_firstW += 1
                map_firstW[i][j].replace('B','W')
            elif (i+j) % 2 != 0 and map_firstW[i][j] == 'W':
                count_firstW += 1
                map_firstW[i][j].replace('W','B')
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and map_firstB[i][j] == 'W':
                count_firstB += 1
                map_firstB[i][j].replace('W','B')
            elif (i+j) % 2 != 0 and map_firstB[i][j] == 'B':
                count_firstB += 1
                map_firstB[i][j].replace('B','W')
    if count_firstB > count_firstW:
        result = count_firstW
    else:
        result = count_firstB
    return result

countList = []
for i in range(m-8+1):
    for j in range(n-8+1):
        mapInstance = [mapOrigin[i][j:j+8] for i in range(i,i+8)]
        # print('before : ', mapInstance)
        tmpResult = countPaint(mapInstance)
        # print('after', tmpResult)
        countList.append(tmpResult)

print(min(countList))
