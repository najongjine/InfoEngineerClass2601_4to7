data = [
    [3, 5, 2, 4, 1],
    [4, 5, 1],
    [4, 4, 1, 5, 4],
    [4, 5]
]
 
result = {}
 
for index, lis in enumerate(data):
    list_sum = sum(lis)
    list_len = len(lis)
 
    result[index] = (list_sum, list_len)
    print(f"result[{index}] = ({list_sum}, {list_len})")

"""
index: 0, lis: [3, 5, 2, 4, 1]
index: 1, lis: [4, 5, 1]
index: 2, lis: [4, 4, 1, 5, 4]
index: 3, lis: [4, 5]

"""
    