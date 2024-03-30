# 题目所给条件
dict_ = {
    0: "ling",
    1: "yi",
    2: "er",
    3: "san",
    4: "si",
    5: "wu",
    6: "liu",
    7: "qi",
    8: "ba",
    9: "jiu"
}

# 获取输出
input_str = input()

# 判断输出
if int(input_str) < 0:
    input_str = input_str[1:]
    print("fu " + " ".join([dict_[int(str_)] for str_ in input_str]))
else:
    print(" ".join([dict_[int(str_)] for str_ in input_str]))