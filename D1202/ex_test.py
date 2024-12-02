# 데이터 형태 변환 즉, 형변환(Type Casting / Casting)

# [1] 이름을 저장 후 bool타입으로 형변환 후 출력
# msg = "팬더"
# print ('str -> bool', bool(msg))
#  ------------------------------
name = '홍길동'
print (bool(name))

# [2] 3.14 데이터를 int타입으로 형변환 후 출력
# msg = 3.14
# print ('float -> int', int(msg))
# ------------------------------
num = 3.14
num = int(num)
print (num)

# [3] 2025 데이터를 float타입으로 형변환 후 출력
year = 2025
print (float(year))


# 입력과 출력

# [1] 숫자 3개를 입력 받으세요. ==> 키보드로부터 입력받기 input()
num1 = input("숫자1 입력:")
num2 = input("숫자2 입력:")
num3 = input("숫자3 입력:")

# 키보드로 입력받은 숫자 데이터의 타입 출력 => type()
print (type(num1), type(num2), type(num3))

# [2] 3개의 숫자를 곱셈한 결과를 출력하세요.
# 곱셈기호 : X ==> *
# 일시적으로 형변환 
print (int(num1) * int(num2) * int(num3))
# num1 = int(num1)
# num2 = int(uum2)
# num3 = int(num3)


