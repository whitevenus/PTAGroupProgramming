# 获取输入
input_num = int(input())

# 输出
for i in range(input_num):
    input_str = input()
    name, breathing_rate, pulse_rate = input_str.split(" ")
    if int(breathing_rate) < 15 or int(breathing_rate) > 20:
        print(name)
        continue
    if int(pulse_rate) < 50 or int(pulse_rate) > 70:
        print(name)
        continue

