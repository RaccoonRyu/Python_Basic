# Python에서 문자열을 표현하는 4가지 방법
a = "Hello World" # 큰 따옴표로 양쪽 둘러싸기
a = 'Python is fun' # 작은 따옴표로 양쪽 둘러싸기
a = """Life is too short""" # 큰 따옴표 3개를 연속으로 써서 양쪽 둘러싸기
a = '''You need python''' # 작은 따옴표 3개를 연속으로 써서 양쪽 둘러싸기

# 문자열에 작은 따옴표(') 포함시키기
a = "Python's favorite food is perl"
print(a) # 큰 따옴표로 둘러싼 문자열에는 작은 따옴표를 문자로 포함할 수 있다.

# 문자열에 큰 따옴표(") 포함시키기
a = '"Python is very easy" he says.'
print(a) # 작은 따옴표로 둘러싼 문자열에는 큰 따옴표를 문자로 포함할 수 있다.

# 백슬래시(\)를 사용하여 작은/큰 따옴표를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say) # 백슬래시 + 작은/큰 따옴표를 사용하여 작은/큰 따옴표를 문자 그대로 사용할 수 있다.