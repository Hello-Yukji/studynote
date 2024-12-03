# 복습 문제

# [1] 2개 숫자를 입력 받아서 비교연산 6가지 수행 결과를 출력하세요.
# 입력되는 데이터 : 0~9
# num1 = input("숫자1 : ") # num = int(input("숫자1 :"))
# num2 = input("숫자2 : ")

# num1 = int(num1)
# num2 = int(num2)

# print(f'{num1} > {num2} = {num1 > num2}')
# print(f'{num1} < {num2} = {num1 < num2}')
# print(f'{num1} >= {num2} = {num1 >= num2}')
# print(f'{num1} <= {num2} = {num1 <= num2}')
# print(f'{num1} == {num2} = {num1 == num2}')
# print(f'{num1} != {num2} = {num1 != num2}')


# [2] 생일을 아래와 같은 형식으로 출력하세요.
# 출력  형태 : 12월 24일 2010년 생일축하!
# 년, 월, 일 : 메모리 저장
month = 12
day = 24
year = 2010

# 방식1
print (month,"월 ",day,"일 ",year,"년  생일축하!", sep="")

# 방식2 => 서식지정자 %알파벳
print ("%d월 %d일 %d년 생일축하!" %(month, day, year))

# 방식3 => f-string
print (f"{month}월 {day}일 {year}년 생일축하!")