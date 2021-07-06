"""
    2021-07-05
    Bokyung Suh
    Python 300
"""

# 081
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a, b, c)
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

# 082
_, _, *valid_score = scores
print(valid_score)

# 083
_, *valid_score, _ = scores
print(valid_score)

# 084
temp = {}
print(type(temp))

# 085
ice = {"Merona": 1000, "P": 1200, "B": 1800}
print(ice)

# 086
ice["J"] = 1200
ice["W"] = 1500
print(ice)

# 087
print("M's price is", ice["Merona"])

# 088
ice["Merona"] = 1300
print(ice)

# 089
del ice["Merona"]
print(ice)

# 090
# no key in dictionary

# 091
inventory = {"M": [300, 20], "B": [400, 3], "J": [250, 100]}
print(inventory)

# 092
print(inventory["M"][0])

# 093
print(inventory["M"][1])

# 094
inventory["W"] = [500, 7]
print(inventory)

# 095
icecream = {"T": 1200, 'P': 1200, 'B': 1800, 'W': 1500, 'M': 1000}
ice = list(icecream.keys())
print(ice)

# 096
value = list(icecream.values())
print(value)

# 097
print(sum(value))

# 098
new_product = {'PP': 2700, 'A': 1000}
icecream.update(new_product)
print(icecream)

# 099
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
