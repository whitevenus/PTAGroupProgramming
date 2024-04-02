# 获取输入
input_str = input()
num1, num2 = int(input_str.split(" ")[0]), int(input_str.split(" ")[1])

# 输出
if num2 > 0:
    print("{}/{}={:.2f}".format(num1, num2, num1 / num2))
elif num2 < 0:
    print("{}/({})={:.2f}".format(num1, num2, num1 / num2))
else:
    print("{}/{}=Error".format(num1, num2))