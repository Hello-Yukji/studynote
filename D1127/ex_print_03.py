# print() 함수 활용하기
# 사용자가 화면에서 글자를 보기 쉽게 줄바꿈 후 출력기능
### => 이스케이프문자 : \ + 알바벳1개
### 줄바꿈 이스케이프문자 : \n
### 탭(tab)키 간격 이스케이프문자 : \t
print("Happy New Year!")
print("Happy \nNew \nYear!")
print("H\ta\tp\tp\ty")

### 문법  ===> print( end="\n") 출력할 재료 끝 부분에 \n을 자동으로 붙임/추가함
print("Merry Christmas!")
print("Happy New Year!", end="♥♡♥♡♥♡♥♡")
print(2025)