# 객체(Object)
# - 메모리 힙(Heap) 영역에 저장된 데이터들을 통칭하는 용어
# - int 타입, float 타입, str타입, bool 타입, ... 타입, ...
# 
# 비교연산자 : 데이터의 타입 비교 X 순수 값 비교
num1 = 10       # <= int 타입   : int타입의 인스턴스
num2 = 10.0     # <= float 타입 : float타입의 인스턴스

print (f"{num1} > {num2} : {num1 > num2}")
print (f"{num1} == {num2} : {num1 == num2}")

# 객체비교연산자 : 데이터의 타입 비교
# A is B     : A와 B가 같다
# A is not B : A와 B가 다르다

num1 = 10
num2 = 10.0
num3 = 11
num4 = 10

print(f"{num1} is {num2} : {num1 is num2}")
print(f"{num1} is {num3} : {num1 is num3}")
print(f"{num1} is {num4} : {num1 is num4}")

print(f"id(num1) 메모리 주소 : {id(num1)}")
print(f"id(num2) 메모리 주소 : {id(num2)}")
print(f"id(num3) 메모리 주소 : {id(num3)}")
print(f"id(num4) 메모리 주소 : {id(num4)}")