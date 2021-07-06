"""
    2021-07-05
    Bokyung Suh
    Python 300
"""

# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 065
interest = ["Samsung", "LG", "Naver"]
print(interest[0], interest[2])

# 066
interest = ["Samsung", "LG", "Naver", "SK", "Mirae"]
print(" ".join(interest))

# 067
print("/".join(interest))

# 068
print("\n".join(interest))

# 069
string = "Samsung/LG/Naver"
interest = string.split("/")
print(interest)

# 070
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 071
my_variable = ()

# 072
movie_rank = ("Dr.Strange", "Split", "Lucky")
print(movie_rank)

# 073
tup = (1,)
print(tup)

# 074
t = (1, 2, 3)
# t[0] = 'a'
print(t)

# 075
t = 1, 2, 3, 4
print(type(t))

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

# 077
interest = ("Samsung", "LG", "SK")
list_interest = list(interest)
print(list_interest)

# 078
tup_interest = tuple(list_interest)
print(tup_interest)

# 079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080
data = tuple(range(2, 100, 2))
print(data)
