"""
2021-07-14
Bokyung Suh
Python 300
"""

import datetime
import time
import os
import numpy as np

# 241
now = datetime.datetime.now()
print(now)

# 242
print(type(datetime.datetime.now()))

# 243
now = datetime.datetime.now()
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

# 244
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

# 245
print(datetime.datetime.strptime('2020-05-04', '%Y-%m-%d'))

# 246
# while True:
#     print(datetime.datetime.now())
#     time.sleep(1)

# 247
# import module
# from module import module func

# 248
print(os.getcwd())

# 249 os.rename('C:/Users/bok_suh/iCloudDrive/KNU/2021-Project/Python 300/test.txt',
# 'C:/Users/bok_suh/iCloudDrive/KNU/2021-Project/Python 300/after.txt')

# 250
for i in np.arange(0, 5, 0.1):
    print(i)


# 251
# class는 설계도면
# 객체는 클래스로 만든 피조물
# 클래스의 인스턴스가 객체

# 252
class Human:
    pass


# 253
areum = Human()


# 254
class Human:
    def __init__(self):
        print('haha')


areum = Human()

# 255
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("name: {} age: {} sex: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print('나의 죽음을 알리지말라')

areum = Human('areum', 25, 'w')

print(areum.name)

# 256
print("name: %s, age: %d, sex: %s" % (areum.name, areum.age, areum.sex))

# 257
areum.who()

# 258
areum = Human('noinfo', 0, 'noinfo')
areum.who()
areum.setInfo('areum', 25, 'w')
areum.who()

# 259
del areum

# 260
class OMG:
    def print(self):# self
        print('oh my god')


myStock = OMG()
myStock.print()
