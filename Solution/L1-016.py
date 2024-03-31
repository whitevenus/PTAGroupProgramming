# 获取输入
total = int(input())

input_list = []
for i in range(total):
    input_list.append(input())


# 定义检查校验码的函数
def check(num_str):
    list_ = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    dict_ = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
    total_ = 0
    tmp = -1
    for idx, s in enumerate(num_str[:-1]):
        total_ += int(s) * list_[idx]
        tmp = total_ % 11
    if tmp != -1 and str(dict_[tmp]) == num_str[-1]:
        return True
    else:
        return False


# 判断输出
flag = True
for item in input_list:
    if not item[:-1].isdigit():
        flag = False
        print(item)
        continue
    else:
        # 检查校验码是否通过
        if not check(item):
            flag = False
            print(item)
            continue
if flag:
    print("All passed")
