"""
    2021-07-05
    Bokyung Suh
    Python 300
"""

# 101
# bool

# 102
print(3 == 5)
# false

# 103
print(3 < 5)  # true

# 104
x = 4
print(1 < x < 5)  # true

# 105
print((3 == 3) and (4 != 3))  # true

# 106
print(3 >= 4)

# 107
if 4 < 3:
    print("Hello World")  # does nothing

# 108
if 4 < 3:
    print("hello world")
else:
    print("Hi, there")

# 109
if True:
    print("1\n2")
else:
    print("3")
print("4")

# 110
if True:
    if False:
        print("1\n2")
    else:
        print("3")
else:
    print("4")
print("5")

# 111
# string = input("input : ")
# print(string * 2)

# 112
# num = input("input num: ")
# print(int(num)+10)

# 113
# num = input()
# if int(num) % 2 == 0:
#     print("even")
# else:
#     print("odd")

# 114
# num = input("input: ")
# if (int(num) + 20) > 255:
#     print("255")
# else:
#     print(int(num) + 20)

# 115
# num = input("input: ")
# res = int(num) - 20
# if res < 0:
#     print(0)
# elif res > 255:
#     print(255)
# else:
#     print(res)

# 116
# time = input("Time: ")
# if time[-2:] == "00":
#     print("o'clock")
# else:
#     print("nope")

# 117
# fruit = ['apple', 'grape', 'persimmon']
# user = input("Fruit I like is? ")
# if user in fruit:
#     print("Correct")
# else:
#     print("Wrong")

# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = input("Name: ")
# if user in warn_investment_list:
#     print("Warning")
# else:
#     print("OK")

# 119
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# user = input("Season I like is? ")
# if user in fruit.keys():
#     print("Correct")
# else:
#     print("Wrong")

# 120
# user = input("Fruit I like is? ")
# if user in fruit.values():
#     print("Correct")
# else:
#     print("Wrong")
