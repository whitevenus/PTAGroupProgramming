# 获取输入
stu_num = int(input())

stu_list = []
for i in range(stu_num):
    stu_list.append(input())


# 整理
stu_dict = {}
record = []
for stu_str in stu_list[:len(stu_list) // 2]:
    tmp_list = stu_str.split(" ")
    j = len(stu_list) - 1
    while j >= 0:
        j_sex, j_name = stu_list[j].split(" ")[0], stu_list[j].split(" ")[1]
        if ((tmp_list[0] == "0" and j_sex == "0") or (tmp_list[0] == "1" and j_sex == "1")) or (j in record):
            j -= 1
        else:
            stu_dict[tmp_list[1]] = j_name
            record.append(j)
            break

# 输出
for key, value in stu_dict.items():
    print(key, value)

