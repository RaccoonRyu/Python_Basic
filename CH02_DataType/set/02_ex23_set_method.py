# 집합(set) 자료형 관련 함수

# 값 1개 추가(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1) # {1, 2, 3, 4} 출력

# 값 여러 개 추가(update)
s2 = set([1, 2, 3])
s2.update([4, 5, 6])
print(s2) # {1, 2, 3, 4, 5, 6} 출력력

# 특정 값 제거(remove)
s3 = set([1, 2, 3])
s3.remove(2)
print(s3) # {1, 3} 출력