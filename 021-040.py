"""
    2021-07-05
    Bokyung Suh
    Python 300
"""

# 021
letters = 'python'
print(letters[0], letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[-4:])

# 023
string = "홀짝홀짝홀짝"
print(string[::2])

# 024
string = "PYTHON"
print(string[::-1])

# 025
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 026
print(phone_number.replace("-", ""))

# 027
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# 028
lang = 'python'
# lang[0] = 'P'
print(lang)

# 029
string = 'abcdfe2a'
print(string.replace('a', 'A'))

# 030
string = 'abcd'
string.replace('b', 'B')
print(string)

# 031
a = "3"
b = "4"
print(a + b)

# 032
print("HI" * 3)

# 033
print("-" * 80)

# 034
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)

# 035
name1 = "Kim"
age1 = 10
name2 = "Lee"
age2 = 13
print("Name: %s Age: %d" % (name1, age1))
print("Name: %s Age: %d" % (name2, age2))

# 036
print("Name: {} Age: {}".format(name1, age1))
print("Name: {} Age: {}".format(name2, age2))

# 037
print(f'Name: {name1} Age: {age1}')
print(f'Name: {name2} Age: {age2}')

# 038
shares = "5,969,782,550"
int_shares = shares.replace(",", "")
print(int(int_shares))

# 039
div = "2020/03(E) (IFRS)"
print(div[:7])

# 040
data = "   Samsung   "
print(data.strip())

# Done
