# 获取输入
input_str = input()

# 整理输出
input_list = input_str.split(" ")
for idx, num_str in enumerate(input_list):
    if num_str == "250":
        print(idx + 1)
        break
