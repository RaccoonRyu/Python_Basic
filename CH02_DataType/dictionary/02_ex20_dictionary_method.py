# 딕셔너리 관련 함수들

# Key 리스트 만들기(keys)
a = {"name" : "pey", "phone" : "0119993323", "birth" : "1118"}
print(a.keys()) # 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다. dict_keys(['name', 'phone', 'birth'])

# dict_keys, dict_values, dict_items 등은 리스트로 반환하지 않더라도 기본적인 반복문(ex for문)을 실행할 수 있다.
# dict_keys 객체를 리스트로 변환하려면 list(딕셔너리명.keys())를 사용한다.
print(list(a.keys())) # ['name', 'phone', 'birth']

# Values 리스트 만들기(values)
print(a.values()) # 딕셔너리 a의 Value만을 모아서 dict_values 객체를 돌려준다. dict_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기(items)
print(a.items()) # 딕셔너리 a의 Key-Value 쌍을 튜플로 모아서 dict_items 객체로 돌려준다.
# dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# dict_values, dict_items 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용할 수 있다.
print(list(a.values())) # ['pey', '0119993323', '1118']
print(list(a.items())) # [('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]

# Key-Value 쌍 모두 지우기(clear)
a.clear()
print(a) # 빈 딕셔너리 {} 출력

# Key로 Value 얻기(get)
# get(x) : x 라는 Key에 대응되는 Value를 반환. 딕셔너리명[x]와 동일한 결과를 반환한다.
a = {"name" : "pey", "phone" : "0119993323", "birth" : "1118"}
print(a.get("name")) # "name"이라는 Key에 대응되는 Value 반환하여 출력. a["name"]과 동일한 결과
print(a.get("nokey")) # get 함수로 딕셔너리에 존재하지 않는 Key로 값을 가져오려할 경우 None 출력
#print(a["nokey"]) # get 함수가 아닌 방식으로 딕셔너리에 존재하지 않는 Key로 값을 가져오려할 경우 에러 발생

# 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때 get(key값, 디폴트값)을 사용
print(a.get("foo", "bar")) # bar 출력

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
b = {"name" : "pey", "phone" : "0119993323", "birth" : "1118"}
print("name" in b) # "name" 문자열이 b 딕셔너리의 Key 중 하나이므로 True 출력
print("email" in b) # "email" 문자열이 b 딕셔너리의 Key에 속하지 않으므로 False 출력