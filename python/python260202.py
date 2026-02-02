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

a=[ x+1 for x in range(4) ]
print(a)

