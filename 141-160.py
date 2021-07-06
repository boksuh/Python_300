"""
    2021-07-06
    Bokyung Suh
    Python 300
"""

# 141
pr = [100, 200, 300]
for price in pr:
    print(price+10)

# 142
food = ["kim", "ramen", "fried"]
for el in food:
    print("Today's menu: %s" % el)

# 143
stock = ["SK", "SS", "LG"]
for el in stock:
    print(len(el))

# 144
animals = ['dog', 'cat', 'parrot']
for animal in animals:
    print(animal, len(animal))

# 145
for animal in animals:
    print(animal[0])

# 146
nums = [1, 2, 3]
for num in nums:
    print("3 x %d" % num)

# 147
for num in nums:
    print("3 x %d = %d" %(num, num*3))

# 148
alphs = ["A", "B", "C", "D"]
for alph in alphs[1:]:
    print(alph)

# 149
for alph in alphs[::2]:
    print(alph)

# 150
for alph in alphs[::-1]:
    print(alph)

# 151
nums = [3, -20, -3, 44]
for num in nums:
    if num < 0:
        print(num)

# 152
nums = [3, 100, 23, 44]
for num in nums:
    if num % 3 == 0:
        print(num)

# 153
nums = [13, 21, 12, 14, 30, 18]
for num in nums:
    if num < 20 and num % 3 == 0:
        print(num)

# 154
words = ["I", "study", "python", "language", "!"]
for word in words:
    if len(word) >= 3:
        print(word)

# 155
alphs = ["A", "b", "c", "D"]
for alph in alphs:
    if alph.isupper():
        print(alph)

# 156
for alph in alphs:
    if alph.islower():
        print(alph)

# 157
animals = ['dog', 'cat', 'parrot']
for animal in animals:
    print(animal[0].upper()+animal[1:])

# 158
files = ['hello.py', 'ex01.py', 'intro.hwp']
for file in files:
    print(file.split(".")[0])

# 159
files = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in files:
    if file.split(".")[1] == 'h':
        print(file)

# 160
for file in files:
    if file.split(".")[1] == 'h' or file.split(".")[1] == 'c':
        print(file)
