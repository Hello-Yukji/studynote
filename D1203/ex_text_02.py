# [실습] 연산자 & 형변환 & 내장함수 실습

# [1] 2개 숫자 데이터 입력 받아서 그 중 큰 숫자를 출력하세요. => max()
# - 출력형태 : -5와 8중 큰 숫자는 8 입니다.
num1 = int(input("숫자 입력1 :"))
num2 = int(input("숫자 입력2 :"))

print(f"{num1}와 {num2}중 큰 숫자는 {max(num1, num2)} 입니다.")

# [2] 2개 숫자 데이터 입력 받아서 거듭제곱값을 출력하세요. ==> pow(a,b) a^b
# - 출력형태 : 8읠 3승 => 512
num3 = int(input("숫자 입력1 :"))
num4 = int(input("숫자 입력2 : "))

print(f'{num3}의 {num4}승 : {pow(num3,num4)}')

# [3] 숫자 데이터를 입력 받은 후 숫자 데이터 여부 검사 출력
#     그리고 그 숫자의 2진수, 8진수, 16진수를 출력하세요.
# 출력형태 : 3은 숫자 데이터 입니다.
#         : 3의 2진수 0b11 => 내장함수 bin() {bin(num)}")
#         : 3의 8진수 0b3 
#         : 3의 16진수 0x3

num5 = int(input("숫자 입력1 :"))
print (f"{num5}은 숫자 : {num5 >="0 and num5 <= 9}")
print(f"{num5}의 2진수 {bin(num5)}")
print(f"{num5}의 8진수 {oct(num5)}")
print(f"{num5}의 16진수 {hex(num5)}")


