# 获取输入数据
input_str = input()
num = int(input_str.split(" ")[0])
symbol_ = input_str.split(" ")[1]

# 获取打印符号的行数
rows = 1
a = 3
total = 1
while total + a * 2 <= num:
    total = total + a * 2
    a += 2
    rows += 2

# 打印上半部分
for i in range(rows, 0, -2):
    print(" " * ((rows - i) // 2) + symbol_ * i)
# 打印下半部分
for i in range(3, rows + 1, 2):
    print(" " * ((rows - i) // 2) + symbol_ * i)
# 打印剩余符号数
print(num - total)
