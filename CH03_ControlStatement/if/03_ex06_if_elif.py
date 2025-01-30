# 다양한 조건을 판단하는 elif
# if-else 만으로 다양한 조건을 판단하기 어렵기 때문에, 다중 조건 판단을 가능케 하는 elif를 사용한다.

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라.")
elif card:
    print("택시를 타고 가라.")
else:
    print("걸어 가라.")
# 택시를 타고 가라 출력

# elif는 이전 조건문이 거짓일 때 수행된다.
# 따라서 if, elif, else를 모두 사용할 때 기본 구조는 아래와 같다.
# elif는 개수에 제한 없이 사용할 수 있다.
"""
If <조건문>:
<수행할 문장 1>
<수행할 문장 2>
...
elif <pt8>:
<수행할 문장 1>
<수행할 문장 2>
...
elif <pt8>:
<수행할 문장 1>
<수행할 문장 2>
...
...
else:
<수행할 문장 1>
<수행할 문장 2>
...
"""