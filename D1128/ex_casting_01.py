#데이터의 타입 확인하기
print(type(3.4),type('a'),type('apple'))
print(type(1),type('1'))
print(type(True))

age=100
name='홍길동'
print(type(age),type(name))

#[1] 정수의 타입 변경
num=100

print(type(num))

print(float(num)) #원래 데이터가 변경되지는 않음
print(num)

num=float(num) #형변환된 데이터가 저장
print(num.id(num))


#함수의 결과값 
value=sum([10,20])
print(value)
value2=print("A")
print(value2)



#파이썬은 클래스 형태로 데이터를 저장 붕어빵틀 처럼 어떤 형태로 저장