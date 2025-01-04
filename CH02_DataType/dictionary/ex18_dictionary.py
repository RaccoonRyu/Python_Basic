# 딕셔너리
# Key와 Value를 한 쌍으로 갖는 자료형
# 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다.
# 기본형 : {Key1 : Value1, Key2 : Value2, ....}
# Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값/변하지 않는 값 모두 사용할 수 있다.

a = {1 : "hi"} # Key로 정수, Value로 문자열 사용용
b = {"a" : [1, 2, 3]} # Value에 리스트 넣을 수 있음

# 딕셔너리 쌍 추가
c = {1 : "a"}
c[2] = "b" # 딕셔너리 c에 Key는 2, Value는 b인 딕셔너리 쌍이 추가된다.
print(c)
c["name"] = "pey" # 딕셔너리 c에 Key는 name, Value는 pey인 딕셔너리 쌍이 추가된다.
print(c)
c[3] = [1, 2, 3] # 딕셔너리 c에 key는 3, Value는 리스트 [1, 2, 3]을 가지는 쌍이 추가된다.
print(c)

# 딕셔너리 요소 삭제
del c[1] # del 딕셔너리명[Key값]을 사용하면 해당 Key에 해당하는 Key-Value 쌍이 삭제된다.
print(c)

