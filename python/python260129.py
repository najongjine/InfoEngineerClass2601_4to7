"""
파이썬은 희한해요.
아무거나 다 담을수 있어요.
타입이 없다는 말이 아니에요.
포인터가 없다는 말도 아닌데,
주소비교를 삭제 했어요
"""

""" 기본 자료형 """
a=1 # 정수
a="ss" # 문자열
a='c' # 문자열
a=1.1 # 소수
a=True # bool

""" 복합 자료형 """
a=[1,2,3] # 배열, list
a=(1,2,3) # 튜플
a={1,2,3} # 세트
a={"a:":1} # 딕셔네리

class Animal:
    def __init__(self):
        pass

a=Animal()

""" 제어문 """
if True:
    a=1
    if True:
        pass
elif True:
    a=2
else:
    a=3

a=404

match a:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case _:
        print("몰라")

switch={
    1:"One",
    2:"Two",
    3:"Three"
}
num=2
print(switch.get(num,"Invalid"))