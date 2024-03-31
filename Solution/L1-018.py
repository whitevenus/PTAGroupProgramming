# 获取输入
input_str = input()

hour = int(input_str.split(":")[0])
minutes = int(input_str.split(":")[1])

# 判断输出
if hour <= 12:
    print("Only {:0>2}:{:0>2}.  Too early to Dang.".format(hour, minutes))
else:
    if minutes == 0:
        print("Dang" * (hour - 12))
    else:
        print("Dang" * (hour - 12 + 1))
