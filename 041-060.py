"""
Bokyung Suh
"""

# 041
ticker = "btc_krw"
print(ticker.upper())

# 042
ticker = "BTC_KRW"
print(ticker.lower())

# 043
string = 'hello'
print(string.capitalize())

# 044
file_name = "report.xls"
print(file_name.endswith("xlsx"))

# 045
print(file_name.endswith(("xlsx", "xls")))

# 046
file_name = "2020_report.xlsx"
print(file_name.startswith("2020"))

# 047
a = "hello world"
split = a.split(" ")
print(split)

# 048
ticker = 'btc_krw'
split = ticker.split("_")
print(split)

# 049
date = "2020-05-01"
split = date.split("-")
print(split)

# 050
data = "039490   "
print(data.rstrip())

# 051
movie_rank = ["Dr.Strange", "Split", "Lucky"]

# 052
movie_rank.append("Batman");
print(movie_rank)

# 053
movie_rank.insert(1, "Superman")
print(movie_rank)

# 054
movie_rank.remove("Lucky")
print(movie_rank)

# 055
movie_rank.remove("Split")
del movie_rank[2]
print(movie_rank)

# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 057
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: %d" % max(nums))
print("min: %d" % min(nums))

# 058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 059
cook = ["P", "r", "M", "Y", "j", "P", "K", "W", "T", "R", "p", "k"]
print(len(cook))

# 060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))
