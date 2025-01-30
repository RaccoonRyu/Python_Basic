# while문의 기본 구조
# 어떤 문장을 반복 수행해야 할 경우 while문을 사용한다.
"""
while <조건문>:
    <수행할 문장 1>
    <수행할 문장 2>
    <수행할 문장 3>
    ...
"""

# while문은 조건문이 참인 동안에 while문 아래의 문장이 반복 수행된다.

treeHit = 0
while treeHit < 10: # while문의 조건문 : treeHit < 10
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")
# 나무를 10 번 찍을 때 까지 나무를 찍은 문장이 반복된다.
# 나무를 10 번 다 찍으면 나무 넘어갑니다.를 출력한다. 이후 조건문이 거짓이 되므로 while문을 탈출한다.