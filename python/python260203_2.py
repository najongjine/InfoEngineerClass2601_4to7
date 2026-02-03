def func1():
    print("func1")

def func2():
    return 10

def func3(a,b):
    return ++a + ++b

def func4(a):
    a[0]=9

a=[1,2,3]
func4(a)
print(a)

"""
파이썬에 포인터가 없다고 포인터 원리가 없는건
아니에요.
list, tuple, set, class, dictionary...
즉 단순 자료형(단일 숫자, bool, 문자열) 빼고는
다 함수에 주소를 넘겨요
"""

"""
dictionary
Java의 Map 이랑 같은 놈이에요
"""
a={"a":1,"b":2}
a["a"]=2
a["c"]=3
print(a)