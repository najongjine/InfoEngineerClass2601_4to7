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