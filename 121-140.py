"""
    2021-07-05
    Bokyung Suh
    Python 300 (121-140)
"""

import requests

# 121
# user = input()
# if user.isupper():
#     print(user.lower())
# else:
#     print(user.upper())

# 122
# user = input()
# score = int(user)
# if 80 < score <= 100:
#     print("grade is A")
# elif 60 < score <= 80:
#     print("grade is B")
# elif 40 < score <= 60:
#     print("grade is C")
# elif 20 < score <= 40:
#     print("grade is D")
# else:
#     print("grade is E")

# 123
# curr = {"dollar": 1167, "yen": 1.096, "euro": 1268, "yuan": 171}
# user = input("input: ")
# num, currency = user.split()
# print(float(num) * curr[currency], "won")

# 124
# num1 = input("1: ")
# num2 = input("2: ")
# num3 = input("3: ")
# arr = [int(num1), int(num2), int(num3)]
# print(max(list))

# 125
# number = input("Tel: ")
# num = number.split("-")[0]
# if num == "011":
#     tel = "SKT"
# elif num == "016":
#     tel = "KT"
# elif num == "019":
#     tel = "LGU"
# else:
#     tel = "Unknown"
# print(tel)

# 126
# user = input("num: ")
# num = user[:3]
# if num in ["010", "011", "012"]
#     print("강북구")
# elif num in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")

# 127
# user = input("id: ")
# check = user[7]
# if check == 1 or 3:
#     print("man")
# else:
#     print("woman")

# 128
# user = input("id: ")
# check = user.split("-")[1]
# if 0 <= int(check[1:3]) <= 8:
#     print("Seoul")
# else:
#     print("not Seoul")

# 129
# num = input("id :")
# check1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# check2 = 11 - (check1 % 11)
# check3 = str(check2)
#
# if num[-1] == check3[-1]:
#     print("Valid")
# else:
#     print("Invalid")

# 130
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])
#
# if (시가+변동폭) > 최고가:
#     print("상승장")
# else:
#     print("하락장")

# 131
fruit = ["사과", "귤", "수박"]
for val in fruit:
    print(val)

# 132
fruit = ["사과", "귤", "수박"]
for val in fruit:
    print("#####")

# 133
for val in ["A", "B", "C"]:
    print(val)

# 134
for val in ["A", "B", "C"]:
    print("print : ", val)

# 135
for val in ["A", "B", "C"]:
    b = val.lower()
    print("change: ", b)

# 136
for val in [10, 20, 30]:
    print("val: ", val)

# 137
for val in [10, 20, 30]:
    print(val)

# 138
for val in [10, 20, 30]:
    print(val, "\n"+("-"*6))

# 139
print("++++")
for val in [10, 20, 30]:
    print(val)

# 140
for val in range(0, 4):
    print("------")
