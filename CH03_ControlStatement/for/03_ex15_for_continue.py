# for문과 continue
# continue문은 for문에서도 사용할 수 있다.
# for문 안에서 문장을 수행하다 continue문을 만나면 for문의 처음으로 돌아가게 된다.

# 60점 이상 수험자에게 축하 메시지를 보내고 나머지 사람에게는 아무 메시지도 전하지 않는 프로그램 작성
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)