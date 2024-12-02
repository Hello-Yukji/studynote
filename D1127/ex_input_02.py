# 키보드로부터 입력 받는 input () 함수
# 문법/규칙 : input ("입력받고 싶은 데이터 요청 메세지")
# 특징 : 키보드에서 엔터키 입력할때까지 모든 데이터를 전달함 
#       키도드에서 입력된 데이터는 전부 글자데이터 입니다.

## [예] 숫자 덧셈 하기 => + 덧셈 기호
print (10+30)
print (10-8)

x = 10
y = 30
print (x+y, x-y)

## 숫자 입력 받아서 계산하기
x = input ("숫자 입력 :")
y = input ("숫자 입력 :")

## 키보드에서 입력 받은 숫자는 숫자가 아닌 글자/문자 입니다.
## 1        <= 정수
## '1'  "1" <= '',"" 글자/문자
print (x+y)