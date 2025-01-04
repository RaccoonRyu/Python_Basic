# 딕셔너리 사용법

# 딕셔너리 Key를 사용해 Value 얻기
grade = {"pey" : 10, "julliet" : 99}
print(grade["pey"]) # Key "Pey"를 통해 Value 10 얻어 출력
print(grade["julliet"]) # Key "julliet"를 통해 Value 99 얻어 출력

a = {1 : "a", 2 : "b"}
print(a[1]) # Key 1을 통해 value "a" 얻어 출력
print(a[2]) # Key 2을 통해 value "b" 얻어 출력

b = {"a" : 1, "b" : 2}
print(b["a"]) # Key "a"를 통해 value 1 얻어 출력
print(b["b"]) # Key "b"를 통해 value 2 얻어 출력

# 정리하면, 딕셔너리가 값을 얻는 방법은 Key를 이용하는 것 단 한 가지 뿐이다. 딕셔너리명[Key값]

# 딕셔너리 생성 시 주의사항
# Key는 고유한 값이므로 중복되는 Key 값을 설정하면 하나를 제외한 나머지 것들이 모두 무시됨을 주의
c = {1 : "a", 1 : "b"}
print(c) # 1개를 제외한 뒤에 입력된 {1: 'b'}만 출력됨을 확인할 수 있음

# Key는 불변하는 값만을 사용해야 하므로 Key에 리스트는 사용할 수 없다.
# 위와 같은 의미로 Key에 불변하는 값인 튜플은 사용할 수 있다.
#d = {[1, 2] : "hi"} # 리스트를 키 값으로 사용할 수 없다는 오류 발생
# 당연히 딕셔너리 또한 Key 값으로 사용할 수 없다.
