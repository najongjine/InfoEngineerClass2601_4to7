a=1
a=a+1 - 1 + 2 / 3 % 3

a=1
a=a<<1
a=3
a=a&1

a=1/3
print(a)
a=1//3
print(a)
print(f"2*3:{2*3}")
print(f"2**3:{2**3}")
print(f" 2^1 : {2^1}")

a=50
print(f"{40<= a <= 55}")
print(f"{a>=40 and a<=55}")

print("a" in "task")
print("z" not in "task")

a=["불고기","비빔밥"]
c=["짜장","짬뽕"]
k=[a,c]

a[0]="바꿈"
print(k)

a="hello python"
for e in a:
    print(e+"a")

print(f"a[-1]:{a[-1]}")

a="hello"
print(f"a[0:2]:{a[0:2]}") # 0~1 까지. 2는 포함 안함
print(f"a[:2]:{a[:2]}") # 0~1 까지. 2는 포함 안함
print(f"a[3:]:{a[3:]}") # 3 index 부터 끝까지
print(f"a[-4:-2]:{a[-4:-2]}") # 음수는 -4 가 -2 보다 더 작은원리
print(f"a[-4:] : {a[-4:]}")
print(f"a[-4:4] : {a[-4:4]}")

a="hello python"
print(f"a[::-1] : {a[::-1]}")
print(f"a[::2] : {a[::2]}")
print(f"a[-7:9:2] : {a[-7:9:2]}")

a=[]
a.append(1)
a.append(2)
a.append([1,2]) # 배열을 append 하면 배열 자체가 추가되 버려요
a.extend([2,3]) # 배열 차원 유치하면서 추가. 늘리기.

a.insert(3,4)
print(f"a: {a}")
a.remove([1,2]) # 원본에서 똑같이 생긴 놈을 제거
print(f"a: {a}")

a=[1,2,3,4,5,6,7]
# 팝콘이 팝 튀는 것처럼 튀어나오고 원본에선 제거. index 기준
print(f"a.pop(1):{a.pop(1)}")

del a[0]
print(f"a:{a}") # index 기준으로 삭제

