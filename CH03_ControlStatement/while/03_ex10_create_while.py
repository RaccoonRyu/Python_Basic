# while문 예제 작성
# 여러 가지 선택지 중 하나를 선택하여 입력받는 예제

prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input()) # input() : 콘솔에서 번호 입력받음 / int() : 괄호 안의 수를 정수로 변환
# number가 4가 아니면 prompt를 계속 출력하고, 4라면 조건문이 거짓이 되어 while문을 빠져나가게 된다.