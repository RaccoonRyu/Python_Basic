# 조건문이란?
# 참과 거짓을 판단하는 문장

# 조건문에 사용하는 비교 연산자
# 비교 연산의 결과로 참/거짓을 반환하여 조건문에 사용할 수 있다.
"""
비교연산자 설명
x < y x가 y보다 작다
x > y x가 y보다 크다
x == y x와 y가 같다
x != y x와 y가 같지 않다
x >= y x가 y보다 크거나 같다
x <= y x가 y보다 작거나 같다
"""

# 비교 연산자 사용 예시
x = 3
y = 2
print(x > y)  # True 출력
print(x < y)  # False 출력
print(x == y)  # False 출력
print(x != y)  # True 출력

# 비교 연산자를 사용한 조건문 예시
money = 2000
if money >= 3000:
    print("택시를 타고 가라.")
else:
    print("걸어가라.")
# 걸어가라 출력
