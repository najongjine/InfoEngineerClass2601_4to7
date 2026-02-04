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


""" 재귀 함수 """

def rec(a):
    if a<=0:
        return 0
    return a+rec(a-1)

print(rec(4))


""" 연습문제 """
def func(n, data):
    if n <= 0:
        return []
    
    # 1. 슬라이싱과 리스트 컴프리헨션
    res = [x for x in data if x % n == 0]
    
    # 2. 튜플 언패킹과 재귀 호출
    return res + func(n - 2, data[1:])

# 초기 데이터
values = [2, 4, 6, 8, 10, 12]
n_val = 4

# 실행
result = func(n_val, values)
print(f"result:{result}")

# 3. 집합을 이용한 중복 제거 및 정렬
final = sorted(list(set(result)), reverse=True)
print(final)