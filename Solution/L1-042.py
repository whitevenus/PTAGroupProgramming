# 获取输入
input_str = input()

# 拆分输出
month, day, year = input_str.split("-")
print("{}-{}-{}".format(year, month, day))