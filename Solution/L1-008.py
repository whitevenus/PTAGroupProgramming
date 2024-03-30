# 获取输入
input_str = input()
num1, num2 = int(input_str.split(" ")[0]), int(input_str.split(" ")[1])

# 整理输出
res = 0
for i in range(num1, num2 + 1, 5):
    for j in range(5):
        if i <= num2:
            res += i
            print(str(i).rjust(5, " "), end="")
            i += 1
    print()
print("Sum =", res)