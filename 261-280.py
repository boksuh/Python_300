"""
2021-07-14
Bokyung Suh
Python 300
"""
import random


# 261
class Stock:
    pass


# 262
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code


Samsung = Stock('Samsung', '005930')
print(Samsung.name)
print(Samsung.code)


# 263
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


a = Stock(None, None)
a.set_name('Samsung')
print(a.name)

# 264
a = Stock(None, None)
a.set_code('005930')

# 265
Samsung = Stock('Samsung', '005930')
print()
print(Samsung.get_code())
print(Samsung.get_name())


# 266
class Stock:
    def __init__(self, name, code, per, pbr, div):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.div = div

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


Samsung = Stock('samsung', '005930', 15.79, 1.33, 2.83)

# 268
class Stock:
    def __init__(self, name, code, per, pbr, div):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.div = div

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, div):
        self.div = div


# 269
Samsung = Stock('samsung', '005930', 15.79, 1.33, 2.83)
Samsung.set_per(12.75)
print(Samsung.per)

# 270
stk = []

Sam = Stock('Samsung', '005930', 15.79, 1.33, 2.83)
Hyundai = Stock('Hyundai', '005380', 8.70, 0.35, 4.27)
LG = Stock('LG', '066570', 317.34, 0.69, 1.37)

stk.append(Sam)
stk.append(Hyundai)
stk.append(LG)

for i in stk:
    print(i.code, i.per)

# 271
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

# 272

class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1


k = Account('kim', 100)
print(Account.account_count)
l = Account('lee', 200)
print(Account.account_count)

# 273
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)


k = Account('kim', 100)
l = Account('lee', 200)
k.get_account_num()

# 274
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount


# 265
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount


# 276
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount

    def display_info(self):
        print("Bank Name: %s" % self.bank)
        print("Name: %s" % self.name)
        print('Number: %s' % self.account_number)
        print('Balance: %d' % self.balance)


p = Account('python', 10000)
p.display_info()

# 277
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount

    def display_info(self):
        print("Bank Name: %s" % self.bank)
        print("Name: %s" % self.name)
        print('Number: %s' % self.account_number)
        print('Balance: %d' % self.balance)


p = Account('lee', 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
print(p.balance)

# 278
lst = []
a = Account('K', 10000000)
b = Account('P', 10000)
c = Account('L', 10000)

lst.append(a)
lst.append(b)
lst.append(c)

print(lst)

# 279
for account in lst:
    if account.balance >= 1000000:
        account.display_info()

# 280
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = 'SC bank'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_log.append(amount)

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount):
        if amount < self.balance:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("Bank Name: %s" % self.bank)
        print("Name: %s" % self.name)
        print('Number: %s' % self.account_number)
        print('Balance: %d' % self.balance)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
