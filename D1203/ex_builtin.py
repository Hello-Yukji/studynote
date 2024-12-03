# 파이썬 기본 제공 함수 즉, 내장함수

# # [1] 절대값 돌려주는 함수 = abs(데이터)
# value = 6.7
# print(f"{value} 절대값 : {abs(value)}")

# # value = "-9" ERROR
# value = 9
# print(f"{value} 절대값 : {abs(value)}")


# # [2] 거듭제곱 계산 함수 = pow(데이터, 데이터)
# m = 2
# n = 3
# print(f'{m}의 {n}승 : {pow(m,n)}')

# # [3] 2개 이상의 숫자에서 최대값 구하는 함수 = max(데이터, 데이터)
# print(f"max(9,-3)   : {max(9,-3)}")
# print(f"max(9.1,-3) : {max(9.1,-3)}")
# print(f"max(a, A) : {max("a","A")}")

# # [4] 2개 이상의 숫자에서 최소값 구하는 함수 = min(데이터, 데이터)
# print(f"min(9,-3)   : {min(9,-3)}")
# print(f"min(9.1,-3) : {min(9.1,-3)}")
# print(f"min(a, A) : {min("a","A")}")

# [5] 실수 데이터의 소수점 처리 함수 = round(데이터, 자릿수)
num = 3.1234567
num2 = 3.56789

print(f"{num} => {round(num)}")
print(f"{num2} => {round(num2)}")

# 소수점 없애기 => 소수점 이하 첫자리수가 1이상이면 반올림

print(f"{num} => {round(num,1)}")
print(f"{num2} => {round(num2,1)}")

# 소수점 없애기 => 소수점 이하 두번째 자리수가 5이상이면 반올림

print(f"{num} => {round(num,5)}")
print(f"{num2} => {round(num2,5)}")

# 소수점 없애기 => 소수점 이하 6번째 자리수가 5이상이면 반올림

print(f"{num} => {round(num,5)}")
print(f"{num2} => {round(num2,5)}")