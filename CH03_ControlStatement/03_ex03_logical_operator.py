# 논리 연산자
# 조건을 판단하기 위해 사용하는 논리 연산자
# and, or, not
"""
x or y : x와 y 둘중에 하나만 참이어도 참이다.
x and y : x와 y 모두 참이어야 참이다.
not x : x가 거짓이면 참이다.
"""

# or 연산자 사용 예시
# 두 조건 중 하나만 참이어도 참
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라.")
else:
    print("걸어가라.")
# 택시를 타고 가라. 출력
