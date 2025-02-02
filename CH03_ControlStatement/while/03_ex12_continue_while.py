# while문의 맨 처음으로 돌아가기
# while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가려면 continue문을 사용한다.

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
# 1~10 까지의 숫자 중 홀수만 출력하는 예제
# a가 2의 배수(a % 2 == 0), 즉 짝수일 때는 continue 문장을 수행하여 while문의 맨 처음으로 돌아간다.