# 输入
input_str = input()

# 排序后输出
num_list = [int(num) for num in input_str.split(" ")]
sorted_list = sorted(num_list)
print("->".join([str(num) for num in sorted_list]))
