"""
set 
중복 불가(Uniqueness): 동일한 값을 여러 번 넣어도 하나만 저장됩니다.
순서 없음 (Unordered): 데이터를 넣은 순서가 유지되지 않습니다. 따라서 인덱싱(s[0])이나 슬라이싱이 불가능합니다.
가변성 (Mutable): 요소를 추가하거나 삭제할 수 있습니다.
"""
a={1,2,2,2,2,2,2,2,2}
a=set([1,2,2,2,2,2])
#print(a) #{1,2}
a=set((1,2,2,2,2,2))
#print(a) #{1,2}
a.add(3) # 추가
a.update([5, 6, 7]) # 뭉탱이로 추가
a.remove(3) # 똑같이 생긴놈 삭제
a.discard(3) # 똑같이 생긴놈 삭제

a={1,2}
b={1,3}
#c=a|b # {1,2,3}
#c=a&b # {1}
#c=a-b # {2}
c=a^b # {2,3}

# list 중복 제거 방식.
a=list(set([1,2,3,3,3,3]))
print(a)

""" set 연습문제 """
data1 = [1, 2, 3, 4, 5, 5]
data2 = [4, 5, 6, 7, 8]

# 1. 중복 제거 및 집합 변환
# {1,2,3,4,5}
set1 = set(data1) 
# {4,5,6,7,8}
set2 = set(data2)

# 2. 집합 연산
# {4,5}
intersect = set1 & set2
# {1,2,3,4,5,6,7,8}
union = set1 | set2

# 3. 데이터 추가 및 수정
# {1,2,3,4,5,6,7,8,10}
union.add(10)
if 5 in intersect:
    # {1,2,3,4,6,7,8,10}
    union.discard(5)

# 4. 결과 연산 및 출력
# List({1,2,3,6,7,8,10}) -> 정렬
result = sorted(list(union - intersect))
print(result)

""" set 연습문제 END """