import math

# 接受输入数据
input_num = int(input())

# 寻找练乘因子
max_len = 0
min_num = 0
for i in range(2, int(math.sqrt(input_num)) + 1):
    tmp_num = input_num
    next_num = i
    tmp_len = 0

    while tmp_num % next_num == 0:
        tmp_num /= next_num
        next_num += 1
        tmp_len += 1
    if tmp_len > max_len:
        max_len = tmp_len
        min_num = i

# 拼接输出
if max_len == 0:
    print(1)
    print(input_num)
else:
    res_str = '*'.join([str(i) for i in range(min_num, min_num + max_len)])
    print(max_len)
    print(res_str)