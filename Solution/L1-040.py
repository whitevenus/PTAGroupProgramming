# 获取输入
num = int(input())

for i in range(num):
    input_str = input()
    # 整理输出
    sex, height = input_str.split(" ")[0], float(input_str.split(" ")[1])
    if sex == "M":
        print("{:.2f}".format(height / 1.09))
    else:
        print("{:.2f}".format(height * 1.09))

