# 불(bool) 자료형
# 참(True), 거짓(False)을 나타내는 자료형
# True, False는 파이썬의 예약어로 true, false로 사용하지 말고 첫 문자를 항상 대문자로 사용해야 한다.

a = True
b = False

# type 함수로 자료형 파악
# type(x) : 값 x의 자료형을 확인하는 함수
print(type(a))
print(type(b)) # a, b 두 변수 모두 자료형이 bool로 지정된 것을 확인할 수 있음. <class 'bool'>

# 불 자료형은 조건문의 반환 값으로 사용
print(1 == 1) # True 출력
print(2 > 1) # True 출력
print(2 < 1) # False 출력
