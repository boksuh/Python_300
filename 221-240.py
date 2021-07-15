"""
2021-07-11
Bokyung Suh
Python 300
"""


# 221


def print_reverse(string):
    print(string[::-1])


print_reverse('python')


# 222


def print_score(scores):
    print(sum(scores) / len(scores))


print_score([1, 2, 3])


# 223


def print_even(nums):
    for num in nums:
        if num % 2 == 0:
            print(num)


print_even([1, 3, 2, 10, 12, 11, 15])


# 224


def print_keys(dictionary):
    for el in dictionary.keys():
        print(el)


print_keys({"name": "ddong", "age": 30, "sex": 0})

# 225
my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}


def print_value_by_key(dic, string):
    print(dic[string])


print_value_by_key(my_dict, "10/26")


# 226


def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1):
        print(line[x * 5: x * 5 + 5])


print_5xn('hellothere')


# 227


def printmxn(string, num):
    chunk_num = int(len(string) / num)
    for x in range(chunk_num + 1):
        print(string[x * num: x * num + num])


printmxn('hellothere', 3)


# 228


def calc_monthly_salary(sal):
    print(int(sal / 12))


calc_monthly_salary(12000000)


# 229


def my_print(a, b):
    print("left: ", a)
    print('right: ', b)


my_print(a=100, b=200)

# 230

my_print(b=100, a=200)

# 231


def n_plus_1(n):
    result = n + 1


n_plus_1(3)
# print(result) result is used in function only

# 232


def make_url(string):
    print('wwww.%s.com' % string)


make_url('naver')

# 233


def make_list(string):
    ls = []
    for char in string:
        ls.append(char)
    print(ls)


make_list('abcd')

# 234


def pickup_even(nums):
    ls = []
    for num in nums:
        if num % 2 == 0:
            ls.append(num)
    print(ls)


pickup_even([3, 4, 5, 6, 7, 8])

# 235


def convert_int(string):
    print(string.replace(',', ''))


convert_int('1,234,567')

# 236


def func(num):
    return num + 4


a = func(10)
b = func(a)
c = func(b)
print(c)

# 237
c = func(func(func(10)))
print(c)

# 238


def func2(num):
    return num * 10


a = func(10)
c = func2(a)
print(c)

# 239


def func3(num):
    num = num + 2
    return func(num)


c = func3(10)
print(c)

# 240


def f0(num):
    return num * 2


def f1(num):
    return f0(num + 2)


def f2(num):
    num = num + 10
    return f1(num)


c = f2(2)
print(c)