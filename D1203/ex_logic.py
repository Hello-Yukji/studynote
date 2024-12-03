# 논리연산자
# - 여러개의 조건들을 비교 평가하는 연산자
# - 결과 => True, False
# - 형식
#   * 모든 조건이 True 여야만 하는 경우
#     A and B and C and ...
#   * 일부 조건 / 1개 이상의 조건이 True여야만 하는 경우
#     A or B or C or ... 
#   * 현재 결과의 반대
#     not A = > not True, not False
# # [1] 청소년 9세이상 24세 미만
# age = int(input("나이 입력 :"))

# print((age >= 9) and (age < 24))

# # [2] 미취학아동 8세미만
# age = int(input("나이 입력 :"))

# print((age < 8))

# # [3] 나이와 성별 입력 받아서 검사
# age = int(input("나이 입력 :"))
# gender = input("성별 입력 [남 또는 여] :")

# # 20세 이상이고 여자인 경우 => and
# print("20세이상이고 여성인 경우 : ",(age<=20) and (gender == "여"))

# # 20세 이상이거나 여자인 경우 => or
# print("20세 이상이거나 여자인 경우 : ",(age<=20) or (gender == "여"))

# # [4] 입력받은 데이터가 알파벳인지 판별
# # a, b ..., z, A, B, ..., Z
# print(f"a와 > b비교 :{'a'>'b'}") # 97>98
# print(f"a와 > A비교 :{'a'>'A'}") # 97>65

# data = input("알파벳 1개 입력 :")

# # 소문자 검사
# print(f"data 소문자 여부 : {data >='a'} and {data <= 'z'} = {data >='a'and data <= 'z'}")

# # 대문자 검사
# print(f"data 대문자 여부 : {data >='A'} and {data <= 'Z'} = {data >='A'and data <= 'Z'}")

# # 알파벳 검사
# print(f"data 알파벳 여부 : {data >='a'} and {data <= 'z'} or {data >='A'and data <= 'Z'}")

# [5] 결과를 반대로 만들어주는 논리연산자
# 숫자(0~9)만 입력하기
number = input("숫자만 입력 : ")

is_number = (number >= '0' and number <='9') 

print(f"is_number : {is_number}")
print(f"숫자 입력 여부 체크 : {number} => {is_number}")

# 숫자 (0~9)를 제외한 문자 입력
print(f"숫자 제외 입력 여부 체크 : {number} => {number < '0' or number >'9'}")
print(f"숫자 제외 입력 여부 체크 : {number} => {not is_number}")