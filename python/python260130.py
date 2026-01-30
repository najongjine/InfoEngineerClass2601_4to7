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
