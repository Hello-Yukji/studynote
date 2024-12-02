#input() 함수와 casting 함수를 이용한 계산구현
#2개의 정수를 입력 받기 => input()
num1=input("정수1 입력:")
num2=input("정수2 입력:")

#[2] 입력받은 데이터 확인
print('num1 타입',type(num1))
print('num2 타입',type(num2))

# str=>int 형변환/캐스팅
num1=int(num1)
num2=int(num2)

print('num1 타입',type(num1))
print('num2 타입',type(num2))

#계산하기
print("덧셈",num1+num2)
print("뺄셈",num1-num2)
print("곱셈",num1*num2)
print("나눗셈",num1/num2)
