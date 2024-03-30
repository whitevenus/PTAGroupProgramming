# 获取输入数据
num = input()
dic_ = {}
for i in range(int(num)):
    str_ = input()
    dic_[str_.split(" ")[1]] = str_.split(" ")[0] + " " + str_.split(" ")[2]
input()
str_ = input()

# 输出结果
list_ = str_.split(" ")
for key in list_:
    print(dic_[key])
