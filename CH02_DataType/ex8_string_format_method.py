# format 함수를 사용한 포맷팅
# 사용법 : 문자열.format(대입할 값 or 변수) 으로 사용하며, 대입할 값이 들어갈 자리는 문자열 내에서 0부터 시작하는 {인덱스}로 표시한다.
print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))
num = 7
print("I eat {0} apples.".format(num))

# format - 2개 이상의 값을 넣는 경우
# 문자열.format(값 1, 값 2, ... , 값 n)으로 사용한다. 이 때 대입할 값은 순서를 가진다.
# 대입할 값이 들어갈 자리는 문자열 내에서 순서대로 0부터 시작하는 {인덱스}를 하나씩 늘려서 표시한다.
num = 10; day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(num, day))

# format - 이름으로 넣기
# {0}, {1}과 같은 인덱스 항목 대신 더 편리한 {name} 형태를 사용할 수 있다.
# {name} 형태를 사용할 경우 format 함수에는 반드시 name=value 형태의 입력값이 있어야한다.
print("I ate {num} apples. so I was sick for {day} days.".format(num=7, day=3))

# format - 인덱스와 이름 혼용해서 넣기
# 인덱스 항목과 name=value 형태를 혼용하는 것도 가능하다.
print("I ate {0} apples. so I was sick for {day} days.".format(13, day=3))

# format - 왼쪽 정렬
# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬 후 문자열의 총 자릿수를 10으로 맞출 수 있다.
print("{0:<10}".format("hi"))

# format - 오른쪽 정렬
# :>10 표현식을 사용하면 치환되는 문자열을 오른쪽으로 정렬 후 문자열의 총 자릿수를 10으로 맞출 수 있다.
print("{0:>10}".format("hi"))

# format - 가운데 정렬
# ^ 기호를 사용하면 치환되는 문자열을 가운데로 정렬 후 문자열의 총 자릿수를 10으로 맞출 수 있다.
print("{0:^10}".format("hi"))

# format - 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y)) # 소수점을 4자리까지만 표현
print("{0:10.4f}".format(y)) # 전체 문자열 길이를 10으로 맞춘 후 오른쪽 정렬하고, 소수점을 4자리까지만 표현
print("{0:<10.4f}".format(y))

# format - 중괄호({}) 표현하기
# format 함수를 사용해 중괄호 문자를 포매팅 문자가 아닌 중괄호 문자 그대로 사용하고 싶은 경우 2개를 연속해서 사용한다.
print("{{ and }}".format())

# f 문자열 포매팅
# 파이썬 3.6 버전부터 사용 가능한 기능
# 문자열 앞에 f 접두사를 붙이면 문자열 포매팅 기능을 사용할 수 있다.
name = "홍길동"
age = 30
print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다.")

# 아래와 같이 변수를 생성한 후 해당 변수의 값을 참조할 수 있고, 표현식 또한 지원한다.
age = 31
print(f"나는 내년이면 {age+1}살이 된다.")

# 딕셔너리는 f 문자열 포매팅에서 아래와 같이 사용된다.
d = {"name" : "홍길동", "age" : 30}
print(f"나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.")

# f 문자열 포매팅에서 정렬은 아래와 같이 할 수 있다.
print(f"{'hi':<10}") # 왼쪽 정렬
print(f"{'hi':>10}") # 오른쪽 정렬
print(f"{'hi':^10}") # 가운데 정렬

# f 문자열 포매팅에서 공백 채우기는 아래와 같이 할 수 있다.
print(f"{'hi':=^10}") # 가운데 정렬하고 = 문자로 공백 채우기
print(f"{'hi':!<10}") # 왼쪽 정렬하고 ! 문자로 공백 채우기

# f 문자열 포매팅에서 소수점은 아래와 같이 표현할 수 있다.
y = 3.42134234
print(f"{y:0.4f}") # 소수점 4자리까지만 표현
print(f"{y:10.4f}") # 소수점 4자리까지만 표현하고 총 자릿수를 10으로 맞춤(오른쪽 정렬)
