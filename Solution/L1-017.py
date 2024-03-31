# 获取输入
input_str = input()

# 分情况设置权重
temperature = 1
if int(input_str) < 0:
    temperature *= 1.5
    input_str = input_str[1:]
if int(input_str) % 2 == 0:
    temperature *= 2
two_nums = input_str.count("2")

tmp = two_nums / len(input_str)

# 计算输出
result = tmp * temperature * 100
print("{:.2f}%".format(result))