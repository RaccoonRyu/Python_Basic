# 문자열 슬라이싱을 이용한 문자열 대체
# 문자열은 immutable(불변) 자료형이기 때문에 문자열의 요소를 바꿀 수 없다.
# 따라서 슬라이싱을 사용하여 문자열을 대체할 수 있다.
# Pithon to Python
a = "Pithon"
print(a[:1]) # P 출력
print(a[2:]) # thon 출력
b = a[:1] + "y" + a[2:]
print(b) # Python 출력

# 문자열 슬라이싱을 사용하여 P와 thon 부분을 나눈 후 사이에 "y" 문자를 추가하여 Python이라는 새로운 문자열을 만들었다.