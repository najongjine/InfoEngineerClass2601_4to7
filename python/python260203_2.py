def func1():
    print("func1")

def func2():
    return 10

def func3(a,b):
    return ++a + ++b

a=1
b=2
print(f"func3(a,b):{func3(a,b)}")
print(f"a:{a}")
print(f"b:{b}")