# 获取输入
input_drink = input()
play_num = int(input())

a_sum = int(input_drink.split(" ")[0])
b_sum = int(input_drink.split(" ")[1])

record_list = []
for i in range(play_num):
    record_list.append(input())


a_drink, b_drink = 0, 0
a_flag, b_flag = False, False
# 开始划拳
for record_str in record_list:

    total = int(record_str.split(" ")[0]) + int(record_str.split(" ")[2])
    a_play, b_play = int(record_str.split(" ")[1]), int(record_str.split(" ")[3])
    if a_play == total and b_play == total:
        # 继续下一轮
        continue
    if a_play == total:
        # 甲喝酒
        a_drink += 1
    if b_play == total:
        # 乙喝酒
        b_drink += 1
    if a_drink > a_sum:
        # 甲倒下
        a_flag = True
        break
    elif b_drink > b_sum:
        # 乙倒下
        b_flag = True
        break

# 输出结果
if a_flag:
    print("A\n{}".format(b_drink))
elif b_flag:
    print("B\n{}".format(a_drink))
