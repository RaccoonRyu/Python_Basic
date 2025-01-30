# 조건문에서 아무 일도 하지 않게 설정하는 pass
# pass : 조건문의 참/거짓에 따라 실행할 행동을 정의할 때, 아무 일도 하지 않도록 설정하는 문장

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라.")
# pocket 리스트 안에 money 문자열이 있기 때문에 if문 다음 문장인 pass가 수행되고 아무 결과도 보여주지 않는다.