""" 
list comprehension -
for loop 부터 수행 한다
range 에 있는 원소를 for loop 
안쪽에 있는 x 에 먼저 담고
마지막에 맨 왼쪽에 있는 x에 담는다.

0 이걸 for 1 이렇게 담고, 아무이상 없으면 
맨 왼쪽에 있는 x에 담는다
1
2
"""
a=[ x for x in range(3) ]

"""
0 - for 0 담기. 아무이상 없네.
0+1 에 담기
1 - for 1 담기. 아무이상 없네?
1+1 에 담기
2-
3-
"""
a=[ x+1 for x in range(4) ]

"""
1. for x in range(10)
2. if x>5
3. [x

0 1 2 3 4 5 6 7 8 9
0- for 0 에 담아요
 if 0>5 조건체크 해요
 True 아니라서 [x 에 안담아요
7- for 7 에 담아요
 if 7>5 조건체크 해요
 True 라서 [x 에 담아요
"""
a=[x for x in range(10) if x>5]

"""
1. for x in range(10)
2. if x>5 else x+2
3. [x

0 1 2 3 4 5 6 7 8 9
0- for 0
 else 로 빠지고 0+2
 2를 [x 에 담아요
7- for 7
 7>5 로 빠지고
 7을 [x 에 담아요
"""
a=[x if x>5 else x+2 for x in range(10) ]


a=[50,85,95,70]
a=['A' if n>=90 else 'B' if n>=80 else 'C' for n in a]
"""
if a[0]>=90:
    print('A')
else:
    if a[0] >= 80:
        print('B')
    else:
        print('C')
"""
#print(a)

""" list comprehensive 연습문제 """
a=[1,2,3,4,5]
b=[x*2 for x in a if x %2==0]

word = "Python"
result=[char.upper() for char in word if char not in 'aeiou']
# ".join("ab") 은 문자열에 ab 붙이기"
#print("".join(result))

a=[1,2,3]
b=[10,20]
result=[x+y for x in a for y in b]
print(result)
""" list comprehensive 연습문제 END """


