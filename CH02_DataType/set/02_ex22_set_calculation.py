# 교집합, 합집합, 차집합
# set 자료형은 교집합, 합집합, 차집합으로 유용하게 사용할 수 있다.
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2) # & 기호를 사용하여 교집합 {4, 5, 6} 출력
print(s1.intersection(s2)) # intersection 함수를 사용하여 교집합 {4, 5, 6} 출력

# 합집합
print(s1 | s2) # | 기호를 사용하여 합집합 {1, 2, 3, 4, 5, 6, 7, 8, 9} 출력
print(s1.union(s2)) # union 함수를 사용하여 합집합 {1, 2, 3, 4, 5, 6, 7, 8, 9} 출력

# 차집합
print(s1 - s2) # - 기호를 사용하여 차집합 {1, 2, 3} 출력
print(s2 - s1) # {8, 9, 7} 출력
print(s1.difference(s2)) # difference 함수를 사용하여 차집합 {1, 2, 3} 출력
print(s2.difference(s1)) # {8, 9, 7} 출력