# 문자열 관련 함수
# 문자열 자료형이 자체적으로 가진 함수(문자열 내장 함수)를 의미
# 문자열 변수명 뒤에 .(dot)을 붙인 다음 함수명을 적어 사용한다.

# 문자 개수 세기 (count)
a = "hobby"
print(a.count('b')) # 문자열 중 문자 b의 개수를 돌려준다

# 특정 문자의 위치 알려주기 1 (find)
b = "Python is the best choice"
print(b.find('b')) # 문자열에서 b가 처음 나온 위치
print(b.find('k')) # 찾는 문자나 문자열이 존재하지 않는다면 -1 반환

# 특정 문자의 위치 알려주기 2 (index)
c = "Life is too short"
print(c.index('t')) # 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환
#print(c.index('k')) # 찾는 문자나 문자열이 존재하지 않으면 오류를 발생시킴 (find와의 차이점) - substring not found

# 문자열 삽입(join)
print(",".join("abcd")) # abcd 문자열의 각 문자 사이에 ','를 삽입

# join 함수는 문자열뿐만 아니라 리스트나 튜플도 입력으로 사용할 수 있다.
print(",".join(['a', 'b', 'c', 'd'])) # join 함수의 입력으로 리스트 사용

# 소문자를 대문자로 바꾸기 (upper)
d = "hi"
print(d.upper()) # 소문자를 대문자로 바꾸어 줌

# 대문자를 소문자로 바꾸기 (lower)
e = "HI"
print(e.lower()) # 대문자를 소문자로 바꾸어 줌

# 왼쪽 공백 지우기 (lstrip)
# 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백을 모두 지움
# l은 left를 의미한다.
f = " dhi d"
print(f.lstrip())

# 오른쪽 공백 지우기 (rstrip)
# 문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백을 모두 지움
# r은 right를 의미한다.
g = "d hid "
print(g.rstrip())

# 양쪽 공백 지우기 (strip)
# 문자열 양 쪽에 있는 한 칸 이상의 연속된 공백을 보두 지운다.
h = " d hi d "
print(h.strip())

# 문자열 바꾸기 (replace)
i = "Life is too short."
print(i.replace("Life", "Your leg")) # replace(바뀔 문자열, 바꿀 문자열)을 사용해서 문자열 안의 특정한 값을 다른 값으로 치환

# 문자열 나누기 (split)
j = "Life is too short."
print(j.split()) # split() 괄호 안에 아무 값도 넣지 않으면 공백 기준으로 문자열 나눔
# 만약 split() 안에 특정 값이 있을 경우(split(":")) 괄호 안의 값을 구분자로 문자열 나눔
# 나눈 값은 리스트에 들어감