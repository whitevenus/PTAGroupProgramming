# 获取输入
input_str = input()
year_str, num = input_str.split(" ")[0], int(input_str.split(" ")[1])

# 计算符合条件的年份和年龄
res_year, res_age = 0, 0
while True:
    s_list = []
    if int(year_str) < 1000:
        year_str = "{:0>4}".format(year_str)
    for s in year_str:
        if s not in s_list:
            s_list.append(s)
        else:
            continue
    if len(s_list) == num:
        res_year = int(year_str)
        break
    year_str = str(int(year_str) + 1)
    res_age += 1

# 输出
if res_year < 1000:
    print(res_age, "{:0>4}".format(res_year))
else:
    print(res_age, res_year)