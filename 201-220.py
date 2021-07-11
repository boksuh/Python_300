"""
2021-07-11
Bokyung Suh
Python 300
"""

# 201


def print_coin():
    print('bit coin')


# 202
print_coin()

# 203
for i in range(100):
    print_coin()

# 204


def print_coins():
    for num in range(100):
        print('bit coin')


# 205
# 정의되기 전에 함수를 호출해서 에러 발생

# 206


def message():
    print('A')
    print('B')


message()
print('C')
message()

# 207
print('A')


def message():
    print('B')


print('C')
message()

# 208
print("A")


def message1() :
    print("B")


print("C")


def message2() :
    print("D")


message1()
print("E")
message2()

# 209


def message1():
    print("A")


def message2():
    print("B")
    message1()


message2()

# 210


def message1():
    print("A")


def message2():
    print("B")


def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()


message3()

# 211


def func(string):
    print(string)


func('hi')
func('hello')

# 212


def fun(a, b):
    print(a + b)


fun(3, 4)
fun(7, 8)

# 213
# No argument

# 214


# def func(a, b):
#     print(a + b)
#
#
# func('hi', 3)
# 'hi' & 3 are not of same type

# 215


def print_with_smile(string):
    print(string+":D")


# 216
print_with_smile('hello')

# 217


def print_upper_price(price):
    print(price * 1.3)


# 218


def print_sum(a, b):
    print(a + b)


# 219


def print_arithmetic_operation(a, b):
    print("%d + %d = %d" % (a, b, a+b))
    print("%d - %d = %d" % (a, b, a-b))
    print("%d * %d = %d" % (a, b, a*b))
    print("%d / %d = %.2f" % (a, b, a/b))


print_arithmetic_operation(3, 4)

# 220


def print_max(a, b, c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)


print_max(1, 2, 3)
