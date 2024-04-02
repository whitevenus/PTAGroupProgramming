# 获取输入
input_num = int(input())

input_list = []
while True:
    input_str = input()
    if input_str == "End":
        break
    else:
        input_list.append(input_str)

# 整理输出
cnt = 0
for str_ in input_list:
    cnt += 1
    if cnt > input_num:
        print(str_)
        cnt = 0
    elif str_ == "ChuiZi" and cnt < input_num:
        print("Bu")
    elif str_ == "JianDao" and cnt <= input_num:
        print("ChuiZi")
    elif str_ == "Bu" and cnt <= input_num:
        print("JianDao")
