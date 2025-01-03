# 여러 줄인 문자열을 변수에 대입하기 위한 방법

# 1. 줄바꿈을 위한 이스케이프 코드 \n 삽입
multiline1 = "Life is too short\nYou need python"
print(multiline1)

# 2. 연속된 작은/큰 따옴표 3개 사용
multiline2 = '''
Life is too short
You need python
'''
print(multiline2) # 줄바꿈을 반영한 여러 줄 문자열이 출력됨을 확인할 수 있다.

"""
이스케이프 코드
- 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 문자의 조합
- 보통 보기 좋게 정렬하는 용도로 사용
\n 문자열 안에서 줄을 바꿀 때 사용
\t 문자열 사이에 탭 간격을 줄 때 사용
\\ 문자 \를 그대로 표현할 때 사용
\' 작은따옴표(')를 그대로 표현할 때 사용
\" 큰따옴표(")를 그대로 표현할 때 사용
\r 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
\f 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
\a 벨 소리(출력할 때 PC 스피커에서 ‘삑’ 소리가 난다)
\b 백 스페이스
\000 널 문자
"""