# 문자열 str 타입의 연산
# - 덧셈(+) : 문자열을 연결해서 새로운 문자열 생성
# - 곱셉(*) : 정수와 곱셈 연산 수행
#             숫자만큼 문자열 반복 연결해서 새로운 문자열 생성

m1 = "Happy"
m2 = "2025"

# 산술 연산 수행
print(f"{m1}+{m2} => {m1+m2}") # str + str 타입끼리만 덧셈 가능
print(f"{m1}+{str(5)} => {m1+str(5)}") # str + str 타입끼리만 덧셈 가능
# print(f"{m1}-{m2} => {m1-m2}") str타입에서 지원하지 않는 연산

print(f"{m1}*5 => {m1*5}") # str * int => 정수 숫자만큼 반복
# print(f"{m1}/{m2} => {m1/m2}") str타입에서 지원하지 않는 연산

# str의 산술 연산 활용
data = "Pithon"

# => "Pithon" ==> "Python" 수정
data = data[0]+ 'y'+ data[2:]

print(data)

line = '*'*50
print(line)
print("TEST")
print(line)