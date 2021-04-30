texts = input()

# 아이디어 :
# '-' 가 처음 나온 후에 (를 생성하고 '-'가 다시 나오는 경우 )로 닫아준다

# '-'로 string을 분리하고 각각의 sub-string을 덧셈처리하고,
# sub-string[0]에서 모두 뺄셈을 해준다

# '-' 기호로 입력 문자열을 분리
sub_text = list(texts.split('-'))

# 결과값 저장용 리스트 생성
resultList = []

# '-'로 분리된 문자열을 각각 덧셈계산
for text in sub_text:
    # 임시 변수 선언
    tmp = 0
    # '+' 기호가 있는 경우 문자열 분리
    sub_chrs = list(text.split('+'))
    # 분리된 숫자 계산
    for ch in sub_chrs:
        tmp += int(ch)
    # 결과 리스트에 append
    resultList.append(tmp)
# 첫 '-'가 나오기 전 까지의 숫자는 모두 덧셈 수행
result = resultList[0]
# 그 다음부터 오는 숫자들은 모두 뺄셈
for i in range(1,len(resultList)):
    result -= resultList[i]
# 결과 값 출력
print(result)

