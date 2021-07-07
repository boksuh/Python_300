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
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

# 172
for i in range(len(price_list)):
    print(i, price_list[i])

# 173
for i in range(len(price_list)):
    print(3 - i, price_list[i])

# 174
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

# 175
my_list = ["A", "B", "C", "D"]
for i in range(3):
    print(my_list[i], my_list[i + 1])

# 176
my_list = ["A", "B", 'C', 'D', 'E']
for i in range(3):
    print(my_list[i], my_list[i + 1], my_list[i + 2])

# 177
my_list = ['A', 'B', 'C', 'D']
for i in [3, 2, 1]:
    print(my_list[i], my_list[i - 1])

# 178
my_list = [100, 200, 400, 800]
for i in range(1, 4):
    print(my_list[i] - my_list[i - 1])

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(4):
    avg = (my_list[i] + my_list[i + 1] + my_list[i + 2]) / 3
    print(avg)

# 180
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
vol = []
for i in range(len(low_prices)):
    vol.append(high_prices[i] - low_prices[i])
print(vol)
