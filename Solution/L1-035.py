# 获取输入
input_list = []
while True:
    input_str = input()
    if input_str == ".":
        break
    input_list.append(input_str)

# 判断输出
list_len = len(input_list)
if list_len >= 14:
    print("{} and {} are inviting you to dinner...".format(input_list[1], input_list[13]))
elif list_len >= 2:
    print("{} is the only one for you...".format(input_list[1]))
else:
    print("Momo... No one is for you ...")