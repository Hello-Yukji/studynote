# 문자열 str타입과 원소변경 => 불가능!!!
# - 변수명 [인덱스] : 특정 인덱스 원소 읽기, 가져오기
# - 변수명 [인덱스] = "새로운값" X

msg = "pithon"

# 오타 수정 => 1번 인덱스의 "i" ==> "y" 변경
msg[1] = "y"

print (f"id(msg)    => {id(msg)}")
print (f"id('pithon') => {id('pithon')}")
