a=1
if a>0:
    a=2
    b=3
else:
    a=1
    b=3

print(f"a:{a}, b:{b}") # 2, 3
"""
파이썬은 {} 기호가 없어서, 함수, class 빼고는 scope가 없어요
if 문 안에 변수 선언해도 바깥쪽에서 실컷 참조할수 있어요
"""

for i in range(3):
    print(i,end=",") # 0,1,2,

print("apple","banana","orange",sep="&")
print("--")