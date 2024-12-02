# 화면에 가독성 좋게 출력하기 위한 출력 양식/서식 설정
# 방법[2] f-string 방법
# - 형식 : F' {변수명}  {변수명}'
#          f ' {변수명}  {변수명}'

# [1] 이름과 나이 출력
# 출력형태 => 이름은 000이고, 나이는 00입니다.
name = '베트맨'
age = 100
print (f"이름은 {name}이고, 나이는 {age}입니다 ")
print ('이름는 %s이고, 나이는 %d입니다.' %(name, age))

# [2] 3개의 숫자를 입력받아서 4칙연산 결과를 출력하세요.
# 4칙연산 : 덧셈(+), 뺼셈(-), 곱셈(*), 나눗셈(/)
num1 = input ( "숫자 1 :")
num2 = input ( "숫자 2 :")
num3 = input ( "숫자 3 :")

# 키보드 입력 => 데이터는 전부 str 타입 => int 형변환 필요
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# 4칙연산 결과 출력
# 출력형태 => 0 + 0 +0 = 0
print (f'{num1} + {num2} + {num3} = {num1+num2+num3}') 
print (f'{num1} - {num2} - {num3} = {num1-num2-num3}') 
print (f'{num1} * {num2} * {num3} = {num1*num2*num3}') 
print (f'{num1} / {num2} / {num3} = {num1/num2/num3}') 
