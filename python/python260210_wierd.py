if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"리스트의 길이는 {n}입니다.")  # 출력: 리스트의 길이는 5입니다.

n=len([1, 2, 3, 4, 5])
if n>3:
    print(f"리스트의 길이는 {n}입니다.")


def square(n):
    return n * n

numbers = [1, 2, 3, 4]
result = list(map(square, numbers))

print(result) # 출력: [1, 4, 9, 16]



str1= "10 20 30"
a, b, c = map(int, str1.split())
print(f"{a} {b} {c}")


numbers = [1, 2, 3]
result = list(map(lambda x: x + 10, numbers))

print(result) # 출력: [11, 12, 13]



def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(is_even, numbers))

print(result) # 출력: [2, 4, 6]



numbers = [10, 25, 30, 45, 50]

# 30보다 큰 숫자만 필터링
result = list(filter(lambda x: x > 30, numbers))

print(result) # 출력: [45, 50]