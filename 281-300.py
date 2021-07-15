"""
2021-07-15
Bokyung Suh
Python 300
"""
import csv


# 281


class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


car = Car(2, 1000)
print(car.wheel)
print(car.price)


# 282


class Bicycle2(Car):
    pass


# 283


class Bicycle3(Car):
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


bicycle = Bicycle3(2, 100)
print(bicycle.price)


# 284


class Bicycle(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        self.system = system


bicycle = Bicycle(2, 100, 'road')
print(bicycle.system)
print(bicycle.wheel)


# 285

class Automobile(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def info(self):
        print("Wheel: ", self.wheel)
        print("Price: ", self.price)


car = Automobile(4, 1000)
car.info()


# 286

class Bicycle(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        self.system = system

    def info(self):
        print("Wheel: ", self.wheel)
        print("Price: ", self.price)


bicycle = Bicycle(2, 100, 'road')
bicycle.info()


# 287
class Bicycle(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        self.system = system

    def info(self):
        print("Wheel: ", self.wheel)
        print("Price: ", self.price)
        print("System: ", self.system)


bicycle = Bicycle(2, 100, 'road')
bicycle.info()


# 288
class Parent:
    def call(self):
        print("Parent Call")


class Child(Parent):
    def call(self):
        print("Child Call")


me = Child()
me.call()


# 289
class Parent:
    def __init__(self):
        print('parent made')


class Child(Parent):
    def __init__(self):
        print('child made')


me = Child()


# 290
class Parent:
    def __init__(self):
        print('Parent made')


class Child(Parent):
    def __init__(self):
        print('Child made')
        super().__init__()


me = Child()

# 291
f = open('buy.txt', mode='wt', encoding='utf-8')
f.write('005930\n')
f.write('005380\n')
f.write('035420')
f.close()

# 292
f = open('buy2.txt', mode='w')
f.write('005930 Samsung\n005380 Hyundai\n035420 Naver')
f.close()

# 293
f = open('stock.csv', mode='w')
writer = csv.writer(f)
writer.writerow(['name', 'code', 'PER'])
writer.writerow(['Samsung', '005930', 15.59])
writer.writerow(['Naver', '035429', 55.82])
f.close()

# 294
f = open('buy.txt', mode='r')
lst = []
lines = f.readlines()
for line in lines:
    code = line.strip()
    lst.append(code)

print(lst)
f.close()

# 295
f = open('buy2.txt', mode='r')
lines = f.readlines()
dic = {}
for line in lines:
    line = line.strip()
    key, value = line.split()
    dic[key] = value

print(dic)
f.close()

# 296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))

    except:
        print(0)

# 297
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)

    except:
        v = 0

    new_per.append(v)

print(new_per)

# 298
try:
    b = 3 / 0
except ZeroDivisionError:
    print("can't divide by zero")

# 299
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

# 300
per = ['10.31', '', '8.00']
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print('clean data')
    finally:
        print('change complete')