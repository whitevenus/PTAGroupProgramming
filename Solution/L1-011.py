# 获取输入
str_a = input()
str_b = input()

# 处理输出
for str_single in str_a:
    if str_single in str_b:
        str_a = str_a.replace(str_single, "")
        # print("*")
print(str_a)