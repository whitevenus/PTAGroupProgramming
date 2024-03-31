# 获取输入
total_num = int(input())
num_list = input().split(" ")

# 统计
odd_num, even_num = 0, 0
for num in num_list:
    if int(num) % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

# 输出结果
print(odd_num, even_num)