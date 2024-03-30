# 获取输入
input_num = int(input())

# 计算输出
res_sum = 0
for i in range(1, input_num + 1):
    tmp_sum = 1
    for j in range(2, i + 1):
        tmp_sum *= j
    res_sum += tmp_sum
print(res_sum)