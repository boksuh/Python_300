"""
    2021-07-06
    Bokyung Suh
    Python 300
"""

# 161
for num in range(100):
    print(num)

# 162
for year in range(2002, 2051):
    if year % 4 == 2:
        print(year)

# 163
for num in range(1, 31):
    if num % 3 == 0:
        print(num)

# 164
for num in range(100):
    print(99 - num)

# 165
for i in range(10):
    print("0.%d" % i)

# 166
for i in range(1, 10):
    print("3 x %d = %d" % (i, i*3))

# 167
for i in range(1, 10):
    if i % 2 == 1:
        print("3 x %d = %d" % (i, i * 3))

# 168
result = 0
for i in range(11):
    result += i
print(result)

# 169
result = 0
for i in range(1, 11):
    if i % 2 == 1:
        result += i
print(result)

# 170
result = 1
for i in range(1, 11):
    result *= i
print(result)

# 171
