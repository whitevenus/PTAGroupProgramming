import math

# 获取输入
people_num = int(input())

people_list = []
for i in range(people_num):
    people_list.append(input())

# 输出
for people_str in people_list:
    height, weight = people_str.split(" ")
    std_weight = (float(height) - 100) * 0.9 * 2
    if math.fabs(float(weight) - std_weight) < std_weight * 0.1:
        print("You are wan mei!")
    elif math.fabs(float(weight) - std_weight) > std_weight * 0.1:
        print("You are tai pang le!")
    else:
        print("You are tai shou le!")
