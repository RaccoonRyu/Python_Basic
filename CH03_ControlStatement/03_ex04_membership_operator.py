# 멤버쉽 연산자
# in, not in
# 특정 값이나 요소가 어떤 그룹 또는 집합에 속하는지 확인하는 데에 사용
"""
x in 리스트 x not in 리스트
x in 튜플 x not in 튜플
x in 문자열 x not in 문자열
"""

# 멤버쉽 연산자 예시
print(1 in [1, 2, 3])  # True 출력
print(1 not in [1, 2, 3])  # False 출력

print("a" in ("a", "b", "c"))  # True 출력
print("j" not in "python")  # True 출력

pocket = ["paper", "cellphone", "money"]
if "money" in pocket:
    print("택시틀 타고 가라.")
else:
    print("걸어가라")
# 택시를 타고 가라 출력
