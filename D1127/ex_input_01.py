# 키보드로부터 입력 받는 input () 함수
# 문법/규칙 : input ("입력받고 싶은 데이터 요청 메세지")
# 특징 : 키보드에서 엔터키 입력할때까지 모든 데이터를 전달함 

## [1] 이름 입력 받기
name = input ("이름을 입력하세요.")

print ("당신의 이름은", name, "이군요.")
print (name, "님! 반갑습니다.", sep="")

## [2] 좋아하는 나라를 입력 받기
nara = input ("좋아하는 국가 :")

print (nara, "에 여행가면 좋겠군요:)", sep="")