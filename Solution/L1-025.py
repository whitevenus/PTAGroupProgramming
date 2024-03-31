import re

# 获取输入
input_str = input()
a_str, b_str = input_str.split(" ", 1)[0], input_str.split(" ", 1)[1]


# 判断是否是小于1000的正整数
def is_pos_digit_than_1000(s):
    pattern = r"^[1-9]\d*$"
    match = re.match(pattern, s)
    if match is not None:
        if int(match.group()) > 1000:
            return False
        else:
            return True
    else:
        return False


# 判断输出
if not is_pos_digit_than_1000(a_str) and is_pos_digit_than_1000(b_str):
    print("?", "+", int(b_str), "=", "?")
elif not is_pos_digit_than_1000(a_str) and not is_pos_digit_than_1000(b_str):
    print("? + ? = ?")
elif is_pos_digit_than_1000(a_str) and not is_pos_digit_than_1000(b_str):
    print(int(a_str), "+", "?", "=", "?")
else:
    print(a_str, "+", b_str, "=", int(a_str) + int(b_str))
