"""
2021-07-11
Bokyung Suh
Python 300
"""

# 181
apart = [['101', '102'], ['201', '202'], ['301', '302']]

# 182
stock = [['start', 100, 200, 300], ['end', 80, 210, 330]]

# 183
stock = {'start': [100, 200, 300], 'end': [80, 210, 330]}

# 184
stock = {'10/10': [80, 110, 70, 90], '10/11': [210, 230, 190, 200]}

# 185
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print("#", j)

# 186
for row in apart[::-1]:
    for col in row:
        print("#", col)

# 187
for row in apart[::-1]:
    for col in row[::-1]:
        print("#", col)

# 188
for row in apart:
    for col in row:
        print("#", col)
        print("-----")

# 189
for row in apart:
    for col in row:
        print("#", col)
    print('-----')

# 190
for row in apart:
    for col in row:
        print('#', col)
print('-----')

# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for price in line:
        print(price * 1.00014)

# 192
for line in data:
    for price in line:
        print(price * 1.00014)
    print('----')

# 193
result = []
for line in data:
    for price in line:
        result.append(price * 1.00014)
print(result)

# 194
result = []
for line in data:
    sub = []
    for price in line:
        sub.append(price * 1.00014)
    result.append(sub)
print(result)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for line in ohlc[1:]:
    print(line[-1])

# 196
for line in ohlc[1:]:
    if line[-1] > 150:
        print(line[-1])

# 197
for line in ohlc[1:]:
    if line[-1] >= line[0]:
        print(line[-1])

# 198
volatility = []
for line in ohlc[1:]:
    volatility.append(line[1] - line[2])
print(volatility)

# 199
for line in ohlc[1:]:
    if line[-1] > line[0]:
        print(line[1] - line[2])

# 200
result = 0
for line in ohlc[1:]:
    result += line[-1] - line[0]
print(result)

