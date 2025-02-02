# for문의 기본 구조
# while문과 비슷한 반복문인 for문
# while문에 비해 문장 구조가 한 눈에 들어온다는 장점이 있다.
"""
for 변수 in 리스트(or 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
"""
# 리스트, 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 "수행할 문장1", "수행할 문장2" 등이 수행된다.

# 예제 1. for문 기본
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# test_list의 첫 번째 요소부터 마지막 요소까지를 반복하며 출력한다.

# 예제 2. 다양한 for문 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
# a 리스트의 요소가 튜플이기 때문에 각 요소가 자동으로 (first, last) 변수에 대입

# 예제 3. for문 응용
# 학생들의 시험점수에 따른 합격/불합격 결과 보여주기
marks = [90, 25, 67, 45, 80]
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
# number : 각 학생에게 붙일 번호로 사용할 변수
# marks에서 점수를 꺼내 mark에 대입하고 for문 안의 문장 수행
# 수행마다 number는 1씩 증가하고, 학생의 합/불합 여부를 출력

