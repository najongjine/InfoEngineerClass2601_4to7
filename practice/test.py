lst = [1,2,3]

dst = {i : i* 2 for i in lst}
#{1:2,2:4,3:6}

s = set(dst.values()) # {2, 4, 6}

lst[0] = 99 # [99,2,3]
dst[2]=7 # {1:2,2:7,3:6}
s.add(99) # {2, 4, 6, 99}

"""
{2, 4, 6, 99}
&
{2,7,6}
"""

print(len(s & set(dst.values())))