# 화면에 가독성 좋게 출력하기 위한 출력 양식/서식 설정
# 방법[1] 서식지정자 방법
# - 형식 : '      %알파벳1개     ' %변수명
# - 서식지정자    %알파벳1개
#   %d(decimal) 10진수 정수
#   %f(float)   타입, 실수 
#   %s(str)     타입, 문자/글자 
# - 1개 출력 형식 : ' %알파벳 '  %변수명
# - 2개 출력 형식 : ' %알파벳 %알파벳 ' %(변수명1, 변수명2)

# [1] str 타입 출력하기
name = "홍길동"
name2 = "의적"
print ("나의 이름은 %s입니다." %name)
print ("이름 %s, 별명 %s" %(name,name2))
       

# [예] 000님! 좋은 하루되세요~^^
# user=input(" ID 입력 : ")
# print ("%s님! 좋은 하루 되세요~^^" %user)

# [2] int 타입 출력하기
kor = 90
math = 88
eng = 100

# 국어 점수 출력하기
print ("국어 점수 : %d" %kor)

# 국어, 수학, 영어 점수 출력하기
print ("국어 : %d , 수학 : %d , 영어 : %d" %(kor, math, eng))

# [3] float 타입 출력하기
avg = 89.4
pi = 3.14

# 평균갑과 pi값 출력하기
print ("평균 : %f, PI : %f" %(avg, pi) )

# [4] int, float, str 혼합해서 출력하기
# 이름, 나이, 키, 몸무게 출력
name ="베트맨"   # str타입
age = 100       # int 타입
height = 180    # int 타입
weight = 91.4   # float 타입

print ("이름 : %s, 나이 : %d, 몸무게 : %d, 몸무게 : %f" %(name, age, height, weight))
