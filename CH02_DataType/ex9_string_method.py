# 문자열 관련 함수
# 문자열 자료형이 자체적으로 가진 함수(문자열 내장 함수)를 의미
# 문자열 변수명 뒤에 .(dot)을 붙인 다음 함수명을 적어 사용한다.

# 문자 개수 세기(count)
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