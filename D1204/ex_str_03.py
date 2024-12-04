# 문자열 str 타입 다루기
# - 문자열에서 일부 문자 또는 문자열 추출
# - 방법 : 슬라이싱
# - 형식 : 변수명 [시작인덱스 : 끝인덱스 +1]

# # [1] 여러개의 원소 읽기
# msg = "Happy New Year!"
# #      012345678901234
# # => New 만 출력하기
# print(msg[6], msg[7], msg[8], sep = '')

# # => New Year 만 출력하기
# print(msg[6], msg[7], msg[8],msg[9], msg[10], msg[11],msg[12], msg[13], sep = '')
# print(msg[6:14])

# # [2] 문자열의 부분만 읽기 즉, 슬라이싱하기
msg = "Merry Christmas ^^ Happy 2025!!"

# => Happy 만 출력하기
print(msg[19:24], msg[-12:-7], msg[-12:24])

# => Christmas ^^ 만 출력하기
print(msg[6:18])

# [3] 특별하녀서 간편한 슬라이싱
msg = "Good Luck~♥"

# => Good 부분만 출력하기
# => 변수명[ :끝인덱스] : 처음부터 즉, 0번 원소부터
print (msg[0:4])

# => Luck~♥ 부분만 출력하기
# => 변수명[ 시작인덱스:] : 끝까지 의미 즉, -1번 원소까지
print(msg[5:11])
print(msg[5:]) 

# => Good Luck~♥ 출력
# => 변수명 [:] => 처음부터 끝까지 의미
print(msg[0:11], msg[:])