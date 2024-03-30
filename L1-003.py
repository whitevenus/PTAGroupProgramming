# 获取输入数据
input_str = input()

# 处理输入数据
tmp_dict = {}
for i in range(len(input_str)):
    num = int(input_str[i])
    if num not in tmp_dict:
        tmp_dict[int(input_str[i])] = 1
    else:
        tmp_dict[int(input_str[i])] += 1

# 输出结果
sorted_kes = sorted(tmp_dict.keys())
res_dict = {str(key): str(tmp_dict[key]) for key in sorted_kes}
for key in res_dict.keys():
    print(key+":"+res_dict[key])




